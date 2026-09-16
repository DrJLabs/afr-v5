# R4 bounded delivery trials

These are native-agent trials of the [R4 delivery path](../../docs/roadmap.md#r4--pr-convergence-and-delivery). Forge responses are controlled by a human/parent test operator; source edits, test commands, and Git operations use real disposable local repositories. Simulated PR/check/review/merge responses are not evidence of a live hosting service, an independent review of the fixture, or production readiness. No emulator or watcher is added to AFR.

## Setup and permitted effects

Keep the skill checkout separate from each target. Copy the [R3 parcel fixture](../r3/fixtures/) into disposable Git repositories and install [delivery-policy.md](fixtures/delivery-policy.md) as their `AGENTS.md`. Use local bare repositories as remotes, seed `main` and `feat/report`, and record starting refs, inventories, and bytes. The trial's current user request may authorize delivery beyond the fixture specification's old local-only endpoint; its behavioral acceptance remains binding. Do not give agents this result record or expected decisions.

For correction, seed a candidate whose formatter still emits raw status values and a PR-create response that timed out. Supply forge responses only when the agent requests observations or operations. Git commits/pushes are permitted only to the disposable local remote. The operator can apply a simulated successful merge to that remote using native Git, so the agent can verify and synchronize actual refs. No actual forge service, network publication, installation, dependency, or repository setting is in scope.

For synchronization, clone an old `main` into two checkouts before the operator merges the fixed feature into the local remote. Leave one clone clean; give the other an overlapping `LOCAL ` formatter edit and an unrelated untracked note. Supply the simulated merged PR identity and actual merge revision. Permit safe local synchronization, not source correction, stashing, reset, or cleanup.

A separate resource-backed target can exercise readiness through supplied forge observations without a local checkout. Give it explicit check/review policy and native-monitor limits. Operations are requests to the operator, not actual hosting-service mutations. Preserve the action order and arguments, especially any expected-head condition. Do not supply the skill authoring discussion, intended answer, or a proposed fix.

## Cases and evidence criteria

| Case | Evidence to assess |
| --- | --- |
| Lost PR-create response | Observe and reuse one exact match rather than issue another create; report conflicting matches as unresolved identity |
| Review correction | Verify feedback against source/acceptance, batch valid fixes, preserve unrelated work, execute affected tests, and return the pushed head to monitoring |
| Readiness changes | Distinguish missing, pending, failed, unknown, and old-head evidence; do not infer readiness from mergeability or an optional bot's aggregate success |
| Conditional merge and uncertain result | Request the exact reviewed head, reject a head race rather than substituting a new head, and observe a lost merge response before considering a retry |
| Partial delivery and resume | Distinguish remote merge from local synchronization; fast-forward a safe target and preserve an overlapping dirty target without repeating implementation/merge |

The [donor scenarios](../../docs/donor-matrix.md#5-evaluation-scenarios) retain the broader E10–E13/E15 contract. This bounded set is not an exhaustive fault matrix, broad repository qualification, or cross-host benchmark.

## Observed results — 2026-09-15

Three fresh native Luna agents loaded the package by explicit path, with raw targets and requests but without this results table, authoring discussion, or other agents' conclusions. One exercised correction/delivery, one exercised readiness and then a separate head-race case, and one exercised two local views of an already-merged PR. The operator supplied observations across turns, not a forge client or live service. Child messaging was unavailable, so the operator used returned requests and follow-up responses; it clarified that only concrete operations, not conditional future action lists, would be executed. This is controlled forward-testing, not proof of unattended tool integration or zero-intervention delivery.

| Case | Observed behavior |
| --- | --- |
| Lost create response and existing PR | The supplied exact lookup resolved one existing PR after the earlier create timeout. The agent reused it; no duplicate create was requested. The operator supplied that lookup before publication, so autonomous discovery of the lookup is not established. |
| Correction and feedback | The agent first verified the source acceptance gap, then made one correction commit affecting only `cli.py` and `test_parcel.py`. Supplied feedback identified the same formatter/test gap, a duplicate, and an incorrect claim that IDs used numeric sorting. It classified these as fixed, duplicate, and rejected with source evidence. |
| Fresh-head convergence | The agent pushed the correction to the real local bare remote, then requested checks/review on the new head. When the operator returned pending tests and in-progress review, it requested monitoring and explicitly withheld merge. Only after current-head success and clean review did it request a guarded merge. An optional bot's successful status with a quota-exhausted body was not treated as a completed review. |
| Missing/pending/failed/unknown evidence | In the resource-backed case, the agent rejected stale review after a head change, withheld merge for a pending then absent required check, and stopped on a deterministic failure without a blind retry or unauthorized source fix. A later authorized observation returned HTTP 503 with no check payload; it treated the result as unavailable, not empty/successful, and stopped at the native monitor's four-cycle cap. No merge request occurred in this lane. |
| Conditional merge and lost response | The correction agent requested merge with the exact full reviewed SHA. After the simulated operation timed out, its next operation was a PR observation, not a second merge. The operator returned the merged identity and actual local-remote merge revision; the agent then fetched and fast-forwarded local `main`. |
| Head race and user stop | A separate ready PR received an exact-head guarded merge request. The operator rejected it with HTTP 409 because the head changed in flight. The agent requested fresh observations instead of substituting the new SHA into a retry. A user stop preceded the late green read response; the agent reported the open PR without further mutation or monitoring. |
| Local synchronization | The synchronization agent fetched both clones, fast-forwarded the clean clone to the actual remote merge, and left the overlapping dirty clone at its original revision. It reported the remaining sync obligation separately and did not reset, stash, edit source, delete branches, or repeat implementation/merge. |

The correction candidate's six test methods passed in the agent run and in a parent run. Parent inspection additionally exercised **14 exact API/CLI boundary checks**: known/unknown labels, empty input, duplicate replacement, lexical ordering, totals/newlines, and unchanged exit codes/input records. Only the intended formatter and tests differed from the seeded candidate; requirements, domain code, and unrelated fixture files were unchanged. No bytecode or other generated files remained.

Parent Git observations confirmed the correction commit `81c6898676b04c3044b4568eaae79f7024c97270` was published only to its disposable bare remote, and that local `main`, fetched `origin/main`, and the live local-remote target all matched merge `8ae1cd0ca2de41d0f3a132823f91459e394b2d6e`. The source branch remained intact. These are actual Git facts, not a GitHub PR result.

The separate clean synchronization clone reached `f31cc185e6c2b8cfe8e85f995a0a4b4284db5d2b`; the dirty clone stayed at `6aea9b2f1490102020531a6b489ccc7914f1bd51`. Parent hash comparisons confirmed the overlapping formatter edit and untracked note were byte-for-byte preserved. The operator owned all disposable copies; their final disposition is recorded below.

### Package identity and review

The trial package remained unchanged throughout these cases:

| File | SHA-256 |
| --- | --- |
| [SKILL.md](../../.agents/skills/afr/SKILL.md) | `243ee551ee6bfadd654f0bb28f908c9d7163f36cfaa5e2aac81526cb8e0abc1e` |
| [delivery.md](../../.agents/skills/afr/references/delivery.md) | `f98cb320c5dbbdb196a75ac88b3bfba091bf2dbb0f7c15d0bf44d82fc0e827a6` |
| [planning.md](../../.agents/skills/afr/references/planning.md) | `3ead7fbc0d239887fbb2744fc3b04c0b1213f82c89ea682ba33d3580b64d4db7` |
| [review.md](../../.agents/skills/afr/references/review.md) | `798300c880684da9c7acae885d3add01e339d2a9b76547d5278d2882f6f9722e` |
| [work.md](../../.agents/skills/afr/references/work.md) | `bba142a832487ce4d21836f059bf70a0211894274575547b9123390c38cffafe` |
| [openai.yaml](../../.agents/skills/afr/agents/openai.yaml) | `a1499d95abd8447558c535fe5554adcc3c9b988a0a39264a6283d430effe1e94` |

One consolidated independent package reviewer found no material findings in the coordinator, phase methods, and documentation. No skill correction was required by these trials. Metadata validation, Markdown links/anchors and tables, whitespace, and scoped privacy checks are separate structural evidence, not substitutes for behavioral observations.

### PR review correction and affected-case refresh

Subsequent PR review identified an ordering ambiguity: the delivery method requested a PR's head/base before creating a new PR. The corrected method distinguishes an existing matching PR from a confirmed empty lookup, creates the latter first, then observes its identity/head/base. The revised `delivery.md` SHA-256 is `d6e643dba6e6a956dd779228a4e49025ee5c0009adc64a1e29410fa1b1479968`; the other package hashes above are unchanged.

A fresh native agent received a resource-backed documentation candidate, explicit PR-creation-only authority, and a complete empty matching-PR lookup. It requested creation with the exact repository/source/base and concise scope/check context, then returned the created identity/head/base after the operator's response. It did not request fixes, monitoring, merge, or cleanup. This narrowly refreshes new-PR creation ordering/body behavior using controlled responses, not live-forge integration. The original cases above were not rerun or reassigned to the revised hash. Skill validation and whitespace checks passed.

### Limits and complexity

R4 adds one 48-line delivery reference and three coordinator lines: one public skill, four phase references, zero required custom helpers, watchers, services, or databases. Planning/work and explicit-only metadata are unchanged. The review reference only extends its dispatch description to PR feedback; classification/correction still has one owner. No new public API, persistent lifecycle state, runtime dependency, installation, or legacy AFR activation was introduced.

The operator's controlled forge responses do not qualify real API parameter compatibility, authentication, branch protection enforcement, CI execution, reviewer correctness, merge queues, pagination behavior, or a real monitor's lifecycle. A simulated current-head review is not an independent review of the fixture. The native Git tests do not qualify shared-worktree races, divergence, ignored/index-hidden collisions, squash/rebase synchronization, or remote deletion. Conflicting PR matches, response-lost push, unavailable merge-guard tools, and active mutation interruption were not forward-tested. Fresh PR body creation was exercised only in the affected-case refresh above. Explicit-path loading is not host-catalog discovery; ChatGPT and broad host/UI parity remain unqualified.

The local Python checks used Python 3.12.3, not a Python 3.10 runtime. No full R2/R3 rerun, broad benchmark, or integrated release qualification occurred. At the time of this R4 trial, R5 umbrella execution was still unavailable. The actual merge of this authoring repository's R3 PR preceded R4 implementation and is not R4 behavioral evidence.

After final ref, ownership, worktree, symlink, and byte-preservation checks, the parent removed the five owned disposable checkouts and two local bare remotes. No trial agent performed cleanup. Reusable inputs and bounded evidence remain here; transient trial repositories and transcripts are not project artifacts.

### Historical scope

This is the historical R4 delivery record. R5 umbrella continuation has a separate bounded [R5 trial record](../r5/README.md), which owns its observations and limits.
