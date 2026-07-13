#!/usr/bin/env python3
"""Run the required weekly builds, including NotebookLM producer briefs.

Usage:
  python3 scripts/build_weekly_edition.py 2026-07-10 \
      --video-title "The Workflow Is the Unit"

This command:
  1. Generates or validates NotebookLM podcast/video producer briefs.
  2. Runs the edition's public-site build script.
  3. Builds the full and simplified SharePoint HTML.
  4. Revalidates the NotebookLM briefs.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
NEWSLETTER_ROOT = SCRIPT_DIR.parent


def run(command: list[str]) -> None:
    print(f"→ {' '.join(command)}")
    subprocess.run(command, cwd=NEWSLETTER_ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Edition date in YYYY-MM-DD format.")
    parser.add_argument(
        "--video-title",
        help="Suggested title used in the NotebookLM video brief.",
    )
    parser.add_argument(
        "--force-briefs",
        action="store_true",
        help="Overwrite manually refined NotebookLM briefs.",
    )
    args = parser.parse_args()

    try:
        edition_date = datetime.strptime(args.slug, "%Y-%m-%d")
    except ValueError as exc:
        parser.error(str(exc))

    builder = NEWSLETTER_ROOT / (
        f"build_{edition_date.strftime('%b').lower()}{edition_date.day:02d}.py"
    )
    if not builder.exists():
        parser.error(
            f"Public build script does not exist: {builder.name}. "
            "Create the per-edition build script first."
        )

    brief_command = [
        sys.executable,
        "scripts/generate_notebooklm_briefs.py",
        args.slug,
    ]
    if args.video_title:
        brief_command.extend(["--video-title", args.video_title])
    if args.force_briefs:
        brief_command.append("--force")

    run(brief_command)
    run([sys.executable, builder.name])
    run(
        [
            sys.executable,
            "sharepoint-package/build_sharepoint.py",
            args.slug,
        ]
    )
    run(
        [
            sys.executable,
            "scripts/generate_notebooklm_briefs.py",
            args.slug,
            "--check",
        ]
    )

    print(f"✓ Weekly build complete for {args.slug}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
