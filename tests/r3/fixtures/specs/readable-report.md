# Human-readable terminal report

Use the established human-readable status labels in the terminal report emitted by `cli.py`, including its `render_report` API. `ok`, `failed`, and `pending` must display as `Success`, `Failed`, and `Pending`; unknown status strings pass through unchanged. The domain helper already defines this vocabulary.

Keep structured records, the `report_rows` API, and exit codes unchanged. Retain one row per parcel ID, the latest event for repeated IDs, ascending lexical ID order, and `Total: N` for the selected rows. Each output line ends in a newline; empty input produces only `Total: 0` and exits 0. The CLI still consumes a JSON list from standard input; invalid JSON handling is not part of this change.

Acceptance must cover both `render_report` and the invoked CLI, including known and unknown statuses, duplicates, non-ascending input IDs, empty input, and existing exit behavior. For example, events for `b/pending`, `a/paused`, then `b/ok` produce `a: paused`, `b: Success`, and `Total: 2`, each on its own line, with exit code 0. A single failed event exits 1; a single pending event exits 2.

Preserve Python 3.10 and standard-library-only support. No dependencies, access-policy changes, network operations, services, or new output modes are requested. This specification is the sufficient source contract; no separate plan file is needed. The endpoint is a verified local candidate, without commit, push, PR, or merge.
