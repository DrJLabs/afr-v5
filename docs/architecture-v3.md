# AFR v5 architecture and behavior specification — R1 v3

**Status:** current design; R3 local work/review, R4 PR delivery, and R5 authorized umbrella continuation are implemented. Host and behavioral qualification is limited to the [R2 historical record](../tests/r2/README.md), [R3 trial record](../tests/r3/README.md), bounded [R4 trial record](../tests/r4/README.md), and separate [R5 trial record](../tests/r5/README.md).
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

This is the target package shape. The [coordinator](../.agents/skills/afr/SKILL.md), [planning reference](../.agents/skills/afr/references/planning.md), [work reference](../.agents/skills/afr/references/work.md), [review reference](../.agents/skills/afr/references/review.md), [delivery reference](../.agents/skills/afr/references/delivery.md), and explicit-only invocation metadata exist. Native host facilities supply tools, workspaces, sessions, and subagents. Git and checks supply local source facts; the delivery reference consumes native forge or external monitoring capabilities without implementing a watcher. File presence is not an installation or host-qualification claim.

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

Operational instructions live in the implemented owners within `afr/`. This architecture summarizes the current R3–R5 package and links to the coordinator as the execution owner rather than duplicating its continuation procedure.

| Owner | Responsibility | Information needed by the next phase |
| --- | --- | --- |
| `SKILL.md` | Explicit activation, authority, host/capability boundary, final route choice, sequencing, stop, resume, continuation, and terminal reporting | Current outcome, available phase capability, authorized endpoint, next action or blocker |
| `references/planning.md` | Discovery, source-intent preservation, context classification, route recommendation, implementation contract, minimal architecture contract, planning assurance, outcome/dependency analysis, plan self-review | Authoritative source and indispensable companions, requirements, decisions/discretion, acceptance/evidence approach, risks, dependencies, parent acceptance when applicable |
| `references/work.md` | Workspace choice, implementation, representative-pattern validation when warranted, focused conformance evidence, actual-diff inspection | Candidate/base identity, changes, requirement coverage, checks and limitations, contradictions or residual concerns |
| `references/review.md` | Risk-selected review, independent conformance and verification-effectiveness assessment when warranted, finding classification, bounded correction and rechecks | Findings/dispositions, reviewed revision, acceptance and verification gaps, remaining material concerns |
| `references/delivery.md` | Authorized PR creation/reuse, native monitoring, feedback through the review method, exact-head merge, and local synchronization | PR/head, delivery facts, evidence needed for dependent work, incomplete obligations |

References return results to the coordinator. They do not independently activate AFR, choose the next umbrella outcome, or redefine lifecycle stop/completion rules. Planning defines acceptance; work and review assess it; delivery establishes delivery facts; the coordinator determines whether the requested scope is complete.

Ordinary transitions use the same agent context. Use concise file-based handoffs for large delegated work or resumption, naming existing sources, revisions, evidence, and remaining concerns. A handoff distinguishes material sources required for correctness from background that may be consulted for rationale or exceptional cases. It can point to authoritative content instead of copying it, but must not make indispensable context undiscoverable. Separate briefs, generated diff packages, certificates, receipts, and JSON result envelopes are not mandatory phase artifacts.

## 4. Coordinator behavior

### Activation and route selection

The [coordinator](../.agents/skills/afr/SKILL.md#planning-and-route-choice) owns explicit activation and the `direct`, `umbrella`, `spike`, and `stop` route/result meanings. Route describes work shape independently of planning assurance. A completed research result is distinct from an implementation-ready contract and from authority to execute it.

### Capability and host boundary

The coordinator's [available-capability boundary](../.agents/skills/afr/SKILL.md#available-capability) keeps explicit planning and research outside implementation and correction authority, while permitting planning artifacts under its stated conditions. R3 provides the local implementation path, R4 adds authorized PR creation/reuse, review convergence, exact-head merge, and separately observed local synchronization, and R5 adds authorized umbrella continuation through the same four phase references. The user's original endpoint remains visible when a missing phase or unsupported host capability prevents fulfillment.

Portable workflow text does not make host support interchangeable. Qualify discovery, loading, tools, delegated work, interruption, and reporting on each supported host. An initial Codex qualification may precede ChatGPT qualification without removing ChatGPT from the product goal; report the actual supported surface honestly.

### Sequence and continuation

Coordinate planning → work → review when warranted → bounded correction/recheck → authorized delivery when requested and supported. New accepted findings use the same correction method, and every pushed fix re-enters the affected review/readiness path at its new head. For an authorized umbrella, the coordinator automatically continues to the next dependency-eligible outcome while authority and prerequisites permit, preserving exact revision/workspace boundaries and returning to combined parent acceptance at integration boundaries. Continue within the direct outcome while scope, authority, and prerequisites permit useful work.

When many outcomes depend on a new or materially uncertain pattern, establish and verify a representative use before reproducing it broadly when a wrong choice would create expensive downstream correction. Existing project conventions, prior qualified implementations, or low-cost reversibility can make that unnecessary. This is a planning judgment, not a mandatory prototype gate.

For an authorized umbrella, the coordinator chooses an unfinished outcome whose dependencies have reached their required revisions or delivery boundaries and whose source/workspace boundary is available. It uses explicit plan order to break otherwise immaterial ties and reuses the direct workflow. An unmerged candidate cannot satisfy a dependency requiring a merged base. If unfinished work exists but none is eligible, report the dependency, cycle, scope, authority, or safety blocker; do not declare completion or add a scheduler.

Check user steering before consequential actions and after delegated results. Honor a stop promptly using host controls. A late result cannot restore authority after a stop. Reobserve uncertain in-flight external actions before reporting their disposition.

### Parent-level umbrella acceptance

Planning defines the parent objective, shared invariants, dependency boundaries, and where combined behavior can be meaningfully checked. At those integration boundaries, assess the actual combined revision/configuration against the parent contract. Examples include interface agreement, migration ordering, and preservation of behavior across outcomes.

Completion requires every required outcome's authorized endpoint, satisfied dependency revisions/boundaries, coherent shared invariants, and evidence that the combined result meets the parent objective. Passing outcome checks or merging every PR alone is insufficient. A failed combined check remains an acceptance gap requiring in-scope correction or a reported blocker, even when every outcome was individually accepted.

Reuse relevant outcome evidence. Run integration checks when combined behavior becomes meaningful or affected evidence changes; do not rerun every check after every outcome. Parent acceptance does not authorize production effects or other checks outside the current boundary.

### Resume and evidence reuse

The coordinator's [stop and resumption method](../.agents/skills/afr/SKILL.md#stop-and-resumption) reconciles current intent, source/workspace observations, PR observations, and valid prior evidence. Resolve existing branches/worktrees before replacements and associate reused implementation, check, review, and delivery evidence with the relevant candidate/base, requirements, prerequisites, and policy. Changed inputs refresh affected work and evidence; still-valid checks remain reusable.

After an ambiguous external write, inspect external state before retrying. A remotely merged PR with incomplete local synchronization resumes at the missing local obligation, not implementation or merge.

### Completion and blockers

The implemented [terminal report](../.agents/skills/afr/SKILL.md#terminal-report) owns R3–R5 outcomes and effects reporting. Local completion additionally requires conformance, risk-appropriate checks, actual-diff inspection, safe temporary-effect disposition, and any selected review/correction. Delivery completion is endpoint-specific: PR creation requires observed publication and PR/head identity; monitoring requires current readiness facts; merge requires readiness plus an exact-head remote merge; synchronization or bookkeeping is required only when requested or otherwise in scope. R5 adds parent acceptance for umbrellas. Failed or unavailable required checks block completion when required by the selected endpoint; an unreviewed, unverified, or not-ready candidate remains partial when that assurance is required.

## 5. Phase requirements

### Planning and the implementation contract

The [planning reference](../.agents/skills/afr/references/planning.md#establish-a-sufficient-implementation-contract) is now the canonical method and field inventory. Its contract separates behavior/constraints, settled decisions, and a revisable approach; it preserves source intent and material acceptance without requiring a duplicate plan or template completion. The minimal architecture-contract test resolves consequential incompatible choices before dependent work while leaving reversible internals discretionary.

Its [outcome/dependency method](../.agents/skills/afr/references/planning.md#size-outcomes-and-dependencies) supplies umbrella parent acceptance and selective representative-pattern verification for R5; the [coordinator](../.agents/skills/afr/SKILL.md#umbrella-continuation) owns authorized continuation and endpoint selection.

### Assurance from planning through review

The [planning assurance and self-review method](../.agents/skills/afr/references/planning.md#planning-assurance-and-self-review) owns the `lean`, `standard`, and `protected` expectations and planning-sufficiency judgment. The [work reference](../.agents/skills/afr/references/work.md) owns local implementation and conformance evidence; the [review reference](../.agents/skills/afr/references/review.md) applies the selected independent review coverage and may increase it for observed risks within authority. The [delivery reference](../.agents/skills/afr/references/delivery.md) owns delivery-specific observation and continuation decisions.

### Work and conformance evidence

The [work reference](../.agents/skills/afr/references/work.md) is the canonical method for local workspace choice, implementation, requirement-based verification, and actual-diff inspection. Explicit planning, research, and review-only requests do not authorize implementation or correction, or ordinary target-source edits. Planning may create or amend a planning artifact when explicitly requested, required by the target, or justified for resumability or risk within authority. An authorized direct implementation may preserve unrelated dirty work, use an isolated workspace when warranted, and stop rather than overwrite unexplained changes or exceed the selected endpoint.

Preserve unrelated changes. Choose a feature branch or isolated worktree according to repository policy and risk; reuse valid isolation. Escalate unexplained overlap that cannot be safely separated. Unrelated dirt alone is not a blanket stop.

Use the host agent for implementation, normally one implementer per cohesive outcome. Delegate only independent, bounded work with clear ownership and cheap synthesis. Native tools own spawning, waiting, interruption, and resumption. Give each implementer the authoritative requirements and required companion context for its outcome; background rationale remains available without being loaded by default.

When the plan identifies a representative-pattern checkpoint, implement and verify that slice before broad repetition. Replan only the dependent work if the pattern fails; preserve unaffected outcomes and evidence. Do not create a prototype ritual for established patterns.

Establish evidence for each material requirement, including preservation and failure behavior. Choose unit, integration, contract, compatibility, property, migration, performance, security, operational, or manual checks according to the requirement. A short explanation or a few links can establish coverage; no mandatory traceability IDs or separate evidence database is required.

Passing implementation-selected tests is insufficient when acceptance remains unmet. Inspect the actual diff and associate evidence with the candidate/base and relevant requirement source. Distinguish passed, failed, timed-out, unavailable, and inconclusive checks. Include useful regression evidence for bug fixes when practical, follow repository requirements, and expand coverage for observed failures or affected risks. Avoid dependency reinstalls or full-baseline reruns without a relevant reason.

### Architecture-aware adoption (M8 draft)

The phase owners now carry a generic architecture-change contract through the existing workflow. Planning discovers the target-owned model, decisions, mappings, native rules, and checks; classifies ordinary versus material boundary changes; and requires a viewable proposal, complexity rationale, and explicit owner selection of the exact revision before dependent implementation. Work carries that selected identity, uses the target's own protocol and checks, and surfaces stale or changed boundaries. Review checks intended design against observed structure and behavior, cumulative complexity, source coverage, exceptions, and control edits. Delivery ties applicable architecture evidence and finalized target-owned identity to the actual candidate and trusted base. The coordinator reobserves that identity on umbrella continuation and resume.

This guidance is deliberately protocol-independent. The consuming project owns proposal format, finalization, native commands, and any trusted gate. It does not add a second workflow, approval system, automatic rebaseline, or architecture runtime. A green model/parser/import check remains insufficient for behavior, and planning or rendering alone does not authorize implementation or establish approval.

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

The [delivery reference](../.agents/skills/afr/references/delivery.md) is the canonical method for R4 PR convergence. It covers exact repository/remote/target/source/PR identity, authorized creation or reuse, native or external monitoring, finding classification through the review method, fresh-head readiness, protected exact-head remote merge, and independently observed safe local synchronization. R5 reuses this method for eligible umbrella outcomes; watcher mechanics remain external and the coordinator remains the continuation owner.

## 6. Deterministic helpers

R1 v3 and R5 retain **zero required custom helpers**. Native Git, repository checks, and forge capabilities are the initial tools. R5 adds no runtime or state store. The donor matrix's candidates remain deferred; donor tests alone do not prove that v5 needs a helper.

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
| R4 | Bounded trial: exercise exact-head readiness, missing/pending/failed/unknown checks, review feedback, and ambiguous external effects within an authorized disposable or controlled setting. Evidence belongs in the [R4 trial record](../tests/r4/README.md); it does not establish broad host or forge qualification. |
| R5 | Bounded trial: exercise the implemented umbrella continuation, dependency/revision/workspace boundaries, shared architecture decisions, selective resume/correction, and combined acceptance, including individually successful outcomes whose combined behavior fails. The [R5 trial record](../tests/r5/README.md) owns bounded evidence and limits. |

R2 was planning-complete but execution-incomplete for the package revision recorded in its trial evidence. R3 established the direct local implementation path, and R4 adds delivery to the same workflow: explicit planning, research, and review-only requests do not authorize implementation or correction, while an authorized direct run may reach a delivered PR through work, evidence, proportional review, bounded correction, and exact-head delivery. R5 adds multi-outcome continuation in the coordinator without a second workflow; its bounded trial evidence remains separate. No milestone may silently substitute an unimplemented phase with an embedded second workflow.

Trial evidence should identify the authoritative source and required companions, target project/workspace, host and skill package identity, relevant revision/base, observed behavior versus expected acceptance, coverage gaps, and intervention or correction needed. Keep evidence in existing project/test artifacts or the task record according to need; do not introduce a trial registry. R4 tests do not themselves grant live push/PR/merge authority.

Early bounded trials are different from broad qualification of an incomplete package. Build R2–R5 in the same package, test available behavior as it appears, then review coherence and broaden integrated qualification across repositories, interruptions, hosts, and risk classes. Proceed between increments unless observed defects require correction; do not infer effectiveness from matching prose or Markdown checks.

Measure accepted outcomes, unnecessary intervention, clarification/replan frequency, scope violations, intent-preservation failures, requirement-to-evidence coverage, verification-gap escapes, context/model turns, correction passes, escaped material defects, repeated work after resume, and process growth. Interpret autonomy and speed alongside correctness; a justified clarification is not a failure to optimize away. The roadmap owns detailed milestones and budgets.

The original v3 increment reconciled the design and evaluation boundary. R2 implementation and bounded observations remain historical evidence in the [R2 trial record](../tests/r2/README.md) for its recorded hashes. R3 and R4 package capabilities are described here and their observations belong in the [R3 trial record](../tests/r3/README.md) and [R4 trial record](../tests/r4/README.md); R5 capability is described here and its observations belong in the separate [R5 trial record](../tests/r5/README.md). Do not infer host qualification or behavioral results from package presence. Installation/discovery claims, broader qualification, and performance claims remain limited by recorded evidence.

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

R2 did not establish local implementation, PR delivery, umbrella continuation, cross-host parity, stable-release readiness, or comparative productivity. R3 defines the local implementation capability and R4 defines PR delivery; their behavioral and host claims require the separate trial records. R5 now defines umbrella execution in the coordinator; its behavioral and host claims require the separate R5 trial record. Exact metadata/frontmatter, prompt wording, fixture locations, and host installation details remain implementation decisions unless evidence exposes a product or authority conflict.

## 9. R3 local implementation readiness

R3 is implemented by the public [coordinator](../.agents/skills/afr/SKILL.md), [planning](../.agents/skills/afr/references/planning.md), [work](../.agents/skills/afr/references/work.md), and [review](../.agents/skills/afr/references/review.md) methods. R4 adds the [delivery reference](../.agents/skills/afr/references/delivery.md), and R5 adds authorized umbrella continuation in the coordinator while reusing those four references. The coordinator owns authority, sequencing, continuation, stop/resume, combined acceptance, and reporting; references own phase methods. Planning, research, and review-only requests do not authorize implementation or correction, while explicitly requested, required, or risk-justified planning artifacts remain allowed. An authorized direct path can reach a verified local candidate and, when delivery authority and host capability are present, carry it through PR convergence and safe synchronization. An authorized umbrella can continue eligible outcomes with exact dependency revision/workspace boundaries and selective evidence refresh, then require combined parent acceptance. A review-only request needs explicit fix authority before correction. The [R3 trial record](../tests/r3/README.md), [R4 trial record](../tests/r4/README.md), and separate [R5 trial record](../tests/r5/README.md) own observations and limits; their presence does not establish broad host qualification, and R2 results remain historical evidence for their recorded hashes.
