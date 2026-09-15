# AFR v5 skill-first architecture roadmap

**Status:** R1 analysis complete; R2 implementation next
**Date:** 2026-09-03
**Repository stage:** design specified; skill implementation pending

The [architecture specification](architecture.md) owns the current behavior and package design. The [donor matrix](donor-matrix.md) owns R1 evidence and extraction decisions. This roadmap owns milestones, sequencing, and complexity budgets; its date records the original roadmap baseline.

## 1. Decision

AFR v5 will return to AFR's original strength: a skill-driven method that lets a capable host agent take a software initiative from planning to completed delivery without requiring the user to supervise every intermediate step.

The canonical product begins as one public `afr` skill with focused phase references. Standard ChatGPT or Codex provides the agent runtime, tools, context, and native subagents. AFR provides the method, sequencing, proportional quality policy, continuation behavior, and stop conditions.

AFR v5 will not begin by rebuilding:

- a custom agent runtime;
- an App Server protocol client;
- a provider-process manager;
- an event-sourced workflow engine;
- a local control-plane service;
- a durable run database; or
- a bespoke subagent scheduler.

Those capabilities may be reconsidered only after the skill-first system has been used on real work and a repeated, material limitation is measured.

## 2. Historical baseline

The redesign will use four AFR history points deliberately. The canonical historical donor repository is `DrJLabs/afr`; access may be restricted, so v5 must distill the lessons it adopts into this public repository rather than assume every user can read the donor.

1. The original `auto-full-run` skill introduced at commit `3a0f5bc7` as the end-to-end orchestration model.
2. The first complete eight-skill AFR-v2 family at commit `8c0d80d3` as the cleanest responsibility split.
3. The native-skill-family design at commit `671d7361` for proportional assurance, file handoffs, and one-implementer/one-reviewer defaults.
4. Later AFR skill and software history as a defect, safety, and failure-scenario corpus—not as architecture to restore wholesale.

### 2.1 Canonical donor source map

R1 must inspect the exact source artifacts below before performing broad archaeology. Use an authenticated `DrJLabs/afr` checkout when available, or retrieve the same Git objects through an authorized repository connection. Portable Git inspection should use commit-qualified paths such as `git show <commit>:<path>`; do not encode a machine-specific donor checkout path into v5.

| Donor purpose | Commit | Primary paths | Extract | Do not inherit |
|---|---|---|---|---|
| Original end-to-end AFR behavior | `3a0f5bc7` | `codex/skills/auto-full-run/SKILL.md` | PR-sized outcome loop; plan → review → implement → verify → PR → babysit → merge → continue; nonterminal checkpoint semantics | Agent Ledger requirement, universal heavy review, broad permission manifest |
| First complete modular skill family | `8c0d80d3` | `codex/skills/auto-full-run-v2/SKILL.md`; `codex/skills/afr-v2-discovery/SKILL.md`; `codex/skills/afr-v2-umbrella-plan/SKILL.md`; `codex/skills/afr-v2-slice-plan/SKILL.md`; `codex/skills/afr-v2-workspace/SKILL.md`; `codex/skills/afr-v2-slice-execute/SKILL.md`; `codex/skills/afr-v2-review/SKILL.md`; `codex/skills/afr-v2-pr/SKILL.md` | Clean responsibility boundaries, planning self-review, compact slice planning, isolated workspaces, one implementer plus consolidated review, PR lifecycle ownership | E0–E15 gate engine as a required workflow, typed transition ceremony for ordinary actions |
| Native skill-family design | `671d7361` | `docs/plans/2026-06-21-umbrella-afr-native-skill-family.md` | Proportional assurance, file handoffs, efficiency budgets, one-implementer/one-reviewer default, small public surface | Planned local-state machinery when native/session/Git state is sufficient |
| Mature pre-software skill behavior | `f3c34e1d` | the same eight `SKILL.md` paths plus their focused references | Later lessons in route sizing, correction batching, review budgets, exact-head PR convergence, resume and user-stop behavior | Certificates, plan-adoption challenges, correction tokens, state-version protocol, duplicated owner gates |
| Late executable skill-era / parallel experiments | `c95ea489` | relevant `afr-v2-*` skills and PR/review helpers | Defect cases, concurrency cautions, PR hardening, evidence about what became too expensive | Concurrent-row state architecture, schema-12 machinery, lifecycle proof stacks |
| Pre-Phase-6 deterministic helper baseline | `5862aa79` | `src/afr_control/workspaces.py`; `src/afr_control/candidates.py`; `src/afr_control/integration.py`; `src/afr_control/targeted_checks.py`; `src/afr_control/delivery.py` | Narrow workspace, candidate, check, integration, and delivery algorithms plus failure cases | The surrounding custom runtime and workflow architecture |

Historical-source precedence is: original behavior first, first modular family second, native-skill design third, then later hardening only to correct proven defects or recover a narrowly useful algorithm. Later complexity does not override the simpler donor merely because it is newer.

**Extraction rule:** recover behavior, invariants, tests, and failure lessons—not historical architecture wholesale. Do not cherry-pick donor phase or feature commits into v5 when they also import obsolete runtime, state, packaging, or ceremony. Reimplement the smallest behavior against the v5 skill-first architecture and record the donor commit/path in the resulting design or code provenance.

The strongest behavior to recover is:

```text
plan one cohesive outcome
  -> review the plan when warranted
  -> implement and verify
  -> perform proportional independent review
  -> create a PR
  -> monitor CI and review feedback
  -> batch and fix valid findings
  -> re-enter monitoring
  -> merge the exact reviewed head
  -> verify local/remote synchronization
  -> continue to the next eligible outcome
```

A plan review, implementation commit, green CI run, open PR, review-fix push, or one merged slice is progress—not terminal completion while eligible work remains.

## 3. Product outcome

A user should be able to invoke AFR with a goal or existing plan and obtain one of four honest routes:

- `direct`: one cohesive, reviewable outcome;
- `umbrella`: multiple independently deliverable outcomes with meaningful dependencies;
- `spike`: bounded research needed before implementation can be planned honestly; or
- `stop`: work is unsafe, rejected, intentionally deferred, or lacks required authority.

For an authorized end-to-end run, AFR should continue through the latest safe delivery boundary without asking the user to approve routine internal choices.

AFR should ask only when a decision materially changes:

- product scope or acceptance;
- destructive or production effects;
- cost or data-sharing boundaries;
- repository or delivery authority;
- a high-impact architecture choice that cannot be inferred safely; or
- a blocker that native tools and ordinary correction cannot resolve.

## 4. Definition of lean

AFR v5 is lean when the normal path is easy to explain, inspect, and execute:

- one canonical workflow;
- no required service or database;
- no custom provider lifecycle;
- no mandatory certificate or receipt chain;
- no gate transition protocol for ordinary local work;
- no repeated loading of full plans, diffs, logs, or history into prompts;
- no maximum-assurance process applied to routine changes; and
- no duplicate state owner competing with Git, the plan, the session, or the PR.

## 5. Target architecture

AFR v5 will have three layers. Only the first is required.

### Layer 1 — canonical skill package

The R1 design maps the five conceptual responsibilities into one skill package:

| Owner within `afr/` | Role |
|---|---|
| `SKILL.md` | Public entrypoint; activation, final route selection, sequencing, continuation, user stop, and final outcome |
| `references/planning.md` | Discovery, route recommendation, outcome-oriented planning, and plan self-review |
| `references/work.md` | Workspace choice, implementation, focused verification, and candidate inspection |
| `references/review.md` | Proportional review, finding assessment, and bounded correction |
| `references/delivery.md` | Authorized PR operations, monitoring, observed merge, and synchronization |

The [architecture specification](architecture.md#3-one-owner-per-behavior) defines the ownership and handoff boundaries. Split a reference into another skill only when use demonstrates a material correctness, context, or reuse benefit.

### Layer 2 — optional deterministic helpers

Small scripts may support facts that should not depend on model judgment:

- plan-shape and dependency validation;
- Git status, ancestry, changed-path, and expected-old checks;
- worktree creation and containment;
- focused test selection and bounded command execution;
- finding normalization and deduplication; and
- exact PR-head, readiness, merge, and synchronization observation.

These helpers must remain narrow utilities. They may not become a hidden workflow engine.

### Layer 3 — optional automation runner

A later runner may use the Codex SDK to:

- launch the AFR skill from a queue or schedule;
- resume an interrupted Codex thread;
- expose status and interruption controls;
- multiplex independent repository jobs; or
- support a future web or mobile supervision surface.

The runner is not AFR's authority. It must pass a goal to Codex, invoke the installed canonical AFR skill, and observe the resulting session. It must not encode planning, review, correction, or delivery logic independently.

The runner will not enter the roadmap's implementation path until the skill-first core works reliably in ordinary interactive Codex sessions.

## 6. Canonical workflow

The current behavior is defined in the architecture specification's [coordinator behavior](architecture.md#4-coordinator-behavior) and [phase requirements](architecture.md#5-phase-requirements). R2–R5 assemble these capabilities in one package. The historical loop in §2 explains the donor rationale; it is not a separate operational instruction set.

## 7. Proportional assurance

The architecture's [review and correction requirements](architecture.md#review-and-correction) define `lean`, `standard`, and `protected` assurance. The budgets in §10 constrain process cost; evaluation scenarios in the donor matrix test both proportionality and safeguards.

## 8. State and resumption

The architecture's [resume requirements](architecture.md#resume-and-evidence-reuse) use the plan, Git, PR observations, and host session. R1 selects no dedicated state file or database. Any later addition must satisfy §10 and the repository's explicit complexity test.

## 9. Delivery roadmap

### R0 — repository bootstrap

**Outcome:** establish the public successor repository and permanent architectural guardrails.

Deliver:

- root `CHAT.md` and `AGENTS.md`;
- public README and roadmap;
- secret- and machine-state-safe ignore rules;
- clean Git history and public remote; and
- explicit anti-complexity constraints.

Exit when the repository is public, clean, and contains no sensitive or machine-specific committed content.

### R1 — donor inventory and behavior specification

**Outcome:** identify what to recover without importing obsolete machinery.

**Delivered:** [architecture and behavior specification](architecture.md) and [donor matrix](donor-matrix.md). The matrix records source coverage, decisions, scenarios, and the limits of R1 verification. Skill behavior has not been executed or qualified.

Start with the exact donor source map in §2.1. Inspect those commit-qualified files before widening the search. Broaden Git history only when a mapped source references another artifact, a behavior's origin remains ambiguous, or a later defect requires tracing.

Inspect and classify:

- the original one-skill AFR workflow at `3a0f5bc7`;
- the first complete eight-skill family at `8c0d80d3`;
- the native skill-family design at `671d7361`;
- mature pre-software skill behavior at `f3c34e1d`;
- late skill-era hardening at `c95ea489` only as needed for defect/concurrency lessons;
- deterministic Git, workspace, finding, PR-observation, and merge-safety helpers; and
- recurring failure scenarios from later AFR software.

Produce one concise architecture document and one donor matrix. Each matrix row must include: capability, donor repository, exact commit, exact path, behavior/invariant to retain, complexity to reject, v5 destination, disposition (`retain`, `adapt`, `rewrite`, or `reject`), and an evaluation scenario that would prove the port useful.

R1 must distinguish **instruction candidates** from **deterministic-helper candidates**. A helper candidate needs a fact or safety property that should not depend on model judgment; historical existence of a script is not sufficient justification.

Do not copy production code during R1. Do not cherry-pick donor commits. Do not make the private donor repository a runtime dependency of v5; any adopted behavior needed by public users must be documented or implemented within v5 or consumed through an explicitly documented external capability.

### R2 — canonical AFR skill prototype

**Outcome:** one public `afr` skill can route and drive a simple task without custom runtime state.

Deliver:

- activation and environment detection;
- `direct`, `umbrella`, `spike`, and `stop` routing;
- concise planning and plan self-review;
- native implementation and focused verification guidance;
- proportional review selection;
- user-stop precedence; and
- a compact terminal report contract.

Use focused instruction walkthroughs and checks during construction. Assemble the core R2–R5 capabilities before a small set of integrated qualifications in disposable repositories; early fragments do not require a three-repository release gate. Keep the prototype independent of the Codex SDK and old AFR runtime.

### R3 — direct end-to-end vertical slice

**Outcome:** AFR completes one ordinary repository change from request through a verified local candidate or branch.

Prove:

- project-instruction discovery;
- safe handling of dirty or unrelated work;
- direct-plan creation only when useful;
- isolated-worktree selection when warranted;
- implementation through native Codex tools;
- focused tests and actual-diff inspection;
- one consolidated review and one correction when selected; and
- an honest completion or blocker result.

Do not add PR automation, a database, or an SDK runner merely to complete this phase.

### R4 — PR convergence and delivery

**Outcome:** AFR can create and carry one authorized PR to a terminal delivery boundary.

Deliver:

- concise PR creation context;
- exact-head observation;
- CI and review monitoring through native facilities or `babysit-pr`;
- verified finding classification;
- batched review-fix cycles;
- fresh-head re-entry into monitoring;
- remote merge only after required readiness; and
- separate local synchronization verification when applicable.

Keep watcher-specific mechanics outside the canonical AFR skill. Add a narrow helper only where native commands cannot safely establish an exact fact.

### R5 — umbrella continuation

**Outcome:** AFR completes a small multi-outcome plan without user babysitting between ordinary stages.

Deliver:

- outcome-sized decomposition and dependency checks;
- deterministic next-eligible-outcome selection;
- reuse of the same direct work, review, and delivery flow;
- progress updates at meaningful phase boundaries;
- automatic continuation after nonterminal plan review, implementation, PR fixes, and intermediate merges; and
- clean stop behavior for dependency, scope, authority, or safety blockers.

Do not introduce a separate child runtime or per-outcome workflow implementation.

### R6 — evidence-driven helper extraction

**Outcome:** automate only mechanical pain observed during R2–R5 trials.

For each proposed helper:

1. cite repeated real failures or measurable waste;
2. show why skill instructions and native tools are insufficient;
3. define a narrow deterministic interface;
4. keep workflow decisions in skills;
5. add focused tests; and
6. measure whether the helper reduces errors, prompts, turns, or wall time.

Likely candidates are Git/worktree inspection, plan validation, test selection, finding normalization, and exact PR-state observation. None is mandatory in advance.

### R7 — optional Codex SDK runner experiment

**Entry condition:** the skill-first workflow has completed at least 10 representative real runs and interactive execution is understood.

Test whether a thin SDK runner adds material value for:

- unattended queues;
- scheduled maintenance;
- resumable long-running sessions;
- multi-repository supervision; or
- a future status UI.

The experiment must use the installed AFR skill as the workflow authority. Reject the runner if it duplicates skill decisions or begins recreating a control plane.

### R8 — public beta and predecessor disposition

**Outcome:** establish whether AFR v5 can replace the prior AFR workflow for new work.

Before beta disposition:

- complete at least 20 representative runs across direct and umbrella work;
- include low-risk, normal feature, and protected-risk examples;
- demonstrate PR review-fix convergence and exact-head merge behavior;
- demonstrate interruption and honest resumption without duplicate implementation;
- document installation for supported skill surfaces;
- publish measured complexity and workflow results; and
- compare outcomes against ordinary Codex and the predecessor AFR where practical.

The predecessor remains available as historical evidence and a donor until v5 proves that its leaner method retains the safety and completion behaviors that matter.

## 10. Complexity budget

The following are design budgets, not targets to fill:

| Surface | Initial budget |
|---|---:|
| Public workflow entrypoints | 1 |
| Primary skills | at most 5 |
| Coordinator `SKILL.md` | about 300 lines or fewer |
| Internal `SKILL.md` | about 200 lines or fewer each |
| Initial package | 1 public skill and 4 phase references; similar per-reference line budget |
| Default implementers per cohesive outcome | 1 |
| Default independent reviewers | 0 for lean; 1 for standard/protected |
| Default correction passes | 1 |
| Core durable databases/services | 0 |
| Custom agent/provider runtimes | 0 |
| Normal fast verification target | under 60 seconds |

Exceeding a budget requires evidence of a recurring problem, a measured expected benefit, and an explicit decision identifying what simpler option failed.

At each roadmap exit, record actual counts and explain growth or reduction.

## 11. Evaluation metrics

Measure complete accepted outcomes, not activity volume:

- percentage of runs completed without unnecessary user intervention;
- accepted-result wall time;
- total model turns and subagent turns;
- prompt and context volume where observable;
- number of review passes and corrections;
- focused and total verification time;
- PR time to merge-ready and merge;
- escaped material defects;
- duplicate or repeated work after resume;
- operator effort;
- helper-script failure rate; and
- complexity-budget growth.

A new mechanism is successful only when it improves a material outcome enough to justify its implementation and maintenance cost.

## 12. Explicit non-goals for the initial release

AFR v5 will not initially attempt to be:

- a general-purpose workflow framework;
- a replacement for Codex, ChatGPT, or their native agent capabilities;
- a multi-provider model gateway;
- a distributed worker scheduler;
- a hosted control-plane service;
- an event-sourcing platform;
- a project-management database;
- a universal CI or deployment system;
- a mandatory review framework for all repositories; or
- a compatibility runtime for every prior AFR state or schema.

## 13. Donor and dependency policy

The canonical historical donor is `DrJLabs/afr`; use the exact commit/path map in §2.1 rather than referring to an unspecified "old AFR" state. Source access is for development archaeology only and must not become a public v5 runtime dependency.

| Source | Intended treatment |
|---|---|
| `3a0f5bc7` original `auto-full-run` | Primary behavioral donor for end-to-end orchestration and continuation |
| `8c0d80d3` first eight-skill AFR-v2 family | Primary structural donor; adapt clean responsibility boundaries and consolidate where progressive disclosure does not justify separate skills |
| `671d7361` native skill-family design | Primary efficiency donor; retain proportional assurance, file handoffs, small-surface goals, and one-implementer/one-reviewer defaults |
| `f3c34e1d` mature skill-era implementation | Secondary hardening donor; salvage route sizing, correction batching, review restraint, stop/resume, and PR convergence while rejecting its growing state ceremony |
| `c95ea489` late executable skill era | Defect/concurrency corpus; use to understand failure modes and complexity traps, not as the target architecture |
| Later `afrctl` gate/state machinery | Failure-history reference only; do not restore by default |
| `5862aa79` pre-Phase-6 deterministic helper baseline | Selectively port narrow Git, candidate, workspace, check, integration, or delivery algorithms only after v5 demonstrates the need; use later software history only to trace a concrete defect |
| `babysit-pr` and review utilities | Consume as external capabilities where useful; do not vendor their full implementations into AFR |
| Codex SDK | Optional future launcher after the skill workflow is proven |
| Other agent frameworks | Sources of patterns and evaluation ideas, not required orchestration layers |

Every adopted behavior or port must record its exact donor commit/path and whether it was retained, simplified, or rewritten. Prefer behavioral reimplementation and focused test-case transfer. Commit-level cherry-picking is prohibited by default when it imports obsolete runtime, state, packaging, compatibility, or ceremony; an exception must explain why the commit is narrowly coherent and architecture-compatible.

## 14. Immediate next increment

R1 is specified in the linked architecture and donor analysis. R2 begins with the public `afr` coordinator and its planning reference, implementing the compact input, route selection, stop conditions, and terminal reporting contract. Subsequent increments add work, review, and delivery methods to the same package, then exercise continuation and resume across them.

Use the donor matrix's scenarios for focused checks as each capability becomes available. After the core is assembled, review its coherence and run representative integrated qualifications. R1 does not establish a need for custom helpers or a runtime layer. Split internal skills only after evaluation shows that progressive disclosure or responsibility isolation materially improves the result.

## 15. Initial stable-release criteria

AFR v5 is ready for an initial stable release when:

- a standard ChatGPT or Codex agent can discover and use the public skill;
- direct and umbrella routes are both usable;
- planning is outcome-oriented and self-reviewed without excessive ceremony;
- ordinary implementation uses native agent capabilities and focused verification;
- review depth is proportional and valid findings converge through bounded correction;
- an authorized PR can be monitored, corrected, and merged at the exact reviewed head;
- the workflow continues across multiple planned outcomes without routine user prompting;
- interruption and resumption do not duplicate completed work;
- installation and usage are documented without machine-specific assumptions;
- public artifacts contain no secrets or private infrastructure data;
- representative-run metrics meet the complexity budget or document an approved exception; and
- no second workflow exists in helpers, a runner, or documentation.

## 16. Roadmap governance

Update this roadmap when product direction, architecture boundaries, milestone outcomes, or complexity budgets materially change. Do not turn it into a live task ledger or append evidence for every implementation step.

Routine implementation status belongs in the active development surface. Durable design decisions should remain concise, current, and easy for an agent to identify without searching historical plans.
