# AFR v5 skill-first architecture roadmap

**Status:** initial roadmap
**Date:** 2026-09-03
**Repository stage:** public architecture bootstrap

## 1. Decision

AFR v5 will return to AFR's original strength: a skill-driven method that lets a capable host agent take a software initiative from planning to completed delivery without requiring the user to supervise every intermediate step.

The canonical product will be a small family of `SKILL.md` workflows. Standard ChatGPT or Codex provides the agent runtime, tools, context, and native subagents. AFR provides the method, sequencing, proportional quality policy, continuation behavior, and stop conditions.

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

The redesign will use four AFR history points deliberately:

1. The original `auto-full-run` skill introduced at commit `3a0f5bc7` as the end-to-end orchestration model.
2. The first complete eight-skill AFR-v2 family at commit `8c0d80d3` as the cleanest responsibility split.
3. The native-skill-family design at commit `671d7361` for proportional assurance, file handoffs, and one-implementer/one-reviewer defaults.
4. Later AFR skill and software history as a defect, safety, and failure-scenario corpus—not as architecture to restore wholesale.

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

### Layer 1 — canonical skill family

A small set of portable skills contains the workflow intelligence:

| Skill | Role |
|---|---|
| `afr` | Public entrypoint; activation, route selection, sequencing, continuation, user stop, and final outcome |
| `afr-plan` | Discovery, assumptions, approaches, direct/umbrella/spike/stop selection, outcome-oriented planning, and plan self-review |
| `afr-work` | Workspace choice, implementation, focused verification, candidate inspection, and implementation handoff |
| `afr-review` | Proportional quality policy, independent review, finding normalization, and bounded correction |
| `afr-deliver` | Branch/PR creation, PR monitoring, review-fix convergence, exact-head merge, synchronization, and next-outcome handoff |

The exact names may change during prototype evaluation. The responsibility count should not grow without evidence that another skill materially improves correctness or progressive disclosure.

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

### Discovery and planning

1. Read current project instructions and inspect relevant source, tests, history, and existing plans.
2. Clarify only material uncertainty that cannot be inferred safely.
3. Record objective, non-goals, acceptance, constraints, risk, and delivery boundary.
4. Compare materially different approaches when a real design choice exists.
5. Choose `direct`, `umbrella`, `spike`, or `stop`.
6. Create the smallest useful durable plan when persistence is warranted.
7. Self-review the plan for contradiction, missing acceptance, overbuild, unnecessary split, weak evidence, and an available simpler approach.

A direct plan is one cohesive delivery outcome. An umbrella contains independently deliverable outcomes, not implementation microtasks.

### Implementation

1. Confirm current Git state and choose the least disruptive safe workspace.
2. Use an isolated worktree for substantial or risky changes; do not require one for every trivial edit.
3. Implement the planned outcome using native Codex capabilities.
4. Use native subagents only for genuinely independent research, review, or decomposed work.
5. Run focused verification during iteration.
6. Inspect the actual diff and repository state before claiming completion.

The default implementation shape is one capable implementer for the whole cohesive outcome. Parallel writers and best-of-N attempts are optional strategies, not the default workflow.

### Quality and correction

1. Derive review depth from changed behavior, risk, repository policy, and delivery boundary.
2. Run deterministic checks first.
3. Use one consolidated independent reviewer when review adds material value.
4. Verify each finding against the source and acceptance criteria.
5. Batch accepted findings into one correction pass.
6. Re-run only evidence invalidated by the correction plus required integration checks.
7. Allow a second correction only when the first made measurable progress or protected-risk work warrants it.
8. Stop or replan after repeated no-progress results.

### Delivery and continuation

1. Create the PR from the intended branch with concise plan, verification, and follow-up context.
2. Monitor CI, mergeability, and review feedback through the platform's native facilities or `babysit-pr` when available.
3. Fix verified material findings in a batch, push, request or await the required fresh review, and resume monitoring.
4. Merge only the exact reviewed head after required checks and feedback are satisfied.
5. Reobserve the remote merge and verify any required local synchronization separately.
6. Mark the current outcome complete and continue to the next eligible umbrella outcome.

## 7. Proportional assurance

AFR v5 will begin with three descriptive levels. They guide judgment; they are not a mandatory gate engine.

| Level | Typical work | Default assurance |
|---|---|---|
| `lean` | docs, configuration, narrow low-risk fixes | focused checks, diff self-review, ordinary CI |
| `standard` | normal features and refactors | focused checks, one independent review, affected broader checks, ordinary PR convergence |
| `protected` | auth, secrets, persistence, migration, deployment, public API, irreversible effects, or major concurrency | explicit risk review, specialist coverage, broader verification, stricter delivery observation |

Rules:

- The lowest level that safely covers the work should be used.
- A protected signal may raise assurance; absence of such a signal must not automatically select protected behavior.
- One reviewer may cover multiple related lenses in a consolidated pass.
- Browser ChatGPT review, multiple reviewer agents, Brooks review, adversarial review, and graph review are selected tools—not a universal stack.
- Existing repository-required checks and branch protections remain authoritative.

## 8. State and resumption

AFR v5 will first rely on existing durable truth:

1. the current user instruction;
2. project instructions;
3. the current plan when one exists;
4. Git branch, worktree, commits, and diff;
5. PR, CI, review, and merge state; and
6. the active agent session or resumable Codex thread.

A concise run-state file may be added only if real trials show that those sources cannot resume safely and economically. It must summarize current outcome, plan, branch, PR, remaining acceptance, blockers, and next action—not reproduce provider or tool lifecycle history.

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

Inspect and classify:

- the original one-skill AFR workflow;
- the first complete eight-skill family;
- the native skill-family design;
- later planning, worktree, review, PR, and babysit hardening;
- deterministic Git and finding helpers; and
- recurring failure scenarios from later AFR.

Produce one concise architecture document and one donor matrix with `retain`, `adapt`, `rewrite`, or `reject`. Do not copy production code during this phase.

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

Test with fixture conversations and at least three disposable repositories. Keep the prototype independent of the Codex SDK and old AFR runtime.

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

| Source | Intended treatment |
|---|---|
| Original `auto-full-run` skill | Retain the end-to-end orchestration philosophy and continuation behavior |
| First eight-skill AFR-v2 family | Adapt the clean responsibility boundaries; consolidate where progressive disclosure does not justify separate skills |
| Native skill-family design | Retain proportional assurance, file handoffs, and efficiency goals |
| Later `afrctl` gate/state machinery | Use as a failure-history reference; do not restore by default |
| Current `afr-control` software | Selectively port narrow Git, candidate, finding, or delivery algorithms only after need is proven |
| `babysit-pr` and review utilities | Consume as external capabilities; do not vendor their full implementations |
| Codex SDK | Optional future launcher after the skill workflow is proven |
| Other agent frameworks | Sources of ideas, not required orchestration layers |

Every port should record its source commit/path and whether it was retained, simplified, or rewritten. Commit-level cherry-picking is discouraged when it imports obsolete runtime or ceremony.

## 14. Immediate next increment

After repository bootstrap, perform R1 as one bounded analysis increment:

1. inventory the original and first-generation skill files and their references;
2. identify the minimum behavior required for a modern public `afr` skill;
3. build a donor matrix covering planning, implementation, review, PR monitoring, merge, continuation, stop, and resume;
4. define the first skill's compact input, workflow, stop conditions, and terminal output;
5. specify representative evaluation scenarios; and
6. recommend what should remain instruction versus become a deterministic helper.

Do not implement a runner, database, service, provider adapter, or complete five-skill family during R1.

R2 should begin with one public `afr` skill prototype. Split internal skills only after evaluation shows that progressive disclosure or responsibility isolation materially improves the result.

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
