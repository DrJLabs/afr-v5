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

## M8 prospective representative run — 2026-09-17

The operator commissioned one real umbrella spanning controlled architecture changes in `codex-session-md` and dependent AFR/Architecture Guard adoption. The diagrams `docs/m8-controlled-architecture-change-plan.md` contract and `docs/implementation-plan.md` Progress section own requirements and delivery status; this section records observations only. The umbrella counts once, only after combined acceptance, separately from candidate-skill authoring trials.

The governing package remains fixed at repository revision `aa87adb11dcdfb1f2491e438bf4984e24e8e7f6c`, skill tree `c4412558fe8240c0a1ac325ca3a4356cb4848683`. Its coordinator and four references have the corrected R5 hashes listed above. It was explicitly loaded by path. The candidate package is edited in a different worktree and is not the governing revision. Host: native Codex on Linux, CLI `0.154.0`; parent model `gpt-6-astra`, reasoning effort `xhigh`, confirmed from the current session's turn metadata. Goal mode: off; no native goal or substitute coordinator was created. Bounded native Luna implementer/reviewer roles are used under repository/skill delegation guidance and recorded separately from parent execution.

Observed initial dependency chronology: inspect contract/current repositories and provider policy; preserve exact uncommitted M8 contract in isolation (SHA-256 `0d6871d8ac571959293c917aa84b0a705c686578c9ea63f968da27793d209ff3`); run the six pre-change M6 static qualification cases; draft E independently while implementing A–D. No dependent E end-to-end acceptance has started. Source roots retain unrelated dirty planning/goal-mode changes; the consumer's unrelated PR 77 remains untouched.

At initial recording all six M6 cases passed in approximately 1.7 seconds wall time (individual cases 0.237–0.280 seconds), including forbidden-import, weakened-policy, unmapped-source, inert-sentinel, and edited-runner rejection/acceptance. This measures local fixture execution, not total engineering cost or performance improvement. Tool versions observed: Import Linter 2.15 and Node 22.23.2; the existing pinned LikeC4 profile is 1.59.3. No broad application or production validation has run.

Interventions so far: the operator added this prospective qualification requirement, including one controlled pause/resume. No continuation nudge or unnecessary architecture-approval stop has occurred. Pause/resume remains unexercised at this recording; a safe pre-migration boundary is arranged, and no coverage is claimed until the operator actually pauses and resumes. Aggregate tokens, monetary cost, and human attention time are not measured. Completion count remains zero pending both outcomes and combined acceptance. Candidate qualification, remote identities, measured checks/waits, pause/resume observations, final gaps and count will be recorded here as observed.

Before provider work, independent bootstrap review accepted the whole-tree promotion approach subject to base-SHA verification, fixed legacy-control/source identities, strict bounded manifest data, and exact preservation of bridge machinery. Those safeguards were added to the local migration draft; this is design/draft review, not review or execution of the final staged candidate. The old required check remains in force. Independent M8 instruction drafting used one Luna implementer; parent review found and corrected two omissions (host-appropriate instruction chain and explicit greenfield/staged planning) before candidate trials. These were review corrections, not operator continuation nudges.

The existing LikeC4 profile validated the unchanged current model and built a self-contained HTML site. PNG export failed because the required headless browser binary was absent. Browser inspection of the local HTML was blocked by browser URL policy; no workaround or installation was attempted, and visual inspection is not claimed. The build remains a viewable artifact, separate from selection or conformance. One scope question was sent concerning publication of the diagrams checkout's pre-existing unpushed M7 commit; M8-independent local work continued while its answer was pending.

### Safe pre-provider checkpoint

At 2026-09-17 06:31 UTC all native workers were idle, with no operation in flight and no GitHub mutation performed. The operator was asked to issue the pause instruction and subsequently resume; operator pause/resume coverage is still unclaimed. The target candidate is uncommitted on `feat/m8-controlled-architecture` at `c469e8b7a8a8d845438e976e735aa775a8fc31d6`. Worker-reported local static transition/failure cases passed, but its plan-validator probe used `/bin/true`: that establishes harness behavior only, not real LikeC4 model validation. The host's approved Node/LikeC4 toolchain exists; the next turn must run the actual parser, finish malformed-record/provider-input tests, and obtain final protected review before any staging PR. Earlier current-model validation/build does not fill that candidate-validator gap.

The candidate AFR source received one independent bounded instruction review. Its minor completeness finding was corrected by explicitly updating affected obligations, assignments, checks, review scope, and evidence after owner selection of a changed revision. This is source review only; candidate behavioral qualification awaits the delivered gate. The eight migration-draft boundary tests passed locally in 0.012 seconds; no full bootstrap or GitHub path was exercised.

Checkpoint identities below bind the uncommitted candidate files for observed-state resumption; they are evidence, not an additional task ledger.

```json
{
  "candidate_afr_package_sha256": {
    "SKILL.md": "2720daf9e6ac8df3863eb5743d5877bd89c03a4a48cb8566a6215f9a10210883",
    "agents/openai.yaml": "a1499d95abd8447558c535fe5554adcc3c9b988a0a39264a6283d430effe1e94",
    "references/delivery.md": "1421bd2246c206f45f27a233eaf7b39f07c72e3d13b5c3b58e8234942c5ac556",
    "references/planning.md": "7d061eee558336740b6d11296e54fa0a746537bd4f8738db2d547a03c81d19c6",
    "references/review.md": "d8597f1dcd2eed986c93aa82c89cde9294f6411988b9e5bb95e5f472a91d26a8",
    "references/work.md": "5d5199d11c7b5c0c478a506467a8f370599761972b161cb390de50fd281f5528"
  },
  "target_candidate_sha256": {
    ".github/workflows/trusted-architecture-plan-validation.yml": "7d131391e559b62820ac178d275617e65a5a4431e54d110837ad66b2c552ad65",
    "architecture/README.md": "68ca04f6a2c744c3fc40a1501d4967f695f7401f1a741c0ad39fa40bf1c4f2b5",
    "architecture/acceptance-policy.json": "9afcc71e913dbe186b91baf4de9c7e2929f4f81e010b6f36dc44de8fad32e9c3",
    "architecture/likec4-package-lock.json": "23e9eda81a90a8581d61e3d1ab4af09ac2daa54ae9e748784da7d2c1af9d5223",
    "architecture/likec4-package.json": "888d6ea6608922d171d05975951b18bd3ba53f00d4fc8806054d7d46f4536e34",
    "architecture/likec4-toolchain.json": "a97b8daa7a0c2b6a9fc3fab38bbeec5c0b1e1bc5e2e8b58b99ce69cd8ac35c87",
    "architecture/plan-schema.json": "4368525bf85f2e2674222d702578c9d9a0a95bfed817a543adb4a1e24240d281",
    "scripts/accept_architecture.py": "96408d932c8bca71972e42e7e4e79dee22eb5eb2c0f04ddef4208edcdcda23f7",
    "scripts/qualify_architecture_acceptance.py": "679bdb111ce36aca8ade2db57395e3f01c904e09cc655c206b69fc9d46326661",
    "scripts/validate_architecture_plan.py": "1370b349a95aec42d4e9e95fd9488f70e45a07ab66898292830f44819f666598"
  }
}
```

### Observed checkpoint resumption — 2026-09-17 23:26 UTC

The run stopped with idle workers at the planned pre-provider checkpoint. The operator asked why the additional pause/resume exchange was needed; the parent acknowledged that asking for a separate “pause” reply added unnecessary friction. The operator then explicitly sent “resume”. This demonstrates a planned checkpoint stop and operator-directed continuation, not native app interruption, abrupt cancellation, crash recovery, or changed-revision handling by itself. Record the clarification as one avoidable operator interaction. The long interval is an external pause, not active execution cost.

On resume, machine, roots, branches, dirty state, immutable M8 input, every recorded target/candidate-AFR file hash, and the fixed governing package were reobserved. All matched the checkpoint. Fresh fetches and provider reads showed unchanged main revisions and required protection; only unrelated consumer PR 77 remained open. Existing worktrees and drafts were reused and no external write was duplicated. No dependent candidate-AFR acceptance began ahead of gate delivery. A real LikeC4 run then passed the 15-case existing harness, replacing the placeholder-parser gap for its valid-record case; malformed-record and provider-input coverage still require additional focused checks.


### Gate qualification before provider migration

After resumption, protected review exposed a regressed inherited base-model membership check; it was restored with whitespace-tolerant matching. The strict record parser is shared by finalization and acceptance. A separate finding established that finalized-record immutability depends on requiring both permanent checks; the documentation and migration endpoint state that dependency explicitly. The first test collection failed because a pytest parameter used the reserved name `request`; renaming the test parameter fixed collection. These are engineering corrections, not operator interventions.

At the final local candidate `227ff4a` (full Git identity available in the consumer repository), 47 focused tests passed in 5.56 seconds with real LikeC4 parsing/export. The native qualification passed 15 cases, including an actual synthetic added module/component/additive rule and an inert execution sentinel. This tests selected static boundaries; it does not exercise the production publisher or dynamic behavior. No broad application suite was needed for the gate-only change.

The exact bootstrap bridge passed nine focused tests plus full offline integration using Git objects and the real Import Linter. Old and proposed gates consumed the same 105 files / 3,069,989 bytes; the old gate failed only for the two reviewed enforcement-control edits, and the proposed gate passed. Extra/missing files, source changes, and changed file modes failed whole-tree equality. These results establish offline bridge behavior only. Final protected review found no outstanding local material issue. The stage payload has 12 exact files and manifest SHA-256 `394e6704e3341f7c350747e29c84037067fc3e5f9d974c9adf40b82a9f6316e3`.

The first authorized M8 remote write published staging PR [82](https://github.com/DrJLabs/codex-session-md/pull/82), head `b6552a28a662a99fe5950d12a53495bb190bab9e`. It leaves the active gate unchanged. Its provider check and remote review are pending at this entry; protection has not yet changed. Candidate AFR end-to-end trials remain dependent on completed gate delivery and provider qualification. The unanswered M7-publication question is resolved conservatively: M8 will be published alone, preserving the unrelated local M7 commit rather than inferring authorization to publish it.


### Provider migration, discovered failure, and recovery boundary

Staging PR82 merged at `f25046eea68bc3ad4968c16b5d4a8048110827ad`. The provider bridge for promotion PR83 passed, observing the same 105 files / 3,069,989 bytes as offline qualification; the old gate failed only for the two reviewed control edits, and the proposed gate passed. The normal exact-head protected merge produced `a1301724e7eedea33eea1378408c9e0bb1d412f3` at 23:49:07 UTC. Full before/bridge/after protection receipts show atomic app-bound context replacement/restoration with strict/admin enforcement and all other fields unchanged. Both permanent checks are required.

PR84 then exposed a verification gap: the plan-validation workflow cannot start because its `setup-node` action pin is nonexistent. The workflow used `49933ea5288caeca8642d1b834dc74c9b0d0a3e`; official GitHub v4.4.0 resolves to `49933ea5288caeca8642d1e84afbd3f7d6820020` (verified commit). The parent introduced this unverified pin and local/native parser tests did not establish provider workflow availability. The other required architecture check passes. CodeRabbit supplied summaries/rate-limit notices, not a substantive remote code review; the protected review evidence is the independent native review.

The exact correction is local commit `20e4879`; a local-only one-file repair bridge binds the full current control set and source. Its offline old/new integration passes on the same 105 files / 3,069,990 bytes and rejects extra/missing/source/mode changes. Its manifest identity is `7ebb8aa4fa8b904bbc4acb542151536aa5b4d6e6e8aaa74e26fdc8734b663ec8`. Independent safety review determined that the broken base-side required workflow plus consumed original bridge prevents normal protected repair. A new owner decision is needed before temporarily reducing the permanent check set to stage an exact repair bridge. Both permanent checks and blocked PR84 are preserved unchanged pending that decision. This is a concrete recovery boundary, not a completed outcome or another planned operator pause.

The unchanged baseline record remains proposed in PR84; no finalized consumer record exists on main, no disposable provider exercise has run, and no candidate AFR end-to-end trial has started ahead of its dependency. Governing real-use evidence therefore remains one prospective, unfinished umbrella with completion count zero. Candidate source review is not candidate behavioral qualification. No global installation, host discovery, ChatGPT parity, runtime activation, deployment, broad application test, or crash-recovery coverage is claimed.

Observed cost through the recovery boundary includes 47 focused tests in 5.56 seconds, 15 native cases (individual gate calls around 0.07–0.28 seconds plus real LikeC4), and original/repair bridge integration. GitHub staging acceptance took 47 seconds; promotion bridge 51 seconds; PR84's plan workflow failed in 3 seconds at action resolution while its acceptance took 28 seconds. Resumed execution began 23:26 UTC; the required run failed at 23:52:19 UTC and was inspected before the 23:55:50 UTC live state read, with local recovery preparation afterward. The long 06:31–23:26 pause is excluded from active effort. Token/monetary cost and operator attention time were not available as reliable aggregate measurements; no estimates are presented as measurements. The extra pause clarification remains one avoidable user interaction; the recovery decision is pending and must be recorded as an intervention if supplied.


Recovery-decision checkpoint at 2026-09-18 00:00:52 UTC: proposed repair staging is local commit `823bd355e174ef45e799db45179cb5f8074b5519`, independently reviewed; direct one-line correction is `20e487990033a415074272cf4e250cd9b19d2ab2`. Neither is pushed. AFR candidate source is committed locally at `5ffca4fc9dd86e5229f7cffddaa9ada89c0addcd`; diagrams M8-only source/progress is local at `19e26da488e6bb66a0bbb9e096bc15c01163855b` before this final receipt update. The source skill hashes remain the recorded candidate hashes. Consumer fetched/live main is `a1301724e7eedea33eea1378408c9e0bb1d412f3`; original consumer checkout stays on its unrelated clean feature branch. Original diagrams M7 and AFR dirty goal-mode work remain untouched. Resumed elapsed wall time to this checkpoint is approximately 35 minutes, including tools and waits; no monetary or token aggregate is available. There is no remote mutation in flight, and completion remains zero.


The operator explicitly authorized the recommended recovery migration. Record this as one additional consequential owner intervention caused by the unverified provider pin. The reviewed repair artifacts and external state were reobserved unchanged before continuing; this does not alter the fixed governing package or start another representative run.


### Authorized repair and delivered prerequisite — 2026-09-18

After the explicit recovery authorization, the parent reobserved the unchanged local repair and protected state. PR85 (`823bd355e174ef45e799db45179cb5f8074b5519`) staged the exact one-file repair bridge; its protected merge was `595233b08e55d59e62c9dd6ebd5ca11481bb3390` at 01:09:20 UTC. Both permanent requirements were restored while promotion ran. PR86 (`68a4bc2d2730e62bf0a03a82271aa9f1e27d79eb`) passed the base-side exact repair bridge in run 35294215058 (37 seconds) and merged normally at `c55c32a260aead9daf0e32b999c3b370f6a967ca` at 01:11:25. Full protection receipts preserve all other settings; both app-bound permanent checks were restored immediately. This owner-approved recovery is an intervention in the same run, not an additional completed umbrella.

PR84's refreshed head `80d63388cd77683f916a794707f1f88fea515a23` passed both permanent provider checks, including real pinned LikeC4 plan validation. It merged normally at `a08f73abb0f4267f95abc3a57ef9cd65910d997a` at 01:15:05. Both temporary bridges were retired. The finalized record selects only the byte-identical previously adopted baseline; no new consumer design was inferred or approved. The required `trusted-architecture-acceptance` and `trusted-architecture-plan-validation` checks remain strict and app-bound with admin enforcement.

Late automated comments were assessed against actual code and official action-tag identities. One preview-path documentation clarification was fixed before PR84 merged. Generic local filesystem race/fsync suggestions did not describe a reachable provider threat in the verified static-blob boundary; incorrect action-version comments were rejected with official tag evidence. Consolidated dispositions and thread resolution were posted to PR82/83/85; native independent review remains the substantive protected review. CodeRabbit summaries are not counted as independent code review.

Disposable PR87 then passed both required checks at `c77e9ca2e6dfa944aaacf4c3fbf2c48afde78edf`, base `a08f73abb0f4267f95abc3a57ef9cd65910d997a`, with observed merge eligibility CLEAN. Its request selects the finalized unchanged baseline, and its top-level raising sentinel was not executed. Runs 35294564362 (38 seconds) and 35294564490 (13 seconds) establish the real provider path. Rejected tampering and closure remain pending at this entry; candidate AFR trials have not started.


At `f9ddf58f0063ae9fbb5ac725bd2b2fae2251b9d4`, PR87 failed both real required checks: acceptance run 35294985661 (53 seconds) reported `trusted_control_drift`, `desired_control_mismatch`, and `native_import_contract_failure`; plan-validation run 35294985742 (14 seconds) rejected modification of the finalized decision. Merge eligibility was BLOCKED. PR87 was closed unmerged at 01:22:58 UTC. The live case uses a no-op selected baseline, while the material transition/stale-plan cases are local synthetic evidence. Only after this observation did the parent start fresh native candidate AFR/Guard agents for the controlled and greenfield fixtures, archived from delivered consumer main `a08f73a`. This satisfies dependency chronology; the candidate trials do not retroactively govern the parent run.


Consumer evidence PR88 (`4e2df98593603592f9c254651ff0017506c824a0`) passed both permanent checks and independent evidence review, then normally merged at `f1dcc5a2b41530f79dfaabb965b14cb70fece4b9` at 01:26:32 UTC. Its task worktree was safely fast-forwarded. Consumer implementation and provider qualification are delivered; dependent candidate trials remain active.


### Candidate M8 instruction trials — separate from governing real use

Two fresh native Luna implementer agents (`gpt-5.6-luna`, high effort) explicitly loaded the candidate coordinator, applicable phase references and candidate Architecture Guard after the live gate prerequisite was qualified. Candidate AFR source hashes remain the checkpoint hashes above; the Guard coordinator SHA-256 is `864a0ce95489c51376ad4131aa865e097f85884f65edada893a56eb887383cc5`. These are guided local synthetic trials, not a switch of the parent run's governing package, another representative run, global discovery, or cross-host qualification. The parent acts as fixture decision owner; its selections cannot approve a real consumer design. The bounded machine-readable evidence is in the diagrams repository's `docs/evidence/m8-adoption-qualification.json`.

The greenfield trial created only a viewable Mermaid proposal before selection. The parent inspected and selected exact proposal SHA-256 `ff67fcaed89544e966ce670ded5426175503b2c324026d4cf4b464030c7fd955`. Only then did the agent implement a pure event-counting utility. Six stdlib behavior tests passed in 0.001 seconds (command wall time 0.05 seconds), covering deterministic counts/order, empty input, one-shot/non-mutating input and invalid records. No architecture enforcement was installed or inferred from the diagram. Parent source/test inspection found the selected boundary preserved.

The controlled trial first clarified one existing source docstring without changing architecture, retained its unrelated operator note, and passed the delivered trusted gate in 0.26 seconds. An `uv` test command implicitly created a disposable environment and installed seven locked packages despite the trial's no-installation constraint. This is an observed scope-compliance failure, not a clean pass. The parent caught it, prohibited further installation and retained the log; the worker removed its generated environment/caches. An existing interpreter then ran the ordinary 20 tests in 0.50 seconds without installation. The hub Python lacked pytest, recorded as unavailable; a stdlib/parser/inventory smoke passed separately. No production/global installation occurred.

Before the new component existed, the agent produced current/proposed Mermaid views and LikeC4 artifacts with complexity rationale. Current/proposed validation took 0.86/0.90 seconds and static builds 5.54 seconds each. Current-view copies added only presentation labels. Browser viewing remains unclaimed. The draft record was rejected as non-final. Parent review corrected one draft owner attribution from the real consumer owner to the synthetic fixture owner, then selected exact proposed map/model/policy hashes. Real trusted validation passed before the parent committed the finalized record in the trusted fixture at `91722d7`. The selected plan hash was `cededce36aae986ac90af0a013a8ec65886a0e579a9a4055d57729b10a53b90a`.

Dependent implementation added one pure JSON formatter, three focused behavior tests, exact selected active controls and the narrow request. The formatter checks passed in 0.27 seconds; the combined ordinary/formatter 23 checks passed in 0.46 seconds. Trusted static acceptance passed in 0.26 seconds and reported no candidate-code execution. These behavioral tests intentionally execute synthetic code separately from the privileged static gate. The existing-record check reused finalization evidence and did not constitute another fresh model parse.

A parent-injected forbidden import plus weakened candidate policy failed with `desired_control_mismatch` and `native_import_contract_failure`; the trusted policy identified the exact deployment-to-Miyo-administration edge. The weakened candidate policy itself reported a pass, demonstrating why candidate-local results cannot self-certify. The agent removed the injected import and restored the exact selected policy, without adding an exception or rebaseline. Trusted acceptance then passed in 0.26 seconds; 64 affected focused tests passed in 0.56 seconds. The formatter, ordinary clarification, selected controls/record and operator note remained unchanged. Their valid earlier evidence was retained.


The revision continuation advanced only the trusted base model annotation (`cdd3d6a`) while the implementation stayed unchanged. The old request visibly failed `stale_plan` in 0.10 seconds. The agent retained the old immutable record, source and behavior evidence, and drafted a new ID. Carrying forward the base comment changed the desired model bytes; parent inspection selected that exact model delta while reusing the unchanged mapping, policy and design selection. This distinction corrects the agent summary's loose “desired content unchanged” phrasing; the draft itself correctly identified the changed model hash and required parent finalization. Real model validation/finalization preceded trusted fixture commit `7d3538a`; the new plan hash is `45751c2f228f4e3772b1997c644b214056259c42cdf3b8b3b4b5fbf66639f585`. The revised request passed actual trusted acceptance in 0.26 seconds and the three-existing-record check in 0.09 seconds. No broad suite was repeated. Exact hashes confirm the ordinary source clarification, formatter, tests, unrelated note and old records were preserved.

Candidate M8 architecture scenarios are now bounded-qualified with the recorded intervention and scope fault. They do not establish flawless authority compliance, unguided benchmark performance, real consumer owner selection, global installation/catalog discovery, ChatGPT parity, app interruption/crash recovery, or production behavior. The same one coordinator and four references remain (101 coordinator lines; phase references 82/41/36/50 lines). No runtime/helper/service/store was added. Source delivery and the governing umbrella's combined acceptance remain pending at this entry; completed representative umbrella count remains zero.
