"""Print a local parcel report from a JSON event list on standard input."""

import json
import sys

from parcel import EXIT_CODES, report_rows


def render_report(events):
    rows = report_rows(events)
    lines = [f'{row["id"]}: {row["status"]}' for row in rows]
    lines.append(f"Total: {len(rows)}")
    return "\n".join(lines) + "\n"


def main():
    events = json.load(sys.stdin)
    sys.stdout.write(render_report(events))
    return max(
        (EXIT_CODES.get(row["status"], 0) for row in report_rows(events)), default=0
    )


if __name__ == "__main__":
    raise SystemExit(main())
