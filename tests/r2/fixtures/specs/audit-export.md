# Operator audit export

Add a CSV export of parcel audit records for operators. The source data includes parcel IDs, project IDs, owner email addresses, and event timestamps. The export must work on the current supported Python version without third-party dependencies.

The security team's `policy/export-policy.md` defines who may export, whether owners' email addresses must be redacted, and the audit retention requirement. This companion contract is required to determine correct visibility and access behavior; this specification does not own those decisions.

Acceptance includes CSV schema stability, policy-correct authorization and redaction, empty-input handling, and evidence that unauthorized users cannot obtain protected values. A technical implementation must preserve existing structured status values and exit codes.
