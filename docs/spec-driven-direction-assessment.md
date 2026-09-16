# AFR v5 spec-driven direction assessment

- **Status:** Design assessment; no AFR v5 skill implementation has been evaluated yet.
- **Date:** 2026-09-15
- **Decision:** Keep the current skill-first architecture and make targeted spec-driven refinements before and during R2/R3.

## 1. Executive decision

AFR v5 is heading in a sound direction. Do not replace it with BMAD, Spec Kit, or another orchestration framework, and do not reopen the old AFR runtime architecture.

The recommended course is narrower:

> Keep AFR's lean execution-and-delivery workflow, but make the intended behavior, implementation boundaries, and evidence of conformance more explicit before implementation begins.

The current design already incorporates most of the strongest spec-driven-development principles:

- inspect the real project before acting;
- reuse an adequate existing plan rather than duplicating it;
- separate planning, work, review, and delivery responsibilities;
- size work around cohesive outcomes rather than arbitrary task or commit counts;
- scale assurance according to risk;
- use native host-agent capabilities instead of a custom runtime;
- preserve exact-revision review, delivery, and resume evidence; and
- avoid databases, daemons, workflow state engines, and persona ceremony without measured need.

The principal gap is not missing planning. It is that delivery and recovery behavior are currently specified more precisely than the contract that determines what should be delivered.

## 2. Evidence and boundary

This assessment is based on the current repository state at commit `186631cf452b944906f693021df1e79522279b6b` on branch `docs/r1-donor-analysis`, including:

- `CHAT.md`;
- `README.md`;
- `docs/architecture.md`;
- `docs/roadmap.md`; and
- `docs/donor-matrix.md`.

Observed project state:

- R1 donor analysis and behavior specification are complete.
- R2 implementation is next.
- No AFR v5 skill, helper, or behavioral test surface exists in this checkout yet.
- The existing documents explicitly distinguish design/provenance checks from runtime qualification.

Therefore, the conclusions below are design recommendations, not findings from a failed implementation.

## 3. Direction to preserve

### 3.1 One canonical skill package

Keep one public `afr` entrypoint with a compact coordinator and selectively loaded planning, work, review, and delivery references. This provides one workflow owner while supporting progressive disclosure.

Do not split responsibilities into separate public personas or services merely to resemble a human software organization. The reasoning functions matter; simulated organizational roles do not.

### 3.2 Native host-agent execution

Keep the host agent as the runtime. AFR should teach a capable agent how to work and should not reproduce the host's tool, session, subagent, scheduling, or provider lifecycle.

### 3.3 Proportional process

Keep direct, umbrella, spike, and stop as structural routes. Keep lean, standard, and protected as assurance levels. These dimensions are useful and should remain distinct:

- route describes the shape of the work;
- assurance describes the consequences of being wrong.

### 3.4 Existing safety and delivery behavior

Preserve the current emphasis on:

- current-state inspection;
- preservation of unrelated work;
- explicit authority boundaries;
- exact candidate and PR-head identity;
- observation before retry after ambiguous external effects;
- separate remote merge and local synchronization evidence;
- bounded correction; and
- honest resume and continuation.

These are material correctness safeguards, not process overhead to remove.

## 4. Recommended adjustments

### 4.1 Define a small implementation contract

`references/planning.md` should require enough information to distinguish three logical layers:

1. **Behavior and constraints** — what must become true and what must remain true.
2. **Technical decisions** — consequential architecture, interface, data, security, migration, or operational choices already settled.
3. **Execution approach** — a revisable implementation sequence and division into coherent work units.

These layers do not require three documents. A small change may express all three in a few sentences. A normal feature may use sections in one plan. A high-risk change may need separate requirements and architecture artifacts.

A sufficient implementation contract should cover, when material:

- objective and explicit non-goals;
- verified current behavior;
- required behavior and invariants;
- preservation and compatibility constraints;
- meaningful failure, edge, retry, ordering, or concurrency behavior;
- binding interfaces, data semantics, and authorization boundaries;
- assumptions and unresolved decisions;
- acceptance criteria and required evidence;
- implementation discretion delegated to the agent;
- dependencies and ordering; and
- authorized delivery endpoint.

The requirement is sufficient decision clarity, not template completion.

### 4.2 Apply assurance during planning

The existing assurance levels should determine pre-implementation rigor as well as review depth.

| Assurance | Planning expectation |
| --- | --- |
| `lean` | Verified problem, intended change, preservation constraints, and focused evidence. Usually chat, an issue, or an existing short plan. |
| `standard` | Explicit behavior and failure cases, affected interfaces, consequential decisions, coherent implementation slices, and requirement-to-evidence coverage. |
| `protected` | Add the specific risk analysis the change requires: security boundaries, migrations, rollback, compatibility, concurrency, performance, reliability, or irreversible effects. |

Readiness should remain a model judgment, not a gate engine or certificate:

> The consequential behavior is sufficiently defined, the important constraints are known, the implementation has a credible verification path, and remaining discretion fits the agent's authority.

### 4.3 Make conformance explicit

Passing implementation-selected tests is not by itself proof that the requested outcome was achieved.

For each material requirement, AFR should establish corresponding evidence. This can be brief for ordinary work and more structured for high-risk changes. Evidence may include unit, integration, contract, compatibility, property, migration, performance, security, operational, or manual validation as appropriate.

Review should receive the authoritative requirement source and exact candidate/base, not only the implementer's summary.

When evidence contradicts the plan, classify the problem correctly:

- implementation defect — correct the implementation;
- invalid technical assumption — revise the approach and refresh affected evidence;
- missing or conflicting product/security decision — surface the decision instead of inventing policy;
- authorized requirement change — update the authoritative requirement and affected work.

The agent must not rewrite acceptance criteria merely to make its implementation appear complete.

### 4.4 Add parent-level acceptance for umbrella work

Outcome-level success does not guarantee umbrella-level success. Independently passing slices may still disagree on shared interfaces, migrations, ordering, or assumptions.

Umbrella completion should therefore establish:

- each required outcome reached its authorized endpoint;
- dependencies were satisfied at the required revision or delivery boundary;
- shared invariants remain coherent; and
- the combined result satisfies the parent objective.

This does not require rerunning every check after every outcome. It requires integration evidence at the boundary where combined behavior becomes meaningful.

### 4.5 Clarify early behavioral trials

Keep the roadmap's rejection of heavyweight qualification for incomplete fragments, but distinguish that from early bounded trials.

Recommended sequence:

- **R2:** exercise coordinator and planning behavior on representative requests, including adequate existing specs, material ambiguity, low-risk work, and protected-risk work;
- **R3:** run at least one real local change through the assembled planning/work/review path and compare it with an ordinary high-quality host-agent prompt;
- **R4:** test delivery against exact-head, pending/failed/unknown checks, review feedback, and ambiguous external effects;
- **R5:** test umbrella continuation and combined acceptance;
- **later qualification:** broaden across repositories, interruption points, and risk classes.

Early trials should measure behavior, not merely validate Markdown structure.

### 4.6 Interoperate with external specifications without stacking frameworks

AFR should accept an adequate existing artifact from BMAD, Spec Kit, an issue tracker, an RFC process, an ADR set, or project-native documentation.

The planning method should:

1. inspect the artifact and current repository state;
2. identify only material gaps or contradictions;
3. reuse the artifact when sufficient; and
4. avoid translating it into an AFR-specific duplicate by default.

Do not add BMAD adapters, Spec Kit adapters, new public skills, or another orchestration layer before repeated use demonstrates a concrete need.

### 4.7 Refine the helper-extraction threshold

Keep zero required custom helpers as the initial decision. Retain the rule that helpers need demonstrated value and must remain narrow and deterministic.

Clarify, however, that evidence may be either:

- repeated real workflow failure or measurable waste; or
- one controlled trial demonstrating a material safety gap that concise instructions and native tools cannot adequately address.

AFR should not wait for repeated destructive incidents before adding a justified narrow safeguard.

## 5. Recommended AFR planning output

The planning phase should be able to return a compact contract resembling the following, with sections omitted when irrelevant:

```text
Outcome
Current state and evidence
Goals and non-goals
Required behavior and preserved invariants
Material interfaces, data, security, and compatibility constraints
Failure and boundary behavior
Settled decisions, delegated discretion, and unresolved blockers
Acceptance criteria and corresponding evidence
Implementation slices and dependencies
Risk-selected review and verification
Authorized endpoint and stop/replan conditions
```

This is a semantic contract, not a mandatory serialization format.

## 6. Authority levels inside a plan

AFR should distinguish three kinds of planning content:

| Level | Meaning |
| --- | --- |
| **Authoritative** | User-visible behavior, external contracts, invariants, security policy, compatibility, non-goals, and acceptance. The agent must not silently change these. |
| **Design decision** | Approved architecture or migration choices. Follow them unless repository evidence materially invalidates them; then surface the contradiction. |
| **Advisory** | Likely files, internal factoring, naming, and reversible implementation suggestions. The implementation agent may improve these. |

This distinction prevents both under-specification and code-prescriptive plans that unnecessarily constrain agent reasoning.

## 7. Proposed extensions to existing evaluation scenarios

Extend the existing E02, E05, E06, E09, E14, and E15 scenarios rather than introducing a new evaluation framework.

Add cases covering:

- an existing specification that is already sufficient and should not be duplicated;
- passing tests while a stated acceptance criterion remains unmet;
- a small code change with protected-risk consequences;
- implementation evidence invalidating a technical assumption;
- a product or security ambiguity the agent must not decide silently; and
- individually successful umbrella outcomes that fail combined acceptance.

Measure:

- accepted outcomes;
- unnecessary user intervention;
- clarification and replan frequency;
- scope violations;
- requirement-to-evidence coverage;
- context and model turns;
- correction passes;
- escaped material defects; and
- process/complexity growth.

Do not optimize documentation volume or autonomous completion independently of correctness.

## 8. Immediate recommended action

Do not perform another architectural restart.

Before or as part of R2:

1. incorporate the implementation-contract and planning-assurance rules into the canonical skill instructions;
2. make outcome-level and umbrella-level conformance explicit;
3. add the focused evaluation cases above;
4. implement the coordinator and planning reference;
5. run bounded behavioral trials; and
6. proceed to R3 unless those trials reveal a concrete defect in the architecture.

As operational skill instructions become canonical, keep the architecture document concise and link to those instructions instead of maintaining a second executable workflow in prose.

## 9. Non-goals of this adjustment

This assessment does not recommend:

- adopting BMAD as AFR's runtime or governance system;
- adopting Spec Kit as a dependency;
- adding mandatory PRDs, ADRs, RFCs, or task matrices to every change;
- creating simulated PM, architect, scrum-master, implementer, and reviewer personas;
- restoring the old AFR state machine, gate protocol, provider layer, or database;
- requiring independent review for every change;
- adding another durable state surface; or
- reopening R1 donor archaeology wholesale.

## 10. Final disposition

- **Architecture:** retain.
- **Planning contract:** strengthen.
- **Assurance:** apply before implementation as well as during review.
- **Verification:** prove conformance, not only test success.
- **Umbrella completion:** add combined acceptance.
- **Qualification:** begin bounded behavioral trials in R2/R3.
- **Framework relationship:** consume useful artifacts without stacking workflows.
- **Next milestone:** proceed to the R2 prototype after incorporating these refinements.

The intended AFR v5 method can be summarized as:

> Understand the real system, establish what must be true, implement in coherent increments, prove conformance, and continue safely to the authorized endpoint.
