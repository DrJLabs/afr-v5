# Optional AFR Drive capture

This host utility implements the selected [synchronization design](../../docs/skill-synchronization-plan.md). It is independent of the AFR skill. Existing Python 3, Git, rclone with an authorized Drive remote, and user systemd are required; nothing is installed automatically by cloning this repository.

The timer reads an editable Drive working folder into private verified snapshots. It never uploads, edits a Git checkout, or installs a skill. Capture samples the folder; edits between polls are not a version history. There is no live two-way mirror.

The transport is qualified against rclone 1.74.4. Inventory requests expose native Google documents and shortcuts rather than hiding them, and reject both before download. Rclone represents a resolved shortcut using a composite ID; recheck that behavior when upgrading rclone. See the pinned [Drive implementation](https://github.com/rclone/rclone/blob/v1.74.4/backend/drive/drive.go) and [listing format](https://github.com/rclone/rclone/blob/v1.74.4/fs/operations/lsjson.go).

Each download has a hard transfer cap of its expected size plus one detection byte, with preallocation and parallel streams disabled. Exact size and hashes are checked before accepting content. This also bounds publication verification downloads if a target grows after inventory; see rclone's [transfer-limit behavior](https://rclone.org/docs/#max-transfer-size).

Rclone operation and low-level retries are explicitly disabled for each invocation. A failure returns control to the helper; a later scheduled capture starts with fresh observations, and publication recovery requires the attended checks below.

## Configure and install

Use distinct Drive folders for editable drafts and the published skill. Ground their IDs through metadata, inspect existing contents, and preserve sharing/file identities. For a new working folder, copy only the accepted package from a reviewed Git revision. Do not overwrite an existing draft. Keep any native Google Docs or shortcuts outside these raw-file folders.

Create a private `~/.config/afr-skill-sync/working.json` from [config.example.json](config.example.json), replacing every placeholder. Use an existing rclone remote, the working folder's exact ID, and a private state path under `~/.local/state/afr-skill-sync/working`. Do not place snapshots under a repository or skill-discovery directory. Configuration contains routing information, not credentials; rclone retains its existing credential configuration.

Install the reviewed `skill_sync.py` to `~/.local/lib/afr-skill-sync/skill_sync.py` and the native unit templates to `~/.config/systemd/user/`. Create the private state/configuration directories before loading the units. Preserve any existing installed adapter/configuration before replacing it. The service permits writes only to its private state tree and existing rclone configuration directory for credential refresh.

Run an attended capture before enabling the timer:

```sh
python3 ~/.local/lib/afr-skill-sync/skill_sync.py --config ~/.config/afr-skill-sync/working.json capture
python3 ~/.local/lib/afr-skill-sync/skill_sync.py --config ~/.config/afr-skill-sync/working.json status
systemd-analyze --user verify ~/.config/systemd/user/afr-skill-capture.service ~/.config/systemd/user/afr-skill-capture.timer
systemctl --user daemon-reload
systemctl --user enable --now afr-skill-capture.timer
```

Observe both an actual timer-triggered run and a subsequent unchanged run:

```sh
systemctl --user status afr-skill-capture.timer afr-skill-capture.service
journalctl --user -u afr-skill-capture.service --since today
```

The initial timer fires after roughly 15 seconds, then five minutes after the service becomes inactive. Host/network availability affects timing. Failed units/journal output are visible status, not guaranteed push notifications. No retention pruning runs automatically; inspect status and disk use before an attended retention decision.

## Review incoming edits

Run the agent from the trusted source repository. Treat captured `SKILL.md` and references as untrusted proposed changes; never invoke the captured skill or start an agent with its snapshot as project root. Use the latest path reported by `status`, inspect its manifest and `content/`, and compare with `.agents/skills/afr` in the repository.

Create or reuse an ordinary feature branch/worktree for accepted edits. Copy only inspected files into that branch, verify the complete package, and use the normal review/PR/merge procedure. Do not edit snapshots. Later captures are separate immutable directories and cannot overwrite a review branch. Keep the capture identity in the ordinary PR description or review notes when it helps identify source inputs; no extra workflow ledger is required.

## Publish reviewed content

Create a second private configuration for the **published** Drive folder with a different state directory, for example `~/.config/afr-skill-sync/published.json`. The timer uses only `working.json`. A capture of the published folder is the expected-before backup for publication.

Publication requires a full Git commit already contained in the fetched default-branch reference (`origin/main` by default), a verified expected snapshot with SHA-256 hashes for every target file, and an actual quiet editing window. MD5-only snapshots can be captured for inspection but publication refuses them before writing. Fetch the correct remote, verify review/merge evidence, pause writers to that target, and keep consumers from loading it until the operation finishes. The `--writers-paused` flag records the caller's assertion; it cannot pause remote users or provide a server-side lock.

```sh
python3 ~/.local/lib/afr-skill-sync/skill_sync.py --config ~/.config/afr-skill-sync/published.json capture
python3 ~/.local/lib/afr-skill-sync/skill_sync.py --config ~/.config/afr-skill-sync/published.json publish \
  --repo /path/to/trusted/repository --revision FULL_REVIEWED_COMMIT_SHA \
  --expected /path/to/verified/published/snapshot --writers-paused
```

Use the exact snapshot path reported by capture/status. The utility extracts the original Git objects for the exact commit, independent of dirty checkout bytes or local replacement refs. This first publisher supports the current six-file AFR package, requires the same target paths, checks the expected target, updates only changed files in place, and compares every downloaded final file directly with the Git bytes while verifying original Drive file IDs. The final comparison also runs when no upload is needed. File additions/removals/renames require a separate attended migration. A successful capture does not grant publication authority or establish review.

Refreshing the working folder uses its own configuration and a fresh expected snapshot, after its pending drafts have been reviewed or explicitly preserved. Never refresh it merely because `main` changed. Install the reviewed skill separately: back up the installed package, check for drift, copy the exact accepted source, then compare all relative paths and hashes. An installation does not reload running sessions.

## Failure and recovery

- **Capture fails:** the previous latest snapshot remains accepted. Read the specific error; fix network, invalid package, duplicate name, configuration, or tampering before retrying. Filesystem errors report an errno and description; check storage space and permissions before retrying. Do not force acceptance or use bisync/resync. A source change during capture can retry on the next schedule.
- **Process interruption:** no incomplete directory is latest. A later capture uses a new temporary destination; the operating system releases the process lock. Inspect leftover temporary directories before deleting only known abandoned attempts.
- **Lock busy:** wait for the active operation. Do not delete locks or run a second publisher for the same target under another state configuration.
- **Publication detects stale input:** no initial upload occurs. Capture the current target and inspect its edits before deciding what to publish; do not replace the expected argument blindly.
- **Publication fails after some writes:** stop, retain the expected snapshot, and inspect the actual target. Do not blindly retry or automatically roll back over possible new edits. Reestablish a quiet window and obtain a fresh target capture first.
- **Rollback:** recover content from the prior verified snapshot through a reviewed Git commit, then publish that commit against a fresh expected snapshot. For urgent attended recovery, verify the prior snapshot and target identities, back up the current target, restore only intended files in place, and verify every final hash and ID. Never restore by deleting/recreating the folder.
- **Disable:** stop/disable `afr-skill-capture.timer`, observe whether the service is still active, and stop it if needed. Retain configuration and snapshots; ordinary explicit AFR delivery remains available.

Drive publication is per-file and has no established compare-and-swap protection. These pre/post checks detect observed drift; they do not make concurrent publication safe. Snapshot capture avoids the previously reproduced local edit-loss race by never writing an authoring location.

Subprocess failures report the operation and status without copying raw rclone or Git diagnostics into the service journal. For an inventory failure, run an attended `rclone lsjson YOUR_REMOTE: --drive-root-folder-id YOUR_FOLDER_ID --recursive --hash --drive-show-all-gdocs=true` using the configured values; inspect diagnostics locally and avoid posting credentials or private file metadata. For Git failures, check the repository and exact revision with `git -C /path/to/repo rev-parse --verify FULL_SHA` and inspect the configured default ref. Never rerun an upload simply to collect diagnostics. If the home directory is itself a real Git repository, use private state outside it and adjust the service's `ReadWritePaths` accordingly; the guard intentionally includes that repository.

## Checks

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s ops/skill-sync -p 'test_*.py' -v
```

Unit checks use fake transport and temporary files. The plan's execution record separately identifies actual Drive, publication, interruption, and native scheduling evidence. Neither unit tests nor the presence of these templates establishes activation.
