# Operator report ordering

Change the operator report produced from `report_rows`.

Acceptance requires every output to be sorted by ascending parcel ID. Acceptance also requires output to preserve input arrival order, including inputs whose IDs are not ascending. Both requirements are binding; the product owner has not chosen a precedence rule or authorized relaxing either requirement.

Continue to keep only the latest event for each parcel ID. Preserve structured status values, unknown-status passthrough, CLI exit codes, Python 3.10, and standard-library-only support. No data-visibility change, service, network connection, or remote delivery is included.
