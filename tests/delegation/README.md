# Native delegation qualification

These bounded manual trials cover selective delegation guidance and its fit with a separately configured Codex roster. They are not a benchmark, an agent runtime, or qualification of every host. AFR remains independent of role names and model settings; the local Codex configuration owns the profiles used here.

## Reproduce the behavioral cases

Copy the [R2 fixtures](../r2/fixtures/) into a disposable Git target outside the skill package, rename `target-guidance.md` to `AGENTS.md`, and establish a clean baseline. Give a fresh native session the raw request and target artifacts, not the expected results below or the authoring conversation. Explicitly select the actual AFR package path so package and target roots differ. Inspect tracked, untracked, and incidental effects afterward.

| Case | Raw request | Evidence to assess |
| --- | --- | --- |
| Small sufficient plan | Use AFR to plan `specs/status-label.md`, without edits | Reuses the adequate source; direct/lean planning; compatibility invariants retained; no compulsory specialist roster, new plan file, or claimed execution |
| Research, analysis, and plan critique | Use AFR to prepare a contract for `specs/audit-export.md`; request the configured researcher for official Python 3.10 `csv.DictWriter` evidence, the planning analyst for approach/acceptance, and the final reviewer for critique | Source applicability, missing policy, grounded acceptance, independent critique, coordinator synthesis, and proposed-versus-executed evidence remain distinct; no implementation or invented owner decision |

Use native spawning and waiting. For a role-discovery probe, retain supported native session evidence of the selected `agent_type`, accepted spawn result, and returned contribution. CLI JSON output may omit information present in the native session record; a final answer alone does not prove a role spawned. Record configured defaults separately from effective child permissions/model/effort. Do not infer all-tool restrictions from a filesystem sandbox.

A useful minimal profile probe supplies two versioned vendor excerpts and an explicit pinned version to the researcher, and a small requirement with preservation constraints to the planning analyst. It needs no browsing, file edits, or code tests. Assess applicability and evidence limits for research, and minimal approach plus observable acceptance for planning. Do not give either role the expected answer.

## Observed results — 2026-09-26

Codex CLI 0.157.1 loaded the repository package by explicit path in separate disposable targets. Two fresh `exec` sessions used read-only mode and the existing user role registry. Hooks, apps, memories, and configured MCP servers were disabled for these bounded probes. This does not qualify the normal full integration surface.

- **Small plan:** returned direct/lean planning, reused the status-label specification, preserved raw status and exit-code contracts, and proposed focused checks without claiming execution or requiring a roster. No source changes, new plan, or untracked files were observed. The ephemeral event stream does not independently establish absence of every possible delegate call.
- **Protected plan:** inspected the actual target, used official version-specific Python documentation, identified the absent security policy, and left policy-dependent implementation unready. Proposed checks covered schema, empty input, access, redaction, retention, compatibility, and preserved contracts. The final synthesis reported research, planning analysis, and independent critique, including a correction distinguishing export-file lifetime from a source-established requirement. These contribution reports are behavioral evidence; the ephemeral CLI stream did not expose the corresponding spawn metadata.
- **Direct role discovery:** a separate minimal, non-ephemeral native session retained actual `spawn_agent` calls selecting `luna_researcher` and `sol_planning_analyst`, each with fresh context and no model/effort override, plus accepted native spawn results. The researcher correctly applied the supplied pinned-version evidence and disclosed that it was not independently verified. The analyst returned a minimal label-correction approach and preservation checks. No file operations or code tests were requested or observed in the parent probe.

Both fixture targets remained byte-identical to their baselines with clean tracked and untracked status. The profile probe also left its target clean. Native session artifacts and private rollback snapshots remain outside the repository.

The configured roster has seven roles: explorer, researcher, implementer, tester, bounded reviewer, planning analyst, and final reviewer. The two added roles and final-reviewer extension were inspected alongside AFR's actual coordinator and phase references. TOML parsing, registry paths, narrow Git allowlisting, baseline-config preservation, skill metadata validation, local links/anchors, and whitespace checks passed. Consolidated independent source review found no material issue.

### Source identity

The skill candidate was based on `9e9cf707e390661d7fb53902adbdfdff1150b440`, with these changed package files:

| File | SHA-256 |
| --- | --- |
| [SKILL.md](../../.agents/skills/afr/SKILL.md) | `18844477eec14abcae6041d53eb256dee01bf6c67b4820155b4c81b468923c26` |
| [planning.md](../../.agents/skills/afr/references/planning.md) | `823bcef2e628e25b06325eda21fa893af617c418330f91e9496d5952b00dcc0b` |
| [work.md](../../.agents/skills/afr/references/work.md) | `0417673cf68ff466f007bf6a0e61ed12ce35abb32cbb277687ae35af634ab01f` |
| [review.md](../../.agents/skills/afr/references/review.md) | `3e8859bc5cf612abe3b89de08754af702ecac18bf9d6c77b6833dd3a659792b7` |

The local role layers under test had these identities; they are configuration evidence, not files installed by AFR:

| Layer | SHA-256 |
| --- | --- |
| `luna-researcher.toml` | `2490912de523fd7d359399a5fee8333251b06a575efba092adaf5ad422ed5bbf` |
| `sol-planning-analyst.toml` | `09d637730bfe819a6fc945e2d6bf77ac09ac8c12061422d8cae43ac228c10988` |
| `sol-final-reviewer.toml` | `be12768d20d518307dbf62dac42b5d77792e934e7bc21d7c9878de8def0aac6c` |

### Limits

The role-discovery probe proves that the two new configured role names were accepted by native spawning and returned useful bounded results. It does not independently prove each child's effective model, reasoning effort, sandbox enforcement, lack of external write capability, or disabled recursive delegation. Those settings were validated in configuration; parent/session overrides and tool-specific controls still matter. The pre-existing final reviewer was extended in configuration and reported in the planning trial, but its fresh effective settings were not separately observed.

These tests do not establish a speed, cost, or accuracy improvement over one agent. The larger case explicitly requested roles to exercise their integration; it is not evidence that three delegates are optimal. Automatic role selection for realistic larger work, concurrent writes and integration, interruption/recovery, installed-package discovery, GUI/ChatGPT parity, and the normal MCP/hook surface remain unqualified. Refresh only affected evidence when the relevant package, profiles, or host changes.
