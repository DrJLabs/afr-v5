# AFR v5 workflow coherence and method-selection review

**Review date:** October 9, 2026  
**Repository:** DrJLabs/afr-v5  
**Reviewed revision:** [9b7def12d900ae787e2b155e0dec53eef7b59146](https://github.com/DrJLabs/afr-v5/commit/9b7def12d900ae787e2b155e0dec53eef7b59146)  
**Source baseline:** canonical authoring checkout, branch main; initially clean. Local HEAD, the local origin/main tracking reference, and GitHub main agreed at inspection.  
**Disposition:** analysis and proposed improvements. This review does not activate AFR or approve implementation, installation, publication, native-goal qualification, or other external effects.

## 1. Overall finding

**AFR v5 has a coherent core workflow. Its most useful next improvements are clearer method selection, a few precise endpoint and provenance rules, and focused qualification of the actual host/loading surface.**

The coordinator and four phase references cover the path from discovering intent through planning, implementation, requirement-based verification, review/correction, authorized PR delivery, synchronization, umbrella acceptance, and resumption. The strongest safeguards are already present: explicit activation; separate package/target/workspace/host identities; preservation of unrelated work; real independent review when required; exact candidate and dependency evidence; conditional merge; observation before retrying uncertain writes; and combined parent acceptance. [S1] [S2] [S3] [S4] [S5]

This review found **no demonstrated need for another workflow phase, mandatory helper, runtime, scheduler, or persistent state surface**. The zero-helper decision remains consistent with the evidence reviewed. The optional skill-synchronization utility is a separate operational facility, not a required AFR execution dependency. [S7] [S14]

An agent can recover the intended method from the present package. However, several decisions are distributed across references or use wording that admits different interpretations. That matters most when the agent starts from a sufficient external specification, has limited review capabilities, receives a publication-only request, or resumes after the package itself changes. The source is more mature than the breadth of current host qualification: implemented instructions, bounded behavioral observations, installed discovery, and reliable repeated use remain different claims.

### Priority summary

“Medium” means a meaningful ambiguity or evidence gap worth addressing in the next small improvement increment. “Low” means a bounded navigation, closure, or maintainability improvement. These are review priorities, not claims of observed production failures.

| ID | Priority | Finding | Primary owner |
| --- | --- | --- | --- |
| F1 | Medium | Contract reuse and standard assurance leave the actual review obligation too implicit | Coordinator and planning assurance |
| F2 | Medium | Umbrella eligibility differs for independent outcomes with no ordering dependency | Coordinator route table |
| F3 | Medium | Draft/review PR creation with known acceptance gaps has no explicit policy | Coordinator and delivery |
| F4 | Medium | Package location is identified, but its governing revision is not consistently carried through loading/resume | Coordinator identity and resumption |
| F5 | Medium | Tool feasibility and current qualification require too much reconstruction | Coordinator capability boundary; existing qualification owners |
| F6 | Medium | A demonstrated implicit-installation failure lacks a recorded focused forward-test of the corrective rule | Existing ordinary-work trial record |
| F7 | Low | The roadmap’s current-status section mixes M10 and historical M8 wording | docs/roadmap.md |
| F8 | Low | Required post-delivery bookkeeping can create an unspecified local change after merge | Planning ownership and delivery |
| F9 | Low | “Changes to components” is broader than the intended architecture-change threshold | Planning architecture classifier |
| F10 | Low | Line budgets underdescribe the amount of text an agent loads | Existing complexity budget and measurements |

## 2. What was reviewed and what this establishes

The review examined the complete current coordinator, four phase references, invocation metadata, root CHAT.md, and Codex-facing AGENTS.md as an audit subject. It followed README navigation into architecture v3, the roadmap, the R6 assessment, and relevant R3/R4/R5, delegation, roadmap, and M9 trial records. The optional synchronization instructions were read only where they bear on package provenance; the synchronization implementation and live services were not audited.

Current local source and Git/worktree identity were inspected through Desktop Commander and the documented DC-Runner interface. GitHub supplied the current default-branch observation and commit-pinned supporting records. Three independent analytical passes covered method selection, execution/delivery, and qualification. Their candidate findings were reconciled against source and counterevidence. Miyo was unavailable; no absence claim was inferred from that failure.

This is a **static and evidence-record review**, including analytical scenario walkthroughs. It is not a fresh AFR execution, live delivery test, installed-package audit, or proof that a host will follow every instruction. Historical observations below retain their recorded package identities. A hypothetical divergent agent response is labeled as a scenario, not an observed defect.

Only this findings document is the intended project change. Existing instructions, package files, plans, tests, branches, and services are outside the change scope.

## 3. End-to-end coherence assessment

| Boundary | Current information and responsibility | Assessment |
| --- | --- | --- |
| Activation and target discovery | Coordinator confirms explicit AFR selection; separates loaded package, target, workspace, and host; reads applicable target instructions and establishes authority | Coherent. Preserve the distinction between auditing AFR and invoking it. Add revision identity to package provenance (F4). |
| Planning or contract reuse | Planning preserves source intent and required companions, separates behavior/decisions/tactics, defines credible acceptance, and recommends route/assurance | Coherent. Make assurance and architecture applicability explicit even when reusing a sufficient contract (F1). |
| Route and bounded scope | Coordinator chooses direct, umbrella, spike, or stop; roadmap selects bounded work without granting authority | Coherent except for the no-dependency umbrella predicate (F2). A roadmap and goal mode are not additional routes. |
| Architecture decisions | Planning classifies changes and requires an exact selected proposal for architectural/greenfield work; native target protocol remains authoritative | Coherent. Narrow one broad phrase (F9); do not remove the deliberate owner-selection boundary. |
| Workspace and implementation | Work checks actual source ownership, dirty state, base, isolation, required local inputs, shared effects, and permitted toolchain | Coherent. A worktree is not isolation for shared ports, services, caches, or external resources. |
| Verification | Work maps material requirements to consumer/integration evidence; inspects commands and assertions; distinguishes pass, failure, timeout, unavailable, and inconclusive | Strong. Requalify the corrective command-effects rule against the known failure class (F6). |
| Review and correction | Review applies assurance, assesses the actual candidate, verifies findings, permits only authorized correction, and refreshes affected evidence | Strong. Clarify when standard’s “normally” independent review becomes binding (F1). |
| PR and merge | Delivery resolves destination and exact candidate, reuses a matching PR, monitors within limits, checks required policy, and guards the reviewed head | Strong merge boundary. Clarify incomplete draft/review PR publication (F3). |
| Local synchronization and closure | Delivery separately observes remote merge and safe synchronization; coordinator reconciles progress and completion | Coherent. Specify disposition of required tracked bookkeeping after delivery (F8). |
| Umbrella continuation | Coordinator observes prerequisites before dependent edits, uses the same direct sequence, and requires combined parent acceptance | Strong. Individually green children or merged PRs are explicitly insufficient. |
| Stop and resume | Coordinator respects current steering, observes in-flight effects, reconciles changed inputs, and resumes at missing obligations | Strong target-state handling. Governing package changes need equivalent treatment (F4). |
| Terminal report | Coordinator reports the reached endpoint, actual evidence, temporary effects, and remaining gaps | Coherent. Keep publication-artifact completion distinct from implementation acceptance where F3 applies. |

The relevant operational owners are the coordinator and its four references. Architecture and roadmap documents should summarize and link to those owners; they should not become another executable workflow. [S1] (lines 100–155) [S2] [S3] [S4] [S5] [S6] (sections 3–5)

### Relationship of the main stages

This diagram summarizes the current intended relationships. The endpoint and authority checks apply throughout; it is not an instruction to run every stage.

~~~mermaid
flowchart TD
    A["Request, target, authority, and endpoint"] --> B{"Sufficient contract?"}
    B -->|No| C["Planning or bounded investigation"]
    C --> D{"Requested result ready?"}
    D -->|Planning or research endpoint| Z["Report result and evidence gaps"]
    D -->|Execution authorized and ready| E["Selected direct outcome"]
    B -->|Yes: reuse| E
    E --> F["Implement and verify requirements"]
    F --> G["Required review and dispositions"]
    G -->|Authorized correction| F
    G -->|Local endpoint| H["Assess outcome acceptance"]
    G -->|Delivery authorized| I["PR, convergence, and requested delivery"]
    I --> H
    H -->|Umbrella work remains eligible| E
    H -->|Outcome endpoints reached| J["Combined acceptance where applicable"]
    J -->|Authorized correction for acceptance gap| E
    J -->|Satisfied or explicit blocker| Z
~~~

Review-only and delivery-only requests may enter at their existing candidate’s missing obligation; they do not repeat valid planning or implementation. Any branch can stop affected work for an unresolved decision, missing authority, unavailable indispensable evidence, or a current user stop. [S1] (lines 35–48, 100–108, 130–155)

## 4. Findings and proposed improvements

### F1 — Make assurance selection and the review obligation explicit on every work entry

**Observation.** The coordinator permits reuse of a sufficient source or prior contract without another planning round. The assurance criteria live in planning, while work requires selected assurance and review explicitly supplies a missing-assurance fallback for review-only requests. Standard assurance calls for “normally” one independent reviewer, while later completion rules refer to required review. [S1] (line 35) [S2] (lines 63, 115–138) [S3] (line 7) [S4] (lines 7–9)

**Possible divergence.** An external specification can be behaviorally sufficient without an AFR assurance label. One agent may derive assurance before implementing; another may arrive at work’s missing-prerequisite boundary and unnecessarily replan. On a host without a separate reviewer, one agent may treat “normally” as permission to complete standard work after self-review; another may treat independence as required.

**Counterevidence.** The coordinator also says new work should read the planning method, and work refuses to invent missing prerequisites. Existing planning covers review depth. These are meaningful safeguards: the problem is clarity and consistent interpretation, not an absent safety barrier. The analogous review-only ambiguity was previously corrected and given a focused trial. [S8] (lines 41–47)

**Proposed improvement.** Add one coordinator invariant, linking to existing sections rather than duplicating their contents:

> Before work, select or reconcile the lowest adequate assurance and determine whether the architecture-change requirements apply, including when reusing a sufficient contract. Resolve only the missing decision; do not rebuild an adequate plan.

In planning’s assurance owner, state the actual required checks and review coverage when selecting assurance. Recommended policy: standard defaults to one independent review; a justified exception must reflect the task’s consequences and may not waive a user/target requirement. Reviewer unavailability alone should not justify an exception. Preserve lean self-review and proportional protected coverage. This proposed policy should be selected explicitly when implementing the improvement, not inferred as already binding.

**Focused check.** Reuse an adequate external contract with no assurance label; compare ordinary and security-sensitive changes, then repeat the required-review case with no reviewer. Expect consistent obligations, no duplicate plan, no fabricated independence, and an honest coverage gap.

### F2 — Allow an umbrella with independent children and no invented dependency

**Observation.** The coordinator’s umbrella row requires several independently deliverable outcomes “with meaningful dependencies.” Planning recommends umbrella for independently deliverable outcomes without requiring a dependency. Continuation already supports several eligible outcomes and immaterial ordering ties. [S1] (lines 40–44, 118) [S2] (lines 75–81)

**Possible divergence.** A bounded milestone provides two independent export formats using an established API. Neither requires the other. An agent could force them into direct work, invent an ordering dependency, or ask the user to select a routine route.

**Counterevidence.** The existing continuation procedure can handle an empty dependency set. This is a predicate mismatch, not a missing execution capability.

**Proposed improvement.** Change the coordinator’s umbrella criterion to:

> Several independently deliverable outcomes within one bounded parent objective; record meaningful dependencies where they exist.

Retain outcome endpoints, shared invariants, explicit scope, and combined parent acceptance. Align summaries when they repeat the predicate; do not add a new route.

**Focused check.** Two independent deliverables select umbrella without manufactured ordering. Both endpoints and their combined parent acceptance are assessed.

### F3 — Decide how an explicitly requested draft PR with known gaps is handled

**Observation.** Delivery says to publish accepted changes and exclude unreviewed changes, but also permits PR bodies to disclose acceptance gaps and returns an observed identity for PR-creation-only requests. The coordinator conditions direct completion on conformance and required assurance. Architecture describes completion as endpoint-specific. [S5] (lines 9–11) [S1] (lines 108, 153) [S6] (line 125)

**Possible divergence.** Request: “Open a draft PR for this candidate so we can discuss the known failing integration case; do not fix or merge.” One reading allows the requested artifact with disclosed gaps; another requires acceptance before any publication. The source does not explicitly settle draft support.

**Counterevidence.** The accepted-candidate path and merge requirements are clear. No observed unsafe publication is asserted.

**Proposed improvement.** Select one explicit policy. Recommended: when clearly requested and permitted by target policy, a draft/review PR can satisfy its publication endpoint while retaining known acceptance gaps. It must not be described as an accepted implementation, merge-ready candidate, or completed broader delivery objective. An accepted production candidate and a requested review artifact have different acceptance criteria. If incomplete drafts are intentionally unsupported, state that boundary directly.

**Focused check.** Distinguish accepted PR creation, explicitly requested draft creation with a known gap, and a merge request with the same gap. The merge remains blocked.

### F4 — Preserve governing package revision across progressive loading and resume

**Observation.** Activation captures package location or host identifier and resolves references relative to it. Resume carefully reconciles target source, contracts, progress, architecture, and delivery, but does not explicitly reconcile a changed governing AFR revision. [S1] (lines 18, 100–106, 132–136)

**Possible divergence.** A run reads the coordinator from a mutable directory; that directory changes before delivery or resumption. A later phase may come from different bytes despite the same package path. The agent could attribute the whole run to an unverified single version.

**Counterevidence.** The optional publisher requires a quiet window and tells operators to keep consumers from loading during publication; installation does not reload running sessions. The representative M8 record separately pinned and rechecked its governing package. Those practices reduce risk but are not a general consumer rule. [S14] (lines 50–61) [S10] (lines 204–208)

**Proposed improvement.** Record the governing source revision or immutable host package version when available, resolve progressive references consistently, and reconcile package changes on resume. Where the host cannot expose immutable identity, report that limit. Use existing session/checkpoint context; do not introduce a manifest, registry, snapshot service, or mandatory eager loading of every reference.

**Focused check.** Change one reference at the same path between phases in a disposable scenario. The agent should disclose/reconcile the boundary and preserve valid target evidence, rather than silently reporting one unchanged governing version.

### F5 — Make selected-endpoint tool feasibility and qualification easy to see

**Observation.** The package correctly delegates execution to host-native capabilities, but a reader must combine activation, assurance, architecture, delivery, and separate trial records to establish which tools and evidence a selected endpoint needs. Current qualification remains bounded. [S1] (lines 10–25, 64–96) [S4] (lines 7–9) [S5] (lines 15–40) [S9] [S11] [S12] [S13]

The current ChatGPT session’s advertised skill catalog exposed legacy AFR-v2 entries without a public v5 afr entry. The v5 source was accessible through repository/file tools. This is a scoped observation about this session, not proof that the Codex installation on the requested machine lacks v5. Older skills were not invoked.

**Consequence.** Source availability can be mistaken for installed discovery; a required independent reviewer or guarded merge operation may be discovered missing late in the run. The user’s question about whether an agent has the necessary information and tools is therefore partly a host qualification question, not solely a skill-writing question.

**Proposed improvement.** In the existing coordinator capability boundary, require early, proportionate confirmation of capabilities needed by the selected endpoint and assurance. Do not probe unused goal controls or every possible tool. Missing future capabilities can leave a useful authorized local result, with the endpoint gap explicit.

Add a compact qualification summary in an existing navigation owner, linking to the dated trial records instead of copying them. State source presence, exercised loading path, behavioral scope, remaining gaps, and the next relevant check. Keep runtime availability as a fresh host observation.

**Focused check.** Raw requests without prescribed routes or rosters should lead to appropriate tool selection. Missing required reviewer, indispensable architecture evidence, complete forge-policy observation, or exact-head merge guard must produce the correct bounded result.

### F6 — Close the known verification-wrapper effects regression independently of goal mode

**Observation.** A historical M8 trial’s uv command created an environment and installed seven locked packages despite a no-installation constraint. The parent caught the violation; an existing interpreter supplied the subsequent checks. Current work instructions explicitly require checking wrappers for installation, environment/cache generation, network access, and other effects. [S10] (line 185) [S3] (line 31)

The explicit proposed forward-test is M9 Case G, marked Not run. The M9 record also preserves the user’s deferral of further qualification. No recorded focused execution of that corrective rule was identified in the reviewed records. [S12] (lines 25–34, 85–87, 118)

**Interpretation.** This is a demonstrated historical failure plus a remaining evidence gap. It is not proof that the corrected current package still fails. Ordinary goal-off compatibility passes do not exercise this particular trap.

**Proposed improvement.** Reuse the scenario as a tiny ordinary-work regression in the existing trial owner. It should inspect a plausible wrapper before execution and choose an available permitted toolchain or report the check unavailable. Do not install packages merely to demonstrate the prohibited effect. This case need not wait for native goal activation or reopen the whole deferred M9 program.

**Focused check.** Observe command inspection before execution, no unauthorized environment/dependency creation, correct fallback or gap reporting, and accurate final effect accounting. This document proposes the check; it does not authorize or execute it.

### F7 — Give the roadmap one unambiguous current next-action section

**Observation.** The roadmap header remains dated September 15 and emphasizes R3–R6/M8. Section 14 calls M10 the current local source increment, then describes “the current increment” as complete for bounded M8. M10 now exists in the reviewed main revision; M9 qualification remains separate and incomplete. [S15] (lines 3–7, 331–349, 428–434)

**Consequence.** An agent resolving current priority has to disentangle historical completion language from current source work. The problem is navigation, not fabricated evidence.

**Proposed improvement.** Rewrite the existing current-status/next-increment section as a concise dated statement distinguishing M10 source and bounded trials, M9 deferred qualification, and remaining discovery/representative-use decisions. Rename the second “current increment” explicitly to M8. Preserve historical trial entries and their original claims; do not rewrite them to imply publication or execution that had not happened at their observation time.

The selected next action should identify a bounded outcome or a required owner decision. A chronological milestone number alone should not select it.

**Focused check.** A fresh reader can identify the latest delivered source, outstanding qualification, and the next selected action without searching old status paragraphs.

### F8 — Specify the disposition of required bookkeeping after delivery

**Observation.** The coordinator updates designated progress and reconciles contract lifecycle at acceptance boundaries. Delivery reconciles required plan bookkeeping after synchronization, and terminal completion includes required bookkeeping. [S1] (lines 58, 153) [S5] (line 48)

**Possible divergence.** If progress lives in the same repository just merged, recording the observed merge may produce a new local documentation change after the delivered revision. Another push/PR is not automatically authorized.

**Counterevidence.** Existing authority rules already prevent assuming extra publication. Target conventions may fully resolve the case.

**Proposed improvement.** During document-owner and endpoint selection, establish the update path: already authorized external progress owner, local retained update, or explicitly scoped follow-up under target convention. Distinguish the observed delivery endpoint from whether a later bookkeeping edit was delivered. Avoid recursive bookkeeping PRs or a second ledger.

**Focused check.** With a tracked roadmap and merge-only authority, report the remote result and exact disposition of any local bookkeeping change without silently starting another delivery cycle.

### F9 — Narrow the architecture classifier’s component wording

**Observation.** Planning preserves ordinary changes within existing boundaries but also classifies “changes to components” as architectural. Work and architecture use the narrower concept of material boundary changes. [S2] (lines 40–48) [S3] (line 23) [S6] (line 155)

**Possible divergence.** A literal reading can turn a bug fix inside a component into a proposed-design/owner-selection exercise.

**Counterevidence.** The surrounding ordinary-work exemption makes the intended threshold recoverable.

**Proposed improvement.** Use “adding/removing components or changing component boundaries or ownership,” alongside the existing dependency-direction, trust/state, service, and material abstraction criteria. An internal parser fix should differ from moving state ownership across a trust boundary. Preserve exact owner selection for genuine architecture changes and greenfield intent.

### F10 — Measure loaded text as well as line count before simplifying further

**Observation.** The current package is inside the stated line budgets, but long paragraphs make line counts an incomplete context measure. Locally measured source counts are:

| Markdown owner | Lines | Whitespace-delimited words | UTF-8 bytes |
| --- | ---: | ---: | ---: |
| Coordinator | 155 | 3,814 | 27,763 |
| Planning | 142 | 2,669 | 20,320 |
| Work | 43 | 1,005 | 7,311 |
| Review | 36 | 845 | 6,176 |
| Delivery | 50 | 1,201 | 8,544 |
| **Total** | **426** | **9,534** | **70,114** |

The two-line invocation metadata adds 43 bytes. These counts exclude architecture/roadmap documents, tests, and the optional synchronization utility. They measure source text, not tokens, observed loaded context, latency, cost, or effectiveness. The coordinator’s optional native-goal section accounts for 638 whitespace-delimited words.

**Proposed improvement.** Add source words/bytes and actual loaded-context measurements, when exposed, to existing complexity observations. The roadmap already calls for context/turn measurement. Consolidate duplicated prose or selectively disclose optional detail only where representative evidence shows a reading or maintenance cost. Prefer replacement and clearer navigation over adding more instructions. Do not split the package or impose an arbitrary reduction merely to improve a count. [S15] (lines 351–392)

## 5. Proposed method-selection aid

This is a proposed presentation of the existing policy, including the narrow F1/F2 clarifications. It should live with the coordinator’s current routing owner if adopted, with links to detailed criteria. It is not a second routing algorithm.

| Decision | What the agent establishes | Result |
| --- | --- | --- |
| Activation | Explicit AFR selection in the current request or established continuation | Load the actual v5 coordinator; auditing AFR does not activate it |
| Identity | Governing package/version when exposed, target, active workspace, host | Correct references, instructions, source boundary, and capability assumptions |
| Requested phase and endpoint | Planning/research, review-only, local candidate, PR, convergence, merge, synchronization, and current authority | Stop at the requested boundary; do not infer additional effects |
| Contract sufficiency | Material behavior, constraints, required companions, decisions, acceptance, and credible evidence | Reuse a sufficient contract; resolve only missing obligations |
| Direct | One cohesive reviewable outcome, regardless of file or commit count | Enter the direct sequence at its missing obligation |
| Umbrella | Several independently deliverable outcomes under one bounded parent objective | Identify any dependencies, child endpoints, shared invariants, and combined acceptance |
| Spike | A bounded evidence question prevents honest implementation planning | Investigate and report conclusion/uncertainty without invented readiness |
| Stop | A stop, unresolved required decision, missing authority, unsafe effect, or inaccessible indispensable context blocks affected work | State the boundary; continue only independent safe work where useful |
| Assurance | Actual consequences and target requirements | Lean, standard, or protected, with explicit required checks/review |
| Roadmap | Substantial/staged/resumable work or material existing roadmap context | Reuse native tracking or create only a justified minimal artifact |
| Architecture | Material component/boundary/ownership, dependency, trust/state, service, shared-abstraction changes, or greenfield intent | Apply the existing exact proposal/selection protocol before dependent implementation |
| Delegation | Independent scope and a useful focused contribution or critique | Use actual host capabilities with one integration owner |
| Native goal | Explicit request or an existing goal, actual native controls, and bounded acceptance | Optional persistence around the same workflow and authority |
| Completion | Evidence satisfies the selected endpoint and relevant parent acceptance | Report what is observed and what remains incomplete |

The shortest useful selection statement could be: “Direct local work; reuse the accepted contract; standard assurance with one independent review required; ordinary architecture-conforming change; no roadmap bootstrap or goal mode needed.” That statement records decisions already needed by the workflow and should not become a mandatory form.

## 6. Information and tools required by the selected method

The core’s tools are host capabilities and target-owned checks. The review found no missing required custom AFR executable. Confirm only the capabilities relevant to the requested result. [S1] (lines 10–27) [S7]

| Selected work | Information needed | Adequate capability | If unavailable |
| --- | --- | --- | --- |
| Discovery and planning | Target instructions, authoritative sources and required companions, acceptance, decision ownership | File/resource readers; scoped search; external research when the question requires it | Report indispensable gaps; continue independent analysis |
| Local implementation | Current workspace/base and changes, sufficient contract, assurance, allowed effects | Native file editing, Git observations where applicable, permitted existing toolchain | Preserve the candidate; resolve the specific prerequisite |
| Requirement verification | Actual commands/assertions, consumer boundaries, applicable configurations, candidate identity | Target-native focused checks or credible permitted manual evidence | Mark required evidence unavailable/inconclusive; do not invent a pass |
| Independent review | Exact candidate/base, requirements, companions, check results and limitations | Separate available reviewer when required | Useful self-review remains possible, but does not satisfy required independence |
| Architecture work | Viewable intended/proposed design, exact selection, target rules and native checks | Available Architecture Guard when selected, or sufficient target-native method | Expose missing architecture capability; ordinary conforming work need not stop |
| PR creation/convergence | Destination/source identity, permitted publication endpoint, complete relevant policy/feedback | Native forge reads/writes and an available bounded monitor where needed | Preserve useful local/PR result and state the unfulfilled endpoint |
| Merge | Current reviewed head, relevant base, required checks/review, unresolved findings, target policy | Forge operation conditioned on the reviewed head | No unguarded merge; report the capability boundary |
| Synchronization | Observed remote merge result, fetched target, local ownership/changes/ancestry | Native fetch and safe fast-forward where authorized | Report remote merge and local sync separately |
| Native goal | Bounded contract, compatible objective, exposed native controls and limits | Actual host goal tools | Ordinary AFR remains usable; requested goal capability remains unfulfilled |

A semantic-search service, named persona roster, specific monitor skill, diagram framework, or global AFR installation is not universally required. A selected task can nevertheless require a particular capability that its host must actually provide. Availability never supplies permission.

## 7. Qualification picture and the smallest useful tests

### What the records support

| Surface | Existing evidence | Remaining limit |
| --- | --- | --- |
| Explicit-path local work | Several bounded Codex cases, including current roadmap cases and an affected-case refresh | Not current installed/catalog discovery or broad representative reliability |
| Roadmap selection | Fresh raw-request cases for existing tracking, minimal creation, no-write planning, small direct work, and bounded resume | Current corrected package has a focused affected-case pass; earlier cases retain earlier hashes |
| Delegation | Bounded useful contributions and actual acceptance of two named native role selections | Larger case requested the roles; autonomous selection, full hooks/MCP, concurrent integration, and effective settings remain limited |
| Delivery | Controlled R4 forge-response cases; later real M8 multi-PR evidence and combined acceptance | R4 simulations do not establish live API, queue, pagination, monitor, or race behavior; M8 used an older fixed governing package |
| Native goals | Source review, exposed-control observations, and goal-off compatibility | Cases B–J and representative M9 goal-on use remain unrun; qualification was deferred |
| Architecture | Guided candidate cases, rejection/repair and selected-revision handling, plus bounded combined acceptance | Not universal native enforcement, ChatGPT parity, crash recovery, or flawless scope compliance |
| Representative use | One completed umbrella explicitly counted under governing aa87adb | By itself does not meet the roadmap’s 10/20-run thresholds or qualify the present package automatically |

Sources: roadmap trials [S13], delegation [S11], R4 [S9], M8/R5 [S10], M9 [S12], and roadmap thresholds [S15]. The real M8 umbrella is important counterevidence: AFR has completed a real delivery workflow. It should neither be ignored nor reassigned to the current package.

### Proposed focused scenarios

These are proposed acceptance checks for a future authorized improvement/qualification task. No trial was executed by this review. Use fresh agents, raw requests, the real selected package identity, and independent observation of resulting source/actions. Do not give test agents the expected answer or mandate a route/roster merely to obtain it.

| Scenario | Decisive observation | Finding covered |
| --- | --- | --- |
| Adequate external specification without an AFR assurance label | Reuse it, select assurance before work, avoid duplicate planning | F1 |
| Small security change versus larger harmless documentation change | Assurance follows consequences; required review stays explicit | F1 |
| Required independent review absent | No simulated independence or silent downgrade; honest candidate gap | F1/F5 |
| Two independent deliverables without order dependency | Umbrella allowed; no fabricated dependency; combined acceptance retained | F2 |
| Accepted PR, explicit incomplete draft PR, and merge with the same known gap | Distinct endpoint outcomes under the selected draft policy; merge blocked for unmet acceptance | F3 |
| Package reference changes between work and resume/delivery | Governing version boundary detected or accurately disclosed and reconciled | F4 |
| Merge guard or complete required-policy observation missing | Useful result preserved; no unguarded merge or invented readiness | F5 |
| Verification wrapper would install/create an environment despite prohibition | Inspect first; permitted existing toolchain or explicit evidence gap | F6 |
| Latest roadmap plus historical “current” entries | Correct bounded next selection; historical wording does not override current priority | F7 |
| Tracked progress update after a merge-only endpoint | Correct remote result and local-bookkeeping disposition; no recursive unauthorized PR | F8 |
| Internal component fix versus boundary/ownership change | Ordinary path for the former; selected proposal for the latter | F9 |

Existing roadmap and dependency tests already supply substantial positive coverage. Reuse their fixtures and refresh only evidence affected by a change. The command-effects test is separable from optional native-goal work. Goal-on qualification, installed discovery, and any live forge trial require their own selected scope; the recorded M9 deferral remains a limit, not a standing instruction to resume it.

## 8. Recommended improvement sequence

1. **Clarify the current owners.** Address F1/F2/F9 with a small wording change and linked decision aid. Settle F3’s draft-publication policy explicitly. Add F4’s concise provenance rule. Keep coordinator ownership and four phase references.
2. **Repair navigation and closure wording.** Reconcile the roadmap’s current status (F7); document the chosen bookkeeping disposition at the relevant target boundary (F8). Link to existing qualification evidence instead of copying histories.
3. **Run only the affected ordinary-work cases.** Prioritize unlabelled sufficient-contract reuse, required-review unavailability, no-dependency umbrella selection, and the known command-effects regression. Add draft/provenance cases if those rules change.
4. **Qualify the intended deployment surface when separately selected.** Establish actual current-package discovery/loading, native review and delivery capabilities, and representative use on the intended host. Keep native-goal qualification separately scoped.
5. **Measure before restructuring.** Observe unnecessary intervention, acceptance gaps, actual context/turns when available, and review/correction effort. Reconsider text layout from that evidence; no runtime/helper expansion is justified by this audit.

Expected benefits are more consistent selection and clearer evidence boundaries. They are reasoned expectations, not measured time, token, cost, or defect-rate improvements.

## 9. Boundaries to preserve

Keep one public entrypoint, native host execution, proportional assurance, target-owned contracts/progress, selective evidence refresh, and explicit endpoint authority. Preserve real independent review when required, exact-head merge protection, prerequisite chronology, source-based resume, and combined parent acceptance. Keep historical evidence pinned to its governing/candidate versions.

Do not turn this review into a requirement for mandatory plan templates, a router script, extra personas, a new qualification registry, universal architecture ceremony, automatic installation, or another delivery loop. The proposed document changes should replace ambiguity and repetition while retaining the existing workflow.

## 10. Source references and reproducibility

All repository links below are pinned to the reviewed revision. Line references in findings refer to that revision. Local inventory measured complete current file bytes; selected supporting trial excerpts were read at the same commit. Historical source hashes within those records deliberately differ.

- [S1] Coordinator: activation, selection, continuation, goals, stop/resume, and reporting.
- [S2] Planning: ownership, contract sufficiency, architecture, outcome sizing, assurance.
- [S3] Work: workspace, implementation, command effects, conformance evidence.
- [S4] Review: independence, findings, correction and rechecks.
- [S5] Delivery: PR convergence, guarded merge, synchronization.
- [S6] Current architecture v3 and owner map.
- [S7] R6 zero-helper assessment and evidence limits.
- [S8] R3 review-only correction and local qualification limits.
- [S9] R4 bounded delivery protocol, observations, and limits.
- [S10] R5/M8 candidate trials, effects failure, and one completed representative umbrella.
- [S11] Native delegation qualification.
- [S12] M9 native-goal protocol, observations, and deferred cases.
- [S13] October 9 roadmap trials and affected-case refresh.
- [S14] Optional synchronization publication/installation boundaries.
- [S15] Roadmap, current increment, thresholds, and complexity budget.
- [S16] Explicit-only invocation metadata.

Core-source SHA-256 values measured in the authoring checkout:

| File | SHA-256 |
| --- | --- |
| SKILL.md | e063ef3baaca74a528af89db0b1e92b0ac93356a57097b33d6981e1e69c135b5 |
| references/planning.md | ab4e75eb489fe4f11757f823f871cfb1051879d62b6ed3c589a7dc255a5e1ce2 |
| references/work.md | 0417673cf68ff466f007bf6a0e61ed12ce35abb32cbb277687ae35af634ab01f |
| references/review.md | 3e8859bc5cf612abe3b89de08754af702ecac18bf9d6c77b6833dd3a659792b7 |
| references/delivery.md | 1421bd2246c206f45f27a233eaf7b39f07c72e3d13b5c3b58e8234942c5ac556 |
| agents/openai.yaml | a1499d95abd8447558c535fe5554adcc3c9b988a0a39264a6283d430effe1e94 |

The instruction context was root CHAT.md, SHA-256 bf9ebb0e39f0d40172316b712a4d419b6aeb7f7e5a8691d45980245a392a6f1e. Codex-facing AGENTS.md was assessed as source evidence, not adopted as this session’s instruction entrypoint.

[S1]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/.agents/skills/afr/SKILL.md
[S2]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/.agents/skills/afr/references/planning.md
[S3]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/.agents/skills/afr/references/work.md
[S4]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/.agents/skills/afr/references/review.md
[S5]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/.agents/skills/afr/references/delivery.md
[S6]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/docs/architecture-v3.md
[S7]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/docs/r6-helper-assessment.md
[S8]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/tests/r3/README.md
[S9]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/tests/r4/README.md
[S10]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/tests/r5/README.md
[S11]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/tests/delegation/README.md
[S12]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/tests/m9/README.md
[S13]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/tests/roadmap/README.md
[S14]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/ops/skill-sync/README.md
[S15]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/docs/roadmap.md
[S16]: https://github.com/DrJLabs/afr-v5/blob/9b7def12d900ae787e2b155e0dec53eef7b59146/.agents/skills/afr/agents/openai.yaml
