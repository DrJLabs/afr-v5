# AFR v5 architecture and behavior specification — R1 v2

**Status:** superseded R1 v2 baseline; retained for comparison. Use [architecture v3](architecture-v3.md) for the current design.
**Date:** 2026-09-15
**Baseline:** R1 v1 at `186631c`, reconciled with the [spec-driven direction assessment](spec-driven-direction-assessment.md).

This document superseded [architecture v1](architecture.md) during R1 v2. [Architecture v3](architecture-v3.md) now owns the current design. The [roadmap](roadmap.md) owns milestones and complexity budgets. The [donor matrix](donor-matrix.md) owns historical provenance, extraction decisions, and evaluation scenarios. Applicable repository instructions and current user authority remain binding. Historical instructions and the assessment supply evidence and recommendations, not execution permission.

## 1. Decision and reconciliation

Retain one public `afr` skill with a compact coordinator and four progressively loaded phase references. Strengthen the definition and verification of intended behavior before adding workflow machinery.

```text
.agents/skills/afr/
├── SKILL.md
└── references/
    ├── planning.md
    ├── work.md
    ├── review.md
    └── delivery.md
```

This is the proposed implementation shape, not an existing package or installation claim. Add host-specific discovery metadata only at the supported-host implementation boundary; keep workflow instructions portable. Native host facilities supply tools, workspaces, sessions, and subagents. Git, checks, and the remote forge supply source and delivery facts.

The original donor supplies the outcome loop; the first modular family clarifies responsibilities; the native-family design supplies proportional assurance and economical handoffs. Later sources contribute specific safeguards. Matrix rows I01–I14 and X01–X03 retain their historical provenance. The refinements below come from the assessment, not newly discovered donor behavior.

| Assessment recommendation | Disposition | Reconciliation with R1 |
| --- | --- | --- |
| §4.1 Small implementation contract | Adopt | Extend sufficient planning with behavior, settled decisions, and a revisable approach; no mandatory template or additional document (§5) |
| §4.2 Assurance during planning | Adopt | Apply the existing assurance levels before implementation as well as during review; route and assurance remain separate (§5) |
| §4.3 Explicit conformance | Adopt | Associate material requirements with evidence and distinguish implementation defects from specification or decision problems (§5) |
| §4.4 Parent-level umbrella acceptance | Adopt | Require evidence for the combined objective and shared invariants in addition to outcome endpoints (§4) |
| §4.5 Early behavioral trials | Adopt with bounded scope | Exercise each available capability during R2–R5; broader qualification still follows core assembly (§7) |
| §4.6 External specifications | Adopt | Reuse adequate artifacts under current authority; no framework adapter, dependency, or duplicate AFR plan (§2, §5) |
| §4.7 One controlled trial as helper justification | Qualify; defer automatic exception | A material safety demonstration warrants stopping the unsafe action and proposing a safeguard. It does not override repository requirements for helper extraction or new layers (§6) |

The assessment's semantic planning output (§5), authority levels (§6), and evaluation extensions (§7) are incorporated below. No additional public skill, persistent state, framework runtime, mandatory planning artifact, or broad donor archaeology is introduced.

The coordinator owns one workflow; references keep phase detail out of the default context. A single large file would load every phase together. Independently invoked skills add routing and ownership costs and remain deferred until use demonstrates a correctness, reuse, or context benefit. Aim for about 300 coordinator lines and about 200 lines per reference; these are budgets, not targets to fill.

No daemon, database, custom agent runtime, scheduler, required run-state file, or SDK runner is part of this design. A future optional launcher must invoke the same canonical skill and meet the roadmap's entry conditions; it cannot become another workflow owner.

## 2. Inputs and authority

Accept a user goal or existing specification, the target project, constraints, and an authorized delivery boundary. Discover missing repository facts before asking. Ordinary language is sufficient; no manifest or mandatory input schema is required.

Before work, establish the requested outcome and observable acceptance; actual project/worktree, applicable instructions, branch/base and existing changes; scope exclusions, risks and required verification; and the latest authorized endpoint: analysis, local candidate, published PR, or merged result, including local synchronization when requested or required.

An adequate BMAD, Spec Kit, issue, RFC, ADR set, or project-native artifact can supply the contract. Inspect its content and the current repository, resolve only material gaps or contradictions, and reuse it when sufficient. Artifact origin does not grant authority or activate its framework. Avoid adapters, additional skills, and AFR-specific translations without demonstrated need.

AFR invocation selects a method, not permission for every effect. Carry forward authority already given. Push, PR creation, merge, deployment, installation, and cleanup must fit the current request and repository policy; merge authority does not imply branch/worktree deletion authority. Ask only for missing authority or a decision materially affecting scope, safety, cost, or data sharing.

The latest user instruction and applicable repository instructions govern. A plan cannot override them. Historical plans, donor fields, and memory do not activate services or supply new permissions. Within a selected plan, distinguish:

| Content level | Meaning | Change boundary |
| --- | --- | --- |
| Authoritative requirements | Intended behavior, external contracts, invariants, security policy, compatibility, non-goals, and acceptance | Do not silently change; obtain the relevant decision or use a requirement change already authorized |
| Approved design decisions | Consequential architecture, interface, data, migration, or operational choices | Follow them; surface materially invalidating evidence before dependent implementation departs from the decision |
| Advisory approach | Likely files, internal factoring, naming, sequence, and reversible implementation suggestions | Improve within delegated discretion while preserving requirements, binding decisions, dependencies, and authority |

These levels express meaning, not mandatory labels on every paragraph. A suggestion does not become binding merely because it appears in a plan, and an unapproved assumption does not become a settled decision.

## 3. One owner per behavior

Operational instructions will live in the following owners within `afr/`. Once implemented, this architecture should summarize and link to them rather than maintain a second executable workflow.

| Owner | Responsibility | Information needed by the next phase |
| --- | --- | --- |
| `SKILL.md` | Explicit activation, authority, final route choice, sequencing, stop, resume, continuation, and terminal reporting | Current outcome, authorized endpoint, next action or blocker |
| `references/planning.md` | Discovery, alternatives when useful, route recommendation, implementation contract, planning assurance, outcome/dependency analysis, plan self-review | Authoritative source, requirements, decisions/discretion, acceptance/evidence approach, risks, dependencies, parent acceptance when applicable |
| `references/work.md` | Workspace choice, implementation, focused conformance evidence, actual-diff inspection | Candidate/base identity, changes, requirement coverage, checks and limitations, contradictions or residual concerns |
| `references/review.md` | Risk-selected review, independent conformance assessment when warranted, finding classification, bounded correction and rechecks | Findings/dispositions, reviewed revision, acceptance gaps and remaining material concerns |
| `references/delivery.md` | Authorized PR operations, native monitoring, feedback through the review method, observed merge and local synchronization | PR/head, delivery facts, evidence needed for dependent work, incomplete obligations |

References return results to the coordinator. They do not independently activate AFR, choose the next umbrella outcome, or redefine lifecycle stop/completion rules. Planning defines acceptance; work and review assess it; delivery establishes delivery facts; the coordinator determines whether the requested scope is complete.

Ordinary transitions use the same agent context. Use concise file-based handoffs for large delegated work or resumption, naming existing sources, revisions, evidence, and remaining concerns. Separate briefs, generated diff packages, certificates, receipts, and JSON result envelopes are not mandatory phase artifacts.

## 4. Coordinator behavior

### Activation and route selection

Activate only when the user explicitly selects AFR planning, execution, or continuation. Explanation or review of AFR itself does not start a run. Ordinary project work does not implicitly select AFR. Planning-only requests end with the requested analysis or plan.

| Route | Meaning | Completion boundary |
| --- | --- | --- |
| `direct` | One cohesive reviewable outcome, possibly several commits | Acceptance and the authorized delivery endpoint are satisfied |
| `umbrella` | Several independently deliverable outcomes with meaningful dependencies | Required outcomes reach their endpoints and parent-level acceptance is satisfied |
| `spike` | Bounded research needed to decide or specify implementation | Evidence, conclusion or remaining uncertainty, and a recommended next step |
| `stop` | Work is unsafe, lacks authority, is explicitly stopped, or is intentionally deferred | Explain the boundary and smallest action needed to resume, when applicable |

A research result does not authorize its proposed implementation. A ready PR does not authorize merge. Route describes the work's shape; assurance describes its risk. A tiny direct change can require protected assurance.

### Sequence and continuation

Coordinate planning → work → review when warranted → the authorized delivery endpoint. New accepted findings use the same correction method; a published fix returns to monitoring. Continue after intermediate progress while scope, authority, and prerequisites permit useful work.

For an umbrella, choose an unfinished outcome whose dependencies have reached their required revisions or delivery boundaries. Use explicit plan order to break otherwise immaterial ties. Reuse the direct workflow. An unmerged candidate cannot satisfy a dependency requiring a merged base. If unfinished work exists but none is eligible, report the dependency blocker or cycle; do not declare completion or add a scheduler.

Check user steering before consequential actions and after delegated results. Honor a stop promptly using host controls. A late result cannot restore authority after a stop. Reobserve uncertain in-flight external actions before reporting their disposition.

### Parent-level umbrella acceptance

Planning defines the parent objective, shared invariants, dependency boundaries, and where combined behavior can be meaningfully checked. At those integration boundaries, assess the actual combined revision/configuration against the parent contract. Examples include interface agreement, migration ordering, and preservation of behavior across outcomes.

Completion requires every required outcome's authorized endpoint, satisfied dependency revisions/boundaries, coherent shared invariants, and evidence that the combined result meets the parent objective. Passing outcome checks or merging every PR alone is insufficient. A failed combined check remains an acceptance gap requiring in-scope correction or a reported blocker, even when every outcome was individually accepted.

Reuse relevant outcome evidence. Run integration checks when combined behavior becomes meaningful or affected evidence changes; do not rerun every check after every outcome. Parent acceptance does not authorize production effects or other checks outside the current boundary.

### Resume and evidence reuse

Resume from current user intent, the authoritative specification/plan, Git/worktree state, PR/check/review observations, and session context. Resolve existing branches and PRs before creating replacements. Check evidence identity and relevance: requirement source, tested/reviewed revision and base, changed surfaces, prerequisites, and applicable policy.

A changed requirement, decision, candidate, base, or prerequisite refreshes the affected implementation and evidence. Preserve still-valid checks. A stale summary cannot establish readiness. Handle invalidated assumptions using the contradiction rules in §5; resumption is not permission to silently rewrite the contract.

After an ambiguous external write, inspect external state before retrying. A remotely merged PR with incomplete local synchronization resumes at the missing local obligation, not implementation or merge.

### Completion and blockers

Completion requires conformance to the authoritative contract, risk-appropriate checks, the authorized endpoint, and safe disposition of temporary effects; umbrellas also require parent acceptance. Failed or unavailable required checks block completion. Explicitly optional checks are reported as not run; partial delivery remains partial.

Report the outcome, changed files/artifacts, relevant acceptance evidence and limitations, actual delivery effects, and remaining assumptions/blockers. Umbrellas expose remaining outcomes and combined acceptance gaps; spikes expose uncertainty. Do not generate status files solely for reporting.

## 5. Phase requirements

### Planning and the implementation contract

Inspect enough current source, tests, instructions, and relevant history to bound the request. Compare alternatives only for real choices. The contract distinguishes three logical layers: behavior and constraints (what must become or remain true), settled technical decisions, and the revisable execution approach. These can fit in a few sentences; three documents are not required.

Cover the following when material, omitting irrelevant sections:

- objective, explicit non-goals, and verified current behavior with evidence;
- required behavior and preserved invariants, including compatibility constraints;
- meaningful failure, edge, retry, ordering, or concurrency behavior;
- binding interfaces, data semantics, security and authorization boundaries;
- settled decisions, assumptions, unresolved decisions, and delegated implementation discretion;
- acceptance criteria with corresponding evidence and known verification limits;
- coherent implementation slices, dependencies, and ordering; parent acceptance for umbrellas;
- risk-selected review/verification, authorized delivery endpoint, and stop/replan conditions.

Use chat, an existing issue/specification, or the project's designated plan according to need. Persist a plan when requested, useful for resumption, or warranted by duration or risk. Reuse sufficient content rather than create a second slice plan or task matrix. If additions are needed, amend the designated source within authority or make a minimal linked supplement with clear ownership; do not create competing requirements.

### Assurance from planning through review

Select the lowest adequate assurance from behavior and consequences, not diff size or route. Required repository checks remain binding.

| Assurance | Planning expectation | Verification and review expectation |
| --- | --- | --- |
| `lean` | Verified problem, intended change, preservation constraints, focused acceptance evidence | Focused checks and self-review; no default independent reviewer |
| `standard` | Explicit behavior/failure cases, interfaces, consequential decisions, coherent slices, requirement-to-evidence coverage | Appropriate behavioral checks and normally one consolidated independent review |
| `protected` | Add analysis for the actual security, migration, rollback, compatibility, concurrency, performance, reliability, or irreversible-effect risks | One consolidated review with relevant specialist coverage and risk-required verification |

Self-review for missing acceptance, contradictory constraints, unsupported assumptions, unnecessary decomposition, and a simpler adequate approach. Implementation is ready when consequential behavior is sufficiently defined, constraints are known, verification is credible, and remaining discretion fits authority. This is a judgment, not a certificate or gate engine. Block only work dependent on a material unresolved decision; continue independent safe work when useful.

Authentication, secrets, persistence, migrations, deployment, public interfaces, irreversible effects, and significant concurrency warrant examination. New evidence can increase assurance within existing authority. Additional data sharing or external effects still need authority. A required review capability that is unavailable is a visible limitation/blocker, never simulated or claimed.

### Work and conformance evidence

Preserve unrelated changes. Choose a feature branch or isolated worktree according to repository policy and risk; reuse valid isolation. Escalate unexplained overlap that cannot be safely separated. Unrelated dirt alone is not a blanket stop.

Use the host agent for implementation, normally one implementer per cohesive outcome. Delegate only independent, bounded work with clear ownership and cheap synthesis. Native tools own spawning, waiting, interruption, and resumption.

Establish evidence for each material requirement, including preservation and failure behavior. Choose unit, integration, contract, compatibility, property, migration, performance, security, operational, or manual checks according to the requirement. A short explanation or a few links can establish coverage; no mandatory traceability IDs or separate evidence database is required.

Passing implementation-selected tests is insufficient when acceptance remains unmet. Inspect the actual diff and associate evidence with the candidate/base and relevant requirement source. Distinguish passed, failed, timed-out, unavailable, and inconclusive checks. Include useful regression evidence for bug fixes when practical, follow repository requirements, and expand coverage for observed failures or affected risks. Avoid dependency reinstalls or full-baseline reruns without a relevant reason.

### Review and correction

Review receives the authoritative requirement source, exact candidate/base, and available evidence and limitations, not only an implementer summary. Assess conformance as well as source defects. Use the assurance selected above, adjusting to observed risks.

| Contradiction | Response |
| --- | --- |
| Implementation fails a valid requirement | Correct implementation and refresh affected evidence |
| Evidence invalidates a technical assumption | Revise the approach within delegated discretion; surface an affected approved design decision before departing from it; refresh dependent work/evidence |
| Missing or conflicting product/security decision | State the decision and impact; seek the relevant authority rather than invent policy; pause dependent work |
| Requirement change is authorized | Update the authoritative source through its permitted path and reassess affected work, acceptance, dependencies, and evidence |

Do not weaken acceptance or rewrite requirements to make an implementation appear complete. Record findings with impact, location, evidence, and disposition: accept, reject with reason, duplicate, or follow-up. Do not relabel a material unresolved finding as follow-up to pass delivery. Out-of-scope findings can require a scope decision but do not authorize unrelated fixes.

Batch accepted findings into one correction by default. A further pass requires observed progress or elevated risk. Recheck affected behavior and required integration evidence; renew review where the revision/finding requires it. Repeated unchanged failure causes stop or replan. PR feedback follows the same method and limits.

### Delivery

Identify exact repository, remote, target branch, source branch, and PR; reuse a matching PR. Authorized creation/updates carry concise scope, verification, acceptance gaps, and residual context.

Use native/platform monitoring or an appropriate external PR-monitoring capability. AFR decides how to respond and continue; it does not implement a watcher. Required checks must be observed successful or explicitly satisfied by repository policy. Missing, pending, failed, and unknown observations are distinct from success.

Readiness belongs to the actual PR head. A pushed fix invalidates old-head readiness and returns to monitoring and affected review. Before merge, reobserve head, target, checks, feedback, and mergeability. Condition merge on the expected reviewed head when supported; if the available mechanism cannot safely protect that revision, stop at the boundary.

Observe remote merge independently from local synchronization. When required, fetch the remote target and fast-forward only a safe local target after inspecting ownership and changes. Do not substitute local merge for remote PR merge, reset a diverged branch, or switch another active worktree's branch. Reconcile required plan bookkeeping through its authorized path and expose incomplete obligations before dependent continuation.

## 6. Deterministic helpers

R1 v2 retains **zero required custom helpers**. Native Git, repository checks, and forge capabilities are the initial tools. The donor matrix's candidates remain deferred; donor tests do not prove that this unimplemented v5 design needs a helper.

The existing extraction threshold remains repeated real v5 failure or measurable waste that concise instructions and native tools cannot adequately address. A proposal must identify the demonstrated problem, inadequate simpler alternatives, narrow deterministic interface, existing work it replaces, operational owner, focused tests, and measurable benefit and ongoing cost. Apply the repository's explicit complexity test and stricter rules for persistent systems or major abstractions.

The assessment rightly rejects waiting for repeated destructive incidents. One safely controlled trial can expose a material safety gap and justify stopping the affected operation and proposing a narrow safeguard. It does **not** automatically satisfy or override a repository rule requiring repeated failure evidence. Where that rule blocks the proposal, seek a scoped policy/design decision before implementation. The single-trial exception is therefore deferred, not silently adopted. Never reproduce destructive incidents to accumulate evidence.

A justified helper supplies a deterministic observation or check. It cannot choose routes, assign agents, manage workflow state, grant authority, or decide completion. A controlled trial does not authorize a persistent subsystem, framework adapter, custom runtime, or relaxed safety boundary.

## 7. Evaluation and implementation boundary

The donor matrix retains E01–E15 as the canonical scenario definitions. Its v2 extensions to E02, E05, E06, E09, E14, and E15 cover sufficient existing specs, missing decisions, protected consequences in small changes, invalid assumptions, passing tests with unmet acceptance, and failed combined umbrella acceptance. Historical donor evidence remains distinct from these new design cases.

| Milestone | Bounded behavioral trial when the capability exists |
| --- | --- |
| R2 | Exercise coordinator/planning on sufficient existing specs, material ambiguity, lean work, and protected-risk work; observe reuse, readiness, route, and authority judgments |
| R3 | Run at least one real local change through planning/work/review; compare acceptance, intervention, and process cost with an ordinary high-quality host-agent prompt on a comparable task/baseline |
| R4 | Exercise exact-head readiness, missing/pending/failed/unknown checks, review feedback, and ambiguous external effects within an authorized disposable or controlled setting |
| R5 | Exercise umbrella continuation, dependency boundaries, and combined acceptance, including individually successful outcomes whose combined behavior fails |

Trial evidence should identify the request/requirement source, relevant revision/base, observed behavior versus expected acceptance, coverage gaps, and intervention or correction needed. Keep evidence in existing project/test artifacts or the task record according to need; do not introduce a trial registry. R4 tests do not themselves grant live push/PR/merge authority.

Early bounded trials are different from broad qualification of an incomplete package. Build R2–R5 in the same package, test available behavior as it appears, then review coherence and broaden integrated qualification across repositories, interruptions, and risk classes. Proceed between increments unless observed defects require correction; do not infer effectiveness from matching prose or Markdown checks.

Measure accepted outcomes, unnecessary intervention, clarification/replan frequency, scope violations, requirement-to-evidence coverage, context/model turns, correction passes, escaped material defects, repeated work after resume, and process growth. Interpret autonomy and speed alongside correctness; a justified clarification is not a failure to optimize away. The roadmap owns detailed milestones and budgets.

This increment reconciles the design and evaluation cases only. Skill implementation, installation, behavioral trials, helper extraction, PR-delivery qualification, and performance claims remain future work. R2 starts with the coordinator and planning reference using this contract; work, review, and delivery extend the same package.
