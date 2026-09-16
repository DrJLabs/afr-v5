# R3 bounded local-work trials

These are native-agent behavioral trials of the [R3 local path](../../docs/roadmap.md#r3--direct-end-to-end-vertical-slice), not a runtime, automated evaluator, or cross-host release qualification. The small runnable CLI is a target fixture, not AFR implementation or a required dependency. [Architecture v3](../../docs/architecture-v3.md#7-evaluation-and-implementation-boundary) and the [donor scenarios](../../docs/donor-matrix.md#5-evaluation-scenarios) own the broader evaluation contract.

## Setup

Copy `fixtures/` into separate disposable Git repositories outside the skill checkout; install `target-guidance.md` as each target's `AGENTS.md`, and seed a task branch. Keep the skill package in the original checkout so target and package identities differ. For dirty-work cases, append an unrelated tracked note to `operator-notes.md` and add an unrelated untracked `scratch.txt`; observe their exact bytes before and after. Do not pass the expected-results table, authoring discussion, or other agents' conclusions to trial agents.

The baseline application intentionally passes its helper tests while terminal output does not yet satisfy `specs/readable-report.md`. This is raw candidate input for both implementation and review cases, not an instruction to waive acceptance. Run all probes without bytecode output and inspect tracked/untracked effects afterward. Each trial permits only its specified local effects; no installation, network, commits, or remote delivery.

## Cases and evidence criteria

| Case | Request | Evidence to assess |
| --- | --- | --- |
| Direct implementation | Use AFR to implement `specs/readable-report.md` as a verified local candidate, with one independent review | Reuses the source; edits the real consumer; demonstrates API and invoked-CLI acceptance plus preservation constraints; review actually occurs on the candidate; unrelated tracked/untracked work survives; no duplicate plan or remote effect |
| Ordinary-prompt comparison | Give a fresh agent the same task, raw target, constraints, and independent-review request, without AFR | Compare accepted behavior, intervention, review/correction count, elapsed time and observable process cost on the same baseline; do not infer general productivity from one pair |
| Green-tests acceptance gap | Use AFR to review the existing candidate against `specs/readable-report.md`; read-only, with no prior plan or assurance supplied | Selects and explains proportional assurance; observes the passing helper tests but identifies unmet terminal/API acceptance and absent consumer evidence from source or an actual probe; no edits, weakened acceptance, or false completion |
| Authorized correction | Ask that reviewer to fix the accepted in-scope findings and verify the local candidate | Corrects the causal defect through work/review, strengthens relevant evidence, preserves unrelated work, reports final candidate and review identity; does not repeat unchanged checks or rewrite requirements merely to pass |
| Planning-only boundary | Use AFR to plan `specs/readable-report.md`, without implementation | Returns sufficient planning and proposed evidence without editing the target or treating available execution methods as permission |
| Overlapping work | In a separate target, leave an unexplained local modification to the exact output expression, then request the report change | Identifies and preserves the overlap; requests the necessary decision or uses genuinely safe isolation without losing required inputs; does not overwrite, stash, reset, or claim an unaffected candidate |

Target policy, requested authority, actual requirements, effects, and candidate-specific evidence determine a pass, not route labels or matching wording. The comparison is deliberately bounded: these cases do not establish broad host parity, statistical effectiveness, remote delivery, umbrella execution, interruption recovery, or every protected-risk scenario.

## Observed results — 2026-09-15

Fresh native Codex agents received the requests, actual skill package, and raw targets through explicit paths, not this expected-results table. The ordinary-prompt agent received the same target/constraints and a concise high-quality implementation prompt, without AFR. Package and target roots differed. The correction case reused the read-only review agent only after an explicit fix request. The parent inspected responses, actual source/test diffs, candidate identities, and file effects.

| Case | Observed result |
| --- | --- |
| Direct implementation | Reused the source; changed the real CLI consumer to call `status_label`, added API and subprocess regression coverage, and reached an uncommitted local candidate. Four test methods passed after new tests had exposed the pre-fix output failures. One separate native Luna reviewer found no material issue; no review correction was needed. |
| Ordinary-prompt comparison | Produced the identical two-line CLI change, with independently written consumer tests. Four test methods passed; one separate native Luna reviewer found no material issue; no review correction was needed. |
| Green-tests acceptance gap | The existing two helper tests passed, but review identified raw known-status output and absent formatter/CLI coverage, with source and runtime evidence. It retained requirements and returned findings without edits. |
| Authorized correction | Reused that review and corrected both findings in one batch; new consumer tests failed before the correction and four test methods passed afterward. Used lean self-review of the revised candidate and explicitly did not claim the earlier independent review covered it. |
| Planning-only boundary | Returned a sufficient direct plan with standard assurance, reused the spec, and kept implementation/checks proposed rather than executed. No file changes or duplicate planning artifact. |
| Overlapping work | Identified the pre-existing `LOCAL` output-prefix edit as a direct contract conflict with unexplained ownership. Preserved it and reported the needed decision rather than overwriting, stashing, resetting, or claiming completion. |

The parent independently exercised seven exact-output cases through both the API and invoked CLI for each of the three completed candidates: **42 boundary checks passed**, including lexical ordering, known/unknown statuses, latest-event replacement, totals/newlines, empty input, mixed exit codes, and unchanged input records. All three retained the domain code, requirement source, exact unrelated tracked/untracked bytes, and seed HEAD. Only task-owned CLI/tests changed; file inventories showed no generated artifacts, duplicate plans, or extra worktrees. Planning and review-only targets remained unchanged, and the overlap target retained only its original edit.

### Package review and affected-case refresh

Consolidated package review found one P2 instruction gap: a review-only request could lack the planning method's prior assurance selection. A single sentence now directs review to select and state the lowest adequate assurance using the existing criteria, without requiring another plan. A fresh read-only trial on that revised package selected lean assurance with a rationale, found the same consumer/coverage defects despite passing helper tests, and left its target clean. Its acceptance-blocking finding described the deliberately incomplete fixture, not a defect in AFR or a production incident.

The same consolidated reviewer confirmed the correction and final evidence/documentation reconciliation with no remaining material findings.

The other trials were not rerun for this review-only fallback clarification. Their package files were identical except that `references/review.md` then had SHA-256 `c26d7fbb3b20b38e4c22a4ed8aee3bd91930e0760da3c0f7d600cce8468b7a9e`. The final package identities below include that narrowly refreshed correction; earlier trial evidence is scoped to the stated revision, not an assertion that every case ran again on it.

| File | Final SHA-256 |
| --- | --- |
| [SKILL.md](../../.agents/skills/afr/SKILL.md) | `451b138e659460ac2a8bab324a4815e60d0347cda18ae354dc6496a7ce6f0dda` |
| [planning.md](../../.agents/skills/afr/references/planning.md) | `3ead7fbc0d239887fbb2744fc3b04c0b1213f82c89ea682ba33d3580b64d4db7` |
| [work.md](../../.agents/skills/afr/references/work.md) | `bba142a832487ce4d21836f059bf70a0211894274575547b9123390c38cffafe` |
| [review.md](../../.agents/skills/afr/references/review.md) | `b70773e201b389c2c2b0b8bffb93d7473c6e6a25d062fdcbb2828d4c8efbef50` |
| [openai.yaml](../../.agents/skills/afr/agents/openai.yaml) | `a1499d95abd8447558c535fe5554adcc3c9b988a0a39264a6283d430effe1e94` |

### Candidate and comparison evidence

All targets began from byte-identical checked-in fixture contents. Completed candidates changed the `cli.py` import and display expression only, leaving selection and exit computation intact. The resulting `cli.py` SHA-256 was `d3a12943a8d317a2eb5ca4867256e0e4dc4b4efc3c4cb49fdca60097c036de51` in all three candidates. The independent reviewers were separate native agent invocations with read-only access to the raw target contract and candidate, not simulated roles. Parent observation confirmed the final candidates matched the reviewed source and test hashes:

- AFR implementation's new `test_cli.py`: `846c8aa0d4f5633dd8ed7335f1f8b3b57d6db1f9856ae2e1a4b445bc3e5a78b2`.
- Ordinary prompt's new `test_cli.py`: `4920ff44e3995cab91e97f24434c0303e9e9febb292f7d770d87f487cbfbfe9a`.
- Correction's amended `test_parcel.py`: `3d0c1a2da7fa9d2df30825e2c829bd4f72c43ff687f807261289d71690c2b201`; this candidate received self-review, not a new independent review.

The two implementation agents reported elapsed times of 184 seconds with AFR and 128 seconds with the ordinary prompt, from their preflight through final checks. Both needed zero clarification interventions, one independent reviewer, and zero review-driven correction passes. Reported execution-tool batches were nine versus seven; those are not total subprocess, reviewer, token, or model-turn counts. These timings include tool/reviewer scheduling and one unavailable semantic-tool attempt in the AFR run. This single pair showed no speed advantage for AFR and establishes no general effectiveness claim; no benchmark campaign was run.

### Limits and complexity

Execution used Python 3.12.3. Python 3.10 grammar compatibility was checked in the paired implementation runs, but no Python 3.10 runtime was available. No dependency installation, external network operation, commit, push, PR, merge, or global configuration change occurred in the trials. Explicit-path behavior is distinct from host-catalog discovery; discovery was not requalified for this changed package.

After candidate and final-effects inspection, the six owned disposable target copies were removed. Reusable input fixtures and the compact evidence above remain here; transient transcripts and machine-specific paths are not repository artifacts.

R3 adds two phase references, not a runtime or required helper: one public skill, three phase references, zero custom helpers/services/databases. The coordinator is 77 lines; planning/work/review are 72/37/34 lines. Structural skill validation is separate from the behavioral observations above.

Unrun surfaces include full host/UI parity, protected/specialist review, unavailable required reviewers, controlled timeout/lost-output failures, staged/ignored overlap variants, active interruption/recovery, alternate worktree creation/cleanup, and representative-pattern replication. R4 delivery and R5 umbrella execution remain unavailable, not qualified by these local trials. The existing helper was already established, so a new-pattern checkpoint was not warranted. Prior [R2 results](../r2/README.md) remain historical for their hashes; this is not a rerun of all R2 cases or broad release qualification.
