---
name: afr
description: Plan, implement, review, or deliver a direct software change when the user explicitly selects AFR. Reuse a sufficient contract and carry the verified candidate to the authorized endpoint. Ordinary coding requests or discussion of AFR do not activate it; automatic umbrella execution is not yet supported.
---

# AFR — direct work and delivery

## Available capability

R4 provides discovery, bounded research, planning, direct implementation, verification, proportional review/correction, and authorized PR delivery through merge and local synchronization. Load [planning](references/planning.md), [work](references/work.md), [review](references/review.md), and [delivery](references/delivery.md) only for the requested phases. The host supplies tools, monitoring, and independent agents when available; a reference is not itself a running reviewer or watcher.

Deployment and automatic umbrella execution remain unavailable. Do not substitute legacy AFR, another workflow, or a placeholder for a missing capability. If a request includes an unsupported endpoint, perform only a useful authorized supported portion and keep the unfulfilled endpoint explicit. For an umbrella, return planning unless the user selects one bounded outcome for direct work; do not automatically execute its siblings. Building this skill in its authoring repository is separate from running it on a target.

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
| `umbrella` | Several independently deliverable outcomes with meaningful dependencies | A parent contract with outcome acceptance, shared choices/invariants, dependency boundaries, and combined acceptance |
| `spike` | A bounded investigation is needed before implementation can be specified honestly | The question, observed evidence, conclusion or remaining uncertainty, and recommended next step |
| `stop` | A user stop, unsafe/prohibited work, missing authority, unresolved required decision, or inaccessible indispensable context prevents further work | The specific boundary and smallest action that would permit resumption, if applicable |

A multi-commit feature does not automatically need an umbrella. Research cannot decide an unassigned product/security policy or authorize its proposed implementation. A useful completed spike is a valid result even when no implementation-ready contract follows.

If a decision blocks only one part of planning, continue independent safe analysis where useful and keep the dependent portion visibly unresolved. Do not turn lack of a future execution phase into a reason to invent work, or repeatedly replan a contract that is already sufficient.

## Direct sequence

Stop at the requested phase: a sufficient plan is not permission to implement; review findings are not permission to fix. For authorized direct implementation with a sufficient contract, load the complete [work method](references/work.md). Continue through implementation and conformance checks without asking for routine approval already given.

Assess the resulting candidate through the complete [review method](references/review.md), using the selected assurance and observed risks. Lean work can use focused self-review; standard work normally uses one consolidated independent reviewer. Respect required review and host availability rather than simulating independence. Review returns findings, dispositions, coverage gaps, and the reviewed candidate identity.

When correction is authorized, accepted findings go through the same work and review methods. Continue the bounded correction/recheck described by review; do not stop merely because implementation or a test run finished. If missing authority, required review, or required evidence prevents completion, preserve the candidate and report that specific gap. Do not silently downgrade assurance to finish.

For an authorized publication, PR, monitoring, merge, or synchronization endpoint, load the complete [delivery method](references/delivery.md). An existing candidate or PR can enter there without repeating valid implementation or planning. PR feedback uses the same review and authorized correction methods; after a pushed fix, return to delivery monitoring for the new head. Continue until the requested boundary is observed or a specific blocker, current stop, or monitoring limit requires a handoff. An intermediate push or completed review is not completion of an authorized merge request.

Finish at the requested boundary after conformance and required assurance are established. A local-only request stops at the candidate/branch; PR creation does not imply merge or cleanup authority. Leave further effects unperformed unless authorized and supported. A requested unsupported endpoint remains partial, not complete.

## Stop and resumption

Honor current user steering before consequential actions and after delegated results, using native host controls. A late result cannot restore authority after a stop. If an already-started external action has an uncertain result, observe its state before considering a retry; do not infer success from a timeout.

On an explicit resume, reconcile current intent, the existing authoritative plan, source and workspace changes, relevant PR/check observations if any, and available session context. Resolve existing artifacts, branches, and worktrees before creating replacements. Associate evidence with the actual candidate/base, requirements, and prerequisites; for uncommitted work include the relevant diff and untracked inputs, not HEAD alone. Refresh only decisions, work, checks, or review invalidated by changed inputs. A summary alone is not current evidence.

Resume at the missing obligation, not by repeating completed implementation or external writes. A remotely merged PR with incomplete required local synchronization resumes at synchronization through the delivery method. Automatic umbrella continuation remains unavailable. Do not create a separate state record merely to resume.

## Terminal report

Prefer source inspection when it answers the question. Executing or importing target code can create caches or other effects even during a diagnostic probe; use non-writing options or isolation when a probe is justified. Before reporting effects, reobserve the target's changes, including untracked files, against the initial observation. Account for incidental artifacts and any authorized cleanup; do not claim that no files were written merely because source files are unchanged. Retain artifacts whose ownership or cleanup authority is uncertain.

Give a concise result appropriate to the route, not a mandatory template:

- route and reason; assurance and consequential risks;
- target/workspace and skill/host identity, with uncertainty where relevant;
- the authoritative contract and required companion paths, or the spike evidence/conclusion;
- material decisions, acceptance and planned evidence, remaining discretion or blockers;
- candidate/base and actual changes; requirement evidence, check outcomes and gaps; review actually performed and finding dispositions, separate from proposed checks or unavailable review;
- when delivery was requested, exact PR/head and separately observed publication, review/check readiness, remote merge, local synchronization, and authorized cleanup facts or gaps;
- the user's requested endpoint, what was reached, and remaining unsupported or unauthorized effects.

Call planning ready only when the planning method's sufficiency judgment is satisfied. Call a candidate complete only when material acceptance, required checks/review, and temporary-effect disposition are satisfied for that candidate; a delivery request also requires observation of its authorized endpoint and any required synchronization/bookkeeping. For a spike, report research completion and uncertainty honestly; for a stop, identify the boundary. Never infer implementation, test success, independent review, delivery, host parity, or the user's full outcome from a plan or intermediate progress. Do not produce status files solely for reporting.
