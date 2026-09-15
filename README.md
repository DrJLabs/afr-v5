# AFR v5

AFR v5 is a skill-first redesign of Auto Full Run: a portable workflow for capable agents to take software work from discovery and planning through implementation, verification, review, pull-request convergence, merge, and continuation.

**Status:** R1 donor analysis and architecture v3 are complete. The AFR v5 skill is not implemented yet; no stable release exists.

## Direction

The host agent is the default runtime. AFR teaches the agent how to work; it does not replace the agent platform.

The initial design is one public `afr` skill with a compact `SKILL.md` coordinator and four phase references. It is intended for standard ChatGPT and Codex environments. Narrow deterministic helpers remain candidates for later evidence-driven extraction.

An optional Codex SDK runner may later launch or resume unattended sessions, but the runner must execute the same canonical AFR skill rather than implement another workflow.

## Intended workflow

```text
understand the request
  -> inspect the project
  -> choose direct work, an umbrella, a research spike, or stop
  -> establish intended behavior, constraints, and acceptance
  -> self-review the plan
  -> implement in an isolated workspace when appropriate
  -> verify conformance with focused evidence
  -> apply proportional review and correction
  -> create and converge the PR
  -> merge remotely and verify synchronization
  -> continue to the next planned outcome
```

## Architectural principles

- One public AFR entrypoint.
- One coordinator with phase references loaded as needed.
- Native host-agent tools and subagents instead of a custom agent runtime.
- One implementer and one consolidated reviewer by default.
- Risk-selected assurance rather than universal maximum review.
- A sufficient implementation contract, requirement-based verification, and combined acceptance for umbrella work.
- Git, tests, CI, and the remote forge as factual authority.
- Deterministic helper scripts only for narrow mechanical work.
- No database, daemon, event-sourced control plane, or provider manager in the core.
- No speculative compatibility or workflow ceremony before demonstrated need.

## Repository guidance

- [`CHAT.md`](CHAT.md) governs ChatGPT work in this repository.
- [`AGENTS.md`](AGENTS.md) governs Codex work.
- [`docs/architecture-v3.md`](docs/architecture-v3.md) specifies the current package, behavior, ownership boundaries, implementation readiness, and focused framework-derived refinements.
- [`docs/donor-matrix.md`](docs/donor-matrix.md) records inspected historical sources, extraction decisions, and evaluation scenarios.
- [`docs/roadmap.md`](docs/roadmap.md) records the delivery sequence and complexity budgets.

The previous AFR implementation is a donor and defect corpus. AFR v5 will recover its strongest skill-based workflow ideas and hardened safety lessons without importing its custom runtime, gate machinery, or accumulated ceremony wholesale.

## Current repository contents

The repository contains project instructions, architecture v3 plus its superseded v2/v1 baselines, the spec-driven direction assessment, donor analysis, roadmap, README, and ignore rules. R2 begins the activation/routing/planning prototype and bounded behavioral trials; R3 introduces the first complete local implementation path. Skills, helpers, tests, and runtime qualification remain future work.
