# R1 donor inventory and extraction decisions

**Status:** analysis complete; no donor code ported and no v5 behavior qualification performed.

R1 inspected the mapped sources in `DrJLabs/afr` as immutable Git objects. The [v1 architecture](architecture.md) records the original design; [architecture v2](architecture-v2.md) records the first spec-driven reconciliation; [architecture v3](architecture-v3.md) is current. The [roadmap](roadmap.md) controls subsequent delivery. This file is historical evidence and evaluation design; it is not loaded as a runtime workflow.

## 1. Evidence and coverage

The original behavior has precedence, followed by the first modular family and native-family design. Later sources supply focused safeguards and failure cases. Newer state machinery does not override a simpler design by age alone.

All 23 concrete primary file versions in the original/family/design/mature/helper groups below were read completely. The late skill-era group was inspected selectively for review, PR, workspace, and concurrency behavior. Supporting references and test excerpts were followed only where they explain a decision or scenario. Two independent readers covered the modular families and helper/failure sources; the author read the original/design sources, integrated the results, and spot-checked consequential delivery and correction evidence.

| Short revision | Full commit in `DrJLabs/afr` | Evidence type and use |
| --- | --- | --- |
| `3a0f5bc7` | `3a0f5bc7d32705556e098ae8f2850253e71d2ad1` | Original skill instructions: outcome loop and continuation |
| `8c0d80d3` | `8c0d80d3ea362df61db494e8a6f68b9c80429777` | First complete modular family: responsibility boundaries |
| `671d7361` | `671d736186d60ef72d53928512f7c2d29d357250` | Design proposal: efficiency goals and native skill methods; targets are not measured results |
| `f3c34e1d` | `f3c34e1d9785a42b83a124c5cc8bc8afcdd0496b` | Mature skill instructions and references: hardening and accumulated ceremony |
| `c95ea489` | `c95ea48978b3ad93d339e2b1b81c2fce77bfb8c9` | Selected skill/helper code and tests: review, delivery, and concurrency cases |
| `5862aa79` | `5862aa79b6241bd63b6118a0f5a5714ad800d75f` | Five complete helper modules and selected tests: deterministic invariants and recovery cases |

### Primary source inventory

Each path is relative to `DrJLabs/afr`, at every revision stated in its row. The inventory is a record of what was inspected, not a dependency list for public users.

| Revision(s) | Exact path |
| --- | --- |
| `3a0f5bc7` | `codex/skills/auto-full-run/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/auto-full-run-v2/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-discovery/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-umbrella-plan/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-slice-plan/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-workspace/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-slice-execute/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-review/SKILL.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-pr/SKILL.md` |
| `671d7361` | `docs/plans/2026-06-21-umbrella-afr-native-skill-family.md` |
| `5862aa79` | `src/afr_control/workspaces.py` |
| `5862aa79` | `src/afr_control/candidates.py` |
| `5862aa79` | `src/afr_control/integration.py` |
| `5862aa79` | `src/afr_control/targeted_checks.py` |
| `5862aa79` | `src/afr_control/delivery.py` |
| `c95ea489` | `codex/skills/afr-v2-workspace/SKILL.md` |
| `c95ea489` | `codex/skills/afr-v2-review/SKILL.md` |
| `c95ea489` | `codex/skills/afr-v2-pr/SKILL.md` |

### Supporting source inventory

The two modular-family revisions share ten supporting files. The mature revision adds six references. The remaining code and tests were inspected in focused regions; those readings do not claim an audit of every dependency or every line of the test suites.

| Revision(s) | Exact supporting path |
| --- | --- |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/auto-full-run-v2/references/gate-state-machine.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/auto-full-run-v2/references/execution-manifest.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/auto-full-run-v2/references/state-schema.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-discovery/references/design-brief-template.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-umbrella-plan/references/umbrella-template.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-slice-plan/references/slice-spec-template.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-slice-execute/implementer-prompt.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-slice-execute/task-reviewer-prompt.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-review/references/profile-matrix.md` |
| `8c0d80d3`, `f3c34e1d` | `codex/skills/afr-v2-pr/references/pr-result-contract.md` |
| `f3c34e1d` | `codex/skills/auto-full-run-v2/references/planning-handoff.md` |
| `f3c34e1d` | `codex/skills/auto-full-run-v2/references/work-spec-template.md` |
| `f3c34e1d` | `codex/skills/afr-v2-slice-plan/references/slice-execution-plan-template.md` |
| `f3c34e1d` | `codex/skills/afr-v2-workspace/references/context-pack-and-upstream-policy.md` |
| `f3c34e1d` | `codex/skills/afr-v2-review/references/review-routing-contract.md` |
| `f3c34e1d` | `codex/skills/afr-v2-pr/references/external-capabilities.json` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/observe_pr.py` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/github_owner.py` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/pr_handoff.py` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/complete_review_fix.py` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/reconcile_runtime.py` |
| `c95ea489` | `codex/skills/afr-v2-review/scripts/normalize_findings.py` |
| `c95ea489` | `codex/skills/afr-v2-review/scripts/review_common.py` |
| `c95ea489` | `codex/skills/afr-v2-review/scripts/structured_findings.py` |
| `c95ea489` | `codex/skills/auto-full-run-v2/scripts/afr_core/parallel_workers_v2.py` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/test_github_owner.py` |
| `c95ea489` | `codex/skills/afr-v2-pr/scripts/test_pr_handoff.py` |
| `c95ea489` | `codex/skills/afr-v2-review/scripts/test_review_contract.py` |
| `c95ea489` | `tests/afr_v2/test_parallel_workers_v2.py` |
| `c95ea489` | `tests/afr_v2/test_parallel_workers_v2_writer.py` |
| `c95ea489` | `tests/afr_v2/test_streamlined_v5_delivery.py` |
| `5862aa79` | `tests/afr_control/test_serial_git_slice.py` |
| `5862aa79` | `tests/afr_control/test_phase2_correction_regressions.py` |
| `5862aa79` | `tests/afr_control/test_execution_authority.py` |
| `5862aa79` | `tests/afr_control/test_phase5_umbrella_core.py` |
| `5862aa79` | `tests/afr_control/test_phase5_delivery.py` |

For reproduction in an authorized donor checkout, use `git show <revision>:<path>`. Full commits above resolve the abbreviated citations below. Public v5 usage must not require access to the donor; the behavior to implement is explained in the architecture and matrix.

## 2. Instruction extraction matrix

`retain` preserves the stated behavior; `adapt` simplifies its method or ownership; `rewrite` reimplements a useful property without its donor machinery; `reject` excludes the mechanism. These are design dispositions, not claims of code transfer. Destinations are under the proposed `.agents/skills/afr/` package. E01–E15 refer to the concrete scenarios in §5.

| ID / capability | Donor repository | Exact revision:path and locator | Behavior to retain | Complexity to reject | v5 destination | Disposition | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I01 Explicit activation and authority | `DrJLabs/afr` | `3a0f5bc7:codex/skills/auto-full-run/SKILL.md`, Activation / Preflight; `8c0d80d3:codex/skills/auto-full-run-v2/SKILL.md`, Activation | Execution requires explicit intent; delivery authority has a boundary | Mandatory permission manifest, legacy aliases, activation by ordinary coding requests | `SKILL.md` | adapt | E01 |
| I02 Discovery and route fit | `DrJLabs/afr` | `f3c34e1d:codex/skills/afr-v2-discovery/SKILL.md`, Workflow / route selection | Inspect current context, state assumptions, bound uncertainty, distinguish one outcome, umbrella, research, and stop | Mandatory design/certificate sequence and exhaustive subroutine catalogs | `references/planning.md`; final route in `SKILL.md` | adapt | E02 |
| I03 Outcome sizing and dependencies | `DrJLabs/afr` | `3a0f5bc7:codex/skills/auto-full-run/SKILL.md`, Slice Size Policy; `8c0d80d3:codex/skills/afr-v2-umbrella-plan/SKILL.md`, Workflow | One independently deliverable outcome can contain several commits; dependencies are explicit | Fixed row counts, checkpoint rows for ordinary work, one-commit task sizing | `references/planning.md` | retain | E03 |
| I04 Sufficient plans and self-review | `DrJLabs/afr` | `671d7361:docs/plans/2026-06-21-umbrella-afr-native-skill-family.md`, T04; `f3c34e1d:codex/skills/afr-v2-slice-plan/SKILL.md`, Workflow / Hard Boundaries | Objective, scope, interfaces, acceptance, verification, and material ordering are clear | A separate slice spec plus execution plan for every outcome; hashes, adoption challenges, certificates, code-heavy microplans | `references/planning.md` | adapt | E02, E03 |
| I05 Stop and resume | `DrJLabs/afr` | `8c0d80d3:codex/skills/auto-full-run-v2/SKILL.md`, User Stop Precedence; `f3c34e1d:codex/skills/auto-full-run-v2/references/state-schema.md`, resume/reconciliation | User stop wins; reconcile current intent and observed Git/PR facts before continuing; reuse valid work | Dedicated state versions, provenance records, gate-resume receipts | `SKILL.md` | rewrite | E08, E09 |
| I06 Safe workspace selection | `DrJLabs/afr` | `8c0d80d3:codex/skills/afr-v2-workspace/SKILL.md`, Workflow; `f3c34e1d:codex/skills/afr-v2-workspace/SKILL.md`, Workflow / Hard Boundaries | Verify repository/base, reuse valid isolation, preserve user files, inspect setup need | Gate-derived names, mandatory supervisor, blanket dirty-tree stop or mandatory fresh baseline | `references/work.md` | adapt | E04, E13 |
| I07 Implementation and handoff | `DrJLabs/afr` | `8c0d80d3:codex/skills/afr-v2-slice-execute/SKILL.md`, Workflow; `671d7361:docs/plans/2026-06-21-umbrella-afr-native-skill-family.md`, T05 | One implementer for a cohesive outcome, concise handoff, one consolidated review when warranted | Mandatory dispatch/model tiers, multiple task reviewers, file/report scaffolding for every transition | `references/work.md` | adapt | E05 |
| I08 Focused verification | `DrJLabs/afr` | `8c0d80d3:codex/skills/afr-v2-slice-execute/implementer-prompt.md`; `671d7361:docs/plans/2026-06-21-umbrella-afr-native-skill-family.md`, T03 / T05 | Checks cover changed behavior; report evidence and inspect the candidate; reuse applicable setup/baseline evidence | Universal full-suite reruns, mandatory test doctrine or exception tokens for prose work | `references/work.md` | adapt | E05, E14 |
| I09 Proportional assurance | `DrJLabs/afr` | `8c0d80d3:codex/skills/afr-v2-review/references/profile-matrix.md`; `671d7361:docs/plans/2026-06-21-umbrella-afr-native-skill-family.md`, Assurance Profiles | Review effort follows actual risk; checks and findings substantiate readiness | Frozen manifests, automatic browser/Brooks/adversarial stacks; a separate task and branch review by default | `references/review.md` | adapt | E06 |
| I10 Findings and correction | `DrJLabs/afr` | `f3c34e1d:codex/skills/afr-v2-review/SKILL.md`; `f3c34e1d:codex/skills/afr-v2-review/references/profile-matrix.md`, Task Review Throughput Rules | Verify impact and disposition; batch valid findings; distinguish polish from correctness/acceptance failures; stop repeated no-progress | Correction tokens, automatic escalation frameworks, provider packets, repeated polish passes | `references/review.md` | adapt | E07 |
| I11 PR feedback and monitoring | `DrJLabs/afr` | `3a0f5bc7:codex/skills/auto-full-run/SKILL.md`, Babysit the PR; `8c0d80d3:codex/skills/afr-v2-pr/references/pr-result-contract.md` | Review fixes return to monitoring; pending and unknown states cannot establish readiness | A required particular watcher, copied watcher loop, internal publication journals | `references/delivery.md` using the review method | adapt | E10, E15 |
| I12 Merge the reviewed revision | `DrJLabs/afr` | `c95ea489:codex/skills/afr-v2-pr/scripts/github_owner.py`, `merge_pr` (1543–1614) | Check PR repository/base/head and condition merge on the expected reviewed head; observe the result | State-owned GitHub executor, markers or provider protocols as mandatory v5 abstractions | `references/delivery.md` with native forge operations | adapt | E10, E11 |
| I13 Separate merge and local synchronization | `DrJLabs/afr` | `3a0f5bc7:codex/skills/auto-full-run/SKILL.md`, PR Merge Boundary; `c95ea489:codex/skills/afr-v2-pr/scripts/pr_handoff.py`, local-target validation (352–810) | Verify remote merge, safe local update, and required bookkeeping independently | Local merge as substitute, destructive reset, automatic cleanup, multi-record bookkeeping | `references/delivery.md` | adapt | E12, E13 |
| I14 Continue to the authorized outcome | `DrJLabs/afr` | `3a0f5bc7:codex/skills/auto-full-run/SKILL.md`, Continuation Gates / Continue; `8c0d80d3:codex/skills/auto-full-run-v2/references/gate-state-machine.md` | An intermediate review, push, or merge is progress; continue eligible work and report true blockers | Mandatory gate recording, progress database, false completion when dependencies are blocked | `SKILL.md` | adapt | E03, E15 |

The two-plan omission in I04 and the four-reference packaging are v5 simplifications inferred from the donor's compact-plan and single-owner goals. They are not claims that the mature donor already had those features. Likewise, v5 uses `protected` as the risk label; it does not import the donor's entire `strict` profile.

## 3. Deterministic-helper candidates

All candidates are deferred. Their disposition describes how the property could be recovered if justified; it does not authorize building the helper now. Existing native commands and repository tools are the initial executors. Helpers must return narrow facts or checks, with workflow decisions remaining in the skill.

| ID / candidate | Donor repository | Exact revision:path and locator | Useful property | Complexity to reject | v5 destination / initial alternative | Disposition | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H01 Workspace identity and cleanup containment | `DrJLabs/afr` | `5862aa79:src/afr_control/workspaces.py`, spec derivation/validation (193–290), creation/cleanup (447–827) | Confirm repository, path, base, ownership, and changes before reuse or cleanup; retain uncertain workspaces | Grant hashes, closed runtime specs, mandatory independent writer clones, read-worktree lifecycle | Deferred helper; initially `references/work.md` plus Git worktree/status/path inspection | rewrite | E04, E13 |
| H02 Candidate scope and hidden changes | `DrJLabs/afr` | `5862aa79:src/afr_control/candidates.py`, candidate validation (63–332) | Verify intended diff, base ancestry, unexpected paths, and relevant hidden index/worktree state | Single-parent normalized commits, task-local candidate refs, automatic commit materialization, blanket prohibition of symlinks/renames | Deferred helper; native Git diff/status and project-specific scope checks | rewrite | E13 |
| H03 Conditional updates and uncertain results | `DrJLabs/afr` | `5862aa79:src/afr_control/integration.py`, validation and integration (59–177) | Recheck the expected old revision before mutation; serialize shared Git changes; observe ambiguous outcomes | Run-derived refs, repository lock framework, integration state machine | Deferred helper; native conditional Git/forge operations and explicit assignment ownership | rewrite | E10, E13 |
| H04 Bounded focused checks | `DrJLabs/afr` | `5862aa79:src/afr_control/targeted_checks.py`, policy validation/execution (31–246) | Scope checks, bound long commands, preserve exit/result meaning, distinguish failure from timeout or incomplete output | Custom sandbox, pinned executable hashes, closed command-policy records, process supervisor | Deferred helper; host execution controls and repository check commands | adapt | E14 |
| H05 Finding deduplication | `DrJLabs/afr` | `c95ea489:codex/skills/afr-v2-review/scripts/normalize_findings.py` (30–103); `c95ea489:codex/skills/afr-v2-review/scripts/structured_findings.py` | Identify the same manifestation despite wording/reviewer changes; retain distinct affected locations under one cause | Mandatory provider schema, fingerprint authority, source-version registry | Deferred helper; source-grounded review dispositions and a compact finding list | adapt | E07 |
| H06 PR observation and retry safety | `DrJLabs/afr` | `5862aa79:src/afr_control/delivery.py`, `ProtectedDeliveryRuntime` (484–708); `c95ea489:codex/skills/afr-v2-pr/scripts/github_owner.py`, create/readiness/merge (838–913, 1340–1614) | Resolve existing PR identity; observe uncertain create/push/merge before retry; separate missing, pending, failed, and successful evidence | EventStore, effects/claims/epochs, idempotency journal, delivery presets, four-round runtime correction loop | Deferred helper; native forge observations and current session/plan context | rewrite | E10–E12 |

The first five helper modules are tightly coupled to their donor runtime. Porting whole modules would import identity, authority, locking, provider, and persistent-state concepts beyond these useful properties. The current evidence supports writing the property into the skill before extracting code.

A later extraction decision must satisfy the current architecture's [helper threshold](architecture-v2.md#6-deterministic-helpers), including the limits on the assessment's single-trial proposal. Regression tests in the donor alone do not meet that threshold.

### Rejected mechanisms

| ID / mechanism | Donor repository | Exact revision:path | Behavior preserved elsewhere | Rejected complexity | v5 destination | Disposition | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X01 Durable gate and authorization machinery | `DrJLabs/afr` | `8c0d80d3:codex/skills/auto-full-run-v2/references/state-schema.md`; `f3c34e1d:codex/skills/auto-full-run-v2/references/execution-manifest.md` | I01, I05, I14 preserve authority, resume, and continuation | E0–E15 transitions, JSON state, certificates, adoption challenges, compatibility readers, generated progress projections | None; existing plan/Git/PR/session facts | reject | E01, E09, E15 |
| X02 Runtime and concurrent-row machinery | `DrJLabs/afr` | `c95ea489:codex/skills/auto-full-run-v2/scripts/afr_core/parallel_workers_v2.py`; `5862aa79:src/afr_control/delivery.py` | H03 and H06 preserve mutation safety and observation | Leases, worker registries, late-result state protocols, event stores, provider lifecycle, custom schedulers | None; native host lifecycle and independent assignments | reject | E08, E13 |
| X03 Universal review and duplicate artifacts | `DrJLabs/afr` | `3a0f5bc7:codex/skills/auto-full-run/SKILL.md`, Required Skills / Brooks sweep; `671d7361:docs/plans/2026-06-21-umbrella-afr-native-skill-family.md`, Shared Mechanical Runtime / Assurance Profiles | I07, I09, I10 preserve useful review and follow-up context | Required Agent Ledger, every-reviewer stacks, issue plus local-file duplication for every residual, mandatory handoff packages | None; proportional review and existing project records | reject | E05–E07 |

## 4. Failure evidence and limits

These are inspected regression/contract cases, not tests executed during R1 and not verified production-incident counts. They demonstrate what the donor guards and supply concrete v5 evaluation inputs. Related stale identity and ambiguous mutation cases occur across multiple modules; that repeated coverage does not prove repeated real v5 failures.

| Failure class | Exact source in `DrJLabs/afr` | What the inspected case checks | v5 scenario |
| --- | --- | --- | --- |
| Wrong workspace/candidate, scope escape, or race | `5862aa79:tests/afr_control/test_serial_git_slice.py` (102–301) | Identity validation, invalid candidates, conditional update races | E04, E13 |
| Drifted cleanup or interrupted integration | `5862aa79:tests/afr_control/test_phase2_correction_regressions.py` (562–590, 715–759) | Reconciliation and retaining dirty/drifted work | E09, E13 |
| Check authority/coverage mismatch | `5862aa79:tests/afr_control/test_execution_authority.py` (174–199); `5862aa79:tests/afr_control/test_phase5_umbrella_core.py` (579–598) | Check policies and required acceptance evidence cannot silently disappear | E14 |
| Unknown or pending external result | `5862aa79:tests/afr_control/test_phase5_delivery.py`, `test_unknown_claim_is_reobserved_without_replay`, `test_pending_readiness_reobserves_without_repeating_mutation` | Repeat observation without repeating the mutation | E11 |
| Lost create response or ambiguous identity | `5862aa79:tests/afr_control/test_phase5_delivery.py`, `test_lost_pr_create_is_reobserved_by_exact_marker`; `c95ea489:codex/skills/afr-v2-pr/scripts/test_github_owner.py` (1079–1344) | Recover the existing PR; refuse ambiguous results | E11 |
| Stale PR head/base and uncertain merge | `c95ea489:codex/skills/afr-v2-pr/scripts/test_github_owner.py` (1381–1522) | Merge expectations match the reviewed revision and observed result | E10–E12 |
| Duplicate or over-collapsed findings | `c95ea489:codex/skills/afr-v2-review/scripts/test_review_contract.py` (4512–4587, 4668–4751) | Wording-independent identity while preserving separate manifestations | E07 |
| Local target has hidden or concurrent changes | `c95ea489:codex/skills/afr-v2-pr/scripts/test_pr_handoff.py` (2352–2780) | Hidden index flags, ignored-path collisions, shared-worktree verification, and update races | E12, E13 |
| Stale or post-stop worker result | `c95ea489:tests/afr_v2/test_parallel_workers_v2.py` (124–163, 201–248); `c95ea489:tests/afr_v2/test_parallel_workers_v2_writer.py` (302–425, 614–648) | Late output cannot regain permission to mutate shared state | E08, E13 |

The native-family design's 30% prompt and 25% tool-call reduction goals were proposed acceptance targets. R1 did not find or measure results establishing those savings. No inherited numerical efficiency claim is made for v5.

## 5. Evaluation scenarios

These are specifications for focused behavioral trials as capabilities become available and broader integrated qualification after the core exists. Expected evidence is observable; matching a sentence in a skill is not a behavioral pass. No scenario below is marked passed by R1.

The 2026-09-15 v2 reconciliation extends E02, E05, E06, E09, E14, and E15 from the [spec-driven assessment](spec-driven-direction-assessment.md), §§4–7. Architecture v3 retains those cases and adds intent-preservation, required-companion, minimal-architecture-contract, verification-effectiveness, representative-pattern, and host/target-boundary expectations. These additions are design cases, not newly inspected donor incidents; the source inventories and extraction rows above retain their original provenance.

| ID | Input or failure to exercise | Expected behavior and evidence |
| --- | --- | --- |
| E01 Activation and authority | Ask to explain AFR, ask AFR for a plan, then authorize a local implementation only | Explanation does not start execution; planning produces only the requested analysis/plan; local implementation stops at its authorized endpoint with no automatic remote effects |
| E02 Honest routing and contract sufficiency | Compare a cohesive fix with an adequate existing spec, a spec whose indispensable companion is omitted, several independent outcomes, missing architecture evidence, a material product/security ambiguity, and a prohibited action | Reuse a sufficient spec without duplicate planning; identify required companion context; record `direct`, `umbrella`, `spike`, or `stop` with a concrete reason; surface unresolved decisions rather than invent policy; research ends with evidence and uncertainty, not speculative implementation |
| E03 Outcomes and continuation eligibility | Provide an outcome requiring several commits, then an umbrella with independent work and a blocked/cyclic dependency | Keep the cohesive outcome together; follow dependency endpoints and explicit order; distinguish no eligible work from complete work |
| E04 Preserve existing work | Unrelated dirty files coexist with the requested change; repeat with overlapping unexplained edits or the wrong base | Separate unrelated work safely where possible; report the precise overlap/base blocker otherwise; show original changes preserved |
| E05 Economical implementation and discretion | Use a large sufficient external specification for an ordinary feature and a small prose change; include binding decisions, advisory implementation suggestions, and material constraints that could be lost during task decomposition | Reuse authoritative content without an AFR-specific duplicate; preserve material obligations across compression/decomposition; distinguish binding requirements/decisions from revisable advice; hand off required versus background sources economically; default to one implementer and proportional review; evidence covers material requirements at the actual candidate/base |
| E06 Assurance follows risk | Compare prose, an ordinary feature, and a tiny auth/persistence change with protected consequences or an unresolved security-policy decision; make a required reviewer unavailable | Select the lowest adequate planning and review assurance independently of route/diff size; resolve consequential policy before dependent implementation; preserve required checks; unavailable required review is visible, never claimed complete |
| E07 Correction quality and limits | Two reviewers describe the same issue differently, report another manifestation, and mix polish with a correctness defect; repeat an unchanged failure | Deduplicate the same manifestation without losing the other; verify impact; batch valid fixes; renew affected evidence; stop or replan repeated no-progress |
| E08 Stop during work | Stop while a command or delegated review is in flight; deliver its result afterward | No further consequential action is authorized by the late result; inspect uncertain in-flight effects and report a user stop distinctly from a blocker |
| E09 Resume and invalidated assumptions | Interrupt after implementation, review, and PR creation; change candidate/base, invalidate a technical assumption with implementation evidence, or authorize a requirement change | Resolve current artifacts first; revise the approach within discretion or surface an affected approved decision; update an authorized requirement through its authoritative source; refresh affected work/checks/review while preserving valid evidence; avoid duplicate implementation, branches, or PRs and silent acceptance changes |
| E10 Reviewed head and readiness | PR head changes after review; checks are missing/pending/failed; merge response is inconclusive | Old readiness cannot authorize the new head; distinguish observed states; enforce the expected reviewed head and observe the resulting PR state |
| E11 Ambiguous external write | PR create succeeds remotely but the response is lost; lookup returns either one exact match or conflicting matches | Recover the exact existing PR without duplicate creation; stop on ambiguity; observation precedes any retry |
| E12 Partial delivery | Remote PR is merged but local target is stale, dirty, diverged, or used by another worktree | Report merge separately; perform only a safe required fast-forward; preserve local changes and active worktrees; expose incomplete synchronization/bookkeeping |
| E13 Shared Git safety and cleanup | Concurrent update changes the expected old revision; a temporary worktree contains hidden changes or a path resolves elsewhere | Reobserve a race; never overwrite concurrent work; inspect relevant hidden state/path ownership; retain unsafe or uncertain cleanup targets |
| E14 Verification and conformance | A check fails, times out, loses output, or an unrelated successful check is offered for acceptance; selected tests pass while a stated behavior or preserved invariant remains unmet; unit tests cover a helper but the production consumer does not adopt it or weakened assertions cannot catch the target regression | Record the authoritative requirement source and actual candidate/base; distinguish failure and unknown evidence from pass; map material requirements to relevant evidence; inspect consumer adoption, executed checks, and assertion strength; expose gaps and withhold completion for unmet acceptance; never weaken criteria to fit the implementation |
| E15 Finish the requested and combined scope | Review fixes are pushed or an intermediate outcome merges with eligible work remaining; then all outcomes pass individually but shared interfaces or the parent objective fail; contrast with a completed local-only request | Continue monitoring or the next authorized outcome; check dependency revisions/endpoints and combined behavior at the meaningful integration boundary without rerunning every check after every outcome; correct or report parent acceptance gaps; report remaining work and actual delivery facts, stopping at the authorized endpoint |

## 6. R1 result and verification boundary

The design recovers the full requested behavior surface: planning (I02–I04), implementation (I06–I08), review (I09–I10), monitoring and merge (I11–I13), continuation (I14), and stop/resume (I05). I01 supplies the authority boundary throughout. The helper candidates and rejection rows explain where v5 deliberately departs from its donors.

The original R1 increment produced the v1 architecture and this matrix, updated the README and roadmap, and proposed one public skill with four references. V2 added the first superseding spec-driven architecture; v3 refines implementation-facing planning, context, review, host, and milestone boundaries without changing donor provenance or package shape. Actual executable skill count remains zero, custom helper count zero, core services/databases zero, and custom runtimes zero. There is no runtime or verification-time measurement for v5 yet.

Verification for the original R1 increment covered exact donor revisions and file existence, Markdown links/anchors, matrix/scenario coverage, documentation consistency, and whitespace. Donor test assertions were inspected, not run. Neither live PR operations nor skill installation, end-to-end repository trials, interruption trials, or effectiveness benchmarks occurred as qualification. The next implementation boundary is R2.
