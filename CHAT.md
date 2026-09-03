# AFR v5 ChatGPT project guidance

## Scope and authority

- This file governs ChatGPT work in this repository.
- The user's latest instruction, authorization, stop, or scope correction has highest authority. Next apply this file, then any plan the user explicitly selects, then local implementation decisions.
- This root `CHAT.md` is the sole automatically loaded project instruction entrypoint for ChatGPT interactions. Do not scan for nested instructions unless this file, the user, or the concrete task directs it.
- Root `AGENTS.md` is written for Codex. Do not automatically load it during ChatGPT work unless the user asks, the task is to author or assess Codex instructions, or this file explicitly directs it.
- Preserve unrelated branches, worktrees, files, and uncommitted changes. Never infer that an AFR-named artifact is disposable.

## Product intent

- AFR v5 is a skill-first successor to AFR: a portable workflow that helps a capable host agent move from discovery and planning through implementation, verification, review, pull requests, merge, and continuation.
- The host agent is the default runtime. Canonical workflow behavior belongs in `SKILL.md` files and concise references, not in a custom agent runtime.
- The core must work in standard ChatGPT and Codex environments without requiring a daemon, database, control plane, or SDK runner.
- A future Codex SDK runner may launch, resume, observe, or schedule sessions, but it must invoke the same canonical AFR skill rather than encode a second AFR workflow.
- Use small deterministic helpers where code is materially better than language: plan validation, Git facts, worktree safety, test selection, finding normalization, and exact PR or merge observations.

## Runaway-complexity guardrails

- Choose the simplest architecture that safely delivers the user-visible capability. Capabilities outrank frameworks, protocols, and internal ceremony.
- Do not add a custom agent runtime, provider protocol wrapper, scheduler, event-sourced control plane, durable database, service, or background daemon to the core without evidence from repeated real workflows and an explicitly approved architecture decision.
- Do not convert ordinary agent actions into grants, receipts, epochs, claims, certificates, reservations, or mandatory state-machine transitions merely because they can be modeled that way.
- Keep one canonical owner for each behavior. Never duplicate workflow logic between skills, scripts, an SDK runner, and documentation.
- A new abstraction or persistent subsystem must identify the concrete recurring failure it solves, the simpler alternative considered, measurable benefit, operational owner, and removal path.
- Prefer replacing or deleting an obsolete layer before adding another. A compatibility layer requires a real supported compatibility obligation, not hypothetical future need.
- Keep one public AFR entrypoint and no more than five primary workflow skills unless measured use shows another skill materially improves behavior or context efficiency.
- Keep the coordinator `SKILL.md` at roughly 300 lines or fewer and internal skills at roughly 200 lines or fewer where practical. Move stable reference detail out of the hot path; do not hide a second workflow in references.
- Default to one implementer, one consolidated reviewer, and one correction pass. Add parallelism, extra reviewers, or another correction only when task structure, risk, or observed progress justifies it.
- Heavy review is risk-selected, not universal. Routine work should not pay the strict workflow's cost.
- Avoid speculative backward compatibility before the first stable v5 release.
- When implementation complexity grows faster than delivered capability, stop expansion and propose simplification before continuing.
- At major milestones, report the complexity budget: primary skills, helper scripts, production lines, durable state surfaces, default model turns, default review passes, and normal verification time.

## Working method

- Inspect current repository facts before acting. Expand inspection according to uncertainty and risk; exhaustive archaeology is not a prerequisite for routine work.
- Plan in chat for routine changes. Create or amend a durable plan only when the user asks, the work is materially complex or risky, or cross-session resumability benefits.
- Do not require JIT plans, certificates, tranches, checkpoint PRs, or formal gate sequences for ordinary development.
- Use the host platform's native tools and subagents rather than reproducing their lifecycle. Parallelize only genuinely independent work with clear integration ownership.
- Prefer file-based handoffs for large context. Prompts should carry the objective, constraints, acceptance, relevant paths, and immediate task—not repeated repository history.
- Let language models make judgment calls; use scripts to establish deterministic facts. Git, tests, CI, and the remote forge remain authoritative for source and delivery state.
- Treat the prior AFR repository and its history as a donor and defect corpus, not as standing architecture. Port capabilities and lessons deliberately; do not bulk-copy old runtime or ceremony.
- Keep historical research and superseded designs outside the default active context. Current architecture and roadmap documents must be easy to identify.

## Git, delivery, and protected effects

- A clear implementation request authorizes in-scope local edits and non-destructive validation. Commits, pushes, repository creation, PRs, merges, deployment, installation, credential changes, and destructive actions require the user's instruction or established task authorization.
- Before publishing, scan tracked content for credentials, tokens, private paths, hostnames, personal data, generated artifacts, and machine-specific state.
- Do not push directly to a protected default branch, bypass required checks, rewrite shared history unsafely, or merge with unresolved material findings.
- Verify the exact PR head before merge. Treat remote merge and local synchronization as separate observable operations.
- Never expose secrets. Use configured credentials only through the intended tool or command surface.

## Verification and completion

- Run the narrowest reliable checks first, then broaden according to changed behavior and risk. Keep the normal inner loop fast; reserve exhaustive recovery, packaging, and release checks for their actual boundaries.
- Do not claim a command, test, review, push, merge, synchronization, cleanup, or external effect unless it was observed.
- Work is complete when the requested capability or artifact exists, acceptance is met, risk-appropriate verification passes, authorized delivery is complete, and task-owned temporary effects have a safe disposition.
- Report material changes, checks and results, remote effects, assumptions, and unresolved blockers. Do not manufacture additional process gates at the end of otherwise complete work.
