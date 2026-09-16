# Terminal and CSV reporting

This is the authoritative parent contract. Build two independently usable outputs for the parcel event stream. The existing domain API is a required companion: inspect `parcel.py` and retain its raw records, latest-event-per-ID selection, ascending lexical ID order, status vocabulary, and exit-code mapping. Python 3.10 and the standard library remain sufficient.

## Outcomes, in execution order

1. **Readable terminal report.** Apply `specs/readable-report.md` to `cli.py` and its API. Its verified local candidate establishes the reporting behavior on which the second outcome depends. Preserve the domain API; do not replace raw statuses with labels in structured data.
2. **CSV consumer.** After the first outcome's verified local candidate is present, add `export_csv.py` with `render_csv(events)` returning CSV text and a CLI reading a JSON list from stdin. Use the selected domain rows, header `id,status`, raw status values, standard CSV quoting, and a newline after every record. Empty input yields the header alone. Its CLI exit code uses the same selected-row exit-code mapping as the terminal CLI. Invalid JSON handling and additional modes are out of scope.

## Shared acceptance and endpoint

Both outputs must describe the same selected parcel IDs in the same lexical order and the same latest statuses, with labels only in terminal text. Check both APIs and invoked CLIs, including duplicate IDs, lexical ordering such as `10` before `2`, all known statuses, an unknown status, empty input, and CSV quoting for an ID containing a comma. The combined acceptance boundary is the local candidate containing both consumers; individually passing consumer tests alone do not establish it.

Use lean assurance for this disposable standard-library fixture: focused behavioral checks and actual-diff self-review are sufficient. All outcomes stop at verified local candidates. No commits, network, publication, merge, installation, production effects, or deletion of unrelated work. Preserve operator notes and existing source ownership. Implementation and causal in-scope correction are authorized when this plan is selected for execution; planning/review-only invocations remain read-only. Do not create another plan or progress journal.
