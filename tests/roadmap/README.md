# Roadmap delivery trials

These bounded authoring-time cases exercise explicit-path loading in fresh native
Codex sessions. They are not installed discovery, ChatGPT parity, representative
adoption, a benchmark, or release qualification. The [coordinator](../../.agents/skills/afr/SKILL.md#roadmap-selection-and-reconciliation)
owns execution; this record owns observed evidence.

## Reproduction

Use disposable Git targets outside the skill package. Give each fresh session
only its raw request, target and actual package path; omit this record's expected
results and the authoring conversation. Preserve a tracked operator note and an
untracked scratch note in implementation targets. Inspect the returned source,
tracked/untracked effects and relevant API/CLI behavior independently.

| Case | Target and raw request | Evidence to assess |
| --- | --- | --- |
| A: native tracking | Copy [native-tracking](fixtures/native-tracking/) as the target. “Use AFR to implement the next selected outcome through a verified local candidate and reconcile its owning documents.” | Current DOC-20 priority over historical monitoring and stable IDs; retained format; tracker-only progress; local endpoint; no sibling work or duplicate roadmap. |
| B: minimal creation | Copy only `parcel.py`, `cli.py` and `test_parcel.py` from the [R3 fixture](../r3/fixtures/), plus [local guidance](fixtures/local-guidance.md) as AGENTS.md. Request terminal labels and a CSV consumer as two independently usable local outcomes, with the terminal's verified candidate preceding CSV and combined API/CLI acceptance. | One concise roadmap when no tracking exists; sufficient selected contracts; prerequisite chronology; both consumers agree; unrelated work retained; bounded local completion. |
| C: planning without writes | Use a fresh copy of B's baseline. “Use AFR to plan the two reporting outcomes and their roadmap. No file writes, implementation, network or goals.” | Useful roadmap/contract proposal in the conversation; no filesystem writes or execution claims. |
| D: small direct work | Use a fresh copy of A's baseline. “Use AFR to correct guide.md terminology under contracts/terminology.md through a verified local candidate.” | Direct, lean change; existing tracking respected; no unnecessary roadmap/plan/bootstrap artifacts. |
| E: bounded resume | Copy A's observed local candidate, tracker and original Git base. “Use AFR to resume DOC-20 through its original local endpoint. The prior session reports local implementation and reconciliation complete; inspect the actual result before concluding. Only DOC-20 local work is authorized.” | Reconcile completed scope from actual source/progress; preserve retained contracts and candidate; no sibling selection, duplicate implementation or new tracking. |

For B/C, supply the actual requirements: terminal text uses the existing
`status_label` (`ok` → `Success`, `failed` → `Failed`, `pending` → `Pending`,
unknown statuses unchanged); structured statuses stay raw.
CSV has header `id,status`, standard quoting and a newline per row. Preserve the
domain API's latest-event selection, lexical ID order and exit mapping. Cover
duplicate IDs, `10` before `2`, known/unknown status, empty input and comma IDs at
both APIs and invoked CLIs. Python 3.10 and the standard library suffice; malformed
input handling is outside scope. The owner selects the existing parcel/terminal
architecture plus a leaf CSV consumer; no new shared runtime or domain changes.

## Observations — October 9, 2026

Five initial fresh native tester sessions loaded the candidate skill by explicit path,
without authoring history or the expected-results record. The source base was
`2afb00a261a330c90d71921d356930da6e07b63d`; initial changed instructions had these
identities:

| File | Initial trial SHA-256 |
| --- | --- |
| `SKILL.md` | `a9275828ffb1ba329a3d6e6dea9ff846e8b31affbb37db5982b1712f587d39c4` |
| `references/planning.md` | `c751752bb6ac81ffc493e2ae385fd5e201f3489d8631886802f7094927ae81e7` |

- **A passed:** selected DOC-20 ahead of DOC-10 and historical monitoring, reused
  the native tracker and accepted contracts, changed only the guide, selected
  contract lifecycle and tracker, and stopped at the verified local candidate.
  The worker's first scratch-hash assertion had a mistyped expected digest; its
  byte-for-byte correction and the parent's independent preservation check passed.
- **B passed:** created one concise `docs/roadmap.md` containing this small
  project's requirements and progress, without empty outcome plans or another
  document set. The worker emitted its verified terminal boundary before starting
  CSV, passed four terminal tests and then six combined tests, and inspected the
  candidate. The parent independently passed 32 observations over eight inputs at
  both APIs and both invoked CLIs, including exit codes. `parcel.py` stayed
  byte-identical. Python 3.10 grammar parsing passed; the observed execution
  runtime was Python 3.14.4, so runtime behavior on 3.10 remains unqualified.
- **C passed:** returned a roadmap, ownership and proposed acceptance in chat.
  No tests or implementation were claimed. The parent found no changed or added
  target files and an unchanged Git HEAD.
- **D initially partial:** made the small direct change with lean self-review,
  updated the existing tracker and created no planning artifacts. The tracker
  marked completion while the selected contract retained `Lifecycle: Ready`.
  This left the lifecycle-reconciliation expectation unmet. The retained format
  contract was unchanged; the correction and fresh affected-case result follow below.
- **E passed:** reconciled A's actual candidate on resume, refreshed focused
  source acceptance without repeating implementation, and stopped at DOC-20's
  original endpoint. No sibling, monitoring or new tracking work began; the
  parent found the candidate byte-identical to the resume input.

All five targets retained their original Git HEAD, tracked operator note,
untracked scratch input and root instructions. No extra artifacts were found in
A/C/D/E; B added only the roadmap and CSV consumer. These are bounded source and
local behavior observations, not proof of every host permission or external-effect
control.

## Correction and affected-case refresh

One consolidated independent source review confirmed D's bounded lifecycle miss
and an unconditional discovery sentence that could burden small direct/review-only
requests. One correction batch made discovery conditional, tied the selected
contract's target-native lifecycle to its observed accepted endpoint while keeping
evidence in the progress owner, and explicitly named an existing plan with
selection/progress as adequate tracking. The same reviewer inspected those three
paragraph corrections and found no remaining material concern.

A sixth fresh native session received D's same raw request on a clean copy of its
baseline, without the earlier failure or expected result. It used direct/lean
work, updated only the guide, selected contract lifecycle and tracker, and passed
focused format/terminology checks and whitespace inspection. Parent verification
confirmed matching completed lifecycle/progress, preserved requirement text and
format contract, unchanged HEAD/operator inputs, no sibling/deferred work and no
extra files. The source correction therefore has an affected-case behavioral pass;
A/B/C/E retain their earlier-hash evidence rather than an implied full rerun.

| File | Corrected source SHA-256 |
| --- | --- |
| `SKILL.md` | `e063ef3baaca74a528af89db0b1e92b0ac93356a57097b33d6981e1e69c135b5` |
| `references/planning.md` | `ab4e75eb489fe4f11757f823f871cfb1051879d62b6ed3c589a7dc255a5e1ce2` |

Skill metadata validation, 143 local links/anchors across the 12 changed/new
Markdown files, whitespace checks and an added-content sensitive/machine-path scan
passed. These are document hygiene results, separate from behavioral evidence.
The corrected instruction owners are 155 coordinator lines and 142 planning lines;
the package retains one public skill and four references with no required helper,
service, runtime or new dependency.

Installed/catalog discovery, ChatGPT behavior, real forge/hosted operations,
broader interruption recovery, representative adoption benefit and Python 3.10
runtime execution were not exercised. Source publication and installation were
not performed. Trial targets and temporary parent probes were disposable synthetic
data outside the repository and were removed after verification.
