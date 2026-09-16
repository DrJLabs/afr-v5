# Shared report semantics

Deliver two independently usable outcomes: a terminal summary and a CSV report. Both consume the events accepted by `report_rows` and report one current record per parcel ID. A later event for the same ID replaces the earlier event. CSV depends on the shared semantics being established in the summary outcome, not merely proposed in a plan.

Both formats must agree on selected records, ordering, status values, and total counts. Preserve the existing structured status values, unknown-status passthrough, and CLI exit codes. No data access or visibility change is included. Keep Python 3.10 and standard-library-only support. No database, new service, or network connection is needed.

The implementer may choose an internal shared representation and factoring, but must state a single ordering decision consistent with current behavior before the two formats are built. Internal function names and file layout are advisory choices. A human label may be formatted differently from the machine status; the CSV machine status must not silently become a display label.

Each outcome must be independently checked against these semantics. Parent acceptance requires the same input, including repeated IDs, unknown statuses, and empty input, to produce equivalent selected records and totals in both formats. The authorized delivery endpoint is local candidates only. No PR or merge is requested. This source can serve as the parent plan without an additional plan file.
