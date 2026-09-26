#!/usr/bin/env python3
"""Small, optional rclone adapter for immutable AFR skill snapshots."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unicodedata
import uuid
from pathlib import Path, PurePosixPath


REQUIRED_FILES = frozenset(
    {
        "SKILL.md",
        "agents/openai.yaml",
        "references/planning.md",
        "references/work.md",
        "references/review.md",
        "references/delivery.md",
    }
)
SNAPSHOT_NAME_RE = re.compile(r"^[0-9]{8}T[0-9]{6}Z-[0-9a-f]{12}$")
HEX_RE = {"md5": re.compile(r"^[0-9a-fA-F]{32}$"), "sha256": re.compile(r"^[0-9a-fA-F]{64}$")}
MANIFEST_NAME = "manifest.json"
OPERATION_TIMEOUT_SECONDS = 150


class SyncError(Exception):
    """An expected validation, transport, or state error safe to show the caller."""


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def config_identity(config: dict) -> dict:
    return {"remote": config["remote"], "folder_id": config["folder_id"]}


def root_identity(config: dict) -> str:
    return "sha256:" + sha256_bytes(canonical_json(config_identity(config)))


def _absolute_state_path(value: object) -> Path:
    if not isinstance(value, str) or not value:
        raise SyncError("state_dir must be an absolute path")
    path = Path(value)
    if not path.is_absolute():
        raise SyncError("state_dir must be an absolute path")
    return path.resolve(strict=False)


def load_config(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as stream:
            raw = json.load(stream)
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise SyncError("could not read config JSON") from None
    if not isinstance(raw, dict):
        raise SyncError("config must be a JSON object")
    allowed = {"remote", "folder_id", "state_dir", "default_ref", "max_files", "max_bytes"}
    if set(raw) - allowed:
        raise SyncError("config contains unsupported keys")

    remote = raw.get("remote")
    folder_id = raw.get("folder_id")
    if not isinstance(remote, str) or not remote.endswith(":") or remote.count(":") != 1:
        raise SyncError("remote must be an existing rclone remote name ending in ':'")
    if any(ord(ch) < 32 for ch in remote) or "/" in remote or "\\" in remote or remote[:-1].startswith("-"):
        raise SyncError("remote name is not valid")
    if not isinstance(folder_id, str) or not folder_id or any(ord(ch) < 32 for ch in folder_id):
        raise SyncError("folder_id must be a non-empty Drive folder ID")
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,256}", folder_id):
        raise SyncError("folder_id is not valid")

    default_ref = raw.get("default_ref", "origin/main")
    if not isinstance(default_ref, str) or not default_ref or default_ref.startswith("-") or any(ch.isspace() for ch in default_ref):
        raise SyncError("default_ref must be a Git reference")
    max_files = raw.get("max_files", 100)
    max_bytes = raw.get("max_bytes", 10485760)
    if isinstance(max_files, bool) or not isinstance(max_files, int) or max_files < 1:
        raise SyncError("max_files must be a positive finite integer")
    if isinstance(max_bytes, bool) or not isinstance(max_bytes, int) or max_bytes < 1:
        raise SyncError("max_bytes must be a positive finite integer")

    return {
        "remote": remote,
        "folder_id": folder_id,
        "state_dir": _absolute_state_path(raw.get("state_dir")),
        "default_ref": default_ref,
        "max_files": max_files,
        "max_bytes": max_bytes,
    }


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate_state_location(state_dir: Path, repo_root: Path | None = None) -> None:
    resolved = state_dir.resolve(strict=False)
    if repo_root is not None and _is_relative_to(resolved, repo_root.resolve()):
        raise SyncError("state_dir must be outside the repository")

    parts = resolved.parts
    for marker in ((".agents", "skills"), (".codex", "skills")):
        if any(parts[i : i + 2] == marker for i in range(max(0, len(parts) - 1))):
            raise SyncError("state_dir must be outside skill-discovery roots")

    # Git metadata files and populated directories identify repositories; empty
    # sentinel directories used by some environments do not.
    for ancestor in (resolved, *resolved.parents):
        marker = ancestor / ".git"
        try:
            info = marker.lstat()
        except FileNotFoundError:
            continue
        except OSError:
            raise SyncError("could not inspect repository marker for state_dir") from None
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
            raise SyncError("state_dir must be outside repositories")
        try:
            if next(marker.iterdir(), None) is not None:
                raise SyncError("state_dir must be outside repositories")
        except OSError:
            raise SyncError("could not inspect repository marker for state_dir") from None

    home = Path.home().resolve(strict=False)
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex")).resolve(strict=False)
    skill_roots = (home / ".agents" / "skills", codex_home / "skills")
    if any(_is_relative_to(resolved, root.resolve(strict=False)) for root in skill_roots):
        raise SyncError("state_dir must be outside skill-discovery roots")


def _check_private_directory(path: Path, create: bool) -> None:
    if create:
        try:
            path.mkdir(mode=0o700, parents=True, exist_ok=True)
        except OSError:
            raise SyncError("could not create private state directory") from None
    try:
        info = path.lstat()
    except OSError:
        raise SyncError("state directory is not initialized") from None
    if not stat.S_ISDIR(info.st_mode) or stat.S_ISLNK(info.st_mode):
        raise SyncError("state_dir must be a real directory")
    if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
        raise SyncError("state_dir must be owned by the current user and private (mode 0700)")


@contextlib.contextmanager
def state_lock(state_dir: Path, exclusive: bool, create: bool = False):
    _check_private_directory(state_dir, create=create)
    lock_path = state_dir / ".lock"
    flags = os.O_RDONLY if not exclusive else (os.O_RDWR | os.O_CREAT)
    flags |= getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(lock_path, flags, 0o600)
    except OSError:
        raise SyncError("state lock is unavailable") from None
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
            raise SyncError("state lock must be a private regular file")
        operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
        try:
            fcntl.flock(descriptor, operation | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SyncError("state is busy; wait for the active operation") from None
        yield
    finally:
        os.close(descriptor)


def normalize_relative_path(value: object) -> str:
    if not isinstance(value, str) or not value or "\x00" in value or "\\" in value:
        raise SyncError("remote contains an unsafe path")
    normalized = unicodedata.normalize("NFC", value)
    if normalized.startswith("/") or normalized.endswith("/"):
        raise SyncError("remote contains an unsafe path")
    parts = normalized.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise SyncError("remote contains an unsafe path")
    if PurePosixPath(normalized).is_absolute():
        raise SyncError("remote contains an unsafe path")
    return normalized


def normalize_inventory(raw_items: object, config: dict) -> list[dict]:
    if not isinstance(raw_items, list):
        raise SyncError("remote inventory is not a JSON array")
    if len(raw_items) > config["max_files"] + 128:
        raise SyncError("remote inventory exceeds the bounded entry count")

    entries = []
    paths: dict[str, bool] = {}
    ids: set[str] = set()
    total_files = 0
    total_bytes = 0
    for item in raw_items:
        if not isinstance(item, dict):
            raise SyncError("remote inventory contains an invalid entry")
        path = normalize_relative_path(item.get("Path"))
        is_dir = item.get("IsDir")
        if not isinstance(is_dir, bool):
            raise SyncError("remote inventory is missing file/directory type")
        if path in paths:
            raise SyncError("remote inventory contains duplicate normalized paths")
        paths[path] = is_dir

        item_id = item.get("ID")
        if not isinstance(item_id, str) or not item_id or any(ord(ch) < 32 or ord(ch) == 127 for ch in item_id):
            raise SyncError("remote inventory is missing a file identity")
        if item_id in ids:
            raise SyncError("remote inventory contains duplicate file identities")
        ids.add(item_id)

        mime = item.get("MimeType")
        if not is_dir and isinstance(mime, str) and mime.lower().startswith("application/vnd.google-apps."):
            raise SyncError("remote package contains a native Google document or shortcut")
        if item.get("IsBucket") or item.get("IsShortcut"):
            raise SyncError("remote package contains an unsupported object type")

        if is_dir:
            size = None
            hashes = {}
        else:
            size = item.get("Size")
            if isinstance(size, bool) or not isinstance(size, int) or size < 0:
                raise SyncError("remote file is missing a valid size")
            total_files += 1
            total_bytes += size
            raw_hashes = item.get("Hashes")
            if not isinstance(raw_hashes, dict):
                raise SyncError("remote file is missing a content hash")
            hashes = {}
            for name, value in raw_hashes.items():
                lowered = str(name).lower().replace("-", "").replace("_", "")
                key = "sha256" if lowered == "sha256" else lowered
                if key not in HEX_RE or not isinstance(value, str) or not HEX_RE[key].fullmatch(value):
                    continue
                hashes[key] = value.lower()
            if not hashes:
                raise SyncError("remote file has no supported MD5 or SHA-256 hash")

        entries.append({"path": path, "is_dir": is_dir, "id": item_id, "size": size, "hashes": hashes})

    for path, is_dir in paths.items():
        components = path.split("/")
        for end in range(1, len(components)):
            parent = "/".join(components[:end])
            if parent in paths and not paths[parent]:
                raise SyncError("remote inventory contains a file/directory path collision")
        if not is_dir and any(other.startswith(path + "/") for other in paths):
            raise SyncError("remote inventory contains a file/directory path collision")

    files = {entry["path"] for entry in entries if not entry["is_dir"]}
    missing = REQUIRED_FILES - files
    if missing:
        raise SyncError("remote package is missing required raw files")
    if total_files > config["max_files"] or total_bytes > config["max_bytes"]:
        raise SyncError("remote package exceeds configured file or byte bounds")
    return sorted(entries, key=lambda entry: entry["path"])


def inventory_digest(entries: list[dict]) -> str:
    return sha256_bytes(canonical_json(entries))


def _hash_file(path: Path, algorithms: set[str] | None = None) -> dict[str, str]:
    names = algorithms or {"md5", "sha256"}
    digests = {name: hashlib.new(name) for name in names}
    try:
        with path.open("rb") as stream:
            while chunk := stream.read(1024 * 1024):
                for digest in digests.values():
                    digest.update(chunk)
    except OSError:
        raise SyncError("could not read snapshot file") from None
    return {name: digest.hexdigest() for name, digest in digests.items()}


def _walk_content(content: Path) -> tuple[set[str], set[str]]:
    files: set[str] = set()
    directories: set[str] = set()
    try:
        root_info = content.lstat()
    except OSError:
        raise SyncError("snapshot content is missing") from None
    if not stat.S_ISDIR(root_info.st_mode) or stat.S_ISLNK(root_info.st_mode):
        raise SyncError("snapshot content must be a regular directory")
    for current, dirnames, filenames in os.walk(content, followlinks=False):
        current_path = Path(current)
        for name in list(dirnames):
            child = current_path / name
            info = child.lstat()
            if not stat.S_ISDIR(info.st_mode) or stat.S_ISLNK(info.st_mode):
                raise SyncError("snapshot contains a symlink or non-directory")
            directories.add(child.relative_to(content).as_posix())
        for name in filenames:
            child = current_path / name
            info = child.lstat()
            if not stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode):
                raise SyncError("snapshot contains a symlink or non-regular file")
            files.add(normalize_relative_path(child.relative_to(content).as_posix()))
    return files, directories


def verify_content(content: Path, entries: list[dict]) -> None:
    expected = {entry["path"]: entry for entry in entries if not entry["is_dir"]}
    actual, _ = _walk_content(content)
    if actual != set(expected):
        raise SyncError("snapshot file set does not match its manifest")
    for relpath, entry in expected.items():
        file_path = content.joinpath(*relpath.split("/"))
        size = file_path.stat().st_size
        if size != entry["size"]:
            raise SyncError("snapshot file size does not match its manifest")
        if _hash_file(file_path, set(entry["hashes"])) != entry["hashes"]:
            raise SyncError("snapshot file hash does not match its manifest")


class RcloneTransport:
    """The only rclone boundary; tests provide an in-memory fake with the same methods."""

    def __init__(self, config: dict, deadline: float | None = None):
        self.config = config
        self.deadline = deadline

    def _run(self, args: list[str], operation: str) -> bytes:
        try:
            remaining = None if self.deadline is None else self.deadline - time.monotonic()
            if remaining is not None and remaining <= 0:
                raise SyncError(f"operation exceeded its {OPERATION_TIMEOUT_SECONDS}s time bound")
            result = subprocess.run(args, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=remaining)
        except subprocess.TimeoutExpired:
            raise SyncError(f"rclone {operation} exceeded the operation time bound") from None
        except SyncError:
            raise
        except OSError:
            raise SyncError(f"could not start rclone during {operation}") from None
        if result.returncode != 0:
            raise SyncError(f"rclone {operation} failed (exit {result.returncode}); no automatic retry was attempted")
        return result.stdout

    def list_inventory(self) -> list[dict]:
        output = self._run(
            [
                "rclone",
                "lsjson",
                self.config["remote"],
                "-R",
                "--hash",
                "--drive-show-all-gdocs=true",
                "--drive-skip-gdocs=false",
                "--drive-skip-shortcuts=false",
                "--drive-skip-dangling-shortcuts=false",
                "--drive-root-folder-id",
                self.config["folder_id"],
            ],
            "inventory",
        )
        try:
            raw = json.loads(output.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError):
            raise SyncError("rclone returned an invalid inventory") from None
        return normalize_inventory(raw, self.config)

    def download(self, relpath: str, destination: Path) -> None:
        self._run(
            [
                "rclone",
                "copyto",
                "--drive-root-folder-id",
                self.config["folder_id"],
                self.config["remote"] + relpath,
                str(destination),
            ],
            "download",
        )

    def upload(self, source: Path, relpath: str) -> None:
        self._run(
            [
                "rclone",
                "copyto",
                "--ignore-times",
                "--drive-root-folder-id",
                self.config["folder_id"],
                str(source),
                self.config["remote"] + relpath,
            ],
            "publication copy",
        )


def _read_json(path: Path, message: str) -> dict:
    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(stream)
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise SyncError(message) from None
    if not isinstance(value, dict):
        raise SyncError(message)
    return value


def _latest_snapshot(state_dir: Path, config: dict) -> tuple[Path, dict] | None:
    latest = state_dir / "latest"
    try:
        info = latest.lstat()
    except FileNotFoundError:
        return None
    except OSError:
        raise SyncError("latest snapshot pointer cannot be read") from None
    if not stat.S_ISLNK(info.st_mode):
        raise SyncError("latest snapshot pointer is not a symlink")
    try:
        target = os.readlink(latest)
    except OSError:
        raise SyncError("latest snapshot pointer cannot be read") from None
    match = re.fullmatch(r"snapshots/([0-9]{8}T[0-9]{6}Z-[0-9a-f]{12})", target)
    if not match:
        raise SyncError("latest snapshot pointer has an unsafe target")
    snapshot_dir = state_dir / target
    return snapshot_dir, verify_snapshot(snapshot_dir, config)


def verify_snapshot(snapshot_dir: Path, config: dict) -> dict:
    try:
        info = snapshot_dir.lstat()
    except OSError:
        raise SyncError("expected snapshot does not exist") from None
    if not stat.S_ISDIR(info.st_mode) or stat.S_ISLNK(info.st_mode):
        raise SyncError("snapshot must be a regular directory")
    manifest_path = snapshot_dir / MANIFEST_NAME
    try:
        manifest_info = manifest_path.lstat()
    except OSError:
        raise SyncError("snapshot manifest is missing or invalid") from None
    if not stat.S_ISREG(manifest_info.st_mode) or stat.S_ISLNK(manifest_info.st_mode):
        raise SyncError("snapshot manifest must be a regular file")
    manifest = _read_json(manifest_path, "snapshot manifest is missing or invalid")
    if manifest.get("schema") != 1 or manifest.get("config_identity") != config_identity(config):
        raise SyncError("snapshot configuration identity does not match this target")
    snapshot_id = manifest.get("snapshot_id")
    if not isinstance(snapshot_id, str) or not SNAPSHOT_NAME_RE.fullmatch(snapshot_id) or snapshot_dir.name != snapshot_id:
        raise SyncError("snapshot manifest identity is invalid")
    entries = manifest.get("inventory")
    if not isinstance(entries, list):
        raise SyncError("snapshot manifest inventory is invalid")
    normalized = []
    for item in entries:
        if not isinstance(item, dict) or set(item) != {"path", "is_dir", "id", "size", "hashes"}:
            raise SyncError("snapshot manifest inventory is invalid")
        path = normalize_relative_path(item["path"])
        if not isinstance(item["is_dir"], bool) or not isinstance(item["id"], str) or not item["id"]:
            raise SyncError("snapshot manifest inventory is invalid")
        if not isinstance(item["hashes"], dict):
            raise SyncError("snapshot manifest inventory is invalid")
        if item["is_dir"]:
            if item["size"] is not None or item["hashes"]:
                raise SyncError("snapshot manifest directory entry is invalid")
        else:
            if isinstance(item["size"], bool) or not isinstance(item["size"], int) or item["size"] < 0:
                raise SyncError("snapshot manifest file entry is invalid")
            if not item["hashes"] or any(key not in HEX_RE or not isinstance(value, str) or not HEX_RE[key].fullmatch(value) for key, value in item["hashes"].items()):
                raise SyncError("snapshot manifest file hashes are invalid")
        normalized.append({"path": path, "is_dir": item["is_dir"], "id": item["id"], "size": item["size"], "hashes": item["hashes"]})
    normalized.sort(key=lambda item: item["path"])
    if normalized != entries or inventory_digest(entries) != manifest.get("inventory_sha256"):
        raise SyncError("snapshot inventory digest does not match its manifest")
    if manifest.get("root_identity") != root_identity(config):
        raise SyncError("snapshot root identity does not match this target")
    file_count = sum(not item["is_dir"] for item in entries)
    total_bytes = sum(item["size"] or 0 for item in entries if not item["is_dir"])
    if file_count > config["max_files"] or total_bytes > config["max_bytes"]:
        raise SyncError("snapshot exceeds configured file or byte bounds")
    if manifest.get("file_count") != file_count or manifest.get("total_bytes") != total_bytes:
        raise SyncError("snapshot manifest totals are invalid")
    try:
        top_entries = {entry.name for entry in snapshot_dir.iterdir()}
    except OSError:
        raise SyncError("snapshot directory cannot be read") from None
    if top_entries != {MANIFEST_NAME, "content"}:
        raise SyncError("snapshot contains unexpected top-level entries")
    verify_content(snapshot_dir / "content", entries)
    return manifest


def _write_manifest(path: Path, manifest: dict) -> None:
    try:
        with path.open("xb") as stream:
            stream.write(canonical_json(manifest))
            stream.write(b"\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(path, 0o600)
    except OSError:
        raise SyncError("could not write snapshot manifest") from None


def _fsync_directory(path: Path) -> None:
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except OSError:
        raise SyncError("could not finalize private snapshot state") from None


def _validate_existing_snapshot_identities(snapshots: Path, config: dict) -> None:
    if not snapshots.exists():
        return
    for entry in snapshots.iterdir():
        if not SNAPSHOT_NAME_RE.fullmatch(entry.name):
            continue
        if entry.is_symlink() or not entry.is_dir():
            raise SyncError("existing snapshot state contains an unsafe entry")
        manifest = _read_json(entry / MANIFEST_NAME, "existing snapshot manifest is missing or invalid")
        if manifest.get("config_identity") != config_identity(config):
            raise SyncError("existing snapshot configuration identity does not match this target")


def capture(config: dict, transport=None) -> dict:
    state_dir = config["state_dir"]
    validate_state_location(state_dir)
    _check_private_directory(state_dir, create=True)
    snapshots = state_dir / "snapshots"

    with state_lock(state_dir, exclusive=True, create=True):
        try:
            snapshots.mkdir(mode=0o700, exist_ok=True)
        except OSError:
            raise SyncError("could not create snapshot directory") from None
        if snapshots.is_symlink() or not snapshots.is_dir():
            raise SyncError("snapshot directory must be a real directory")
        if stat.S_IMODE(snapshots.stat().st_mode) & 0o077:
            raise SyncError("snapshot directory must be private")
        deadline = time.monotonic() + OPERATION_TIMEOUT_SECONDS
        transport = transport or RcloneTransport(config, deadline)
        # Reject a repointed state directory before contacting the other target.
        latest = _latest_snapshot(state_dir, config)
        if latest is None:
            _validate_existing_snapshot_identities(snapshots, config)
        first = transport.list_inventory()
        if latest and latest[1]["inventory"] == first:
            second = transport.list_inventory()
            if first != second:
                raise SyncError("remote inventory changed while confirming an unchanged snapshot")
            manifest = latest[1]
            return _capture_result(config, latest[0], manifest, "unchanged")

        staging = Path(tempfile.mkdtemp(prefix=".capture-", dir=snapshots))
        os.chmod(staging, 0o700)
        content = staging / "content"
        content.mkdir(mode=0o700)
        try:
            for entry in first:
                if entry["is_dir"]:
                    continue
                destination = content.joinpath(*entry["path"].split("/"))
                destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                transport.download(entry["path"], destination)
                try:
                    file_info = destination.lstat()
                    if not stat.S_ISREG(file_info.st_mode) or stat.S_ISLNK(file_info.st_mode):
                        raise SyncError("download did not create a regular local file")
                    os.chmod(destination, 0o600)
                except OSError:
                    raise SyncError("download did not create a regular local file") from None
            verify_content(content, first)
            second = transport.list_inventory()
            if first != second:
                raise SyncError("remote inventory changed during download; the attempt was discarded")

            file_count = sum(not item["is_dir"] for item in first)
            total_bytes = sum(item["size"] or 0 for item in first if not item["is_dir"])
            snapshot_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:12]
            manifest = {
                "schema": 1,
                "snapshot_id": snapshot_id,
                "captured_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                "config_identity": config_identity(config),
                "root_identity": root_identity(config),
                "inventory": first,
                "inventory_sha256": inventory_digest(first),
                "file_count": file_count,
                "total_bytes": total_bytes,
                "capture_method": "rclone lsjson inventory plus verified copyto",
            }
            _write_manifest(staging / MANIFEST_NAME, manifest)
            _fsync_directory(content)
            _fsync_directory(staging)
            final_dir = snapshots / snapshot_id
            if final_dir.exists() or final_dir.is_symlink():
                raise SyncError("snapshot identity collision; attempt was discarded")
            os.rename(staging, final_dir)
            _fsync_directory(snapshots)

            link_temp = state_dir / (".latest-" + uuid.uuid4().hex)
            try:
                os.symlink(f"snapshots/{snapshot_id}", link_temp)
                os.replace(link_temp, state_dir / "latest")
                _fsync_directory(state_dir)
            except OSError:
                with contextlib.suppress(OSError):
                    link_temp.unlink()
                raise SyncError("complete snapshot retained, but latest pointer could not be updated") from None
            return _capture_result(config, final_dir, manifest, "captured")
        except Exception:
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)
            raise


def _capture_result(config: dict, snapshot_dir: Path, manifest: dict, result: str) -> dict:
    return {
        "operation": "capture",
        "result": result,
        "snapshot_id": manifest["snapshot_id"],
        "snapshot_path": str(snapshot_dir.resolve()),
        "root_identity": manifest["root_identity"],
        "inventory_sha256": manifest["inventory_sha256"],
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
    }


def _retained_summary(state_dir: Path) -> tuple[int, int]:
    snapshots = state_dir / "snapshots"
    count = 0
    total_bytes = 0
    try:
        entries = list(snapshots.iterdir())
    except OSError:
        return 0, 0
    for entry in entries:
        if not SNAPSHOT_NAME_RE.fullmatch(entry.name) or entry.is_symlink() or not entry.is_dir():
            continue
        count += 1
        try:
            manifest = _read_json(entry / MANIFEST_NAME, "invalid retained manifest")
            number = manifest.get("total_bytes")
            if isinstance(number, int) and not isinstance(number, bool) and number >= 0:
                total_bytes += number
        except SyncError:
            continue
    return count, total_bytes


def status(config: dict) -> dict:
    state_dir = config["state_dir"]
    validate_state_location(state_dir)
    with state_lock(state_dir, exclusive=False):
        latest = _latest_snapshot(state_dir, config)
        if latest is None:
            raise SyncError("no accepted snapshot exists")
        snapshot_dir, manifest = latest
        retained_count, retained_bytes = _retained_summary(state_dir)
        return {
            "operation": "status",
            "result": "verified",
            "snapshot_id": manifest["snapshot_id"],
            "snapshot_path": str(snapshot_dir.resolve()),
            "remote": config["remote"],
            "folder_id": config["folder_id"],
            "root_identity": manifest["root_identity"],
            "inventory_sha256": manifest["inventory_sha256"],
            "file_count": manifest["file_count"],
            "total_bytes": manifest["total_bytes"],
            "retained_snapshot_count": retained_count,
            "retained_bytes_estimate": retained_bytes,
        }


def _git(repo: Path, args: list[str], operation: str, deadline: float | None = None) -> bytes:
    remaining = 20 if deadline is None else min(20, deadline - time.monotonic())
    if remaining <= 0:
        raise SyncError("publication exceeded its time bound")
    try:
        result = subprocess.run(
            ["git", "--no-replace-objects", "-C", str(repo), *args],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=remaining,
        )
    except subprocess.TimeoutExpired:
        raise SyncError(f"Git {operation} exceeded its time bound") from None
    except OSError:
        raise SyncError(f"could not start Git during {operation}") from None
    if result.returncode != 0:
        raise SyncError(f"Git {operation} failed")
    return result.stdout


def git_package(repo_arg: str, revision: str, default_ref: str, config: dict, deadline: float | None = None) -> tuple[Path, dict[str, bytes]]:
    if not re.fullmatch(r"[0-9a-fA-F]{40}", revision):
        raise SyncError("revision must be a full 40-character Git commit SHA")
    try:
        repo = Path(repo_arg).resolve(strict=True)
    except OSError:
        raise SyncError("repo path does not exist or cannot be resolved") from None
    if not repo.is_dir():
        raise SyncError("repo must be a Git working tree")
    try:
        root_text = _git(repo, ["rev-parse", "--show-toplevel"], "repository discovery", deadline).decode("utf-8").strip()
    except UnicodeError:
        raise SyncError("Git returned an invalid repository path") from None
    root = Path(root_text).resolve()
    validate_state_location(config["state_dir"], root)

    commit = revision.lower()
    resolved = _git(repo, ["rev-parse", "--verify", "--end-of-options", commit + "^{commit}"], "revision validation", deadline).decode().strip().lower()
    if resolved != commit:
        raise SyncError("revision does not resolve to the requested full commit")
    ref_commit = _git(repo, ["rev-parse", "--verify", "--end-of-options", default_ref + "^{commit}"], "default-ref validation", deadline).decode().strip()
    remaining = 20 if deadline is None else min(20, deadline - time.monotonic())
    if remaining <= 0:
        raise SyncError("publication exceeded its time bound")
    try:
        ancestry = subprocess.run(
            ["git", "--no-replace-objects", "-C", str(repo), "merge-base", "--is-ancestor", commit, ref_commit],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=remaining,
        )
    except subprocess.TimeoutExpired:
        raise SyncError("Git default-ref ancestry check exceeded its time bound") from None
    except OSError:
        raise SyncError("could not check Git default-ref ancestry") from None
    if ancestry.returncode != 0:
        raise SyncError("revision is not contained in the configured default_ref")

    listing = _git(repo, ["ls-tree", "-r", "-z", "--full-tree", commit, "--", ".agents/skills/afr"], "package inspection", deadline)
    files: dict[str, bytes] = {}
    prefix = b".agents/skills/afr/"
    for record in listing.split(b"\0"):
        if not record:
            continue
        try:
            header, raw_path = record.split(b"\t", 1)
            mode, object_type, object_id = header.split(b" ", 2)
        except ValueError:
            raise SyncError("Git package tree is invalid") from None
        if not raw_path.startswith(prefix):
            raise SyncError("Git package tree contains an unexpected path")
        try:
            relpath = normalize_relative_path(raw_path[len(prefix) :].decode("utf-8", "strict"))
        except UnicodeError:
            raise SyncError("Git package path is not UTF-8") from None
        if mode not in (b"100644", b"100755") or object_type != b"blob":
            raise SyncError("Git package contains a symlink or non-regular entry")
        if relpath in files:
            raise SyncError("Git package contains duplicate paths")
        blob = _git(repo, ["cat-file", "blob", object_id.decode("ascii")], "package extraction", deadline)
        if b"\0" in blob:
            raise SyncError("Git package contains a non-text file")
        try:
            blob.decode("utf-8", "strict")
        except UnicodeError:
            raise SyncError("Git package file is not UTF-8") from None
        files[relpath] = blob

    if set(files) != REQUIRED_FILES:
        raise SyncError("Git package must contain exactly the six required raw files")
    if len(files) > config["max_files"] or sum(map(len, files.values())) > config["max_bytes"]:
        raise SyncError("Git package exceeds configured file or byte bounds")
    return root, files


def _expected_snapshot_path(expected: str, state_dir: Path) -> Path:
    supplied = Path(expected)
    if supplied.is_absolute():
        path = supplied
    elif SNAPSHOT_NAME_RE.fullmatch(expected):
        path = state_dir / "snapshots" / expected
    else:
        raise SyncError("expected must be a snapshot ID or absolute snapshot path")
    try:
        if stat.S_ISLNK(path.lstat().st_mode):
            raise SyncError("expected must identify a direct snapshot directory")
        resolved = path.resolve(strict=True)
    except SyncError:
        raise
    except OSError:
        raise SyncError("expected snapshot does not exist") from None
    snapshots_root = (state_dir / "snapshots").resolve(strict=True)
    if resolved.parent != snapshots_root:
        raise SyncError("expected must identify a direct snapshot directory")
    if not SNAPSHOT_NAME_RE.fullmatch(resolved.name):
        raise SyncError("expected snapshot name is invalid")
    return resolved


def _entry_file_map(entries: list[dict]) -> dict[str, dict]:
    return {entry["path"]: entry for entry in entries if not entry["is_dir"]}


def _require_sha256(entries: list[dict], label: str) -> None:
    if any("sha256" not in entry["hashes"] for entry in entries if not entry["is_dir"]):
        raise SyncError(f"{label} lacks SHA-256 for one or more files; publication is refused")


def _expected_after_write(current: list[dict], path: str, data: bytes) -> list[dict]:
    result = []
    for entry in current:
        updated = dict(entry)
        if not entry["is_dir"] and entry["path"] == path:
            updated["size"] = len(data)
            all_hashes = {"md5": hashlib.md5(data).hexdigest(), "sha256": sha256_bytes(data)}
            updated["hashes"] = {name: all_hashes[name] for name in entry["hashes"]}
        result.append(updated)
    return result


def publish(config: dict, repo_arg: str, revision: str, expected: str, writers_paused: bool, transport=None) -> dict:
    if not writers_paused:
        raise SyncError("publication requires the caller's --writers-paused assertion")
    state_dir = config["state_dir"]
    validate_state_location(state_dir)

    with state_lock(state_dir, exclusive=True):
        deadline = time.monotonic() + OPERATION_TIMEOUT_SECONDS
        transport = transport or RcloneTransport(config, deadline)
        snapshot_dir = _expected_snapshot_path(expected, state_dir)
        manifest = verify_snapshot(snapshot_dir, config)
        _require_sha256(manifest["inventory"], "expected snapshot")
        _, source_files = git_package(repo_arg, revision, config["default_ref"], config, deadline)
        baseline_files = _entry_file_map(manifest["inventory"])
        if set(source_files) != set(baseline_files) or set(source_files) != REQUIRED_FILES:
            raise SyncError("Git package and expected snapshot must have the same six-file set")
        snapshot_content = snapshot_dir / "content"
        snapshot_bytes = {
            path: snapshot_content.joinpath(*path.split("/")).read_bytes() for path in sorted(baseline_files)
        }
        changed = [path for path in sorted(source_files) if source_files[path] != snapshot_bytes[path]]

        # The first fresh observation is the stale-snapshot guard and the pre-write check.
        current = transport.list_inventory()
        _require_sha256(current, "current target")
        if current != manifest["inventory"]:
            raise SyncError("expected snapshot is stale; no publication writes were made")

        staging = Path(tempfile.mkdtemp(prefix=".publish-", dir=state_dir))
        os.chmod(staging, 0o700)
        source_root = staging / "source"
        verification_root = staging / "verification"
        source_root.mkdir(mode=0o700)
        verification_root.mkdir(mode=0o700)
        try:
            for relpath, data in source_files.items():
                output = source_root.joinpath(*relpath.split("/"))
                output.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                output.write_bytes(data)
                os.chmod(output, 0o600)

            completed = 0
            for index, relpath in enumerate(changed):
                if index > 0:
                    observed = transport.list_inventory()
                    _require_sha256(observed, "current target")
                    if observed != current:
                        raise SyncError("remote changed during publication; stopped before the next copy")
                local_file = source_root.joinpath(*relpath.split("/"))
                transport.upload(local_file, relpath)
                current = _expected_after_write(current, relpath, source_files[relpath])
                completed += 1

            # Verify the full remote bytes and IDs, then verify inventory stability across downloads.
            observed = transport.list_inventory()
            _require_sha256(observed, "final target")
            if observed != current:
                raise SyncError("final remote inventory differs from the expected in-place publication")
            for relpath in sorted(source_files):
                destination = verification_root.joinpath(*relpath.split("/"))
                destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                transport.download(relpath, destination)
            verify_content(verification_root, current)
            for relpath, source_bytes in source_files.items():
                if verification_root.joinpath(*relpath.split("/")).read_bytes() != source_bytes:
                    raise SyncError("final downloaded bytes differ from the immutable Git source")
            final_inventory = transport.list_inventory()
            _require_sha256(final_inventory, "final target")
            if final_inventory != current:
                raise SyncError("remote inventory changed during final verification")
            final_ids = {entry["path"]: entry["id"] for entry in final_inventory if not entry["is_dir"]}
            original_ids = {entry["path"]: entry["id"] for entry in manifest["inventory"] if not entry["is_dir"]}
            if final_ids != original_ids:
                raise SyncError("publication changed one or more Drive file IDs")
            source_digest = sha256_bytes(
                canonical_json([{"path": path, "sha256": sha256_bytes(source_files[path])} for path in sorted(source_files)])
            )
            return {
                "operation": "publish",
                "result": "verified",
                "revision": revision.lower(),
                "default_ref": config["default_ref"],
                "source_sha256": source_digest,
                "snapshot_id": manifest["snapshot_id"],
                "root_identity": manifest["root_identity"],
                "inventory_sha256": inventory_digest(final_inventory),
                "changed_files": completed,
                "file_count": len(source_files),
                "total_bytes": sum(len(data) for data in source_files.values()),
            }
        except SyncError as exc:
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)
            if changed and "no publication writes" not in str(exc):
                raise SyncError(f"{exc}; publication stopped. Reobserve the target before any recovery.") from None
            raise
        except Exception:
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)
            raise SyncError("publication stopped after an unexpected error; reobserve the target before any recovery") from None
        finally:
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture verified AFR Drive snapshots or publish an immutable Git revision.")
    parser.add_argument("--config", required=True, help="private JSON configuration")
    subparsers = parser.add_subparsers(dest="operation", required=True)
    subparsers.add_parser("capture", help="capture or verify the latest snapshot")
    subparsers.add_parser("status", help="verify and report the latest local snapshot")
    publish_parser = subparsers.add_parser("publish", help="publish a reviewed Git commit to Drive")
    publish_parser.add_argument("--repo", required=True, help="trusted Git repository")
    publish_parser.add_argument("--revision", required=True, help="full 40-character commit SHA")
    publish_parser.add_argument("--expected", required=True, help="verified snapshot ID or absolute path")
    publish_parser.add_argument("--writers-paused", action="store_true", help="assert the Drive target has a quiet editing window")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = load_config(args.config)
        if args.operation == "capture":
            result = capture(config)
        elif args.operation == "status":
            result = status(config)
        else:
            result = publish(config, args.repo, args.revision, args.expected, args.writers_paused)
        sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
        return 0
    except SyncError as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 1
    except KeyboardInterrupt:
        if args.operation == "publish":
            sys.stderr.write("error: publication interrupted; reobserve the target before any recovery.\n")
        else:
            sys.stderr.write("error: interrupted; no partial snapshot was promoted. Inspect private temporary state before cleanup.\n")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
