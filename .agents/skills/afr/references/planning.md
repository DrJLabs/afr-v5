# Discovery and planning

Use this method when dispatched by the AFR coordinator. Return planning results and recommendations to it; activation, authority, route selection, stop, resumption, and final reporting belong to `SKILL.md`.

## Ground the request

Inspect current target instructions, relevant source/tests, and selected specifications enough to distinguish verified behavior from assumptions. Discover local facts before asking the user. Compare alternatives only where a consequential choice exists; avoid an exhaustive architecture exercise for ordinary work.

Reuse an adequate issue, RFC, ADR set, BMAD/Spec Kit artifact, or project-native plan. Its origin does not select its framework. Identify the authoritative requirement source, who may change it, and indispensable companion contracts. Distinguish **required context for correctness** from **background to consult when needed**. Missing background need not stop planning; an inaccessible required companion leaves the dependent contract unresolved.

When compressing or decomposing a source, check both directions:

- Every material requirement, invariant, non-goal, and compatibility constraint is preserved directly or through an explicitly required reference.
- Every proposed commitment has support in the request, target contract, an approved decision, or delegated discretion; do not invent product policy.

Use references instead of copying large sources when the recipient can access them. A delegated assignment must make required context discoverable; do not bury it among optional reading. Preserve source ownership when an artifact is derived or mirrored. Within permitted planning changes, amend the designated source or add a minimal linked supplement; do not create competing requirements or a duplicate AFR-specific plan by default.

## Resolve roadmap and document ownership

Discover the target's current planning/progress entrypoints from its instructions and document map, when present. Identify the owner of current priority/progress, the accepted requirements and acceptance, execution procedures, and dated evidence. These roles may share one document or use linked documents. Establish the actual planning root and code workspace; a parent planning directory need not be a Git repository. Do not infer document authority or live runtime state from a filename, branch, or old summary.

Reuse an adequate roadmap, existing plan with outcome selection/progress, milestone/issue set, or other target-native structure that can select bounded outcomes and retain progress. Preserve its format, status vocabulary, source ownership, and release procedures. Existing projects need no AFR-specific document set or conversion. Keep completed contracts as binding references until explicitly changed or superseded; lifecycle labels indicate disposition, not permission or proof of acceptance. Locate deferral reasons/resumption conditions and replacement links where applicable.

When substantial project delivery lacks an adequate structure, prepare one concise, human-readable roadmap in the target's designated location, or `docs/roadmap.md` if it has no convention. Creation must fit the coordinator's planning-artifact authority; an explicit no-write request keeps the draft in the conversation. If artifact writes are unavailable or unauthorized, return the proposed roadmap and the gap without writing or blocking useful authorized analysis.

Include only the established objective and scope boundaries, outcome-sized milestones with observable success, meaningful dependencies/order, the current selected next outcome, and known open decisions or deferred proposals. Separate owner-selected scope from recommendations; missing product direction remains unresolved. Reference sufficient existing contracts rather than copying them. A small roadmap can itself provide the implementation contract; add a linked outcome plan only when necessary detail would obscure it. Detail the selected work now and leave later outcomes at useful outcome-level resolution.

Link a new or changed contract from its owning outcome and update an existing document map when needed within authority. Do not create empty plans for every milestone, mandatory templates, a new document map, or a second status checklist merely to bootstrap. Return the source ownership, selected scope/contract, proposed acceptance and dependencies, and evidence gaps to the coordinator's [selection and reconciliation](../SKILL.md#roadmap-selection-and-reconciliation) method; discovery cannot settle unassigned priority or authorize execution.

## Delegate evidence and bounded analysis

Use the coordinator's [delegation policy and assignment brief](../SKILL.md#native-delegation) when a separate context or parallel inquiry will materially help. Choose capabilities for the question: a repository explorer traces local behavior and dependencies; a research analyst resolves decision-relevant external facts; a planning analyst compares a bounded set of alternatives or drafts acceptance and dependencies from established evidence. The coordinator still produces one authoritative contract and decides routing, assurance, and what remains unresolved. Do not commission parallel full plans or require this roster on every task.

Ask research to prioritize current primary sources, identify version and applicability, and return source references with the claims they support, contradictions, and remaining gaps. Local facts need source locations; recommendations and inferences must be distinguishable from observations. Stop the inquiry once the bounded question has adequate evidence or its decisive gap is clear; additional sources without decision value are not progress.

Give a planning analyst the grounded evidence and the specific unresolved design question. Request the smallest adequate approach, credible alternatives only where consequential, dependency boundaries, observable acceptance, and what still requires an owner decision. The analyst may recommend a plan but cannot settle unassigned policy, authorize implementation, or replace the coordinator. Incorporate accepted conclusions into the existing source rather than maintaining an agent's competing plan.

## Ground architecture changes

Discover the target's architecture entrypoint, relevant component and ownership records, native rules, decisions, and configured checks alongside its root instructions. Classify the proposed work before choosing ceremony: ordinary changes within existing boundaries use the existing contract and proportional checks; changes to components, dependency direction, trust or state ownership, runtime services, or material shared abstractions are architectural changes.

When architecture mapping or design authoring is in scope, use the available Architecture Guard skill identified by the user or target workflow and its `references/architecture-mapping.md` method. It supports first-time mapping, existing-system proposals and greenfield design independently of AFR. Consume its target-owned viewable artifacts, relevant source identity, coverage/evidence gaps, and any proposal revision and owner decision; AFR's coordinator retains sequencing and continuation. Accepting a current-state map as accurate does not select it as the desired design. Reuse adequate existing maps and refresh only affected evidence. If that skill is unavailable, use a sufficient target-native method or report the missing capability needed for the requested result; do not assume a sibling checkout, install a skill, duplicate its procedure, or block ordinary conforming work.

For an architectural change, require a viewable proposed design, a viewable current design where one exists, the affected boundaries and rationale, and a complexity explanation covering the requirement, simpler alternative considered, ongoing cost, owner, and what the addition replaces. An explicit owner must select the exact proposal revision before dependent implementation. Reuse that selection only while the proposal is unchanged; changed content requires renewed selection. An unavailable, unviewable, stale, or ambiguous proposal leaves dependent work unresolved while independent safe analysis may continue.

Keep intended architecture, observed source structure, and behavioral evidence separate. The target owns the format, revision protocol, native checks, and decision record; generic AFR guidance must not invent a schema or promote an observed graph into approved intent. A green model or import check does not establish runtime behavior or approval.

For a greenfield target, require a viewable initial intent and explicit owner selection before implementation; an empty source tree is not conformance evidence. For staged delivery, define and accept the intermediate architecture boundary, checks, and evidence separately; do not treat a partial stage as conformant to a later full design.

## Establish a sufficient implementation contract

Keep three logical layers distinct: **behavior and constraints**, **settled technical decisions**, and the **revisable execution approach**. They may fit in a few sentences rather than separate documents.

Cover what is material:

- objective, explicit non-goals, and current behavior with evidence;
- required behavior, preserved invariants, and compatibility;
- meaningful failure/edge behavior, retries, ordering, and concurrency;
- binding interfaces, data semantics, security boundaries, and operational constraints;
- settled decisions, assumptions, unresolved decisions, and delegated discretion;
- observable acceptance criteria and corresponding verification, including limitations;
- coherent implementation slices and meaningful dependencies/order;
- planned review depth, authorized endpoint, and conditions requiring a decision or replan.

Do not silently change behavior, external contracts, invariants, security policy, compatibility, non-goals, or acceptance. Follow approved architecture/migration decisions; surface contradictory evidence before dependent work departs from them. Likely files, naming, internal factoring, and reversible sequencing can remain advisory. An assumption is not an approved decision.

Apply a minimal architecture-contract test: could two competent implementers following these requirements choose incompatible answers to a consequential, non-obvious tradeoff? Settle that choice within discretion, or identify the decision owner and leave dependent work unresolved until it is settled. Do not prescribe reversible internals simply to fill a plan.

Map each material requirement to credible evidence. Depending on behavior, that may be a unit, integration, contract, compatibility, property, migration, security, performance, operational, or manual check. Name what it must demonstrate; an existing green test is not automatically evidence for a new acceptance criterion. Record proposed checks as proposed, not executed. No traceability IDs, machine schema, or separate evidence database is required.

For an optimization outcome, define comparable baseline and final measurement conditions, the decisive metric, and known limitations before claiming improvement; qualitative outcomes need no invented numerical target.

## Size outcomes and dependencies

Recommend `direct` for one cohesive outcome even if it spans files or commits. Recommend `umbrella` only for independently deliverable outcomes, not implementation microsteps. Each required outcome needs observable acceptance and a delivery boundary consistent with the user's endpoint.

For umbrellas, identify dependencies and what satisfies them: a particular contract/revision, local candidate, or merged base as appropriate. Plan order breaks ties only when the choice is immaterial. Expose cycles and unsatisfied dependencies instead of treating no eligible work as completion.

Define the parent objective, shared invariants/architecture choices, and evidence for combined acceptance at a meaningful integration boundary. Individually successful outcomes or merged PRs do not alone prove the parent objective. Reuse valid outcome evidence; do not prescribe full-suite reruns after every outcome.

If a new, materially uncertain shared pattern will be replicated widely and a wrong choice would be expensive, propose one representative implementation/verification point before broad repetition. Established conventions, qualified prior use, independent constraints, or cheap reversibility can make this unnecessary. Planning the checkpoint does not itself authorize implementation.

## Project a native goal

Use this section when goal mode is requested, an existing goal needs reconciliation, or a compact suggested objective would materially help an authorized long run. The coordinator owns [activation and lifecycle](../SKILL.md#native-goal-integration); a suggested projection does not start a goal. Use a sufficient contract for the requested endpoint, including a bounded planning/research result when implementation is not yet specified or authorized. Do not create a competing specification or require another plan file.

Project only the essentials:

- **Target and result:** the target and observable outcome.
- **Authoritative contract:** discoverable specification, issue, plan, selected architecture revision, and indispensable companions as applicable; reference their requirements rather than copying them.
- **Authorized endpoint:** sufficient plan, review result, verified local candidate, PR creation/convergence, remote merge, or merge plus required synchronization, as actually requested.
- **Decisive acceptance:** the few observations distinguishing completion from activity, including combined parent acceptance for an umbrella.
- **Continuation:** unfinished dependency-eligible work within existing authority, preserving each prerequisite's required revision and boundary.
- **Stops:** current user stop, missing authority, consequential unresolved decisions, stale selected requirements, inaccessible indispensable evidence, unsafe effects, or repeated failure without progress; host limits remain binding.

Aim for roughly 1,000–2,000 characters when useful and stay within the actual host's objective limit; shorter sufficient objectives are valid. Keep detailed requirements and progress in their existing authoritative sources, accessible from the target/session on resume. Check that the projection preserves the contract's outcome and boundary without adding commitments. Return it to the coordinator, retaining a compatible existing objective instead of rewriting it merely to match this format.

For substantial work needing resumable written context, use the target's authoritative contract and designated progress record rather than a separate goal plan. Keep one compact checkpoint in that progress owner, linking the contract when requirements live separately, with verified obligations and evidence locations, remaining obligations, candidate/base and relevant untracked inputs, the next eligible action and unmet acceptance it advances, blockers, and in-flight effects. Record material discoveries or changed decisions where they already belong, using the coordinator's [reconciliation method](../SKILL.md#roadmap-selection-and-reconciliation). A small task needs no mandatory plan or per-tool journal. A checkpoint cannot change authority or weaken acceptance.

On continuation or compaction recovery, re-read the relevant contract/checkpoint and confirm required sources still resolve. The coordinator's [stop and resumption](../SKILL.md#stop-and-resumption) rules govern reconciliation, evidence refresh, and the next action. A Markdown plan can guide execution independently of host Plan mode; qualify the actual mode and loading path rather than treating a plan file as proof of native activation or continuation.

For a future explicitly selected run, a compact natural-language request could be:

```text
Use AFR with one native goal to implement the accepted contract in
docs/parser-migration-plan.md through a verified local candidate.
Read its required companions. Preserve its binding behavior, constraints,
dependencies, and unrelated work. Complete only when its decisive checks,
required review, and applicable combined acceptance hold for the candidate.
Continue unfinished eligible work and causal corrections within that authority.
Keep the target's designated progress checkpoint current at meaningful boundaries.
Honor user stops, host limits, and unresolved authority or evidence gaps.
```

This is an illustrative request, not qualified combined slash syntax. Replace the example path and acceptance wording with the real accessible contract and its decisive observations. It grants no publication or merge authority; supply a token budget only when explicitly requested. The coordinator owns activation and lifecycle, including conflicts or materially changed objectives.

## Planning assurance and self-review

Recommend the lowest adequate assurance from actual consequences, independently of route, diff size, or document length. Applicable target requirements remain binding.

| Assurance | Planning expectation | Expected later verification/review |
| --- | --- | --- |
| `lean` | Verified problem, intended change, preservation constraints, focused evidence | Focused checks and self-review |
| `standard` | Explicit behavior/failures, interfaces, consequential decisions, coherent slices, requirement coverage | Behavioral checks and normally one consolidated independent review |
| `protected` | Add analysis for the actual security, migration, rollback, compatibility, concurrency, performance, reliability, or irreversible-effect risks | Risk-specific checks and relevant specialist coverage in consolidated review |

These expectations select assurance for the work and review methods; they do not establish that review has occurred or that the host supplies independent reviewers. Do not create simulated specialist personas or stack reviewers to produce a plan.

Self-review the proposed contract against the sources: missing obligations, unsupported commitments, contradictory constraints, unjustified assumptions, incompatible cross-outcome choices, verification gaps, unnecessary decomposition, and a simpler adequate approach. A small security-sensitive edit can still need protected assurance.

For a consequential or materially uncertain plan, use an independent reviewer when required by the target or when a separate critique is likely to change the decision. Supply the actual plan revision and required sources, not just its author's summary. Ask for omissions, unsupported decisions, incompatible dependencies, weak acceptance, and simpler adequate alternatives; review proposed verification as a plan, not as executed evidence. Reuse the available review capability rather than inventing another persona or adding a mandatory approval stage. The coordinator resolves findings and preserves any required owner selection; a reviewer recommendation is not approval.

Planning is sufficient when consequential behavior is defined, important constraints are known, verification is credible, and remaining implementation discretion fits authority. Do not require ritual template completion or another plan when the existing source meets that test. Ask only for a missing decision that materially prevents safe progress; leave dependent work unresolved without blocking unrelated safe analysis.

When evidence contradicts the plan, distinguish:

- an implementation defect against a valid requirement: identify the needed correction and affected evidence;
- an invalid technical assumption: revise an advisory approach within discretion, or surface an affected approved decision;
- a missing/conflicting product or security decision: identify its owner and impact rather than inventing policy;
- an authorized requirement change: update through the source's permitted path and reassess affected acceptance, dependencies, and evidence.

For a recommended spike, bound the question, evidence to inspect, and what would resolve it. Return the actual conclusion or remaining uncertainty without fabricating an implementation contract. Return the planning result, assurance and route recommendation, source references, and limitations to the coordinator.
