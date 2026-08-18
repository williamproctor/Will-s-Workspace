#!/usr/bin/env python3
"""Source-diversity check for The Monday Signal.

Counts linked domains in each edition markdown file and flags editions where a
single publication dominates the citations. The rule this enforces: synthesis
and roundup outlets are discovery tools, not citation crutches. Every story
should cite the outlet that did the original reporting, the vendor's own
report, the company filing, or the primary post.

Primary-source platforms (x.com, linkedin.com, youtube.com, podcast hosts) are
exempt from the failure threshold because concentration there means the
primary-source policy is working, not failing.

Usage:
    python3 scripts/check_source_diversity.py                 # check all editions
    python3 scripts/check_source_diversity.py 2026-08-17.md   # check one

Exit code 1 if any edition fails.
"""

import re
import sys
from collections import Counter
from pathlib import Path

EDITIONS_DIR = Path(__file__).resolve().parent.parent / "editions"

# Domains where heavy concentration is expected and desired (primary posts,
# episodes, and the subject companies' own documents).
PRIMARY_PLATFORMS = {
    "x.com",
    "linkedin.com",
    "youtube.com",
    "podscripts.co",
    "listennotes.com",
    "podcasts.apple.com",
    "open.spotify.com",
}

FAIL_SHARE = 0.40  # a single outlet backing 40%+ of links means it wrote the edition
WARN_SHARE = 0.22
FAIL_MIN_LINKS = 8  # ignore tiny editions where shares are noisy


def domain_of(url: str) -> str:
    m = re.match(r"https?://([^/)\s\"]+)", url)
    if not m:
        return ""
    host = m.group(1).lower()
    return host[4:] if host.startswith("www.") else host


def check_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    urls = re.findall(r"https?://[^\s)\"<>]+", text)
    counts = Counter(domain_of(u) for u in urls if domain_of(u))
    total = sum(counts.values())
    ok = True

    print(f"\n{path.name} — {total} links")
    for dom, n in counts.most_common(6):
        share = n / total if total else 0
        tag = ""
        if dom not in PRIMARY_PLATFORMS and total >= FAIL_MIN_LINKS:
            if share >= FAIL_SHARE:
                tag = "  << FAIL: one outlet dominates; cite the origins instead"
                ok = False
            elif share >= WARN_SHARE:
                tag = "  << warn: getting heavy; check each cite is their original reporting"
        print(f"  {n:3d}  {share:5.1%}  {dom}{tag}")
    return ok


def main() -> int:
    args = sys.argv[1:]
    if args:
        files = [EDITIONS_DIR / a for a in args]
    else:
        files = sorted(
            p for p in EDITIONS_DIR.glob("*.md") if p.name != "manifest.json"
        )
    all_ok = all([check_file(p) for p in files])
    print("\n" + ("PASS: no single outlet dominates any edition." if all_ok
                  else "FAIL: re-source the flagged editions to original reporting."))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
