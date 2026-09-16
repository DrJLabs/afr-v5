# R6 evidence-driven helper assessment

**Decision:** complete this assessment with **zero helper extractions**. Retain native tools and the current skill package; gather representative-use evidence before reconsidering a helper. This is a bounded decision about the available evidence, not proof that instructions will always suffice.

**Evidence baseline:** merged R5 at `691af88e4b49160e1f3b5f52a7016d80d55fcf4d`. Sources are the revision-scoped [R2](../tests/r2/README.md), [R3](../tests/r3/README.md), [R4](../tests/r4/README.md), and [R5](../tests/r5/README.md) records, current package instructions, and the authoring corrections in Git. No new behavioral trial, live delivery, installation, or benchmark is claimed by this assessment.

The [architecture's extraction threshold](architecture-v3.md#6-deterministic-helpers) and [R6 contract](roadmap.md#r6--evidence-driven-helper-extraction) remain unchanged. The [donor candidates H01–H06](donor-matrix.md#3-deterministic-helper-candidates) are historical leads, not repeated v5 incidents or permission to port their runtime. This document owns the R6 disposition, not workflow policy or another progress registry.

## Evidence and diagnosis

| Source | Observed issue or cost | What the evidence supports |
| --- | --- | --- |
| [R2 observations](../tests/r2/README.md#observed-results--2026-09-15) | Two first-pass agents imported target Python and created bytecode while initially reporting no writes. | A genuinely repeated effects-reporting defect within one trial batch. Non-writing probes and final tracked/untracked observation were added to the coordinator; five fresh cases on the corrected package left clean targets. Repetition occurred, but inadequacy of the simpler correction was not demonstrated. |
| [R2 PR follow-up](../tests/r2/README.md#pr-review-coverage-follow-up--2026-09-15) | Review required additional compressed-handoff and material-ambiguity evidence; invocation documentation was clarified in `a33f91f`. `1430529` corrected a helper-threshold link from historical architecture v2 to current v3. | Two fresh cases supplied the missing coverage without a skill change. These are qualification/documentation gaps, not evidence for a plan parser or installer. An existence-only link checker would not detect a valid link pointing to superseded policy. |
| [R3 package review](../tests/r3/README.md#package-review-and-affected-case-refresh) | A review-only request could lack prior assurance selection. | One sentence in the existing review method supplied the fallback; a fresh affected case selected and explained assurance. The deliberately incomplete fixture's green helper tests and broken consumer were detected, not an escaped AFR implementation defect. |
| [R3 comparison](../tests/r3/README.md#candidate-and-comparison-evidence) | Reported elapsed time was 184 seconds with AFR versus 128 with an ordinary prompt; execution-tool batches were nine versus seven. | One pair showed no speed advantage. Timing includes scheduling and an unavailable semantic-tool attempt; batches are not model turns or subprocess counts. The record does not isolate a mechanical bottleneck or establish helper savings. |
| [R4 observations and correction](../tests/r4/README.md#pr-review-correction-and-affected-case-refresh) | PR review found that new-PR delivery asked for PR head/base before creation. | `097775b` corrected ordering in the delivery reference; one fresh controlled case created first and observed the resulting identity. The original controlled cases distinguished stale/failed/absent evidence and reobserved uncertain writes. These are bounded results, not live-forge compatibility proof. |
| [R5 initial execution and refresh](../tests/r5/README.md#initial-execution--final-behavior-passed-sequencing-failed) | One agent implemented dependent outcomes together before the required prerequisite verification/update, despite final checks passing. | A coordinator instruction and fresh affected-case trial established the required ordering. A final-state plan validator would not prove chronology; adding a scheduler or mandatory lifecycle-state mechanism is not justified by this corrected instruction failure. No post-correction recurrence is recorded. |
| [R5 resume](../tests/r5/README.md#resume--causal-correction-with-a-verification-follow-up) | The agent corrected the seeded first/latest-event mismatch, but its handoff overstated coverage: direct API verification was missing. | One parent-requested API check closed the evidence gap without a source change or broad rerun. This is an actual verification-completeness concern, not a zero-intervention success. The seeded implementation defect is not a second escaped AFR defect. |
| [R4](../tests/r4/README.md#package-identity-and-review) and [R5 structural checks](../tests/r5/README.md#review-and-verification) | Package metadata, local links/tables, hashes, and whitespace were checked repeatedly; R5 records 122 links, 17 tables, and six package hashes. | Repeated authoring work is observable, but neither repeated checker failures nor isolated checker cost/savings were measured. Counts are not a demonstrated bottleneck or an automated behavioral evaluation. |

Authoring commits, reviews, and merges establish source/delivery history, not representative runs of the AFR skill. Controlled forge responses are not live API results; injected fixture defects are not production incidents. This assessment does not rerun or extend any historical package's qualification.

## Candidate dispositions

No candidate passes both the evidence and simpler-alternative tests. “Defer” means reconsider against new evidence, not preapprove an interface, dependency, or implementation.

| Candidate | Adequate initial mechanism / limitation | R6 disposition and useful reopening evidence |
| --- | --- | --- |
| H01 workspace identity/containment | Native root/path, worktree, status and ownership inspection. R3 preserved unrelated work and stopped on overlap; R4 distinguished safe and dirty synchronization. | **Retain native inspection.** Shared-worktree races and hidden collisions remain unqualified. Reopen for recurring identity/containment errors or measured inspection cost that native checks and instructions fail to address. Never induce destructive incidents to meet a count. |
| H02 candidate scope/hidden changes | Native diff/status plus contract-specific preservation checks. R2's bytecode/effects problem received an instruction correction and fresh trials. | **Retain corrected instructions and native checks.** Reopen if omitted effects recur after those checks, isolating a deterministic omission the proposed checker could actually detect. |
| H03 conditional mutation | Native conditional Git/forge operations, exact revisions, and fresh observation. R4 exercised guarded rejection and uncertain-result observation with controlled responses. | **Retain native conditional operations.** Installed `gh` 2.79.0 help exposes `pr merge --match-head-commit`; that is interface availability, not an R6 merge test. Reopen for a demonstrated unprotected boundary; stop that operation if the guard is unavailable. |
| H04 bounded checks / test selection | Host command controls and target-owned tests; the work/review methods require consumer-level evidence. A generic selector cannot infer that a direct API obligation was satisfied by CLI-only coverage. | **Defer automation; retain source-grounded coverage review.** Track recurrence of R5's omission and whether the existing method was followed. Reopen only if a stable, explicit input/output contract can catch a recurring mechanical omission or reduce measured repeated check cost. |
| H05 finding normalization | Source-grounded dispositions and a compact finding list. R4's supplied valid/duplicate/incorrect feedback was classified without a helper. | **Retain the review method.** Reopen for recurring lost manifestations, incorrect duplicates, or measured normalization cost; do not treat reviewer labels or counts as source truth. |
| H06 PR observations/retry safety | Native forge reads and an available external monitor; the delivery method owns interpretation and uncertainty handling. New-PR ordering was corrected there. | **Retain native/external capability.** Reopen for recurring parsing, pagination, identity, or retry errors not handled by those tools. Authentication, real protection/queues and API compatibility remain qualification gaps, not reasons to import a watcher or delivery engine. |
| Plan/dependency validation | Ordinary source-linked Markdown, coordinator prerequisite checks, and native revision observations. R2 handled ambiguity; R5 corrected chronology and respected controlled dependency blocks. | **Defer a schema/parser.** Reopen for repeated mechanically recognizable shape/reference defects after concise guidance. Semantic acceptance and actual execution order remain skill/review concerns. |
| Package/link/hash validation | Existing one-off authoring checks and ordinary tools; none is required by an AFR target run. | **Defer a repository utility.** Measure repeated failures or authoring cost first. If justified later, replace the repeated check with one focused development utility, not a runtime gate, second workflow, or mandatory target dependency. |

## Complexity and evidence limits

The existing extraction questions have a negative implementation result: native observations and focused instruction corrections cover the observed mechanical issues; no remaining narrow helper has a demonstrated benefit that outweighs ownership, tests, interface and maintenance costs. No helper API or test suite is invented for an unselected candidate. The architecture's single-safety-trial caveat still applies: stop an unsafe operation and seek a scoped policy/design decision when needed, without silently waiving the threshold.

Actual package counts at this boundary are unchanged:

| Surface | Count |
| --- | ---: |
| Public skills | 1 |
| Phase references | 4 |
| Coordinator lines | 97 |
| Planning / work / review / delivery lines | 72 / 37 / 34 / 48 |
| Explicit-only metadata lines | 2 |
| Custom helpers / runtimes / services / databases / run-state files / new dependencies | 0 |

R6 adds one assessment document and updates its README/roadmap pointers; it changes no skill instructions, fixtures, runtime behavior, default tool calls, or required verification steps. No speed improvement, error-rate improvement, under-60-second behavioral path, or helper return on investment is claimed. R5 did not measure wall time, full prompt volume or tokens; R3's single pair cannot fill those gaps.

## Next evidence boundary

The assessment is complete, not blocked on inventing code. Its zero-helper result does not satisfy R7's entry condition or establish release readiness.

The next useful work is qualification of the assembled package on a real, naturally multi-outcome task: observe a required merged dependency in the dependent workspace, combined acceptance, and a deliberate pause/resume without duplicate implementation. Choose the task and authorize its target/delivery effects separately. Record the package revision, acceptance, interventions/corrections, repeated mechanical work, and time/turn counts where observable in existing task evidence; missing metrics remain unknown, and no new registry is needed.

Live installation is not required for this assessment or explicit-path trials. A separately authorized installation/discovery check should precede relying on normal cross-repository `$afr` discovery; leave predecessor skills unchanged. Historical R2 CLI discovery does not qualify the current R5 package, a full prompt-to-result invocation, or ChatGPT.

Keep the [R7 and R8 thresholds](roadmap.md#r7--optional-codex-sdk-runner-experiment): at least 10 representative real skill-first runs before considering the optional SDK experiment, and at least 20 with the specified coverage before beta disposition. R2–R5 fixture counts, API assertions, authoring PRs, and this assessment are not substitutes. Reopen only the candidate supported by new evidence; there is no automatic helper or SDK phase to implement next.
