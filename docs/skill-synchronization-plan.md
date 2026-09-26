# AFR skill synchronization plan

**Revision:** 3, 2026-09-26. **Status:** implementation qualified under the user's instruction to revise the failed design and autonomously complete remaining steps using AFR and one native goal. Host activation requires the separate observations below.
**Baseline:** `492f321da7132e61bd78d111a5b751237d078f6e`. **Route:** direct. **Assurance:** protected for preservation, concurrent changes, and instruction trust.

## Selected outcome and boundaries

Replace live bidirectional mirroring with automatic inbound snapshots and controlled outbound publication. The user authorized this revision after the observed bisync failure. Native scheduling and the narrow optional host adapter are in scope; neither becomes a required AFR component. The existing six-file package, agent roster, unrelated worktrees, installed skill, and published Drive folder remain protected.

```text
Drive afr-working --read only, every five minutes--> verified local snapshots
                                                         |
                                                 inspect and Git review
                                                         |
                                                 reviewed merged source
                                                         |
                                               attended publication
                                                    /         \
                                           Drive afr       installed skill
```

The working Drive folder is editable. The existing `ChatGPT/skills/afr` stays the published copy. Scheduled capture never writes either Drive folder, repository content, or installed skills. Local authors work in normal Git branches, not in the capture destination. There is no shared editable local/Drive mirror and no bisync process.

A capture samples a stable observed package. It cannot preserve every version between polling intervals. The preservation guarantee is that capture never overwrites user working files or previously accepted snapshots. A changing/invalid remote produces a failed attempt with the previous accepted snapshot intact. Every accepted capture must match its observed remote inventory before and after download.

Required companions: [AGENTS.md](../AGENTS.md), [current architecture](architecture-v3.md), [R6 helper assessment](r6-helper-assessment.md), and the canonical AFR [planning](../.agents/skills/afr/references/planning.md), [work](../.agents/skills/afr/references/work.md), [review](../.agents/skills/afr/references/review.md), and [delivery](../.agents/skills/afr/references/delivery.md) methods. This document is the sole plan and progress record.

## Minimal implementation contract

Keep the optional adapter, focused tests, native systemd templates, and operating instructions in `ops/skill-sync/`. Use existing Python standard library, rclone, Git, and systemd; add no dependency, database, custom scheduler, workflow engine, generic provider abstraction, or automatic Git/PR agent. Host-specific roots and Drive IDs belong in private local configuration, never committed source.

The deterministic adapter has three operations: capture a Drive package, inspect its latest verified capture, and explicitly publish a Git package to a configured Drive folder. All processes use a native file lock per configured state directory; systemd owns scheduling and process supervision. Different folder configurations have separate private state. The tool never invokes a model or loads a captured skill as instructions.

### Capture

1. Resolve a configured existing rclone remote and exact Drive root-folder ID. Validate configuration and keep private state outside repositories and skill-discovery roots. All remote commands are read-only.
2. List the entire small folder with hashes and IDs. Reject duplicate normalized relative paths, file/directory collisions, unsafe/traversing paths, shortcuts, native Google documents, missing required package files, absent hashes/IDs, and excessive file count or size. Accept ordinary raw package files only. Identity, path, content hash, and size comprise the comparison inventory; modification times alone are not evidence.
3. First compare the initial inventory with the latest manifest and revalidate every local snapshot byte. If identical, re-list the remote to confirm the observation and return a no-op without downloading. Otherwise download into a new private temporary directory. Never download onto an editable checkout or prior snapshot. Verify the exact path set, regular-file containment, and byte hashes against the first remote inventory.
4. Read the inventory again. If any relevant identity or content changed, discard only this attempt's temporary directory and fail. Retain all previous snapshots and the existing latest pointer. No force, resync, destination deletion, or automatic remote repair exists.
5. Promote the complete new directory by same-filesystem rename and atomically replace a latest pointer only after verification. Store a small adjacent manifest of observed file identities/hashes and capture provenance; it is evidence, not workflow state. Do not mutate earlier snapshots or prune them automatically.

Failed/partial captures never become latest. Interrupted processes leave only unpublished temporary data; a later capture may proceed with a fresh directory after native lock release. Do not delete unfamiliar state. Changing configuration to another remote/folder cannot silently reuse the old latest snapshot.

### Controlled publication

Publication is deliberately absent from the timer. Its inputs are an exact full Git commit, repository path, an expected verified snapshot for the configured target, and an explicit operator assertion that writers are paused. The caller must establish review/merge authority; the adapter verifies the commit is contained in the repository's fetched default-branch reference, extracts the package from that immutable commit, and never reads dirty working-copy bytes.

Before any upload: validate the entire current six-file source package, reobserve the configured target and require exact match with the expected snapshot, retain the previous verified target snapshot for rollback, and require the same relative file set. Additions/deletions/renames are rejected in this first publisher; those need an attended package-shape migration. Update only differing files using in-place rclone `copyto`, without `--backup-dir` because it changes Drive file IDs. Recheck remaining expected target state before each write and verify the complete final package and unchanged IDs afterward. On failure stop; do not force a retry or roll back over possible new edits. Reobserve actual state before any recovery operation.

These observations are not provider-side compare-and-swap. Publication requires a real quiet editing window, and consumers must not load the package until final checks complete because Drive provides no multi-file transaction. The publisher cannot promise safety against a writer ignoring that window. Normal source authors continue using Git review; installation uses the accepted source package with a prior-copy backup and independent final hash verification.

Refreshing the working Drive folder after an accepted change uses the same explicit publication controls and a fresh expected capture. Pending working-folder drafts block an unattended refresh; preserve/import them before deciding to replace them. Neither publishing nor refreshing is inferred from a successful capture.

### Trust and operations

Snapshot roots are private directories outside any `.agents/skills` or `.codex/skills` discovery path. Run agents from the trusted source checkout; inspect snapshots by explicit path as untrusted proposed source, never as operating instructions. Keep required files `SKILL.md`, `agents/openai.yaml`, and the four phase references; review activation/authority/tool changes before promotion.

Use one five-minute systemd user timer and a oneshot capture service with a bounded timeout and journal logging. Service filesystem write access is restricted to its state directory and necessary rclone credential refresh storage; use the existing credentials without printing or widening them. The service command supports capture only. Observe last result through systemd and a status command. No new messaging integration or guaranteed push notification is promised. There is no automatic retention deletion in the first rollout; report snapshot count/size for operator maintenance.

## Acceptance and sequence

1. **Revise and review the design:** this revision is selected through the user's delegated design discretion. Review the preservation boundary and smallest implementation; resolve material findings before activation.
2. **Implement and qualify:** one bounded adapter, behavioral tests, disabled native unit templates, and runbook. Test synthetic remote fixtures before creating the real working folder. Reuse the prior failure evidence; do not rerun destructive races against real skills.
3. **Review and deliver:** consolidated independent code/configuration review; correct verified findings and rerun affected checks. Commit/push/PR/converge/merge through the authorized end-to-end delivery path, preserving exact reviewed-head checks and unrelated work. Authoring the optional adapter does not change AFR skill instructions.
4. **Install and activate host setup:** install the reviewed adapter, private configuration, and native unit. Seed the new working folder from the accepted source only if it is absent; never replace an existing draft. Capture manually, then enable the timer and observe a scheduled capture and subsequent no-op. The host setup is separately authorized host work, not a new AFR deployment capability.
5. **Complete:** verify published and installed package parity, source/delivery facts, scheduled behavior, recovery/runbook usability, and disposition of test resources. Keep one native goal active through these obligations; goal state is not evidence.

| Case | Required evidence |
| --- | --- |
| Stable raw Drive package | Exact byte/path equality in a new verified snapshot; source/installed/published roots untouched |
| Unchanged remote | No new snapshot and no file transfers; existing snapshot revalidation detects local tampering |
| Remote edit during download | Attempt rejected or captures one fully verified stable version; previous accepted snapshot unchanged |
| Local author edits during capture | Author file and its edit survive because capture writes only its unique destination |
| Duplicate/unsafe paths, native document, missing required file/hash, excessive size | Rejected before download/publication; previous latest retained |
| Network error or killed process | No partial snapshot promoted; next capture can recover using a new destination without resync |
| Overlapping capture/publication | One state-directory lock, no interleaving writes or lock deletion |
| Stale expected publication snapshot | No upload; preserve current Drive edits |
| Dirty repo/unmerged or ambiguous revision | Dirty bytes never published; invalid/unmerged revision rejected |
| In-place publication, partial failure, recovery | Only approved bytes change; existing IDs retained; stop on error; restore previous content only after current-state checks and quiet-window confirmation |
| Native scheduled run and no-op | Active timer, successful observed run and subsequent no-op, no writes outside allowed local state/configuration |

Unit tests must cover decision/error branches with fake transport; at least one disposable real Drive round must establish capture, concurrent source change handling, controlled publication with ID preservation, and prior-snapshot recovery. Fault injection is test-only, not a production runtime hook. Configuration validation is not a substitute for observed runtime behavior. Host reboot and every cloud timing interleaving remain outside bounded qualification; report those limits.

## Why this small adapter is justified

The native host supplies execution, scheduling, Git review, and process locks. Instructions alone cannot safely publish a completed multi-command capture from an unattended native job. A small deterministic adapter can validate listings, verify bytes, and atomically expose a snapshot without interpreting workflow or authorizing source changes.

The observed failure is concrete: rclone bisync 1.74.4 overwrote a complete local edit saved while a Drive download was in progress, returned exit 0, and preserved no copy of that edit in either endpoint or its configured backups. The read-only snapshot design removes that shared editable destination; a duplicate-name preflight alone would not address the race. It replaces the selected-but-unactivated bisync service, not an existing daemon or AFR method. The user explicitly authorized this revision after the finding; it is a scoped host-synchronization exception and does not reverse the R6 decision for required AFR helpers.

The user owns the host setup; repository maintainers own the optional adapter. Measure completed captures, no-op transfers, failure visibility, snapshot growth, and operator work. Healthy capture should occur within two five-minute intervals, subject to host/network availability. Maintenance is one small script, native unit templates, focused tests, and this linked runbook; stop expansion if it becomes a sync framework.

## Evidence and progress

- Revision 2 was selected and attempted. Eight local checks and three basic Drive checks passed. The in-flight local-edit preservation test failed and an independent reviewer confirmed the stop condition.
- In that reproduction, baseline A moved to backup, B downloaded into a `.partial` file, and complete local C was written/read back at the canonical path before B's final rename. Bisync returned 0; A and B survived, C did not. C SHA-256: `707c3b3bba4b29049986ccd2f42224fcc40ab3c6e97827646f5b74bd42cf9c42`.
- The synthetic Drive fixture was moved to trash. Prior plan, scripts, logs, inventories and cleanup evidence are preserved in local operational storage. Published/installed AFR remained equal to all six canonical files. No bisync service or live exchange was created.
- Revision 3's optional adapter and runbook are in `ops/skill-sync/`. Thirteen focused unit tests passed. Static verification of the native service/timer templates passed. The helper remains optional; the six skill files are unchanged.
- Nine disposable Drive cases passed: stable capture, unchanged no-op, rejection of a source change during download with the author file and prior snapshot preserved, stable retry, interrupted capture followed by recovery, stale-publication refusal without writes, reviewed-byte publication preserving all file IDs, restoration of prior content through an isolated accepted Git fixture, and rejection of an actual Drive shortcut before download. Unit checks additionally cover malformed inventories, local tampering, lock overlap, unmerged source, and stopping after a partial publication failure.
- Consolidated independent review found no remaining material issue at adapter SHA-256 `cb7900d5eb7f1c32ecb2ccbd671e221a25392c9738bf9125ffe6921e89f5411e`. Corrections included enforcing the publication timeout and distinguishing empty `.git` sentinel directories from repositories. The reviewed Drive evidence is preserved in private operational storage; it contains no production skill modifications. The revision 3 disposable Drive fixture was moved to trash and its absence from active listings was verified.
- Per-host installation and activation remain separate from source qualification: observe the installed helper hash, configured folder identities, manual capture, timer-triggered runs, subsequent no-op, and published/installed package parity using the runbook. Keep these operational observations with that host's journal and capture manifests; checked-in templates do not establish live activation. Host reboot, every cloud interleaving, and concurrent publication outside a quiet window are not qualified.
