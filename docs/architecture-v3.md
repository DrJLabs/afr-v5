# AFR v5 architecture and behavior specification — R1 v3

**Status:** current design; R3 coordinator, planning, work, and review methods implemented. R4 remote delivery and R5 umbrella continuation remain design requirements; host and behavioral qualification is limited to the [R2 historical record](../tests/r2/README.md) and the [R3 trial record](../tests/r3/README.md).
**Date:** 2026-09-15
**Baseline:** [R1 v2](architecture-v2.md), refined after a focused comparison with current BMAD planning, architecture, build, and review methods.

This document supersedes architecture v2, which supersedes [architecture v1](architecture.md), and owns the current design. The [roadmap](roadmap.md) owns milestones and complexity budgets. The [donor matrix](donor-matrix.md) owns historical provenance, extraction decisions, and evaluation scenarios. Applicable repository instructions and current user authority remain binding. Comparative frameworks and historical instructions supply evidence and techniques, not execution permission or runtime dependencies.

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

This is the target package shape. The [coordinator](../.agents/skills/afr/SKILL.md), [planning reference](../.agents/skills/afr/references/planning.md), [work reference](../.agents/skills/afr/references/work.md), [review reference](../.agents/skills/afr/references/review.md), and explicit-only invocation metadata exist; the delivery reference remains unavailable. Native host facilities supply tools, workspaces, sessions, and subagents. Git and checks supply local source facts; the remote forge remains an R4 concern. File presence is not an installation or host-qualification claim.

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

The prior assessment's semantic planning output, authority levels, and evaluation extensions remain incorporated. V3 adds implementation-facing refinements from the comparative review without changing the package shape or complexity budget:

| Comparative finding | Disposition | AFR v3 treatment |
| --- | --- | --- |
| Preserve intent when compressing or decomposing specifications | Adopt | Derived plans and assignments retain material obligations or point to an explicitly required source; unsupported commitments are not introduced (§5) |
| Distinguish indispensable context from optional background | Adopt | Handoffs identify sources required for correctness separately from rationale/history to consult when needed (§2, §3, §5) |
| Use a minimal cross-outcome architecture contract | Adopt | Settle consequential choices that independently reasonable implementations could make incompatibly; leave reversible internals to implementers (§5) |
| Review whether verification catches realistic failures | Adopt | Review examines consumer adoption, selected checks, and assertion strength; zero findings is valid and finding quotas are rejected (§5) |
| Establish an uncertain shared pattern before repeating it widely | Adopt | Validate a representative slice when uncertainty and downstream replication make early error expensive; proven patterns need no ritual prototype (§4, §5) |
| Distinguish skill package, target project, workspace, and host support | Adopt | Resolve references from the skill package, instructions from the target project, and qualify support per host (§2, §4) |
| Clarify R2 versus R3 | Adopt | R2 is an activation/routing/planning prototype; R3 is the first complete local implementation path (§4, §7, §8) |
| Adopt an external workflow renderer, canonical memory log, autonomous worker, regeneration loop, dirty-tree blanket stop, or review quota | Reject | AFR retains native host execution, project-owned sources, preservation of unrelated work, causal correction, and evidence-backed review (§1, §5, §6) |

No additional public skill, persistent state, framework runtime, mandatory planning artifact, or broad donor archaeology is introduced.

The coordinator owns one workflow; references keep phase detail out of the default context. A single large file would load every phase together. Independently invoked skills add routing and ownership costs and remain deferred until use demonstrates a correctness, reuse, or context benefit. Aim for about 300 coordinator lines and about 200 lines per reference; these are budgets, not targets to fill.

No daemon, database, custom agent runtime, scheduler, required run-state file, or SDK runner is part of this design. A future optional launcher must invoke the same canonical skill and meet the roadmap's entry conditions; it cannot become another workflow owner.

## 2. Inputs and authority

The implemented [activation, identity, and authority contract](../.agents/skills/afr/SKILL.md#activation-identity-and-authority) owns these instructions. Inputs remain an ordinary-language goal or selected specification, target, constraints, and endpoint, without an execution manifest. Its four identities separate the skill package, target project, active workspace, and host so package location cannot import authoring-repository policy into an unrelated target.

The [planning method](../.agents/skills/afr/references/planning.md) owns specification reuse, required-versus-background context, source-intent preservation, and the distinction between requirements, approved decisions, and advisory implementation choices. External artifacts supply content, not permission or a second framework. These are semantic distinctions rather than mandatory record formats.

## 3. One owner per behavior

Operational instructions live in the implemented owners within `afr/`; delivery remains planned. This architecture summarizes the current R3 package and preserves future-phase requirements rather than acting as its execution entrypoint.

| Owner | Responsibility | Information needed by the next phase |
| --- | --- | --- |
| `SKILL.md` | Explicit activation, authority, host/capability boundary, final route choice, sequencing, stop, resume, continuation, and terminal reporting | Current outcome, available phase capability, authorized endpoint, next action or blocker |
| `references/planning.md` | Discovery, source-intent preservation, context classification, route recommendation, implementation contract, minimal architecture contract, planning assurance, outcome/dependency analysis, plan self-review | Authoritative source and indispensable companions, requirements, decisions/discretion, acceptance/evidence approach, risks, dependencies, parent acceptance when applicable |
| `references/work.md` | Workspace choice, implementation, representative-pattern validation when warranted, focused conformance evidence, actual-diff inspection | Candidate/base identity, changes, requirement coverage, checks and limitations, contradictions or residual concerns |
| `references/review.md` | Risk-selected review, independent conformance and verification-effectiveness assessment when warranted, finding classification, bounded correction and rechecks | Findings/dispositions, reviewed revision, acceptance and verification gaps, remaining material concerns |
| `references/delivery.md` | Authorized PR operations, native monitoring, feedback through the review method, observed merge and local synchronization | PR/head, delivery facts, evidence needed for dependent work, incomplete obligations |

References return results to the coordinator. They do not independently activate AFR, choose the next umbrella outcome, or redefine lifecycle stop/completion rules. Planning defines acceptance; work and review assess it; delivery establishes delivery facts; the coordinator determines whether the requested scope is complete.

Ordinary transitions use the same agent context. Use concise file-based handoffs for large delegated work or resumption, naming existing sources, revisions, evidence, and remaining concerns. A handoff distinguishes material sources required for correctness from background that may be consulted for rationale or exceptional cases. It can point to authoritative content instead of copying it, but must not make indispensable context undiscoverable. Separate briefs, generated diff packages, certificates, receipts, and JSON result envelopes are not mandatory phase artifacts.

## 4. Coordinator behavior

### Activation and route selection

The [coordinator](../.agents/skills/afr/SKILL.md#planning-and-route-choice) owns explicit activation and the `direct`, `umbrella`, `spike`, and `stop` route/result meanings. Route describes work shape independently of planning assurance. A completed research result is distinct from an implementation-ready contract and from authority to execute it.

### Capability and host boundary

The coordinator's [available-capability boundary](../.agents/skills/afr/SKILL.md#available-capability) keeps explicit planning and research outside implementation and correction authority, while permitting planning artifacts under its stated conditions. R3 provides the first complete local implementation path: an authorized direct run may implement, verify, review, and apply a bounded correction within that authority. R4 adds remote delivery and R5 adds umbrella continuation; both remain unavailable. The user's original endpoint remains visible when a missing phase prevents fulfillment.

Portable workflow text does not make host support interchangeable. Qualify discovery, loading, tools, delegated work, interruption, and reporting on each supported host. An initial Codex qualification may precede ChatGPT qualification without removing ChatGPT from the product goal; report the actual supported surface honestly.

### Sequence and continuation

Coordinate planning → work → review when warranted → bounded correction/recheck within the authorized local endpoint. New accepted findings use the same correction method. Remote delivery and umbrella continuation are not current capabilities; a published fix and cross-outcome continuation remain future R4/R5 behavior. Continue within the local direct outcome while scope, authority, and prerequisites permit useful work.

When many outcomes depend on a new or materially uncertain pattern, establish and verify a representative use before reproducing it broadly when a wrong choice would create expensive downstream correction. Existing project conventions, prior qualified implementations, or low-cost reversibility can make that unnecessary. This is a planning judgment, not a mandatory prototype gate.

For an umbrella, choose an unfinished outcome whose dependencies have reached their required revisions or delivery boundaries. Use explicit plan order to break otherwise immaterial ties. Reuse the direct workflow. An unmerged candidate cannot satisfy a dependency requiring a merged base. If unfinished work exists but none is eligible, report the dependency blocker or cycle; do not declare completion or add a scheduler.

Check user steering before consequential actions and after delegated results. Honor a stop promptly using host controls. A late result cannot restore authority after a stop. Reobserve uncertain in-flight external actions before reporting their disposition.

### Parent-level umbrella acceptance

Planning defines the parent objective, shared invariants, dependency boundaries, and where combined behavior can be meaningfully checked. At those integration boundaries, assess the actual combined revision/configuration against the parent contract. Examples include interface agreement, migration ordering, and preservation of behavior across outcomes.

Completion requires every required outcome's authorized endpoint, satisfied dependency revisions/boundaries, coherent shared invariants, and evidence that the combined result meets the parent objective. Passing outcome checks or merging every PR alone is insufficient. A failed combined check remains an acceptance gap requiring in-scope correction or a reported blocker, even when every outcome was individually accepted.

Reuse relevant outcome evidence. Run integration checks when combined behavior becomes meaningful or affected evidence changes; do not rerun every check after every outcome. Parent acceptance does not authorize production effects or other checks outside the current boundary.

### Resume and evidence reuse

The coordinator's [stop and resumption method](../.agents/skills/afr/SKILL.md#stop-and-planning-resumption) reconciles current intent, source/workspace observations, and valid prior evidence for planning and the local direct path. Resolve existing branches/worktrees before replacements and associate reused implementation, check, and review evidence with the relevant candidate/base, requirements, prerequisites, and policy. PR observations and remote synchronization remain future R4 concerns. Changed inputs refresh affected work and evidence; still-valid checks remain reusable.

After an ambiguous external write, inspect external state before retrying. A remotely merged PR with incomplete local synchronization resumes at the missing local obligation, not implementation or merge.

### Completion and blockers

The implemented [terminal report](../.agents/skills/afr/SKILL.md#terminal-report) owns R3 local outcomes and effects reporting. Local completion additionally requires conformance, risk-appropriate checks, actual-diff inspection, safe temporary-effect disposition, and any selected review/correction. R4 will add an authorized delivery endpoint and R5 parent acceptance for umbrellas. Failed or unavailable required checks block completion; an unreviewed or unverified candidate remains partial.

## 5. Phase requirements

### Planning and the implementation contract

The [planning reference](../.agents/skills/afr/references/planning.md#establish-a-sufficient-implementation-contract) is now the canonical method and field inventory. Its contract separates behavior/constraints, settled decisions, and a revisable approach; it preserves source intent and material acceptance without requiring a duplicate plan or template completion. The minimal architecture-contract test resolves consequential incompatible choices before dependent work while leaving reversible internals discretionary.

Its [outcome/dependency method](../.agents/skills/afr/references/planning.md#size-outcomes-and-dependencies) supplies umbrella parent acceptance and selective representative-pattern verification as plans for R5; it does not authorize an R5 execution loop in the current package.

### Assurance from planning through review

The [planning assurance and self-review method](../.agents/skills/afr/references/planning.md#planning-assurance-and-self-review) owns the `lean`, `standard`, and `protected` expectations and planning-sufficiency judgment. The [work reference](../.agents/skills/afr/references/work.md) owns local implementation and conformance evidence; the [review reference](../.agents/skills/afr/references/review.md) applies the selected independent review coverage and may increase it for observed risks within authority. Unavailable R4 delivery or R5 continuation remains visible rather than simulated.

### Work and conformance evidence

The [work reference](../.agents/skills/afr/references/work.md) is the canonical method for local workspace choice, implementation, requirement-based verification, and actual-diff inspection. Explicit planning, research, and review-only requests do not authorize implementation or correction, or ordinary target-source edits. Planning may create or amend a planning artifact when explicitly requested, required by the target, or justified for resumability or risk within authority. An authorized direct implementation may preserve unrelated dirty work, use an isolated workspace when warranted, and stop rather than overwrite unexplained changes or exceed the selected endpoint.

Preserve unrelated changes. Choose a feature branch or isolated worktree according to repository policy and risk; reuse valid isolation. Escalate unexplained overlap that cannot be safely separated. Unrelated dirt alone is not a blanket stop.

Use the host agent for implementation, normally one implementer per cohesive outcome. Delegate only independent, bounded work with clear ownership and cheap synthesis. Native tools own spawning, waiting, interruption, and resumption. Give each implementer the authoritative requirements and required companion context for its outcome; background rationale remains available without being loaded by default.

When the plan identifies a representative-pattern checkpoint, implement and verify that slice before broad repetition. Replan only the dependent work if the pattern fails; preserve unaffected outcomes and evidence. Do not create a prototype ritual for established patterns.

Establish evidence for each material requirement, including preservation and failure behavior. Choose unit, integration, contract, compatibility, property, migration, performance, security, operational, or manual checks according to the requirement. A short explanation or a few links can establish coverage; no mandatory traceability IDs or separate evidence database is required.

Passing implementation-selected tests is insufficient when acceptance remains unmet. Inspect the actual diff and associate evidence with the candidate/base and relevant requirement source. Distinguish passed, failed, timed-out, unavailable, and inconclusive checks. Include useful regression evidence for bug fixes when practical, follow repository requirements, and expand coverage for observed failures or affected risks. Avoid dependency reinstalls or full-baseline reruns without a relevant reason.

### Review and correction

The [review reference](../.agents/skills/afr/references/review.md) is the canonical method for proportional independent review, finding assessment, bounded correction, and affected rechecks. Its review receives the exact local candidate/base and evidence from the work method; the coordinator retains authority over whether review/correction is authorized and whether the local endpoint is complete.

Review receives the authoritative requirement source, required companion context, exact candidate/base, and available evidence and limitations, not only an implementer summary. Assess conformance, source defects, and whether the verification would detect realistic failures at the behavior's observable boundary. Use the assurance selected above, adjusting to observed risks.

For material behavior, ask: **what realistic regression at the consumer or integration boundary should make this evidence fail?** Inspect whether production callers adopt the changed path, whether the intended checks actually ran, and whether assertions remain strong enough to detect the failure. Do not claim a verification gap without inspecting the available evidence. A review with zero material findings is valid; findings require demonstrated impact, not a quota. A reviewer label or prompt instruction does not make a finding self-verifying.

| Contradiction | Response |
| --- | --- |
| Implementation fails a valid requirement | Correct implementation and refresh affected evidence |
| Evidence invalidates a technical assumption | Revise the approach within delegated discretion; surface an affected approved design decision before departing from it; refresh dependent work/evidence |
| Missing or conflicting product/security decision | State the decision and impact; seek the relevant authority rather than invent policy; pause dependent work |
| Requirement change is authorized | Update the authoritative source through its permitted path and reassess affected work, acceptance, dependencies, and evidence |

Do not weaken acceptance or rewrite requirements to make an implementation appear complete. Record findings with impact, location, evidence, and disposition: accept, reject with reason, duplicate, or follow-up. Independently verify consequential findings against the source and candidate; do not automatically trust a category merely because the reviewer was instructed to gather evidence. Do not relabel a material unresolved finding as follow-up to pass delivery. Out-of-scope findings can require a scope decision but do not authorize unrelated fixes.

Batch accepted findings into one correction by default. Correct the causal defect while preserving valid work; do not default to reverting and regenerating the entire outcome. A further pass requires observed progress or elevated risk. Recheck affected behavior and required integration evidence; renew review where the revision/finding requires it. Repeated unchanged failure causes stop or replan. PR feedback follows the same method and limits.

### Delivery

Identify exact repository, remote, target branch, source branch, and PR; reuse a matching PR. Authorized creation/updates carry concise scope, verification, acceptance gaps, and residual context.

Use native/platform monitoring or an appropriate external PR-monitoring capability. AFR decides how to respond and continue; it does not implement a watcher. Required checks must be observed successful or explicitly satisfied by repository policy. Missing, pending, failed, and unknown observations are distinct from success.

Readiness belongs to the actual PR head. A pushed fix invalidates old-head readiness and returns to monitoring and affected review. Before merge, reobserve head, target, checks, feedback, and mergeability. Condition merge on the expected reviewed head when supported; if the available mechanism cannot safely protect that revision, stop at the boundary.

Observe remote merge independently from local synchronization. When required, fetch the remote target and fast-forward only a safe local target after inspecting ownership and changes. Do not substitute local merge for remote PR merge, reset a diverged branch, or switch another active worktree's branch. Reconcile required plan bookkeeping through its authorized path and expose incomplete obligations before dependent continuation.

## 6. Deterministic helpers

R1 v3 retains **zero required custom helpers**. Native Git, repository checks, and forge capabilities are the initial tools. The donor matrix's candidates remain deferred; donor tests alone do not prove that v5 needs a helper.

V3 also rejects adding a workflow renderer, generated-instruction runtime, canonical memory log, autonomous child workflow, framework adapter, blanket dirty-tree refusal, automatic revert-and-rederive correction loop, or review-finding quota to the core. A later proposal must identify the recurring AFR failure it solves and satisfy the same complexity and ownership tests as any other new layer.

The existing extraction threshold remains repeated real v5 failure or measurable waste that concise instructions and native tools cannot adequately address. A proposal must identify the demonstrated problem, inadequate simpler alternatives, narrow deterministic interface, existing work it replaces, operational owner, focused tests, and measurable benefit and ongoing cost. Apply the repository's explicit complexity test and stricter rules for persistent systems or major abstractions.

The assessment rightly rejects waiting for repeated destructive incidents. One safely controlled trial can expose a material safety gap and justify stopping the affected operation and proposing a narrow safeguard. It does **not** automatically satisfy or override a repository rule requiring repeated failure evidence. Where that rule blocks the proposal, seek a scoped policy/design decision before implementation. The single-trial exception is therefore deferred, not silently adopted. Never reproduce destructive incidents to accumulate evidence.

A justified helper supplies a deterministic observation or check. It cannot choose routes, assign agents, manage workflow state, grant authority, or decide completion. A controlled trial does not authorize a persistent subsystem, framework adapter, custom runtime, or relaxed safety boundary.

## 7. Evaluation and implementation boundary

The donor matrix retains E01–E15 as the canonical scenario family. Its v2 extensions cover sufficient existing specs, missing decisions, protected consequences in small changes, invalid assumptions, passing tests with unmet acceptance, and failed combined umbrella acceptance. V3 adds focused trial expectations for intent preservation, indispensable companion context, architecture-contract consistency, verification effectiveness, representative-pattern establishment, and host/target separation. These are new design cases, not newly inspected donor incidents.

| Milestone | Bounded behavioral trial when the capability exists |
| --- | --- |
| R2 | Exercise activation, target-root and host detection, reuse of sufficient specifications, preservation of intent through compression/decomposition, missing required companion context, material ambiguity, lean work, and protected-risk work. Observe route, planning assurance, architecture-contract decisions, and honest reporting of unavailable execution phases. |
| R3 | Run at least one real local change through planning/work/review. Include a realistic verification gap, a case where selected tests pass but acceptance remains unmet, and—when suitable—an uncertain shared pattern established before wider replication. Compare acceptance, intervention, and process cost with an ordinary high-quality host-agent prompt on a comparable baseline; record evidence in `tests/r3/README.md`. |
| R4 | Future trial: exercise exact-head readiness, missing/pending/failed/unknown checks, review feedback, and ambiguous external effects within an authorized disposable or controlled setting. The current package does not provide remote delivery. |
| R5 | Future trial: exercise umbrella continuation, dependency boundaries, shared architecture decisions, and combined acceptance, including individually successful outcomes whose combined behavior fails. The current package does not provide umbrella execution. |

R2 was planning-complete but execution-incomplete for the package revision recorded in its trial evidence. R3 is the first milestone that can claim the direct local implementation path: explicit planning, research, and review-only requests do not authorize implementation or correction, while an authorized direct run may reach a verified local candidate through work, evidence, proportional independent review, and bounded correction. Planning artifacts remain permitted under the coordinator's authority conditions. R4 and R5 add delivery and multi-outcome continuation. No milestone may silently substitute an unimplemented phase with an embedded second workflow.

Trial evidence should identify the authoritative source and required companions, target project/workspace, host and skill package identity, relevant revision/base, observed behavior versus expected acceptance, coverage gaps, and intervention or correction needed. Keep evidence in existing project/test artifacts or the task record according to need; do not introduce a trial registry. R4 tests do not themselves grant live push/PR/merge authority.

Early bounded trials are different from broad qualification of an incomplete package. Build R2–R5 in the same package, test available behavior as it appears, then review coherence and broaden integrated qualification across repositories, interruptions, hosts, and risk classes. Proceed between increments unless observed defects require correction; do not infer effectiveness from matching prose or Markdown checks.

Measure accepted outcomes, unnecessary intervention, clarification/replan frequency, scope violations, intent-preservation failures, requirement-to-evidence coverage, verification-gap escapes, context/model turns, correction passes, escaped material defects, repeated work after resume, and process growth. Interpret autonomy and speed alongside correctness; a justified clarification is not a failure to optimize away. The roadmap owns detailed milestones and budgets.

The original v3 increment reconciled the design and evaluation boundary. R2 implementation and bounded observations remain historical evidence in the [R2 trial record](../tests/r2/README.md) for its recorded hashes. The R3 package capability is described here and its new observations belong in the [R3 trial record](../tests/r3/README.md); do not infer R3 host qualification or behavioral results from R2 evidence or package presence. Installation/discovery claims, R4/R5 behavior, broader qualification, and performance claims remain limited by recorded evidence.

## 8. R1 v3 implementation readiness

R1 v3 supplied the design used by the R2 prototype. The following R2 acceptance boundary is retained as historical evidence; the trial record distinguishes demonstrated behavior for its recorded package identity from unverified host surfaces and later R3 behavior.

The R2 prototype delivered and verified:

- one discoverable public `afr` entrypoint and the planning reference, using the planned package shape;
- explicit identification of skill package root, target project/workspace, target instructions, and available host capabilities;
- activation, authority, `direct`/`umbrella`/`spike`/`stop` routing, planning assurance, intent preservation, minimal architecture-contract reasoning, and plan self-review;
- reuse of adequate existing specifications, including required companion context, without an AFR-specific duplicate by default;
- an explicit capability result that stops at planning when work/review/delivery methods are not implemented;
- concrete behavioral trials for the R2 cases above, recording observations rather than merely checking for instruction text; and
- concise documentation of the actually qualified host/loading path and unsupported surfaces.

R2 did not establish local implementation, PR delivery, umbrella continuation, cross-host parity, stable-release readiness, or comparative productivity. R3 now defines the local implementation capability; its behavioral and host claims require the separate R3 trial record. R4/R5 delivery and umbrella claims remain future work. Exact metadata/frontmatter, prompt wording, fixture locations, and host installation details remain implementation decisions unless evidence exposes a product or authority conflict.

## 9. R3 local implementation readiness

R3 is implemented by the public [coordinator](../.agents/skills/afr/SKILL.md), [planning](../.agents/skills/afr/references/planning.md), [work](../.agents/skills/afr/references/work.md), and [review](../.agents/skills/afr/references/review.md) methods. The coordinator owns authority, sequencing, stop/resume, and reporting; the references own phase methods. Planning, research, and review-only requests do not authorize implementation or correction, while explicitly requested, required, or risk-justified planning artifacts remain allowed. An authorized direct path can reach a verified local candidate through requirement-based work, evidence, actual-diff inspection, proportional review, and bounded correction within that implementation authority. A review-only request needs explicit fix authority before correction. The [R3 trial record](../tests/r3/README.md) owns observations; its presence does not establish host qualification or trial results, and R2 results remain historical evidence for their recorded hashes. R4 remote delivery and R5 umbrella continuation remain unavailable.
