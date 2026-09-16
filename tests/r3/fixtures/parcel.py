"""Minimal standard-library domain code for local workflow trials."""

EXIT_CODES = {"ok": 0, "failed": 1, "pending": 2}


def status_label(status):
    return {"ok": "Success", "failed": "Failed", "pending": "Pending"}.get(
        status, status
    )


def report_rows(events):
    latest = {}
    for event in events:
        latest[event["id"]] = event
    return [latest[key] for key in sorted(latest)]
