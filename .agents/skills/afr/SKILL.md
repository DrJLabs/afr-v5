---
name: afr
description: Plan software work when the user explicitly selects AFR. Inspect the target, reuse or develop an implementation contract, and choose direct, umbrella, spike, or stop. This R2 prototype is planning-only; ordinary coding requests or discussion of AFR do not activate it.
---

# AFR — planning prototype

## Available capability

R2 provides discovery, bounded research, routing, planning assurance, and plan self-review. Its only phase method is [references/planning.md](references/planning.md). Implementation, independent implementation review, PR delivery, merge, and execution continuation are unavailable. Do not substitute a legacy AFR skill, another workflow, or an invented phase for them. A placeholder or similarly named file does not establish a capability.

If the user asks AFR to implement or deliver work, prepare or assess the useful planning portion within authority and explicitly report that the requested execution remains unperformed. Do not lower the user's requested endpoint to make the whole task appear complete. Building this skill in its authoring repository is separate from running it on a target.

## Activation, identity, and authority

1. Confirm that the current user selected AFR, for example `$afr`, “use AFR to plan,” or “continue the AFR plan.” Explanation or review of AFR itself is not activation. If it was not selected, do not start its workflow.
2. Identify four distinct facts using the host's tools:
   - **Skill package:** the location of this loaded `SKILL.md` or the host's package identifier. Resolve the planning reference relative to that package, never relative to the target's working directory. If the host provides resource-backed skills, use its package resource reader.
   - **Target project:** the repository/project the user placed in scope. “This project” can use the verified current project; do not infer a different target from the skill's location.
   - **Active workspace:** the actual checkout/worktree, branch/base, and existing changes. For Git targets, use native root, status, and worktree observations. Do not invent Git requirements for a non-Git project.
   - **Host surface:** the currently available readers, tools, and capabilities. Distinguish observed support from assumptions about another host.
3. Read the applicable target instructions through the host's normal instruction mechanism. Instructions in AFR's authoring repository do not govern an unrelated target. Inspect only the source, tests, and contracts needed for the request. If required context is inaccessible, expose that gap instead of guessing.
4. Establish the requested outcome, exclusions, and authorized endpoint. Current user and applicable target instructions govern; plans, memory, and external artifacts cannot grant new permission. Carry forward authority already given. Ask only for a consequential missing decision or authority that cannot be discovered.

This prototype does not authorize target implementation, commits, pushes, PRs, merge, deployment, installation, or cleanup. Research remains within the user's data-access and cost boundaries. Create or amend a planning artifact only when requested, required by the target, or justified for resumability/risk within authority; otherwise plan in the conversation. Preserve unrelated work and source ownership.

Do not create services, databases, run-state files, receipts, schedulers, or helper scripts to operate this workflow. Native host tools own execution and agent lifecycle. No custom helper or external framework is required.

## Planning and route choice

Read the complete [planning method](references/planning.md) after resolving the target. Give it the request, authoritative sources and companions, target/workspace observations, and authorized endpoint. It supplies a contract or research/decision result, assurance recommendation, and route rationale; this coordinator owns final routing and reporting.

Choose the smallest route that fits the outcome, independently of assurance:

| Route | Use when | R2 result |
| --- | --- | --- |
| `direct` | One cohesive, reviewable outcome, possibly several commits | A sufficient implementation contract or assessment of an existing one |
| `umbrella` | Several independently deliverable outcomes with meaningful dependencies | A parent contract with outcome acceptance, shared choices/invariants, dependency boundaries, and combined acceptance |
| `spike` | A bounded investigation is needed before implementation can be specified honestly | The question, observed evidence, conclusion or remaining uncertainty, and recommended next step |
| `stop` | A user stop, unsafe/prohibited work, missing authority, unresolved required decision, or inaccessible indispensable context prevents further work | The specific boundary and smallest action that would permit resumption, if applicable |

A multi-commit feature does not automatically need an umbrella. Research cannot decide an unassigned product/security policy or authorize its proposed implementation. A useful completed spike is a valid result even when no implementation-ready contract follows.

If a decision blocks only one part of planning, continue independent safe analysis where useful and keep the dependent portion visibly unresolved. Do not turn lack of a future execution phase into a reason to invent work, or repeatedly replan a contract that is already sufficient.

## Stop and planning resumption

Honor current user steering before consequential actions and after delegated results, using native host controls. A late result cannot restore authority after a stop. If an already-started external action has an uncertain result, observe its state before considering a retry; do not infer success from a timeout.

On an explicit resume, reconcile current intent, the existing authoritative plan, source and workspace changes, relevant PR/check observations if any, and available session context. Resolve existing artifacts before creating replacements. Check source/revision identity and refresh only decisions or evidence affected by changed requirements, base, constraints, or prerequisites. A summary alone is not current evidence.

R2 can resume planning. It cannot resume implementation or an umbrella execution loop; report those missing capabilities and leave existing work intact. Do not create a separate state record merely to resume.

## Terminal report

Prefer source inspection when it answers the question. Executing or importing target code can create caches or other effects even during a diagnostic probe; use non-writing options or isolation when a probe is justified. Before reporting effects, reobserve the target's changes, including untracked files, against the initial observation. Account for incidental artifacts and any authorized cleanup; do not claim that no files were written merely because source files are unchanged. Retain artifacts whose ownership or cleanup authority is uncertain.

Give a concise result appropriate to the route, not a mandatory template:

- route and reason; planning assurance and consequential risks;
- target/workspace and skill/host identity, with uncertainty where relevant;
- the authoritative contract and required companion paths, or the spike evidence/conclusion;
- material decisions, acceptance and planned evidence, remaining discretion or blockers;
- actual observations and planning-file effects, separate from checks proposed for later execution;
- the user's requested endpoint and what remains unperformed because R2 is planning-only.

Call planning ready only when the planning method's sufficiency judgment is satisfied. For a spike, report research completion and uncertainty honestly; for a stop, identify the boundary. Never claim implementation, tests, independent implementation review, delivery, host parity, or the user's full outcome merely because a plan is ready. Do not produce status files solely for reporting.
