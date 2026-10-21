#!/usr/bin/env python3
"""Pre-publication QA for one Monday Signal edition (full + simplified).

Errors (exit code 1) block publishing; warnings need a human or agent look.

Usage:
  python3 scripts/qa_edition.py 2026-10-26            # text checks + source diversity
  python3 scripts/qa_edition.py 2026-10-26 --urls     # also audit every cited URL
  python3 scripts/qa_edition.py 2026-10-26 --fix      # normalize curly quotes first
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDITIONS = ROOT / "editions"

FOOTER = ("*Monday Signal is a weekly AI and tech briefing for marketers, produced for the GrowthX team. "
          "Curated with AI assistance. Questions or suggestions? Reply to this message.*")
FULL_SECTIONS = ["## The Conversation", "## Voices", "## This Week in Marketing AI", "## Platform & Tool Watch",
                 "## Common Threads", "## Angles for the Week", "## Sources"]
SIMPLIFIED_SECTIONS = FULL_SECTIONS[:-1]
WORD_BUDGET = {"full": 5800, "simplified": 1500}
MAX_EDITOR_NOTES = 3

BANNED = [
    r"isn't just", r"not just", r"here's the", r"here is the", r"bottom line", r"worth noting", r"worth watching",
    r"worth it", r"the real question", r"it's important to", r"game-chang", r"\bdelve", r"testament", r"rather than",
    r"\bcrucial", r"\bpivotal", r"\blandscape", r"\bunderscor", r"\bhighlight(s|ed|ing)?\b", r"\bshowcas", r"\bseamless",
    r"\bnotabl", r"\brobust", r"\bleverag", r"\badditionally", r"\bmoreover", r"\bfurthermore", r"\bthe catch\b",
    r"\bthe trap\b", r"\bis real\b", r"\bthis matters\b", r"\bkey (role|takeaway|moment|lesson|question)",
]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
DATE_RE = re.compile(r"\b(" + "|".join(WEEKDAYS) + r"),? (" + "|".join(MONTHS) + r") (\d{1,2})\b")
QUOTED_RE = re.compile(r'"[^"\n]*"')
URL_RE = re.compile(r"https?://[^\s)\"<>]+")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def prose(line: str) -> str:
    """The line with URLs and double-quoted spans removed (quotes are verbatim, so rules skip them)."""
    line = re.sub(r"\]\(https?://[^)]+\)", "]", line)
    return QUOTED_RE.sub('""', line)


def is_exempt_line(n: int, line: str) -> bool:
    return n == 1 or line.startswith("**Source:**") or re.match(r"^\d+\. \[", line) is not None


def check_text(path: Path, kind: str, slug_date: dt.date, rep: Report) -> None:
    name = path.name
    if not path.exists():
        rep.error(f"{name}: missing")
        return
    text = path.read_text()
    lines = text.splitlines()

    expected_title = f"# Monday Signal — Week of {slug_date.strftime('%B')} {slug_date.day}, {slug_date.year}"
    if not lines or lines[0].strip() != expected_title:
        rep.error(f"{name}: first line should be '{expected_title}'")
    for section in FULL_SECTIONS if kind == "full" else SIMPLIFIED_SECTIONS:
        if section not in lines:
            rep.error(f"{name}: missing section '{section}'")
    if kind == "simplified" and "## Sources" in lines:
        rep.warn(f"{name}: simplified editions don't carry a Sources section")
    if FOOTER not in text:
        rep.error(f"{name}: footer line missing or altered")

    curly = len(re.findall("[\u201c\u201d\u2018\u2019]", text))
    if curly:
        rep.error(f"{name}: {curly} curly quote marks (run with --fix to normalize)")

    for n, line in enumerate(lines, 1):
        if is_exempt_line(n, line):
            continue
        body = prose(line)
        if "\u2014" in body:
            rep.error(f"{name}:{n}: em dash outside a verbatim quote: {line.strip()[:110]}")
        for pattern in BANNED:
            m = re.search(pattern, body, re.IGNORECASE)
            if m:
                rep.error(f"{name}:{n}: banned phrase '{m.group(0)}': {line.strip()[:110]}")
        for weekday, month, day in DATE_RE.findall(line):
            month_no = MONTHS.index(month) + 1
            year = slug_date.year
            if month_no == 12 and slug_date.month == 1:
                year -= 1
            elif month_no == 1 and slug_date.month == 12:
                year += 1
            try:
                actual = dt.date(year, month_no, int(day)).strftime("%A")
            except ValueError:
                rep.error(f"{name}:{n}: impossible date {month} {day}")
                continue
            if actual != weekday:
                rep.error(f"{name}:{n}: says {weekday}, {month} {day}, but that date is a {actual}")

    notes = len(re.findall(r"\*Editor's note", text))
    if notes > MAX_EDITOR_NOTES:
        rep.warn(f"{name}: {notes} editor's notes (keep to {MAX_EDITOR_NOTES} or fewer)")
    words = len(text.split())
    if words > WORD_BUDGET[kind]:
        rep.warn(f"{name}: {words} words (budget {WORD_BUDGET[kind]})")

    if kind == "full" and "## Sources" in lines:
        idx = lines.index("## Sources")
        body_urls = set(URL_RE.findall("\n".join(lines[:idx])))
        source_urls = set(URL_RE.findall("\n".join(lines[idx:])))
        missing = sorted(body_urls - source_urls)
        if missing:
            rep.warn(f"{name}: {len(missing)} body URL(s) not listed under Sources, e.g. {missing[0]}")


def check_diversity(slug: str, rep: Report) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_source_diversity.py"), f"{slug}.md", f"{slug}-simplified.md"],
        cwd=ROOT, capture_output=True, text=True,
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        rep.error("source diversity check failed (one outlet above 40%)")


def http_status(url: str) -> tuple[str, str]:
    result = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-L", "--max-time", "25", "-A", UA, "-w", "%{http_code}", url],
        capture_output=True, text=True,
    )
    return url, result.stdout.strip() or "000"


def check_urls(paths: list[Path], rep: Report) -> None:
    urls = sorted({u for p in paths if p.exists() for u in URL_RE.findall(p.read_text())})
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(http_status, urls))
    bad = [(u, c) for u, c in results if not c.startswith(("2", "3"))]
    print(f"URL audit: {len(urls)} unique URLs, {len(bad)} non-2xx/3xx")
    for url, code in bad:
        if code in ("404", "410"):
            rep.error(f"dead link ({code}): {url}")
        else:
            rep.warn(f"HTTP {code} (likely bot-blocking; confirm the exact URL appears in a search result): {url}")


def normalize_quotes(paths: list[Path]) -> None:
    for p in paths:
        if p.exists():
            t = p.read_text()
            fixed = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
            if fixed != t:
                p.write_text(fixed)
                print(f"normalized curly quotes in {p.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug")
    parser.add_argument("--urls", action="store_true", help="Audit every cited URL with curl.")
    parser.add_argument("--fix", action="store_true", help="Normalize curly quotes before checking.")
    args = parser.parse_args()

    slug_date = dt.date.fromisoformat(args.slug)
    full = EDITIONS / f"{args.slug}.md"
    simplified = EDITIONS / f"{args.slug}-simplified.md"
    if args.fix:
        normalize_quotes([full, simplified])

    rep = Report()
    check_text(full, "full", slug_date, rep)
    check_text(simplified, "simplified", slug_date, rep)
    check_diversity(args.slug, rep)
    if args.urls:
        check_urls([full, simplified], rep)

    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    print(f"\n{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
