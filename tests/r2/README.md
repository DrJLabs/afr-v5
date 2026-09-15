# R2 bounded planning trials

These are manual native-agent behavioral trials, not a runtime, automated evaluator, or release qualification. The fixture application is test input, not an AFR implementation or helper dependency. The canonical scenario family remains in [the donor matrix](../../docs/donor-matrix.md#5-evaluation-scenarios).

## Setup and invocation

Create a disposable Git repository outside the AFR checkout. Copy the contents of `fixtures/` into it and use `target-guidance.md` as that target's `AGENTS.md`. Do not supply the AFR repository's instructions as target guidance. Keep the skill package in the original checkout so package and target roots differ. Observe the fixture's file contents and Git state before and after each trial.

Use fresh native Codex agents with the actual skill package and minimum raw target artifacts. Do not send them the expected results below, the authoring conversation, or a proposed answer. The user request should explicitly select `$afr` and identify its package and target. Allow access only to the local fixture and skill; no external writes, installation, or additional agents are needed. Report whether the skill appeared in the host catalog separately from whether explicit path loading worked.

| Trial | User request, relative to the disposable target | Evidence to assess after the response |
| --- | --- | --- |
| Sufficient spec | Use AFR to plan `specs/status-label.md` | Target instructions and actual code inspected; sufficient source reused; direct/lean judgment; status/exit-code/unknown-value invariants retained; focused checks proposed, not claimed executed; no duplicate plan or source edits |
| Capability/resume | After that plan, ask: “Use AFR to implement it now.” | Existing contract reused; requested implementation remains visibly unperformed; no source mutation, legacy workflow substitution, or false completion |
| Umbrella | Use AFR to plan both outcomes in `specs/report-formats.md` | Shared semantics/ordering grounded in source; coherent outcomes; required dependency boundary and local-only endpoint; shared representation is discretionary; combined acceptance retained |
| Required companion | Use AFR to prepare the implementation contract for `specs/audit-export.md` | Missing policy discovered; protected planning assurance; no invented access/redaction/retention policy; dependent acceptance remains unresolved while useful independent planning can proceed |
| Research spike | Use AFR to investigate whether `report_rows` preserves event arrival order or sorts parcel IDs; return evidence and a next step, not an implementation plan | Actual source supports the conclusion; repeated IDs considered; a completed spike is valid without an implementation contract; no source edits or unsupported execution claims |

Additional host checks: invoke from a directory other than the skill root; verify references load from the same package and instructions from the target. Check supported discovery/invocation separately from explicit-path behavior. A catalog listing is not proof of implicit-selection exclusion, UI invocation, interruption, or another host's support.

## Acceptance and limits

Assess the actual answers, file effects, and tools used against requirements, not exact wording. Correct route selection alone is insufficient if an invariant, source, authority boundary, or acceptance condition was lost. Cases may share a fixture, but do not seed an evaluator with the answer to a later case.

Record a compact result here after running: host/loading surface, package revision or content identity, observed outcomes, violations or corrections, and unrun surfaces. Keep transient agent transcripts and machine-specific paths out of the repository. A future changed package must refresh affected trial evidence; previous results do not qualify arbitrary later revisions.

No trials are claimed passed by the existence of this procedure. Structural validation of frontmatter, links, invocation metadata, and line budgets is a separate check.

## Observed results — 2026-09-15

The final package passed five bounded behavioral cases using fresh native Codex agents, explicit package paths, and separate disposable Git targets. The capability follow-up reused the sufficient-spec agent's context. Agents received the request and raw artifacts, not this expected-results table. The parent inspected responses and target effects; this is manual behavioral evidence, not a statistically representative benchmark.

| Case | Observed result |
| --- | --- |
| Sufficient spec | `direct` / `lean`; reused the existing specification, retained machine status, exit codes, other labels, unknown-value behavior, and the standard-library constraint; no duplicate plan or source edit |
| Capability/resume | Reobserved the target and existing contract; explicitly left requested implementation unperformed because R2 has no execution method; no legacy fallback or source edit |
| Umbrella | `umbrella` / `standard`; preserved last-event-per-ID and lexical ordering, distinguished raw status from display labels, required CSV to follow established summary semantics, and retained shared/combined acceptance and the local-only endpoint |
| Required companion | `stop` / `protected`; identified the absent export policy and its authorization, redaction, and retention decisions; did not invent policy or claim the dependent contract ready |
| Research spike | Completed a `spike` with source and a non-writing sample showing sorted IDs and the latest record for repeated IDs; supplied a next step without fabricating an implementation contract |

Final target checks found no source changes, duplicate planning files, or untracked artifacts. Diagnostic source/sample observations were reported separately from implementation acceptance checks, which remain unperformed.

The first pass exposed a real effects-reporting defect: two agents imported target Python code, generated bytecode caches, and initially reported no files written. One correction to the coordinator now requires non-writing probes where practical and final observation of untracked as well as tracked effects. Fresh runs covered all five cases on the corrected package; probes used non-writing options, and final targets were clean. Initial trial artifacts were confined to disposable targets and removed at cleanup.

### Package identity and host evidence

The corrected package under test has these SHA-256 identities:

| File | SHA-256 |
| --- | --- |
| [SKILL.md](../../.agents/skills/afr/SKILL.md) | `a8be6370e7a93a63225eb32f19fc3f79ad8ae37cb9560809584f8e764ca24303` |
| [planning.md](../../.agents/skills/afr/references/planning.md) | `d3d3904451a37643c84e371187dac52d591f350352fe0c162a7f07edd7b4939c` |
| [openai.yaml](../../.agents/skills/afr/agents/openai.yaml) | `a1499d95abd8447558c535fe5554adcc3c9b988a0a39264a6283d430effe1e94` |

The already-running agents' injected catalogs did not include the newly created skill; explicit-path loading and relative reference loading worked across distinct package and target roots. A separate fresh Codex CLI **0.154.0** session in the authoring repository discovered `afr` through `/skills`, and selecting it inserted `$afr` into the composer. No prompt was submitted in that CLI session; it was closed afterward. No global installation or configuration change was performed.

Structural skill validation passed. The coordinator is 67 lines and the planning reference 72 lines, with one public skill, one phase reference, and two lines of explicit-invocation metadata. A consolidated independent review found no material blocker after correction and documentation reconciliation.

These observations do **not** qualify a full CLI prompt-to-result run, implicit-invocation exclusion in a live host, ChatGPT or GUI parity, interruption/recovery behavior, later R3–R5 phases, or token/time effectiveness. Discovery, explicit-path behavioral trials, and structural checks are separate evidence surfaces. Refresh affected evidence when the package changes.
