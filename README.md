# AFR v5

AFR v5 is a skill-first redesign of Auto Full Run: a portable workflow for capable agents to take software work from discovery and planning through implementation, verification, review, pull-request convergence, merge, and continuation.

**Status:** the R2 planning prototype is implemented. It does not implement local code changes, independent implementation review, PR delivery, or execution continuation. No stable release exists; observed host/trial coverage is recorded in [R2 trials](tests/r2/README.md).

## Direction

The host agent is the default runtime. AFR teaches the agent how to work; it does not replace the agent platform.

The initial design is one public `afr` skill with a compact coordinator and four phase references. The [coordinator](.agents/skills/afr/SKILL.md) and [planning reference](.agents/skills/afr/references/planning.md) exist now; work, review, and delivery remain later increments. The product is intended for standard ChatGPT and Codex environments, with support qualified separately per host. Narrow deterministic helpers remain candidates for later evidence-driven extraction.

An optional Codex SDK runner may later launch or resume unattended sessions, but the runner must execute the same canonical AFR skill rather than implement another workflow.

## Use the planning prototype

Explicitly select AFR and identify the target project and goal or existing specification. Where the host has the skill available, use its [explicit invocation syntax](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills):

- Codex CLI or IDE: `$afr Plan the change in <specification> for <target project>`.
- ChatGPT: `@afr Plan the change in <specification> for <target project>`.

The ChatGPT example describes the host syntax, not an AFR installation or qualification claim; ChatGPT loading and behavior remain unqualified. For explicit-path use on a host that can read the package, ask it to use [.agents/skills/afr/SKILL.md](.agents/skills/afr/SKILL.md) for the request. The package and target may be in different repositories.

The checked-in location and explicit-only `agents/openai.yaml` policy follow the [official Codex skill conventions](https://learn.chatgpt.com/docs/build-skills#where-to-save-skills). Metadata conformance is distinct from observed catalog/UI discovery. No global installation or host configuration change is made by this repository. See the trial record for the tested loading surface and unverified surfaces.

R2 returns a sufficient contract, a bounded research result, or an honest blocker. Asking it to implement does not silently activate a different workflow or mark the requested implementation complete.

## Intended end-to-end workflow

The implementation, review, and delivery portions below are future R3–R5 capabilities.

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
- [`.agents/skills/afr/SKILL.md`](.agents/skills/afr/SKILL.md) owns the implemented R2 workflow; its planning reference owns the planning method.
- [`docs/architecture-v3.md`](docs/architecture-v3.md) specifies the current package, behavior, ownership boundaries, implementation readiness, and focused framework-derived refinements.
- [`docs/donor-matrix.md`](docs/donor-matrix.md) records inspected historical sources, extraction decisions, and evaluation scenarios.
- [`docs/roadmap.md`](docs/roadmap.md) records the delivery sequence and complexity budgets.

The previous AFR implementation is a donor and defect corpus. AFR v5 will recover its strongest skill-based workflow ideas and hardened safety lessons without importing its custom runtime, gate machinery, or accumulated ceremony wholesale.

## Current repository contents

The repository contains the R2 skill, bounded trial fixtures/procedure, project instructions, current architecture v3 and superseded baselines, the spec-driven assessment, donor analysis, and roadmap. There are no required custom helpers, services, or runtime dependencies. R3 introduces the first complete local implementation path; delivery, cross-host support, and broader qualification remain future work.
