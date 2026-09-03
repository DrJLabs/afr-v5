# AFR v5 Codex repository instructions

## Scope and authority

- This file governs Codex work throughout this repository.
- The user's latest instruction, authorization, stop, or scope correction has highest authority. Next apply this file, then an explicitly selected plan or specification, then local implementation decisions.
- `CHAT.md` is the ChatGPT interaction contract. It does not supersede this file for Codex repository work.
- Do not create nested `AGENTS.md` files unless a subtree has genuinely different commands or safety boundaries.
- Preserve unrelated branches, worktrees, files, and uncommitted changes. Stop when intended edits overlap unexplained work or source authority is genuinely ambiguous.

## Mission and architectural boundary

- Build AFR v5 as a skill-first workflow for standard Codex and ChatGPT. The host agent is the normal execution runtime.
- AFR's canonical behavior belongs in a small set of `SKILL.md` files and concise references. The primary flow is discovery and planning through implementation, verification, review, PR convergence, merge, and continuation.
- The core must not require a daemon, database, event-sourced control plane, custom App Server client, provider process manager, or SDK runner.
- Use native Codex tools, worktrees, sessions, and subagents for agent lifecycle. Do not reproduce spawning, waiting, steering, interruption, resume, or thread scheduling in AFR.
- A future Codex SDK component may be a thin optional launcher for unattended or queued sessions. It must invoke the canonical AFR skill and must not contain a second workflow implementation.
- Use code for deterministic facts and safety checks: plan shape, Git identity, worktree containment, test execution, finding normalization, and exact remote observations.
- Treat prior AFR repositories and commits as donors and a defect corpus. Port capabilities and tests deliberately; never bulk-copy the old runtime or ceremony.

## Complexity budget and rejection rules

- Use the simplest design that safely delivers the requested capability. Do not add architecture for hypothetical future scale.
- Do not introduce custom runtimes, schedulers, durable databases, background services, provider abstractions, event registries, or workflow engines without an explicitly approved design backed by repeated observed failures in the skill-first system.
- Do not model ordinary local agent actions as grants, epochs, leases, claims, reservations, certificates, receipts, or mandatory state transitions.
- One behavior has one canonical owner. Never duplicate workflow policy across the coordinator skill, internal skills, scripts, an SDK runner, and prose documentation.
- Every proposed persistent subsystem or major abstraction must state: the recurring failure it solves, evidence that the failure occurs, the simpler option rejected, measurable benefit, operational owner, and what existing mechanism it replaces.
- Prefer deletion and consolidation over additive compatibility layers. Before the first stable v5 release, backward compatibility exists only when the user explicitly authorizes a concrete obligation.
- Keep one public AFR skill entrypoint and no more than five primary workflow skills unless measurements show another skill improves correctness or context efficiency.
- Keep the coordinator `SKILL.md` near 300 lines or fewer and internal skills near 200 lines or fewer where practical. References may hold stable detail but must not hide a duplicate workflow.
- Default execution is one implementer, one consolidated reviewer, and one correction pass. A second correction requires observed progress or elevated risk.
- Default review is proportional. Do not stack reviewers, full-suite verification, or browser review on routine work.
- Parallelize only independent assignments with clear source ownership and a cheap synthesis path. Native Codex owns subagent mechanics.
- If a change increases concepts, persistent state, default tool calls, or verification time without a comparable user-visible gain, stop and propose a leaner design.

Before adding a new layer, answer all of these in the change description or design:

1. Can the host agent already do this natively?
2. Can a concise skill instruction solve it?
3. Can one small deterministic helper solve it?
4. Has the failure occurred repeatedly in real AFR runs?
5. What existing code, state, or process will this replace?
6. How will the benefit and ongoing cost be measured?

If the answers do not justify the layer, do not add it.

## Working model

- Inspect current Git status, relevant instructions, code, tests, and delivery state before editing. Expand inspection according to uncertainty and risk, not by default.
- Plan in chat for routine work. Write a durable plan only when requested, materially risky, long-lived, or useful for cross-session continuation.
- Do not require JIT plans, certificates, tranches, checkpoint PRs, controller declarations, or formal gate graphs for ordinary work.
- Read the complete target file before editing it. Make the smallest coherent change and re-read the result.
- Prefer outcome-oriented plans and acceptance criteria. Avoid implementation microsteps that reduce agent judgment without adding safety.
- Use file-based handoffs for large context and concise prompts for immediate work. Do not repeatedly paste plans, diffs, logs, or repository history into agent prompts.
- Use native subagents for independent research, review, or decomposed work only when their expected value exceeds coordination cost.
- Git, tests, CI, and the remote forge are authoritative for source and delivery facts. Model summaries are not proof.

## Skill and helper design

- The public AFR skill owns activation, workflow selection, continuation, stop conditions, and final outcome. Internal skills own focused methods, not separate lifecycle state.
- Skills should use progressive disclosure: keep the hot path concise and load a reference only when the active task needs it.
- Do not repeat the same policy or field inventory across skills. Link to one canonical reference or schema when deterministic structure is truly necessary.
- Helpers must have narrow inputs, deterministic outputs, useful `--help`, and focused tests. They must not become an implicit workflow engine.
- Prefer human-readable Markdown plans and ordinary Git state. Add machine-readable state only when resumption cannot be handled safely from the plan, Git, PR, and session context.
- Keep historical material outside the default active context. Maintain one clearly current architecture document and one current roadmap.
- Do not commit secrets, credentials, personal data, absolute home paths, hostnames, environment dumps, transient agent state, or machine-specific artifacts.

## Git, review, and delivery

- Use a feature branch or isolated worktree for reviewable changes once the repository is shared. The initial repository bootstrap may commit and publish `main` when explicitly authorized.
- Do not push directly to a protected default branch, bypass required checks, rewrite shared history unsafely, or merge with unresolved material findings.
- A local implementation request does not automatically authorize a push, PR, merge, deployment, installation, repository setting change, or destructive cleanup.
- Batch related review findings into one correction. Verify findings against the repository before changing code.
- Treat PR creation, review convergence, remote merge, and local synchronization as distinct observable outcomes, but do not build a state machine merely to name them.
- Verify the exact reviewed PR head before merge. Reobserve an ambiguous remote mutation rather than blindly repeating it.
- Use `babysit-pr` or the platform's native PR monitoring capability when requested or useful; keep watcher mechanics outside AFR's canonical workflow definition.

## Verification discipline

- Run the narrowest reliable checks first, then broaden according to changed behavior and risk.
- Keep the normal `fast` path under roughly 60 seconds as an architectural goal. Separate focused, core, recovery, package, and release checks rather than putting all scenarios in the inner loop.
- Test behavior and contracts, not repeated prose strings. Avoid large generated fixtures or exhaustive fault matrices until the related failure class is real and materially harmful.
- Full package, recovery, or release qualification belongs at the matching boundary, not every source edit.
- Do not claim a test, review, CI result, push, merge, synchronization, or cleanup unless it was observed.

## Completion and escalation

- Work is complete when the requested capability or artifact exists, acceptance is met, risk-appropriate checks pass, authorized delivery is complete, and temporary effects have a safe disposition.
- Report changed files, user-visible behavior, verification performed, remote effects, assumptions, and unresolved blockers.
- Stop for a current user stop, uncertain authority, overlapping unexplained work, missing authorization for a protected effect, or a required check that cannot be satisfied.
- Do not turn an ordinary implementation decision into another approval or process gate. Ask only for the smallest decision that materially changes scope, safety, cost, or external effect.
