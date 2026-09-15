# Correct the success label

Change the human-readable label returned for status `ok` from `Sucess` to `Success`.

Preserve the structured status value `ok`, all CLI exit codes, all other labels, unknown-status passthrough, and the `status_label` interface. This change does not involve report ordering, new statuses, dependencies, or data access.

Acceptance: `status_label("ok")` is `Success`; known and unknown other statuses retain their behavior; `EXIT_CODES` is unchanged. Focused checks of these examples and the actual diff are sufficient. Likely location: `parcel.py`; this is an implementation suggestion, not an obligation to restructure the module.

This specification is sufficient as the planning source. No separate plan document is requested.
