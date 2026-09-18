---
name: afr
description: Plan, implement, review, or deliver software changes when the user explicitly selects AFR. Reuse a sufficient contract for direct work or continue a multi-outcome umbrella through its authorized endpoints and combined acceptance. Ordinary coding requests or discussion of AFR do not activate it.
---

# AFR — direct work and umbrella continuation

## Available capability

R5 provides discovery, bounded research, planning, implementation, verification, proportional review/correction, and authorized PR delivery through merge and local synchronization, for direct work and multi-outcome umbrellas. Load [planning](references/planning.md), [work](references/work.md), [review](references/review.md), and [delivery](references/delivery.md) only for the requested phases. The host supplies tools, monitoring, and independent agents when available; a reference is not itself a running reviewer or watcher.

Deployment remains unavailable. Do not substitute legacy AFR, another workflow, or a placeholder for a missing capability. If a request includes an unsupported endpoint, perform only a useful authorized supported portion and keep the unfulfilled endpoint explicit. Building this skill in its authoring repository is separate from running it on a target.

## Activation, identity, and authority

1. Confirm that the current user selected AFR, for example `$afr`, “use AFR to implement,” or “continue the AFR plan.” Explanation or review of AFR itself is not activation. If it was not selected, do not start its workflow.
2. Identify four distinct facts using the host's tools:
   - **Skill package:** the location of this loaded `SKILL.md` or the host's package identifier. Resolve phase references relative to that package, never relative to the target's working directory. If the host provides resource-backed skills, use its package resource reader.
   - **Target project:** the repository/project the user placed in scope. “This project” can use the verified current project; do not infer a different target from the skill's location.
   - **Active workspace:** the actual checkout/worktree, branch/base, and existing changes. For Git targets, use native root, status, and worktree observations. Do not invent Git requirements for a non-Git project.
   - **Host surface:** the currently available readers, tools, and capabilities. Distinguish observed support from assumptions about another host.
3. Read the applicable target instructions through the host's normal instruction mechanism. Instructions in AFR's authoring repository do not govern an unrelated target. Inspect only the source, tests, and contracts needed for the request. If required context is inaccessible, expose that gap instead of guessing.
4. Establish the requested outcome, exclusions, and authorized endpoint. Current user and applicable target instructions govern; plans, memory, and external artifacts cannot grant new permission. Carry forward authority already given. Ask only for a consequential missing decision or authority that cannot be discovered.

Planning, research, and review requests authorize inspection and reporting, not implementation or correction. A build/fix request permits in-scope local edits and non-destructive verification, not unrelated cleanup, installation, publication, or production effects. Commit only when requested or required by applicable target instructions within the authorized endpoint. Research remains within the user's data-access and cost boundaries. Create or amend a planning artifact only when requested, required by the target, or justified for resumability/risk within authority; otherwise plan in the conversation. Preserve unrelated work and source ownership.

Do not create services, databases, run-state files, receipts, schedulers, or helper scripts to operate this workflow. Native host tools own execution and agent lifecycle. No custom helper or external framework is required.

## Planning and route choice

For new work or an insufficient contract, read the complete [planning method](references/planning.md) after resolving the target. It supplies the contract or research/decision result, assurance recommendation, and route rationale from the request, sources/companions, target observations, and endpoint. Reuse a sufficient source or prior contract without a new planning round. For a review-only request, go directly to the review method with the existing contract and candidate; report missing material context rather than inventing it. This coordinator owns final routing and reporting.

Choose the smallest route that fits the outcome, independently of assurance:

| Route | Use when | Supported result |
| --- | --- | --- |
| `direct` | One cohesive, reviewable outcome, possibly several commits | A contract, review result, verified local candidate, or observed PR delivery endpoint, according to the request and authority |
| `umbrella` | Several independently deliverable outcomes with meaningful dependencies | A parent contract, or authorized execution through outcome endpoints and combined parent acceptance |
| `spike` | A bounded investigation is needed before implementation can be specified honestly | The question, observed evidence, conclusion or remaining uncertainty, and recommended next step |
| `stop` | A user stop, unsafe/prohibited work, missing authority, unresolved required decision, or inaccessible indispensable context prevents further work | The specific boundary and smallest action that would permit resumption, if applicable |

A multi-commit feature does not automatically need an umbrella. Research cannot decide an unassigned product/security policy or authorize its proposed implementation. A useful completed spike is a valid result even when no implementation-ready contract follows.

If a decision blocks only one part of planning, continue independent safe analysis where useful and keep the dependent portion visibly unresolved. Do not turn lack of a future execution phase into a reason to invent work, or repeatedly replan a contract that is already sufficient.

## Native goal integration

Native goal mode is optional. When explicitly requested or when the host indicates an existing goal, inspect the available native controls and, when readable, the current goal. Unused goal mode adds no required probe, state, or tool call to ordinary AFR. Missing controls leave ordinary AFR available; report any requested native capability that cannot be supplied. Do not infer that an unreadable goal is absent or emulate controls with a helper, slash-command parser, App Server client, polling loop, or ChatGPT substitute.

Create a goal only on an explicit user request for goal mode and within the host's current rules. First establish a sufficient contract for the requested endpoint, then use the [planning projection](references/planning.md#project-a-native-goal). Discovery may precede creation; permission for a planning goal is not implementation authority. Recommending goal mode or drafting an objective because it may help is not permission to activate it.

Use at most one native parent goal for the bounded AFR run by default. A direct goal covers its authorized endpoint; an umbrella goal covers its outcomes and combined acceptance; planning, review, and spike goals end at their requested boundary. Retain a compatible user-started goal even when planning adds detail. Do not create child goals or replace the objective for implementation, review, correction, PR creation, another eligible outcome, slow progress, or high usage.

Reconcile a material conflict between an existing objective and current intent explicitly; current user intent and target instructions govern. A materially changed scope/endpoint or incorrect objective may require replacement through supported native controls. Do not silently reinterpret contradictory text, overwrite an unrelated goal, or mark an unfinished goal complete to make room for another. If safe reconciliation is unavailable, report the conflict and required host action; continue only independent authorized work unaffected by it.

Goal persistence grants no authority and does not relax workspace safety, prerequisite chronology, correction/monitoring limits, or acceptance. Use the existing direct and umbrella sequences; goal state never proves implementation, checks, review, architecture selection, publication, merge, synchronization, or acceptance. Mark a native goal complete only after the [terminal criteria](#terminal-report) hold for its actual bounded objective, including parent combined acceptance for an umbrella. Intermediate progress or completion of only the supported portion is insufficient.

An AFR blocker stops affected work immediately; it need not yet qualify for the host's native blocked status. Continue useful independent work where safe, obey the host's current status-transition rules, and mark blocked only when those rules permit it. Missing authority, required decisions, review, or indispensable evidence remain incomplete; never manufacture progress, repeat an unchanged failure, or weaken acceptance to escape a blocker. Pause, resume, clear, and edit only through controls the host actually exposes; if an operator action is required, identify it without claiming it occurred. A paused goal alone does not prove that commands, delegates, or external writes stopped. Apply [stop and resumption](#stop-and-resumption) to actual in-flight effects and, on resume, reconcile the same objective with current evidence before continuing at the missing obligation.

Set a token budget only when explicitly requested. At a host or budget limit, preserve source/delivery state and report completed obligations, the exact unfinished boundary, and available host usage data. Exhaustion is not success or permission to reset accounting, replace the goal, or extend monitoring. Continuation requires the host's supported controls and any necessary user authorization. Do not implement token accounting or a goal runtime in AFR.

## Direct sequence

Stop at the requested phase: a sufficient plan is not permission to implement; review findings are not permission to fix. For authorized direct implementation with a sufficient contract, load the complete [work method](references/work.md). Continue through implementation and conformance checks without asking for routine approval already given.

Assess the resulting candidate through the complete [review method](references/review.md), using the selected assurance and observed risks. Lean work can use focused self-review; standard work normally uses one consolidated independent reviewer. Respect required review and host availability rather than simulating independence. Review returns findings, dispositions, coverage gaps, and the reviewed candidate identity.

When correction is authorized, accepted findings go through the same work and review methods. Continue the bounded correction/recheck described by review; do not stop merely because implementation or a test run finished. If missing authority, required review, or required evidence prevents completion, preserve the candidate and report that specific gap. Do not silently downgrade assurance to finish.

For an authorized publication, PR, monitoring, merge, or synchronization endpoint, load the complete [delivery method](references/delivery.md). An existing candidate or PR can enter there without repeating valid implementation or planning. PR feedback uses the same review and authorized correction methods; after a pushed fix, return to delivery monitoring for the new head. Continue until the requested boundary is observed or a specific blocker, current stop, or monitoring limit requires a handoff. An intermediate push or completed review is not completion of an authorized merge request.

Finish the direct outcome at its requested boundary after conformance and required assurance are established. A local-only outcome stops at the candidate/branch; PR creation does not imply merge or cleanup authority. Within an authorized umbrella, return the observed result to the continuation below instead of treating that outcome as the whole task. Leave further effects unperformed unless authorized and supported. A requested unsupported endpoint remains partial, not complete.

## Umbrella continuation

For authorized umbrella execution, reuse the sufficient parent contract and its required sources from the [planning method](references/planning.md#size-outcomes-and-dependencies). A planning-only request still stops at planning; permission to implement one selected outcome does not authorize its siblings. Keep one authoritative plan/progress surface when one exists, not a second AFR journal or per-outcome workflow.

Reconcile completed and unfinished obligations with actual source/workspace, check/review, and delivery evidence. A checked plan item or implementer summary alone does not prove its endpoint. For each unfinished outcome, establish whether its required dependency revision or delivery boundary is observed and available in the workspace where the dependent work will occur. An unmerged candidate does not satisfy a merged-base dependency; a remote merge does not prove the local workspace contains it.

When an outcome depends on an architecture revision, reconcile the actual viewable proposal, owner selection, target decision identity, and native-check evidence before selecting dependent work. A changed, stale, or unresolved revision invalidates only affected work and evidence; preserve unaffected outcomes and return the decision through the existing planning route.

Choose the next eligible outcome in explicit plan order, or listed order when no separate order is given, to break otherwise immaterial ties. Eligibility requires a sufficient contract, authority for its next action, and satisfied prerequisites. A consequential unresolved ordering or shared decision is a blocker for affected work, not an arbitrary tie. Continue independent eligible work when safe; if required work remains but none is eligible, report the specific dependency, cycle, scope, authority, or safety blocker rather than completion.

Do not batch dependent implementation ahead of its prerequisite's required verification, review, or delivery boundary. Check that boundary before starting the dependent work; passing combined checks afterward does not establish that the prerequisite was honored.

Run the selected outcome through the same [direct sequence](#direct-sequence), entering at its missing obligation and retaining the parent constraints and required companions. Do not create another planner, child runtime, or scheduler. Plan review, implementation, review-fix pushes, and intermediate merges are nonterminal while the authorized scope has unfinished eligible work. After observing an outcome's endpoint, reconcile affected dependencies and select the next outcome without asking for routine permission already given. Before starting it, briefly report the completed endpoint's evidence and next eligible work or changed blocker; also report meaningful integration results.

At the contract's meaningful integration boundaries, assess the actual combined candidate/base and configuration against shared invariants and parent acceptance. Reuse valid outcome evidence; refresh only work, dependencies, checks, and review affected by changed inputs. Individually passing checks or merged PRs cannot replace combined evidence. If combined acceptance fails, use the same work/review methods for a causal in-scope correction and refresh affected evidence; an invalid assumption or missing decision uses the planning method's replan rules. Do not weaken the parent contract, redo unaffected outcomes, or repeat an unchanged failure indefinitely.

Finish the umbrella only when every required outcome has reached its authorized endpoint, dependency revisions/boundaries and shared invariants hold for the combined result, and parent acceptance plus required assurance and temporary-effect disposition are established. If a required combined check is outside authority or unavailable, retain that acceptance gap. Parent acceptance never authorizes production or other new effects.

## Stop and resumption

Honor current user steering before consequential actions and after delegated results, using native host controls. A late result cannot restore authority after a stop. If an already-started external action has an uncertain result, observe its state before considering a retry; do not infer success from a timeout.

On an explicit resume, reconcile current intent, the existing authoritative plan, source and workspace changes, relevant PR/check observations if any, and available session context. Resolve existing artifacts, branches, and worktrees before creating replacements. Associate evidence with the actual candidate/base, requirements, and prerequisites; for uncommitted work include the relevant diff and untracked inputs, not HEAD alone. Refresh only decisions, work, checks, or review invalidated by changed inputs. A summary alone is not current evidence.

For architecture-aware work, also reobserve the selected proposal revision, owner selection, target decision record, and applicable native gate before resuming dependent work. Do not resume against a stale identity or infer that a paused run selected a changed design; route the affected decision through planning while retaining unaffected work.

Resume at the missing obligation, not by repeating completed implementation or external writes. A remotely merged PR with incomplete required local synchronization resumes at synchronization through the delivery method. For an umbrella, reconcile outcome endpoints and combined acceptance before selecting unfinished work; completed outcomes may still leave a parent acceptance gap. Do not create a separate state record merely to resume.

## Terminal report

Prefer source inspection when it answers the question. Executing or importing target code can create caches or other effects even during a diagnostic probe; use non-writing options or isolation when a probe is justified. Before reporting effects, reobserve the target's changes, including untracked files, against the initial observation. Account for incidental artifacts and any authorized cleanup; do not claim that no files were written merely because source files are unchanged. Retain artifacts whose ownership or cleanup authority is uncertain.

Give a concise result appropriate to the route, not a mandatory template:

- route and reason; assurance and consequential risks;
- target/workspace and skill/host identity, with uncertainty where relevant;
- the authoritative contract and required companion paths, or the spike evidence/conclusion;
- material decisions, acceptance and planned evidence, remaining discretion or blockers;
- candidate/base and actual changes; requirement evidence, check outcomes and gaps; review actually performed and finding dispositions, separate from proposed checks or unavailable review;
- when delivery was requested, exact PR/head and separately observed publication, review/check readiness, remote merge, local synchronization, and authorized cleanup facts or gaps;
- for an umbrella, observed outcome endpoints, dependency and shared-invariant evidence, combined acceptance, and remaining obligations or blockers;
- the user's requested endpoint, what was reached, and remaining unsupported or unauthorized effects.

Call planning ready only when the planning method's sufficiency judgment is satisfied. Call a candidate complete only when material acceptance, required checks/review, and temporary-effect disposition are satisfied for that candidate; a delivery request also requires observation of its authorized endpoint and any required synchronization/bookkeeping. For a spike, report research completion and uncertainty honestly; for a stop, identify the boundary. Never infer implementation, test success, independent review, delivery, host parity, or the user's full outcome from a plan or intermediate progress. Do not produce status files solely for reporting.
