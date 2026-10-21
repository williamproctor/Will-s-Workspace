#!/usr/bin/env python3
"""Work out which Monday Signal edition is due and which weeks are missing.

Editions are dated on Mondays and cover the previous Monday through Sunday.
"Now" is read in US Pacific time: a Sunday-night or Monday run resolves to that
Monday's edition, and a Tuesday-Saturday run resolves to the most recent Monday.

Usage:
  python3 scripts/edition_dates.py            # human-readable summary
  python3 scripts/edition_dates.py --json     # machine-readable
  python3 scripts/edition_dates.py --slug 2026-10-26
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "editions" / "manifest.json"
PACIFIC = ZoneInfo("America/Los_Angeles")


def due_monday(today: dt.date) -> dt.date:
    if today.weekday() == 6:
        return today + dt.timedelta(days=1)
    return today - dt.timedelta(days=today.weekday())


def long_date(d: dt.date) -> str:
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def describe(monday: dt.date) -> dict:
    start = monday - dt.timedelta(days=7)
    end = monday - dt.timedelta(days=1)
    return {
        "slug": monday.isoformat(),
        "title": f"Week of {long_date(monday)}",
        "heading": f"# Monday Signal — Week of {long_date(monday)}",
        "window_start": start.isoformat(),
        "window_end": end.isoformat(),
        "window": f"Monday {start.strftime('%B')} {start.day} – Sunday {end.strftime('%B')} {end.day}, {end.year}",
        "previous_slug": start.isoformat(),
        "next_slug": (monday + dt.timedelta(days=7)).isoformat(),
    }


def published_slugs() -> list[str]:
    data = json.loads(MANIFEST.read_text())
    return sorted(e["slug"] for e in data["editions"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--slug", help="Override the due edition (YYYY-MM-DD, a Monday).")
    parser.add_argument("--json", action="store_true", help="Print JSON.")
    args = parser.parse_args()

    now = dt.datetime.now(PACIFIC)
    if args.slug:
        monday = dt.date.fromisoformat(args.slug)
        if monday.weekday() != 0:
            parser.error(f"{args.slug} is a {monday.strftime('%A')}, not a Monday")
    else:
        monday = due_monday(now.date())

    slugs = published_slugs()
    latest = slugs[-1] if slugs else None
    missing = []
    if latest:
        cursor = dt.date.fromisoformat(latest) + dt.timedelta(days=7)
        while cursor <= monday:
            missing.append(cursor.isoformat())
            cursor += dt.timedelta(days=7)
    elif monday.isoformat() not in slugs:
        missing.append(monday.isoformat())

    info = describe(monday)
    info.update({
        "now_pacific": now.isoformat(timespec="minutes"),
        "production_date": now.date().isoformat(),
        "already_published": monday.isoformat() in slugs,
        "latest_published": latest,
        "missing_editions": missing,
    })

    if args.json:
        print(json.dumps(info, indent=2))
        return 0

    print(f"Now (Pacific):      {info['now_pacific']}")
    print(f"Due edition:        {info['slug']}  ({info['title']})")
    print(f"Coverage window:    {info['window']}")
    print(f"Already published:  {info['already_published']}")
    print(f"Latest published:   {latest}")
    print(f"Missing editions:   {', '.join(missing) if missing else 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
