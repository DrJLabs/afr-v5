# AFR v5 architecture and behavior specification

**Status:** superseded R1 v1 baseline; retained for historical comparison. Use [architecture v3](architecture-v3.md) for the current design.

The design below records R1 at `186631c`; its original behavior text is preserved. The [roadmap](roadmap.md) owns delivery sequencing and complexity budgets. The [donor matrix](donor-matrix.md) owns historical provenance, extraction decisions, and evaluation scenarios. Historical instructions are evidence, never authority for a v5 run.

## 1. Decision and rationale

Begin with one public `afr` skill. Its `SKILL.md` coordinates the workflow and loads four phase references when needed:

```text
.agents/skills/afr/
├── SKILL.md
└── references/
    ├── planning.md
    ├── work.md
    ├── review.md
    └── delivery.md
```

This is the R1 recommended implementation shape, not an existing package or an installation claim. Host-specific discovery metadata can be added at the implementation boundary if required by the supported host. The workflow text should remain portable.

The original donor supplies the complete outcome loop. The first modular family clarifies responsibilities. The native-family design supplies proportional review and economical handoffs. Later sources contribute specific safeguards; their control planes and mandatory records are not adopted. See matrix rows I01–I14 and X01–X03 for the source evidence.

| Approach | Benefit | Cost and decision |
| --- | --- | --- |
| All instructions in one large file | One invocation and obvious ownership | Loads every phase together; use focused references for detail |
| One coordinator with four references | One invocation, one workflow owner, detail loaded as needed | Selected starting shape; the coordinator must name the next reference explicitly |
| Five independently invoked skills | Separate reuse and invocation | Defer until real use shows meaningful reuse, isolation, context savings, or repeated reference-routing failures |

Aim for about 300 coordinator lines and about 200 lines per phase reference. These are design budgets, not reasons to add another skill automatically. R2–R5 build capabilities inside this package; broad integrated qualification follows assembly of the core.

No daemon, database, custom agent runtime, scheduler, required run-state file, or SDK runner is part of this design. Native host facilities supply tools, workspaces, sessions, and subagents. Git, checks, and the remote forge supply observable source and delivery facts.

## 2. Inputs and authority

Accept a user goal or an existing plan, the target project, and any stated constraints or delivery boundary. Discover missing repository facts locally before asking. Use ordinary language; no execution manifest or mandatory input schema is required.

Before starting work, establish:

- the requested outcome and observable acceptance;
- the actual project/worktree, applicable instructions, branch, base, and existing changes;
- scope exclusions, material risks, and required verification;
- the latest authorized endpoint: analysis, local candidate, published PR, or merged result, including local synchronization when requested or required.

Invocation of AFR selects its method. It does not grant every external effect. Carry forward authorization already given; ask only for missing authority or a decision that materially changes scope, safety, cost, or data sharing. Push, PR creation, merge, deployment, installation, and cleanup must each fit the current request and repository policy. Authorization to merge does not imply authorization to delete a worktree or branch.

The latest user instruction and applicable project instructions govern the run. A plan records intent but cannot override them. Historical plans, donor fields, and retrieved memories do not activate legacy services or supply new permissions.

## 3. One owner per behavior

The paths below are relative to the proposed `afr/` package. The implementation should put operational instructions in these owners. Once implemented, this design should summarize and link to those instructions rather than maintain a second executable workflow in documentation.

| Owner | Responsibility | Information needed by the next phase |
| --- | --- | --- |
| `SKILL.md` | Explicit activation; authority; final route choice; phase sequence; stop, resume, continuation, and terminal reporting | Current outcome, authorized endpoint, next action or blocker |
| `references/planning.md` | Discovery, alternatives when useful, route recommendation, outcome sizing, acceptance and dependency analysis, plan self-review | Scope, acceptance, constraints, relevant files/interfaces, verification approach, dependencies |
| `references/work.md` | Workspace selection, implementation, focused verification, actual-diff inspection | Candidate branch/revision, changes, checks and their scope, residual concerns |
| `references/review.md` | Risk-selected review, finding assessment, consolidated correction and necessary rechecks | Findings and dispositions, reviewed revision, remaining material concerns |
| `references/delivery.md` | Authorized PR operations, native monitoring, feedback handling through the review method, observed merge and local synchronization | PR/revision, delivery facts, incomplete obligations |

Phase references return their results to the coordinator; they do not independently activate AFR, select the next umbrella outcome, or define competing stop/completion rules. Delivery uses the review method for new feedback instead of defining another correction policy.

Ordinary transitions happen in the same agent context. A separate brief or report is useful for large delegated work or resumption, not mandatory for every phase. Handoffs name existing files, revisions, evidence, and remaining concerns; they do not require generated diff packages, certificates, receipts, or JSON result envelopes.

## 4. Coordinator behavior

### Activation and route selection

Activate only when the user explicitly selects AFR planning, execution, or continuation. A planning-only request uses discovery and planning and ends with the requested analysis or plan. Discussion, explanation, or review of AFR itself does not start an autonomous run. Ordinary project work does not implicitly select AFR.

Choose the smallest route that honestly fits the request:

| Route | Meaning | Completion boundary |
| --- | --- | --- |
| `direct` | One cohesive, reviewable outcome, potentially containing several commits | Acceptance and the authorized delivery endpoint are satisfied |
| `umbrella` | Several independently deliverable outcomes with meaningful dependencies | All required outcomes reach their authorized endpoints; unresolved dependency work remains visible |
| `spike` | Bounded research needed to decide or specify implementation | Deliver the question's evidence, conclusion or remaining uncertainty, and a recommended next step |
| `stop` | Current work cannot proceed safely, lacks authority, is explicitly stopped, or is intentionally deferred | Explain the specific boundary and the smallest action needed to resume, when applicable |

A research result does not automatically authorize its proposed implementation. A ready PR does not automatically authorize merge. Conversely, an intermediate review, fix push, or merge does not finish an authorized umbrella while eligible work remains.

### Sequence and continuation

For implementation, coordinate planning → work → review when warranted → the authorized delivery endpoint. Send new accepted review findings through the same correction method. Return to monitoring after a fix that changes a published PR.

For an umbrella, select an unfinished outcome whose dependencies have reached their required endpoints. Use explicit plan order to break ties when the choice otherwise has no material consequence. Reuse the same direct workflow. Dependencies that require a merged base cannot be satisfied by an unmerged local candidate.

Continue after intermediate progress while scope, authority, and prerequisites still permit useful work. If unfinished outcomes exist but none is eligible, report the blocking dependency or cycle; do not declare the umbrella complete. Do not impose a new schema or scheduler to make this selection.

Check for user steering before the next consequential action and after delegated results. Honor a stop promptly using the host's controls. Reobserve any already-started external action whose outcome is uncertain before reporting its disposition.

### Resume and evidence reuse

Resume from the latest user intent, existing plan, Git/worktree state, PR/check/review observations, and available session context. Resolve an existing branch or PR before creating another. Check the identity and relevance of any reused evidence: tested/reviewed revision, changed surfaces, prerequisites, and applicable policy.

If a revision, base, acceptance criterion, or prerequisite changes, refresh the affected evidence. Preserve still-valid evidence rather than repeat every successful check. A stale summary cannot establish current readiness.

When an external write times out or returns an ambiguous result, inspect the external state before retrying. A remotely merged PR with incomplete local synchronization resumes at the missing local operation, not at implementation or merge.

### Completion and blockers

Completion requires accepted work, risk-appropriate checks, the authorized endpoint, and a safe disposition of temporary effects. A failed or unavailable required check is a blocker; an explicitly optional check is reported as not run. Partial delivery remains partial.

Give a compact final report containing the outcome, changed files or artifact links, relevant verification and its limitations, actual delivery effects, and remaining assumptions or blockers. For an umbrella, include remaining outcomes; for a spike, include the conclusion and uncertainty. Do not produce mandatory status files solely to satisfy reporting.

## 5. Phase requirements

### Planning

Inspect enough current source, tests, instructions, and relevant history to bound the request. Compare alternatives only where a real design choice exists. Keep objectives and acceptance observable; describe outcomes rather than minute-by-minute implementation steps.

Use chat for small work. Use the project's designated durable plan when requested, useful for interruption/resumption, or warranted by risk or duration. Reuse a sufficient existing outcome specification; do not create a second slice plan by default. For umbrellas, state dependencies and independently deliverable acceptance.

Self-review for missing acceptance, contradictory constraints, unsupported assumptions, unnecessary decomposition, and a simpler adequate approach. An unanswered question becomes a blocker only when it materially prevents safe progress.

### Work

Inspect current changes and preserve unrelated work. Choose a feature branch or isolated worktree according to repository policy and risk; reuse valid isolation when appropriate. Escalate an unexplained overlap that cannot be safely separated. Do not treat every unrelated dirty file as a reason to stop.

Use the host agent for implementation. Default to one implementer for a cohesive outcome. Delegate only independent, bounded work with clear ownership and a cheap synthesis path. Native tools own spawning, waiting, interruption, and resumption.

Run focused behavioral checks appropriate to the change, including meaningful regression evidence for a bug fix when practical. Follow required repository checks and expand coverage for failures or affected risks. Inspect the actual diff and associate evidence with the candidate being handed off. Do not reinstall dependencies or repeat a full baseline suite without a relevant reason.

### Review and correction

Select the lowest adequate assurance level from actual behavior and risk. `lean` work uses focused checks and self-review; `standard` work normally uses one consolidated independent review; `protected` work adds the relevant specialist coverage and verification required by its risks. Existing repository requirements remain binding.

Authentication, secrets, persistence, migrations, deployment, public interfaces, irreversible effects, and significant concurrency are signals to examine. New risk can increase review depth within existing authority; additional data sharing or external effects need their own authority. A required review capability that is unavailable must be reported, not simulated or claimed.

Verify each finding against source and acceptance. Record enough to explain its impact, location, evidence, and disposition: accept, reject with reason, duplicate, or follow-up. A material unresolved finding cannot be relabeled as a follow-up to make delivery pass. Out-of-scope findings may require a scope decision but do not authorize unrelated implementation.

Batch accepted findings into one correction by default. A further pass requires observed progress or elevated risk. Recheck affected behavior and required integration evidence; renew review where the revision or finding requires it. Repeated unchanged failure causes a stop or replan. New PR feedback uses these same limits and judgments.

### Delivery

Identify the exact repository, remote, target branch, source branch, and PR. Reuse an existing matching PR. Create or update a PR only within authority, with concise scope, verification, and residual context.

Use available native/platform monitoring or an appropriate external PR-monitoring capability for CI and feedback. AFR owns the response to observations and the continuation decision; it does not implement a watcher. Required checks must be observed as successful or explicitly satisfied by repository policy. Missing, pending, failed, and unknown observations are distinct from success.

Associate readiness with the actual PR head. A pushed fix invalidates readiness for the old head and returns the PR to monitoring and affected review. Before merge, reobserve the head, target, checks, feedback, and mergeability. Use a merge operation conditioned on the expected head when the platform supports it; if the available mechanism cannot safely protect the reviewed revision, stop at that boundary.

Observe the remote merge independently from local synchronization. When synchronization is required, fetch the remote target and fast-forward only a safe local target after inspecting its ownership and changes. Do not substitute a local merge for remote PR merge, reset a diverged branch, or switch another active worktree's branch. Reconcile the plan through its authorized path when required; report any incomplete obligation before dependent continuation.

## 6. Deterministic helpers

R1 selects **zero required custom helpers**. The donor matrix records candidates for Git/worktree identity and containment, candidate scope, verification coverage, finding identity, and PR/merge observations. Initially use native Git, repository checks, and forge capabilities to establish those facts.

The donor code and tests demonstrate useful invariants and regression scenarios. They do not establish repeated failures of this unimplemented v5 design. Extract a helper only after a real v5 run shows a recurring failure or measurable waste that instructions and native tools cannot adequately address, following the roadmap's complexity test.

A justified helper supplies a narrow deterministic observation or check with focused tests. It does not select routes, assign agents, manage workflow state, grant authority, or decide completion. No historical schema, database, compatibility engine, or run identifier is required to use it.

## 7. Evaluation and R1 boundary

The donor matrix defines evaluation scenarios with concrete expected evidence. They are a specification for later checks, not a claim that v5 passed them. R1 verifies source provenance, coverage of the required behaviors, consistency of ownership, and the absence of unjustified machinery.

During R2–R5, use focused instruction walkthroughs and checks of any implementation that actually exists. Assemble planning, work, review, delivery, continuation, and resume behavior, then perform a coherence review and a small set of representative integrated runs. Measure accepted outcomes, interruptions, repeated work, context/tool cost, correction passes, and escaped defects. Do not infer behavioral effectiveness from Markdown validation.

The first implementation increment is the public coordinator and its planning reference. The remaining references extend the same package. Installation details, empirical helper extraction, runtime effectiveness, PR delivery trials, and release qualification remain subsequent work.
