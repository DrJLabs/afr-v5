import fcntl
import hashlib
import importlib.util
import json
import os
import subprocess
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).with_name("skill_sync.py")
SPEC = importlib.util.spec_from_file_location("skill_sync", MODULE_PATH)
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


PACKAGE_A = {
    "SKILL.md": b"skill A\n",
    "agents/openai.yaml": b"policy: A\n",
    "references/planning.md": b"planning A\n",
    "references/work.md": b"work A\n",
    "references/review.md": b"review A\n",
    "references/delivery.md": b"delivery A\n",
}
PACKAGE_B = {path: data.replace(b"A", b"B") for path, data in PACKAGE_A.items()}


def raw_items(blobs, ids=None, md5_only=False):
    ids = ids or {}
    dirs = {"agents", "references"}
    result = []
    for directory in sorted(dirs):
        result.append(
            {
                "Path": directory,
                "IsDir": True,
                "ID": ids.get(directory, "id-" + directory),
                "MimeType": "application/vnd.google-apps.folder",
                "Size": 0,
                "Hashes": {},
            }
        )
    for path, data in sorted(blobs.items()):
        hashes = {"MD5": hashlib.md5(data).hexdigest()}
        if not md5_only:
            hashes["SHA-256"] = hashlib.sha256(data).hexdigest()
        result.append(
            {
                "Path": path,
                "IsDir": False,
                "ID": ids.get(path, "id-" + path),
                "MimeType": "text/plain",
                "Size": len(data),
                "Hashes": hashes,
            }
        )
    return result


class FakeTransport:
    def __init__(self, blobs, config, fail_download=None, md5_only=False):
        self.blobs = dict(blobs)
        self.config = config
        self.fail_download = fail_download
        self.md5_only = md5_only
        self.download_override = None
        self.download_count = 0
        self.upload_count = 0
        self.list_count = 0
        self.id_map = {item["Path"]: item["ID"] for item in raw_items(self.blobs)}
        self.after_download = None
        self.changed_during_download = False
        self.fail_upload_number = None

    def list_inventory(self):
        self.list_count += 1
        return sync.normalize_inventory(raw_items(self.blobs, self.id_map, self.md5_only), self.config)

    def download(self, relpath, destination):
        self.download_count += 1
        payload = self.blobs[relpath]
        if self.download_override is not None:
            payload = self.download_override.get(relpath, payload)
        destination.write_bytes(payload)
        if self.fail_download == "network":
            raise sync.SyncError("fake transport network failure")
        if self.fail_download == "interrupt":
            raise KeyboardInterrupt()
        if self.after_download and not self.changed_during_download:
            self.changed_during_download = True
            self.after_download(self)

    def upload(self, source, relpath):
        self.upload_count += 1
        if self.fail_upload_number == self.upload_count:
            raise sync.SyncError("fake upload failure")
        self.blobs[relpath] = source.read_bytes()


class SkillSyncTests(unittest.TestCase):
    def setUp(self):
        # Use an isolated temporary filesystem location for private state and Git fixtures.
        self.temp = tempfile.TemporaryDirectory(prefix="afr-skill-sync-test-")
        self.root = Path(self.temp.name)
        self.config = {
            "remote": "drive:",
            "folder_id": "working-folder-id",
            "state_dir": self.root / "state",
            "default_ref": "refs/remotes/origin/main",
            "max_files": 100,
            "max_bytes": 10485760,
        }

    def tearDown(self):
        self.temp.cleanup()

    def test_capture_noop_revalidates_and_status_detects_tampering(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        first = sync.capture(self.config, transport)
        self.assertEqual(first["result"], "captured")
        self.assertEqual(transport.download_count, 6)

        transport.download_count = 0
        transport.list_count = 0
        unchanged = sync.capture(self.config, transport)
        self.assertEqual(unchanged["result"], "unchanged")
        self.assertEqual(transport.download_count, 0)
        self.assertEqual(transport.list_count, 2)
        status = sync.status(self.config)
        self.assertEqual(status["snapshot_path"], first["snapshot_path"])
        self.assertEqual(status["retained_snapshot_count"], 1)
        self.assertEqual(status["retained_bytes_estimate"], sum(map(len, PACKAGE_A.values())))

        target = Path(first["snapshot_path"]) / "content" / "SKILL.md"
        target.write_bytes(b"tampered\n")
        with self.assertRaisesRegex(sync.SyncError, "size|hash"):
            sync.capture(self.config, transport)
        with self.assertRaisesRegex(sync.SyncError, "size|hash"):
            sync.status(self.config)
        self.assertEqual(transport.download_count, 0)

    def test_race_rejection_preserves_prior_snapshot_and_author_file(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        first = sync.capture(self.config, transport)
        previous = Path(first["snapshot_path"]) / "content" / "SKILL.md"
        author_file = self.root / "author-worktree" / "notes.md"
        author_file.parent.mkdir()
        author_file.write_text("local draft survives\n", encoding="utf-8")
        transport.blobs = dict(PACKAGE_B)
        transport.after_download = lambda current: current.blobs.update({"SKILL.md": b"changed mid-download\n"})

        with self.assertRaisesRegex(sync.SyncError, "changed during download"):
            sync.capture(self.config, transport)
        self.assertEqual(previous.read_bytes(), PACKAGE_A["SKILL.md"])
        self.assertEqual(author_file.read_text(encoding="utf-8"), "local draft survives\n")
        self.assertEqual(os.readlink(self.config["state_dir"] / "latest"), f"snapshots/{first['snapshot_id']}")

    def test_new_snapshot_retains_prior_snapshot_and_does_not_touch_author_file(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        first = sync.capture(self.config, transport)
        old_content = Path(first["snapshot_path"]) / "content" / "SKILL.md"
        author_file = self.root / "checkout" / "SKILL.md"
        author_file.parent.mkdir()
        author_file.write_bytes(b"author's unsaved change\n")
        transport.blobs = dict(PACKAGE_B)
        second = sync.capture(self.config, transport)
        status = sync.status(self.config)

        self.assertNotEqual(first["snapshot_id"], second["snapshot_id"])
        self.assertEqual(old_content.read_bytes(), PACKAGE_A["SKILL.md"])
        self.assertEqual(author_file.read_bytes(), b"author's unsaved change\n")
        self.assertEqual(status["retained_snapshot_count"], 2)
        self.assertEqual(status["retained_bytes_estimate"], sum(map(len, PACKAGE_A.values())) + sum(map(len, PACKAGE_B.values())))

    def test_interrupted_and_network_failed_capture_never_promote_partial_state(self):
        network = FakeTransport(PACKAGE_A, self.config, fail_download="network")
        with self.assertRaisesRegex(sync.SyncError, "network failure"):
            sync.capture(self.config, network)
        self.assertFalse((self.config["state_dir"] / "latest").exists())
        self.assertFalse(list((self.config["state_dir"] / "snapshots").glob("*")))

        interrupted = FakeTransport(PACKAGE_A, self.config, fail_download="interrupt")
        with self.assertRaises(KeyboardInterrupt):
            sync.capture(self.config, interrupted)
        self.assertFalse((self.config["state_dir"] / "latest").exists())
        self.assertTrue(list((self.config["state_dir"] / "snapshots").glob(".capture-*")))
        interrupted.fail_download = None
        result = sync.capture(self.config, interrupted)
        self.assertEqual(sync.status(self.config)["snapshot_id"], result["snapshot_id"])

    def test_lock_prevents_overlapping_capture(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        sync.capture(self.config, transport)
        descriptor = os.open(self.config["state_dir"] / ".lock", os.O_RDONLY)
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            list_count = transport.list_count
            with self.assertRaisesRegex(sync.SyncError, "busy"):
                sync.capture(self.config, transport)
            self.assertEqual(transport.list_count, list_count)
        finally:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
            os.close(descriptor)

    def test_inventory_guards_duplicates_paths_docs_hashes_and_bounds(self):
        good = raw_items(PACKAGE_A)
        with self.assertRaisesRegex(sync.SyncError, "duplicate normalized"):
            sync.normalize_inventory(good + [dict(good[-1], Path="references/review.md")], self.config)
        with self.assertRaisesRegex(sync.SyncError, "unsafe path"):
            sync.normalize_inventory(good + [dict(good[-1], Path="../escape", ID="extra")], self.config)
        with self.assertRaisesRegex(sync.SyncError, "native Google"):
            sync.normalize_inventory([dict(item, MimeType="application/vnd.google-apps.document") if item["Path"] == "SKILL.md" else item for item in good], self.config)
        with self.assertRaisesRegex(sync.SyncError, "hash"):
            sync.normalize_inventory([dict(item, Hashes={}) if item["Path"] == "SKILL.md" else item for item in good], self.config)
        small = dict(self.config, max_bytes=1)
        with self.assertRaisesRegex(sync.SyncError, "bounds"):
            sync.normalize_inventory(good, small)

    def test_shortcuts_with_resolved_composite_ids_are_rejected(self):
        listing = raw_items(PACKAGE_A)
        listing = [dict(item, ID=item["ID"] + "\tshortcut-id") if item["Path"] == "SKILL.md" else item for item in listing]
        with self.assertRaisesRegex(sync.SyncError, "identity"):
            sync.normalize_inventory(listing, self.config)

    def _git_repo(self, package=PACKAGE_B, name="repo"):
        repo = self.root / name
        repo.mkdir()
        subprocess.run(["git", "init", "-b", "main", str(repo)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.invalid"], check=True)
        package_root = repo / ".agents" / "skills" / "afr"
        for path, data in package.items():
            output = package_root / path
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
        subprocess.run(["git", "-C", str(repo), "add", ".agents/skills/afr"], check=True)
        subprocess.run(["git", "-C", str(repo), "commit", "-m", "qualified source"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        revision = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
        subprocess.run(["git", "-C", str(repo), "update-ref", "refs/remotes/origin/main", revision], check=True)
        return repo, revision

    def test_publish_uses_immutable_commit_and_preserves_drive_ids(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        expected = sync.capture(self.config, transport)
        repo, revision = self._git_repo()
        dirty_file = repo / ".agents/skills/afr/SKILL.md"
        dirty_file.write_bytes(b"dirty worktree bytes\n")
        original_ids = {entry["path"]: entry["id"] for entry in transport.list_inventory() if not entry["is_dir"]}

        result = sync.publish(self.config, str(repo), revision, expected["snapshot_path"], True, transport)
        final_ids = {entry["path"]: entry["id"] for entry in transport.list_inventory() if not entry["is_dir"]}
        self.assertEqual(transport.blobs, PACKAGE_B)
        self.assertEqual(dirty_file.read_bytes(), b"dirty worktree bytes\n")
        self.assertEqual(final_ids, original_ids)
        self.assertEqual(result["revision"], revision)
        self.assertEqual(result["changed_files"], 6)
        self.assertFalse(list(self.config["state_dir"].glob(".publish-*")))

    def test_default_publish_transport_gets_bounded_operation_deadline(self):
        initial = FakeTransport(PACKAGE_A, self.config)
        expected = sync.capture(self.config, initial)
        repo, revision = self._git_repo(PACKAGE_A)
        default_transport = FakeTransport(PACKAGE_A, self.config)
        with mock.patch.object(sync, "RcloneTransport", return_value=default_transport) as factory:
            result = sync.publish(self.config, str(repo), revision, expected["snapshot_path"], True)
        self.assertEqual(factory.call_count, 1)
        deadline = factory.call_args.args[1]
        self.assertIsInstance(deadline, float)
        self.assertGreater(deadline, time.monotonic())
        self.assertLessEqual(deadline - time.monotonic(), sync.OPERATION_TIMEOUT_SECONDS)
        self.assertEqual(result["changed_files"], 0)
        self.assertEqual(result["snapshot_id"], expected["snapshot_id"])

    def test_md5_only_publication_is_rejected_without_writes(self):
        transport = FakeTransport(PACKAGE_A, self.config, md5_only=True)
        expected = sync.capture(self.config, transport)
        repo, revision = self._git_repo(PACKAGE_B, name="md5-only-repo")
        list_count = transport.list_count

        with self.assertRaisesRegex(sync.SyncError, "SHA-256.*refused"):
            sync.publish(self.config, str(repo), revision, expected["snapshot_path"], True, transport)
        self.assertEqual(transport.upload_count, 0)
        self.assertEqual(transport.list_count, list_count)
        self.assertEqual(transport.blobs, PACKAGE_A)
        self.assertEqual((Path(expected["snapshot_path"]) / "content" / "SKILL.md").read_bytes(), PACKAGE_A["SKILL.md"])

    def test_md5_only_fresh_target_is_rejected_before_first_upload(self):
        config = dict(self.config, state_dir=self.root / "sha-snapshot-md5-target-state")
        transport = FakeTransport(PACKAGE_A, config)
        expected = sync.capture(config, transport)
        transport.md5_only = True
        repo, revision = self._git_repo(PACKAGE_B, name="md5-target-repo")

        with self.assertRaisesRegex(sync.SyncError, "SHA-256.*refused"):
            sync.publish(config, str(repo), revision, expected["snapshot_path"], True, transport)
        self.assertEqual(transport.upload_count, 0)
        self.assertEqual(transport.blobs, PACKAGE_A)

    def test_rclone_upload_forces_copy_for_selected_files(self):
        transport = sync.RcloneTransport(self.config)
        result = mock.Mock(returncode=0, stdout=b"", stderr=b"")
        with mock.patch.object(sync.subprocess, "run", return_value=result) as run:
            transport.upload(self.root / "source.txt", "SKILL.md")
        command = run.call_args.args[0]
        self.assertIn("--ignore-times", command)
        self.assertNotIn("--checksum", command)

    def test_stale_publish_and_unmerged_revision_make_no_writes(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        expected = sync.capture(self.config, transport)
        repo, revision = self._git_repo()
        transport.blobs["SKILL.md"] = b"new remote edit\n"
        with self.assertRaisesRegex(sync.SyncError, "stale"):
            sync.publish(self.config, str(repo), revision, expected["snapshot_path"], True, transport)
        self.assertEqual(transport.upload_count, 0)

        transport = FakeTransport(PACKAGE_A, self.config)
        expected = sync.capture(self.config, transport)
        branch, base_revision = self._git_repo(name="unmerged-repo")
        package_file = branch / ".agents/skills/afr/SKILL.md"
        package_file.write_bytes(b"unmerged branch\n")
        subprocess.run(["git", "-C", str(branch), "add", ".agents/skills/afr/SKILL.md"], check=True)
        subprocess.run(["git", "-C", str(branch), "commit", "-m", "unmerged source"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        unmerged_revision = subprocess.run(["git", "-C", str(branch), "rev-parse", "HEAD"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
        subprocess.run(["git", "-C", str(branch), "update-ref", "refs/remotes/origin/main", base_revision], check=True)
        with self.assertRaisesRegex(sync.SyncError, "contained"):
            sync.publish(self.config, str(branch), unmerged_revision, expected["snapshot_path"], True, transport)
        self.assertEqual(transport.upload_count, 0)

    def test_partial_publish_stops_without_retry_or_rollback(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        expected = sync.capture(self.config, transport)
        repo, revision = self._git_repo()
        transport.fail_upload_number = 2

        with self.assertRaisesRegex(sync.SyncError, "Reobserve the target"):
            sync.publish(self.config, str(repo), revision, expected["snapshot_path"], True, transport)
        self.assertEqual(transport.upload_count, 2)
        self.assertEqual(transport.blobs["SKILL.md"], PACKAGE_B["SKILL.md"])
        self.assertEqual(transport.blobs["agents/openai.yaml"], PACKAGE_A["agents/openai.yaml"])
        self.assertEqual((Path(expected["snapshot_path"]) / "content" / "SKILL.md").read_bytes(), PACKAGE_A["SKILL.md"])
        self.assertFalse(list(self.config["state_dir"].glob(".publish-*")))

    def test_config_identity_and_expected_snapshot_path_are_enforced(self):
        transport = FakeTransport(PACKAGE_A, self.config)
        snapshot = sync.capture(self.config, transport)
        changed_target = dict(self.config, folder_id="different-folder")
        with self.assertRaisesRegex(sync.SyncError, "configuration identity"):
            sync.status(changed_target)
        with self.assertRaisesRegex(sync.SyncError, "direct snapshot"):
            sync._expected_snapshot_path(str(self.config["state_dir"] / "latest"), self.config["state_dir"])

    def test_empty_git_sentinel_is_allowed_but_initialized_repository_is_not(self):
        sentinel_root = self.root / "empty-sentinel"
        (sentinel_root / ".git").mkdir(parents=True)
        sync.validate_state_location(sentinel_root / "state")

        repo = self.root / "real-repository"
        repo.mkdir()
        subprocess.run(["git", "init", str(repo)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with self.assertRaisesRegex(sync.SyncError, "outside repositories"):
            sync.validate_state_location(repo / ".local" / "state")


if __name__ == "__main__":
    unittest.main()
