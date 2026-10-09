# AFR native goal usage refinement: implementation plan

**Date:** 2026-10-09. **Baseline:** `596fa519d44e9c901e0dbffdae14bddbfe018909`.
**Status:** local instruction refinement complete; further qualification deferred by the user; native goal-on qualification and adoption remain pending. This document does not activate AFR or a native goal.
**Basis:** [September 27 research assessment](goal-gpt6-research-assessment.md).

## Outcome and authority

Refine AFR's existing optional native goal integration so an agent can recommend persistence appropriately, project a sufficient contract into one objective, recover useful context from the existing plan, and report completion accurately. Demonstrate the affected behavior through the existing M9 protocol before claiming reliable goal-on execution or advertising a host-specific invocation.

The user selected local implementation through a verified candidate, then explicitly deferred further qualification and authorized commit, push, PR creation, review, merge, local `main` synchronization, and cleanup of this feature branch. Native goal mode and package installation have not been selected. The work has three distinct evidence boundaries: a reviewed instruction change, bounded native qualification, and the representative-run adoption decision. Completing and delivering the instruction patch leaves native qualification and adoption pending; those later boundaries do not block the currently authorized delivery.

This is one cohesive instruction refinement with staged validation, suitable for the direct route. Use standard assurance for the later candidate because authority, continuation, and completion semantics affect subsequent work. No architecture expansion is proposed.

## Verified starting point

The authoring checkout is on `docs/goal-gpt6-research`, at the same commit as local `main`. Before this document was added, the research assessment was the only Git-reported change and was untracked. Keep both documents available as required inputs if execution moves to another branch or worktree; a checkout of the baseline commit alone does not contain them.

- The [coordinator](../.agents/skills/afr/SKILL.md#native-goal-integration) already preserves explicit goal selection, one parent objective, host-owned lifecycle controls, authority limits, acceptance, and ordinary goal-off operation.
- The [planning projection](../.agents/skills/afr/references/planning.md#project-a-native-goal) already defines the compact objective's contents, but has no worked example or concrete checkpoint guidance.
- The [M9 record](../tests/m9/README.md#observations) contains historical source checks and a bounded goal-off fixture. Cases B–J remain marked not run; broader goal-off fallback is also untested.
- The [README](../README.md#afr-with-native-goal-mode) correctly withholds a qualified combined invocation. The [M9 roadmap](roadmap.md#m9--native-goal-integration-and-qualification) still requires native evidence and a representative goal-on disposition.
- The [synchronization plan](skill-synchronization-plan.md) requests one native goal, but its wording and delivered artifacts do not establish which native transitions occurred.

> 🧠 **From Hindsight memory (M9 native goal integration and qualification)** — M9 deliberately keeps native persistence around one AFR coordinator and rejects a second workflow or goal-state subsystem. Its recorded follow-ups include selection guidance, a goal-plus-plan example, and native qualification. The current coordinator, planning reference, and M9 record confirm those boundaries; current qualification claims must come from observed evidence.

The research's external sources and tool observations are dated. At execution, refresh any version-sensitive claim needed for the actual host against its live tool contracts and current official documentation. An installed CLI version does not identify the runtime serving a conversation. No new native behavior was exercised while authoring this plan.

## Change ownership

| File and section | Proposed change | Completion evidence |
| --- | --- | --- |
| `.agents/skills/afr/SKILL.md`, Native goal integration | Add a concise recommendation rule while retaining the existing explicit-selection and lifecycle rules | Positive/negative selection review; M9 A/B observations |
| `.agents/skills/afr/SKILL.md`, Terminal report | Report native completion usage when the host requires it, using the actual completion result | Source review and observed budgeted completion when authorized and supported |
| `.agents/skills/afr/references/planning.md`, Project a native goal | Add one worked objective and checkpoint guidance; distinguish a plan document from host Plan mode | Source review; M9 B/C/F/I observations |
| `.agents/skills/afr/references/planning.md`, Establish a sufficient implementation contract | Add comparable baseline/final evidence for optimization outcomes | Review a concrete optimization contract; execution evidence if that task is selected |
| `tests/m9/README.md` | Append dated control observations and focused additions to existing cases; record actual outcomes | Native results tied to the candidate and host; historical observations preserved |
| `README.md` | Add a host-specific invocation only after the exact loading/control sequence passes | Link to the qualifying M9 observation and its limitations |
| `docs/roadmap.md`, M9 | Record the evidence-backed retain/revise/remove disposition when available | Representative-run evidence and comparison, with confounders |

The initial operational patch belongs in the coordinator and planning reference. M9 owns trial instructions and observations; the roadmap owns adoption. Work, review, delivery, invocation metadata, fixtures, and synchronization code need no change unless an observed defect justifies a narrowly scoped correction.

## Instruction changes

### 1. Recommend goal mode without activating it

Insert a short paragraph near the start of Native goal integration, before creation instructions. Suggested substance:

> Recommend native goal mode when one bounded, auditable outcome is likely to need several evidence-and-correction iterations or resume boundaries, and available inputs and authority permit useful independent progress. A clear finish line may coexist with an uncertain method. Ordinary focused work can use ordinary AFR. A recommendation does not select goal mode; continue authorized work without making optional persistence another approval gate.

Retain the following paragraph's explicit user-selection requirement and the rule that unused goal mode adds no probe or state. Avoid a mandatory scoring system, task classifier, minimum duration, or tool call merely to decide whether to recommend a goal.

Review these examples as decisions, not executable transition tests:

| Request | Expected recommendation |
| --- | --- |
| One small, understood text or code edit | Ordinary AFR; no required goal inspection or creation |
| A bounded migration with defined compatibility checks and likely repair iterations | Goal mode may help; creation still requires explicit selection |
| A research artifact with agreed claim coverage, sources, and stopping conditions | A bounded research goal may help; implementation remains outside the endpoint |
| Several unrelated backlog items without a shared acceptance condition | Clarify the contract; persistence does not establish a coherent parent outcome |
| A task blocked on a consequential owner decision | Surface the decision; goal mode does not supply authority or remove the blocker |

### 2. Couple the objective to one authoritative plan

Extend Project a native goal after its existing projection guidance. Keep its field list and approximate length guidance as the canonical objective shape; do not reproduce them in another template or reference.

Add one compact natural-language example. The following is draft wording for a future authorized task, not a command to execute now or qualified combined slash syntax:

```text
Use AFR with one native goal to implement the accepted contract in
docs/parser-migration-plan.md through a verified local candidate.
Read its required companions. Preserve its binding behavior, constraints,
dependencies, and unrelated work. Complete only when its decisive checks,
required review, and applicable combined acceptance hold for the candidate.
Continue unfinished eligible work and causal corrections within that authority.
Keep the existing plan's checkpoint current at meaningful boundaries.
Honor user stops, host limits, and unresolved authority or evidence gaps.
```

The example path is illustrative and must be replaced with the real accessible contract. A real projection must name that contract's decisive acceptance rather than leave it vague. Do not introduce a token budget unless requested, promise automatic continuation, or imply local implementation includes publishing or merging.

Add concise guidance to the same planning section:

- Reuse the existing target-owned plan when sufficient. Keep requirements, settled decisions, and the revisable approach distinguishable within its existing structure.
- For work needing resumable written context, keep one compact checkpoint: verified obligations and evidence locations, remaining obligations, candidate/base including relevant untracked inputs, next eligible action, blockers, and in-flight effects. Record material discoveries or changed decisions where they already belong in the plan.
- Update at meaningful acceptance boundaries, material discoveries, or handoff. No per-tool journal, separate progress file, goal-state file, or mandatory plan for a small task.
- On continuation or compaction recovery, re-read the relevant contract/checkpoint, verify that required sources still resolve, and apply the coordinator's [stop and resumption](../.agents/skills/afr/SKILL.md#stop-and-resumption) rules. Refresh affected evidence and resume the missing obligation; ordinary progress keeps the same objective.
- A Markdown plan can guide execution independently of the host's Plan mode. Qualify the actual mode and loading path; the presence of a plan file proves neither activation nor continuation.

Checkpoint updates cannot change authority or silently weaken acceptance. Keep objective-conflict resolution and native lifecycle policy in the coordinator; link to that owner rather than duplicating it here.

### 3. Tighten evidence and completion reporting

In Establish a sufficient implementation contract, add one sentence requiring comparable baseline and final measurements when the outcome claims an optimization. Name relevant conditions, the decisive metric, and limitations; do not impose numerical acceptance on qualitative research or unrelated work.

The existing correction limits remain sufficient. The checkpoint should identify the unmet acceptance condition, evidence gained, and next causal action. A successful unchanged check is reused unless changed inputs or an unresolved concern justify rerunning it. No extra correction phase or verification loop is added.

In Terminal report, add a brief native-goal reporting instruction: after actual completion under the existing terminal criteria, report the host-provided completion usage when required for a budgeted goal. Identify unavailable usage honestly; do not substitute an estimate, null-as-zero, or a pre-completion reading for the completion result. Keep status-transition thresholds and pause rules governed by the current host rather than copying a dated tool schema into portable policy.

## Execution sequence

### Stage 1 — Reconcile inputs and evidence

Once execution is selected, recheck the actual checkout, branch, changes, package, target instructions, and required documents. Use a feature branch or existing isolated worktree as appropriate; preserve untracked research/plan inputs and unrelated work. Record the selected candidate in this document's checkpoint and the exact package bytes with each M9 observation.

Inspect the synchronization run's original native observations if available within authorized access. Look for actual read/create results, governing package, objective, host turns, completion result, authorized endpoint, and unfinished obligations. Map only supported observations to the existing M9 cases. If records are inaccessible or insufficient, record the gap and proceed with fresh qualification; successful delivery is not a substitute. Do not query or adopt Agent Ledger, copy private transcripts, or retroactively grant a blanket pass.

### Stage 2 — Make and review the focused instruction patch

Apply the three changes above in their canonical owners. Preserve explicit activation, ordinary goal-off behavior, compatible-goal reuse, conflict handling, one parent objective, dependency chronology, combined acceptance, selective resumption, and host budget/stop rules.

Self-review the complete candidate and obtain one consolidated independent source review for the proposed standard assurance. Supply the research, this plan, changed instructions, relevant M9 protocol, and actual diff including untracked inputs. Review source semantics and acceptance coverage; do not report proposed trials as executed. Batch verified findings into one correction and repeat only affected checks.

Keep the coordinator near its existing size and below the repository's roughly 300-line budget; keep the planning reference near 200 lines where practical. Remove redundant wording rather than moving duplicated policy into a new goal reference.

### Stage 3 — Qualify the actual native surface

Use the [existing M9 protocol](../tests/m9/README.md#native-qualification-protocol), disposable targets, and fresh native sessions. Explicit trial selection is needed before creating goals or exercising lifecycle controls; any budget or external effect must be within the trial's authority. Record declarations separately from calls, retain the historical preflight, and append new dated observations.

Establish Case B's supported controls before dependent goal-on cases. At least one successful goal-on case must cross an actual host-turn boundary. Reuse R3/R5 fixtures where adequate, with only small necessary adaptations. The cases remain one protocol rather than a new harness or automated runtime.

| Existing coverage | Focused addition or observation |
| --- | --- |
| A / B | Review recommendation examples; observe no implicit activation or required probes in goal-off work, explicit selection, compatible-goal retention, conflict preservation, and bounded planning/review endpoints |
| B / C | Observe the real package and contract loading path, native activation, meaningful continuation across host turns, and completion only after required checks/review/correction |
| D / E | Verify plan dependency boundaries before dependent edits and parent acceptance when individual outcomes pass |
| F | Exercise supported explicit pause/resume controls; separately observe commands, delegates, and external effects; reconcile changed plan/source inputs. Add compaction recovery only where supported and record it separately |
| G | Preserve existing hidden-command-effect coverage; inspect wrappers without performing forbidden installation/environment creation |
| H | Stop affected work immediately, continue useful independent work, then obey the actual host's blocked eligibility. No artificial turns or meaningless tool calls |
| I | Preserve one parent objective through normal phases and checkpoint updates; distinguish material requirement changes from ordinary progress |
| J | Use only an explicitly authorized, genuinely exposed limit; preserve unfinished acceptance and accounting. Separately observe successful budgeted completion reporting if authorized and supported |

Mark each observation passed, failed, unavailable, or not run; explain unsupported surfaces without treating them as passes. Reuse valid earlier evidence only when its candidate, host, and scope apply. Correct observed causes and repeat affected cases; do not repeat every historical suite after an unrelated wording change.

### Stage 4 — Evaluate adoption and update discoverability

After bounded evidence supports the intended surface, choose one naturally useful authorized real task. Do not manufacture a long task to exhaust a budget or count synthetic cases, child outcomes, or resumed turns as separate representative runs.

Record accepted-result time, unnecessary continuation prompts, necessary owner decisions, operator interventions, repeated work after resume, exposed token usage, correction passes, escaped findings, and authority/acceptance violations. Separate external waits and unavailable metrics. Compare with suitable goal-off evidence, holding task class, package, host, model/effort, and endpoint comparable where practical; disclose differences and avoid a controlled-comparison claim from unlike tasks.

Use the roadmap's existing retain/revise/remove criteria. Add a README invocation example only for a loading/control sequence actually qualified on the named host surface, with its scope and evidence link. Update M9 adoption status only after required native and representative evidence exists. Keep R7/R8 thresholds and their separate authorization boundaries intact.

## Validation and completion criteria

Source validation is the normal short inner loop. Run `git diff --check`, inspect local links/anchors, fences and tables, and scan changed content for private or machine-specific material. Because the two planning documents are untracked initially, inspect them explicitly; tracked diff checks alone omit them. Use available tools or a one-off check, with no new dependency or persistent validator solely for this change.

If a disposable R3 fixture is used, run its contract's checks from that target, including `python3 -B -m unittest discover -v` when applicable. A green renderer test does not prove native goal activation or continuation. Synchronization adapter tests, full recovery/package qualification, and live Drive operations are unrelated to this instruction patch unless a later change touches those boundaries.

| Boundary | Required evidence |
| --- | --- |
| Instruction refinement complete | Focused owner changes exist; selection, checkpoint, completion, and preserved safeguards pass source review and mechanical checks; remaining native gaps are explicit |
| Native surface qualified | Candidate/host-specific observations cover the claimed behavior, with actual controls, a real continuation boundary, and all unsupported/unrun portions labeled |
| M9 adoption disposition complete | Required bounded evidence plus a representative real goal-on outcome and justified comparison support retain/revise/remove; roadmap and invocation claims match the evidence |

Failure or unavailable required evidence leaves that boundary incomplete. A document, passing source check, installed package, or goal status alone cannot establish a later boundary. Publishing, installation, live activation, merge, and synchronization remain separate actions when selected by the user.

## Rollback and remaining decisions

There is no data migration, new dependency, configuration change, or installation in the proposed source patch. For a rejected local candidate, undo only the refinement's owned hunks after checking for subsequent work. Preserve the research, this plan, and truthful trial observations. If an observation caused a published invocation claim, correct the claim alongside the evidence; any installed-package rollback requires separate authority and its own package verification.

The method does not need an additional product or architecture decision. Local implementation has reached its selected endpoint, and the user has authorized delivery while deferring further qualification. Native qualification still needs an actual trial host/loading path, a suitable representative task, and any budget or external-effect authority required by that task. Resolve those when selecting qualification rather than inventing assumptions now.

## Implementation checkpoint (2026-10-09)

- **Candidate:** instruction/document changes authored on `docs/goal-gpt6-research`, based on `596fa519d44e9c901e0dbffdae14bddbfe018909`; the research and this plan are included in the delivery candidate.
- **Implemented:** coordinator selection/completion guidance, planning measurement/example/checkpoint guidance, and focused M9 case/control observations.
- **Checks/review:** skill metadata validation and scoped Markdown links/anchors, tables, fences, whitespace, and private-marker checks passed. One consolidated independent source review found no material findings; reviewed operational hashes match M9. Original research and unrelated package/docs inputs were preserved.
- **PR correction:** a later GitHub review identified repeated resumption policy in planning. Checkpoint/source validation stays there; lifecycle behavior is delegated to the coordinator. M9 records the corrected planning hash separately from the earlier goal-off package; focused source checks cover this correction without upgrading behavioral evidence.
- **Goal-off refresh:** the revised package completed the bounded R3 local fixture with lean self-review. Five focused tests and 14 parent API/CLI boundary checks passed; unrelated tracked/untracked files, baseline HEAD, and inputs were preserved. Configured native agents reported no goal-tool calls. Detailed evidence and limitations are in M9.
- **Synchronization audit:** the plan and available project records were inspected, but original native control/turn evidence was not recovered from the inspected local session locations. No qualification status was upgraded.
- **Reached endpoint:** verified local instruction candidate on the existing branch; implementation and source review are complete, with bounded goal-off evidence.
- **Deferred by the user:** further qualification, including explicit native goal-on trial selection, remaining selection/control cases, representative comparison, and adoption decision. README invocation claims and roadmap disposition remain unchanged.
- **Authorized delivery:** commit, push, create and review a PR, merge, synchronize local `main`, and remove this feature branch locally and remotely. Git and the PR record own the observed delivery facts; no qualification pass or installation is implied.
- **Next action if qualification is selected:** establish the actual host/loading path and Case B controls before dependent goal-on trials; supply a budget or external-effect authority only when required and explicitly selected.
- **Effects at this implementation checkpoint:** local instruction/document edits, one read-only goal inspection, and an inspected disposable goal-off target removed after verification; no goal mutation or package installation. Remote delivery follows under the authorization above.

Keep the latest implementation checkpoint here. Detailed trial evidence stays in M9 and adoption status stays in the roadmap; do not duplicate them as a second progress ledger.
