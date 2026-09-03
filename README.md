# AFR v5

AFR v5 is a skill-first redesign of Auto Full Run: a portable workflow for capable agents to take software work from discovery and planning through implementation, verification, review, pull-request convergence, merge, and continuation.

**Status:** architecture bootstrap. No stable AFR v5 skill release exists yet.

## Direction

The host agent is the default runtime. AFR teaches the agent how to work; it does not replace the agent platform.

The core is intended to work in standard ChatGPT and Codex environments through a small set of `SKILL.md` files. Small deterministic helpers may support facts and safety checks where code is better than prose.

An optional Codex SDK runner may later launch or resume unattended sessions, but the runner must execute the same canonical AFR skill rather than implement another workflow.

## Intended workflow

```text
understand the request
  -> inspect the project
  -> choose direct work, an umbrella, a research spike, or stop
  -> create an outcome-oriented plan when useful
  -> self-review the plan
  -> implement in an isolated workspace when appropriate
  -> run focused verification
  -> apply proportional review and correction
  -> create and converge the PR
  -> merge remotely and verify synchronization
  -> continue to the next planned outcome
```

## Architectural principles

- One public AFR entrypoint.
- A small, progressively disclosed skill family.
- Native host-agent tools and subagents instead of a custom agent runtime.
- One implementer and one consolidated reviewer by default.
- Risk-selected assurance rather than universal maximum review.
- Git, tests, CI, and the remote forge as factual authority.
- Deterministic helper scripts only for narrow mechanical work.
- No database, daemon, event-sourced control plane, or provider manager in the core.
- No speculative compatibility or workflow ceremony before demonstrated need.

## Repository guidance

- [`CHAT.md`](CHAT.md) governs ChatGPT work in this repository.
- [`AGENTS.md`](AGENTS.md) governs Codex work.
- [`docs/roadmap.md`](docs/roadmap.md) records the initial architecture and delivery sequence.

The previous AFR implementation is a donor and defect corpus. AFR v5 will recover its strongest skill-based workflow ideas and hardened safety lessons without importing its custom runtime, gate machinery, or accumulated ceremony wholesale.

## Current repository contents

This initial commit intentionally contains only the project instructions, roadmap, README, and ignore rules. Skills and helper code will be added through evidence-driven vertical increments.
