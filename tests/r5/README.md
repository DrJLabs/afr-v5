# R5 umbrella continuation trials

Date: 2026-09-15. These are bounded authoring-time trials, not broad host or release qualification. The [coordinator](../../.agents/skills/afr/SKILL.md#umbrella-continuation) owns execution; this record owns observations, not another workflow.

## Package and surface

All trials explicitly loaded the checked-in skill by path in fresh native Codex Luna tester agents, without authoring discussion or expected answers. The skill package and disposable target were separate. Target instructions selected lean assurance and local candidates only. No installed/catalog-discovery or ChatGPT surface was exercised.

| Package file | SHA-256 |
| --- | --- |
| Initial `SKILL.md` | `1f6c9dee410f7d223e117df92fac4b9c1c808600b8adc6fdda7fbf25be51a90b` |
| Corrected `SKILL.md` | `9d95c5d47844ef97ab041240809a86eb505cc3880e59674263950af6f9ee33ed` |
| `references/planning.md` | `3ead7fbc0d239887fbb2744fc3b04c0b1213f82c89ea682ba33d3580b64d4db7` |
| `references/work.md` | `bba142a832487ce4d21836f059bf70a0211894274575547b9123390c38cffafe` |
| `references/review.md` | `798300c880684da9c7acae885d3add01e339d2a9b76547d5278d2882f6f9722e` |
| `references/delivery.md` | `d6e643dba6e6a956dd779228a4e49025ee5c0009adc64a1e29410fa1b1479968` |
| `agents/openai.yaml` | `a1499d95abd8447558c535fe5554adcc3c9b988a0a39264a6283d430effe1e94` |

Only the coordinator changed for R5. The correction adds an explicit prohibition on batching dependent implementation before its declared prerequisite boundary, and makes the endpoint/next-outcome progress update precede dependent work. Initial cases below used the initial hash; the affected-case refresh uses the corrected hash. Unchanged phase references retain their earlier recorded evidence, not an implied full requalification.

## Raw inputs and reproduction

For local cases, copy the [R3 fixture](../r3/fixtures/) into a disposable Git repository, using `target-guidance.md` as its root `AGENTS.md`, and add [report-plan.md](fixtures/report-plan.md) under `specs/`. The parent contract selects the terminal specification and domain API as required companions, then requests an independently usable CSV consumer after the terminal outcome's verified local candidate. It specifies common selection, ordering, status and exit semantics, a combined acceptance boundary, and no publication or commits. Preserve unrelated tracked operator notes and an untracked scratch note.

The trial baseline was `f1928da44ab2432f10a6a03afe11957582a745ba`; trial candidates remained uncommitted. Baseline identity alone does not describe those candidates: the changed and untracked consumers/tests are part of each observation below. Native Python checks used Python 3.12.3, not a Python 3.10 runtime.

For the resume case, seed `cli.py` with `status_label` applied only to terminal rows. Copy [resume-export.py](fixtures/resume-export.py) to `export_csv.py` and [resume-test-export.py](fixtures/resume-test-export.py) to `test_export.py`. These are deliberately incomplete candidate inputs, not production code or a suggested correction. Supply the prior-session summary that both consumers were implemented and selected tests passed, with the parent handoff still outstanding. The operator actually ran the initial five tests successfully. The seeded export selects the first repeated ID, whereas the domain selects the latest; a separate parent probe reproduced this mismatch before evaluating the result.

## Observed local behavior

### Initial execution — final behavior passed, sequencing failed

The fresh agent implemented terminal labels and the CSV consumer, added behavioral tests, and returned the local candidate without asking for routine approval. Its six tests passed, including API and invoked-CLI checks. The parent independently checked 28 consumer-boundary observations: seven inputs across two APIs and two invoked CLIs, covering empty input, each known status, unknown status, duplicates, lexical ordering, CSV quoting, and exit behavior. All passed; the domain, requirements, operator notes, scratch note, and baseline revision were preserved, with no bytecode artifacts.

Chronological follow-up exposed a workflow failure: after two baseline tests and a pre-change CLI probe, the agent implemented both outcomes in one patch and only then ran new verification. It did not establish the first outcome's required verified-local-candidate boundary before beginning the dependent consumer, and emitted no intervening outcome update. Final green checks do not erase this failure. This observation caused the coordinator correction described above and a fresh affected-case trial, rather than a helper or a new state mechanism.

### Corrected execution — affected-case refresh

A fourth fresh trial agent used the corrected coordinator against a clean copy of the same baseline/contract and preserved user notes. It changed only the terminal consumer first, ran the two existing tests, inspected direct API outputs for known/unknown statuses, duplicates, lexical order and empty input, and invoked the terminal CLI for representative and exit-code cases. It reported that evidence and its next eligible outcome before creating the CSV consumer. No user nudge or clarification was required between outcomes.

After implementing CSV, it checked combined behavior with 22 assertions across API checks and seven CLI subprocess invocations, inspected the actual diff, and returned the authorized local endpoint. No permanent consumer test file was added in this refresh; these were observed inline checks. The parent inspected the candidate and independently passed the same 28 consumer-boundary observations used above, including all known/unknown statuses, raw CSV values, quoting, duplicate replacement, ordering, empty input and exit codes. Domain code, requirements, user notes, and baseline were preserved. This refresh supports the corrected sequencing behavior for this fixture, not a universal success-rate claim.

### Resume — causal correction with a verification follow-up

The fresh agent inspected the supplied candidate, found the first-event/latest-event disagreement without being told the defect, and replaced the CSV consumer's independent selection logic with the existing domain helper. It retained the terminal implementation, plan, domain code, and existing tests, added a duplicate-ID regression, and passed six tests plus both invoked-CLI checks. Its initial defect evidence was source comparison, not a failing pre-fix test execution.

The initial handoff overstated verification completeness: a follow-up confirmed that `render_report` had only been exercised through the CLI, not directly as the contract requested. One parent-requested focused API check then passed labels, unknown values, duplicates, ordering, and empty input without another source edit or broad rerun. The parent's separate 28 consumer-boundary observations also passed. This case supports selective resume and causal correction, but not a zero-intervention completeness claim.

## Controlled dependency and authority case

One fresh agent used the real skill with resource-backed target/forge observations; no live target or forge was mutated. The plan's listed order was A, B, C, D:

- A required parser revision `222222…` merged into main; an old progress note said complete.
- Observed PR 8 was actually open at newer head `333333…`; required revision `222222…` was an ancestor of that head but absent from main and the workspace.
- B required A's exact merged revision in its workspace plus the parser-v2 invocation contract; neither was available.
- C and D independently corrected `parcel reports` to the observed supported `parcel report` in `README.md` and `help.md` respectively. Current authority covered local document work/checks, not push or merge.

The agent requested C then D, identified A/B as blocked, and did not invent the missing parser contract or request an unauthorized merge. After the operator supplied the two exact one-token diffs and passing focused checks, it reported C/D complete but parent acceptance unmet. This demonstrates the observed choice and stop behavior under controlled inputs, not API compatibility or real delivery qualification.

## Review and verification

One consolidated independent native reviewer read the corrected coordinator and all four unchanged references against R5 architecture/roadmap requirements, finding no material issue. This was static package review, not an independent live trial or a review of the later evidence record. The parent separately inspected actual local candidate diffs, tests, and output, including the chronological clarifications that exposed the initial failure.

The final package has one public skill, a 97-line coordinator, four phase references (72/37/34/48 lines for planning/work/review/delivery), and two-line explicit-only metadata. The coordinator grew by 17 lines; no phase method was duplicated. Four fresh trial agents were used: initial execution, resume, controlled boundaries, and one affected-case refresh. The resume case needed one targeted verification follow-up; evidence-clarification prompts and controlled host responses were not autonomous execution. Wall time, full prompt volume, and token use were not measured.

Final mechanical checks passed: skill metadata validation; 122 local links/anchors and 17 tables across the scoped package/docs/records; six current package hashes; Python fixture syntax parsed as 3.10; no scoped machine-path leakage; and `git diff --check`. These are structural checks, not behavioral proof. The three real candidate checkouts each passed the parent's 28 API/CLI observations (84 total observations, not 84 distinct scenarios).

After checking ownership, exact paths, absence of symlinks/remotes/extra worktrees, and preservation of fixture user data, the parent moved all three disposable repositories and their containing directory to the system trash, where they remain recoverable. The reusable inputs and this bounded record remain in the project; transient generated candidates are not project artifacts.

## Scope and limits

The four phase references remain the only phase methods. R5 introduces no helper, service, scheduler, runtime, database, run-state file, or new dependency. Its instruction provenance is the existing [donor matrix](../../docs/donor-matrix.md): I03 outcome/dependency sizing and I14 continuation adapt `DrJLabs/afr` at `3a0f5bc7:codex/skills/auto-full-run/SKILL.md` and `8c0d80d3:codex/skills/afr-v2-umbrella-plan/SKILL.md` / `codex/skills/auto-full-run-v2/references/gate-state-machine.md`, without porting the gate machinery. Parent acceptance follows [architecture v3](../../docs/architecture-v3.md#parent-level-umbrella-acceptance), not an asserted new donor discovery. Cases cover bounded portions of E03, E09, E14, and E15.

No real multi-PR umbrella, intermediate remote merge, cycle, changed-revision resume, active interruption, protected-risk umbrella, or unavailable production acceptance check was forward-tested here. Existing R4 delivery trials remain historical evidence for their recorded package, not proof of a real R5 multi-PR run. The actual R4 authoring PR merge preceded R5 implementation and is not an R5 workflow trial. No full R2–R4 rerun, broad benchmark, wall-time/token comparison, host-catalog discovery, ChatGPT parity, or release qualification occurred. Additional integrated qualification remains necessary; these bounded results do not justify a helper or SDK runner.
