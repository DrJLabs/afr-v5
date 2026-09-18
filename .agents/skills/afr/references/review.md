# Review and bounded correction

Use when dispatched by the AFR coordinator for a local candidate, PR feedback, or a review-only request. Return evidence-backed findings, dispositions, coverage, and candidate identity. The coordinator owns authority, sequencing, stop/resume, and final completion; this method does not authorize edits or remote delivery.

## Select and ground the review

Apply the assurance selected by the [planning method](planning.md#planning-assurance-and-self-review), raising coverage for observed risks within authority. If a review-only request has no prior assurance selection, use those criteria to choose and state the lowest adequate level from the actual consequences; do not require a new plan just to select it. Lean changes may use focused self-review. Standard work normally uses one consolidated independent reviewer; protected work adds the specialist coverage warranted by actual consequences, not a stack of simulated personas. Target-required checks and review remain binding.

An independent review must actually be performed by a separate available reviewer. For an explicitly requested review of someone else's candidate, the current agent can be that reviewer. An implementer rereading its own work is self-review, not independence. If required independent or specialist review is unavailable, report the gap; do not silently downgrade assurance or pretend a second role performed it. Useful self-review can still expose issues without satisfying that requirement.

Give the reviewer the authoritative requirements and indispensable companions, target instructions, exact candidate/base or working-tree diff, relevant checks and limitations, and the review-only boundary. An implementer summary is context, not the source of truth. Review may inspect source and run safe relevant checks but must not edit the candidate unless correction is separately authorized. Distinguish preexisting changes from this outcome.

## Assess the actual outcome

Review conformance, source defects, compatibility, scope, architecture revision, risk-specific safeguards, and verification effectiveness together. Inspect changed paths and relevant consumers, not just a summary or passing test list. For material behavior ask: **what realistic failure at the consumer/integration boundary should make this evidence fail?** Check that callers adopt the changed behavior, intended checks actually ran, and assertions could detect the regression.

For architectural changes, verify the proposal is viewable, the selected owner and exact revision are recorded by the target's process, and the implementation matches the declared boundaries. Compare intended design with observed source structure and behavioral evidence without treating any one as a substitute. Assess cumulative complexity, source-coverage changes, new or removed exceptions, and edits to controls or check configuration. A material departure or changed revision invalidates affected evidence and returns to planning; it is not an automatic rebaseline or approval.

A green suite can leave acceptance unmet. Demonstrate a claimed gap with the requirement, relevant code/path, and a concrete failure or missing observation. Do not claim a verification defect without inspecting the available evidence. Zero material findings is a valid result; neither a finding quota nor speculative polish improves acceptance.

Record findings compactly with impact/severity, location, requirement or invariant, evidence, and proposed disposition. Independently verify consequential reviewer claims against the source and candidate before correcting them. Deduplicate repeated reports of the same manifestation while retaining distinct affected locations or failures. Accept valid in-scope findings; reject with a reason, mark duplicates, or identify genuinely out-of-scope follow-up. An unresolved material acceptance failure cannot be relabeled follow-up to declare success.

## Correct only within authority

A review-only request returns findings without edits. When correction is authorized, distinguish:

| Evidence | Response |
| --- | --- |
| Implementation violates a valid requirement | Correct the causal defect through the work method; refresh affected evidence |
| A technical assumption is invalid | Revise advisory tactics within discretion; return an affected binding decision for resolution |
| Product/security policy is missing or contradictory | Identify the decision owner and pause dependent correction; do not invent policy |
| A requirement change is authorized | Update its authoritative source through the permitted path and reassess affected acceptance |

Batch accepted findings into one correction pass by default. Preserve valid work instead of reverting and regenerating the whole outcome. A further pass requires observed progress or elevated risk; repeated unchanged failure returns a stop/replan recommendation. Out-of-scope findings do not grant authority for unrelated changes.

After correction, inspect the resulting diff and rerun checks invalidated by the fix plus required integration checks. Renew independent review when the changed behavior, risk, target policy, or finding requires it; do not repeat every review or unchanged passing check by default. Earlier review does not automatically cover a materially changed candidate. Report the final reviewed identity, each disposition, actual rechecks, remaining material findings, and unavailable evidence to the coordinator. A corrected line or a passing command alone is not proof of acceptance.
