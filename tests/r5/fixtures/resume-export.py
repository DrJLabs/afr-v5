"""CSV consumer candidate used by the interrupted-work trial."""

import csv
import io
import json
import sys

from parcel import EXIT_CODES


def selected_rows(events):
    selected = {}
    for event in events:
        selected.setdefault(event["id"], event)
    return [selected[key] for key in sorted(selected)]


def render_csv(events):
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["id", "status"])
    writer.writerows((row["id"], row["status"]) for row in selected_rows(events))
    return output.getvalue()


def main():
    events = json.load(sys.stdin)
    sys.stdout.write(render_csv(events))
    return max(
        (EXIT_CODES.get(row["status"], 0) for row in selected_rows(events)), default=0
    )


if __name__ == "__main__":
    raise SystemExit(main())
