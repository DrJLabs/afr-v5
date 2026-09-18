# Discovery and planning

Use this method when dispatched by the AFR coordinator. Return planning results and recommendations to it; activation, authority, route selection, stop, resumption, and final reporting belong to `SKILL.md`.

## Ground the request

Inspect current target instructions, relevant source/tests, and selected specifications enough to distinguish verified behavior from assumptions. Discover local facts before asking the user. Compare alternatives only where a consequential choice exists; avoid an exhaustive architecture exercise for ordinary work.

Reuse an adequate issue, RFC, ADR set, BMAD/Spec Kit artifact, or project-native plan. Its origin does not select its framework. Identify the authoritative requirement source, who may change it, and indispensable companion contracts. Distinguish **required context for correctness** from **background to consult when needed**. Missing background need not stop planning; an inaccessible required companion leaves the dependent contract unresolved.

When compressing or decomposing a source, check both directions:

- Every material requirement, invariant, non-goal, and compatibility constraint is preserved directly or through an explicitly required reference.
- Every proposed commitment has support in the request, target contract, an approved decision, or delegated discretion; do not invent product policy.

Use references instead of copying large sources when the recipient can access them. A delegated assignment must make required context discoverable; do not bury it among optional reading. Preserve source ownership when an artifact is derived or mirrored. Within permitted planning changes, amend the designated source or add a minimal linked supplement; do not create competing requirements or a duplicate AFR-specific plan by default.

## Ground architecture changes

Discover the target's architecture entrypoint, relevant component and ownership records, native rules, decisions, and configured checks alongside its root instructions. Classify the proposed work before choosing ceremony: ordinary changes within existing boundaries use the existing contract and proportional checks; changes to components, dependency direction, trust or state ownership, runtime services, or material shared abstractions are architectural changes.

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

## Size outcomes and dependencies

Recommend `direct` for one cohesive outcome even if it spans files or commits. Recommend `umbrella` only for independently deliverable outcomes, not implementation microsteps. Each required outcome needs observable acceptance and a delivery boundary consistent with the user's endpoint.

For umbrellas, identify dependencies and what satisfies them: a particular contract/revision, local candidate, or merged base as appropriate. Plan order breaks ties only when the choice is immaterial. Expose cycles and unsatisfied dependencies instead of treating no eligible work as completion.

Define the parent objective, shared invariants/architecture choices, and evidence for combined acceptance at a meaningful integration boundary. Individually successful outcomes or merged PRs do not alone prove the parent objective. Reuse valid outcome evidence; do not prescribe full-suite reruns after every outcome.

If a new, materially uncertain shared pattern will be replicated widely and a wrong choice would be expensive, propose one representative implementation/verification point before broad repetition. Established conventions, qualified prior use, independent constraints, or cheap reversibility can make this unnecessary. Planning the checkpoint does not itself authorize implementation.

## Planning assurance and self-review

Recommend the lowest adequate assurance from actual consequences, independently of route, diff size, or document length. Applicable target requirements remain binding.

| Assurance | Planning expectation | Expected later verification/review |
| --- | --- | --- |
| `lean` | Verified problem, intended change, preservation constraints, focused evidence | Focused checks and self-review |
| `standard` | Explicit behavior/failures, interfaces, consequential decisions, coherent slices, requirement coverage | Behavioral checks and normally one consolidated independent review |
| `protected` | Add analysis for the actual security, migration, rollback, compatibility, concurrency, performance, reliability, or irreversible-effect risks | Risk-specific checks and relevant specialist coverage in consolidated review |

These expectations select assurance for the work and review methods; they do not establish that review has occurred or that the host supplies independent reviewers. Do not create simulated specialist personas or stack reviewers to produce a plan.

Self-review the proposed contract against the sources: missing obligations, unsupported commitments, contradictory constraints, unjustified assumptions, incompatible cross-outcome choices, verification gaps, unnecessary decomposition, and a simpler adequate approach. A small security-sensitive edit can still need protected assurance.

Planning is sufficient when consequential behavior is defined, important constraints are known, verification is credible, and remaining implementation discretion fits authority. Do not require ritual template completion or another plan when the existing source meets that test. Ask only for a missing decision that materially prevents safe progress; leave dependent work unresolved without blocking unrelated safe analysis.

When evidence contradicts the plan, distinguish:

- an implementation defect against a valid requirement: identify the needed correction and affected evidence;
- an invalid technical assumption: revise an advisory approach within discretion, or surface an affected approved decision;
- a missing/conflicting product or security decision: identify its owner and impact rather than inventing policy;
- an authorized requirement change: update through the source's permitted path and reassess affected acceptance, dependencies, and evidence.

For a recommended spike, bound the question, evidence to inspect, and what would resolve it. Return the actual conclusion or remaining uncertainty without fabricating an implementation contract. Return the planning result, assurance and route recommendation, source references, and limitations to the coordinator.
