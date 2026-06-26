#!/usr/bin/env python3
"""
Build SharePoint-ready HTML body files for a given AVS AI Dispatch edition.

Produces two HTML files per edition:
  - YYYY-MM-DD-full.html      (full edition)
  - YYYY-MM-DD-summary.html   (quick summary)

Each file is body-only (no <html>, <head>, <body> wrappers), contains a
scoped <style> block at the top, and has no JavaScript. Drop each file
into a SharePoint document library, then reference the file URL from a
SharePoint list item (see SHAREPOINT_LIST_SCHEMA.md).

Usage:
  python3 build_sharepoint.py 2026-04-17
  python3 build_sharepoint.py --all          # rebuild every edition found in ../editions/
"""

import argparse
import html
import os
import re
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
NEWSLETTER_ROOT = os.path.dirname(ROOT)
EDITIONS_DIR = os.path.join(NEWSLETTER_ROOT, "editions")
OUT_ROOT = os.path.join(ROOT, "editions")

# Public site origin — used to rewrite relative asset paths (e.g.
# /editions/2026-04-24/arena-leaderboard.png) to absolute URLs so that
# images and cross-edition links still resolve once the HTML body is
# embedded inside a SharePoint page (different origin, no base URL).
PUBLIC_SITE_ORIGIN = "https://avaidispatch.com"


# ───────────────────────────────────────────────────────────────────────────────
# Markdown → HTML (port of shared.js markdownToHtml / convertTables / convertLists)
# ───────────────────────────────────────────────────────────────────────────────

def convert_tables(md: str) -> str:
    lines = md.split("\n")
    out, in_table, is_header = [], False, True
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if all(re.fullmatch(r"[-:]+", c) for c in cells):
                continue
            if not in_table:
                out.append("<table>")
                in_table = True
                is_header = True
            tag = "th" if is_header else "td"
            out.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>")
            if is_header:
                is_header = False
        else:
            if in_table:
                out.append("</table>")
                in_table = False
            out.append(line)
    if in_table:
        out.append("</table>")
    return "\n".join(out)


def convert_lists(md: str) -> str:
    lines = md.split("\n")
    out, in_list = [], False
    for line in lines:
        m = re.match(r"^- (.+)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{m.group(1)}</li>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(line)
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def markdown_to_html(md: str) -> str:
    code_blocks: list[str] = []

    def stash_code_block(match: re.Match) -> str:
        idx = len(code_blocks)
        code = match.group(1).rstrip("\n")
        code_blocks.append(f"<pre><code>{html.escape(code)}</code></pre>")
        return f"\n@@CODEBLOCK_{idx}@@\n"

    md = re.sub(r"```[^\n]*\n([\s\S]*?)```", stash_code_block, md)
    md = convert_tables(md)
    md = convert_lists(md)

    md = re.sub(r"^### (.+)$", r"<h3>\1</h3>", md, flags=re.M)
    md = re.sub(r"^## (.+)$", r"<h2>\1</h2>", md, flags=re.M)
    md = re.sub(r"^# (.+)$", "", md, flags=re.M)
    md = re.sub(r"^> (.+)$", r"<blockquote>\1</blockquote>", md, flags=re.M)
    md = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", md)
    md = re.sub(r"\*(.+?)\*", r"<em>\1</em>", md)
    md = re.sub(r"`([^`]+)`", r"<code>\1</code>", md)
    md = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        r'<figure class="edition-figure"><img src="\2" alt="\1" loading="lazy"><figcaption>\1</figcaption></figure>',
        md,
    )
    md = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        md,
    )
    md = re.sub(r"^---$", "<hr>", md, flags=re.M)
    md = md.replace("\n\n", "</p><p>")
    md = re.sub(r"^(?!<)(.+)$", r"<p>\1</p>", md, flags=re.M)
    md = md.replace("<p></p>", "")
    md = re.sub(r"<p>(<h[23]>)", r"\1", md)
    md = re.sub(r"(</h[23]>)</p>", r"\1", md)
    md = re.sub(r"<p>(<hr[^>]*>)</p>", r"\1", md)
    md = re.sub(r"<p>(<blockquote>)", r"\1", md)
    md = re.sub(r"(</blockquote>)</p>", r"\1", md)
    md = re.sub(r"<p>(<table)", r"\1", md)
    md = re.sub(r"(</table>)</p>", r"\1", md)
    md = re.sub(r"<p>(<ul)", r"\1", md)
    md = re.sub(r"(</ul>)</p>", r"\1", md)
    md = re.sub(r"<p>(<figure)", r"\1", md)
    md = re.sub(r"(</figure>)</p>", r"\1", md)
    md = re.sub(
        r"<p>@@CODEBLOCK_(\d+)@@</p>",
        lambda m: code_blocks[int(m.group(1))],
        md,
    )
    md = re.sub(
        r"@@CODEBLOCK_(\d+)@@",
        lambda m: code_blocks[int(m.group(1))],
        md,
    )
    return md


# ───────────────────────────────────────────────────────────────────────────────
# Scoped CSS — all rules namespaced to .avs-dispatch so we don't collide with
# SharePoint's own page styles. No @font-face or external fonts — SharePoint
# sandboxes will often strip them anyway. Font stack falls back cleanly.
# ───────────────────────────────────────────────────────────────────────────────

SCOPED_CSS = """
.avs-dispatch {
  --dispatch-blue: #4a6da7;
  --dispatch-blue-05: rgba(74, 109, 167, 0.05);
  --dispatch-blue-10: rgba(74, 109, 167, 0.10);
  --parchment: #f5f0e8;
  --parchment-light: #faf8f3;
  --parchment-dark: #ddd5c4;
  --ink: #1a1a2e;
  --ink-soft: #2d2d42;
  --ink-muted: #4a4a5e;
  --ink-faint: #9e9eb0;
  --white: #ffffff;
  --radius: 12px;
  --radius-lg: 16px;
  font-family: "Segoe UI", "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--ink);
  line-height: 1.7;
  max-width: 1080px;
  margin: 0 auto;
  background: var(--parchment-light);
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--parchment-dark);
}
.avs-dispatch * { box-sizing: border-box; }
.avs-dispatch .edition-header {
  padding: 24px 32px;
  border-bottom: 1px solid var(--parchment-dark);
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 12px;
  background: var(--parchment-light);
}
.avs-dispatch .edition-badge {
  font-family: "Consolas", "JetBrains Mono", monospace;
  font-size: 10px; font-weight: 500;
  letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--white); background: var(--dispatch-blue);
  padding: 4px 12px; border-radius: 999px;
  display: inline-block;
}
.avs-dispatch .edition-date {
  font-size: 13px; color: var(--ink-muted);
  margin-left: 12px;
}
.avs-dispatch .edition-kicker {
  font-size: 11px; color: var(--ink-faint);
  letter-spacing: 1px; text-transform: uppercase;
  font-weight: 600;
}
.avs-dispatch .edition-body { padding: 36px 32px; }
.avs-dispatch .edition-body h2 {
  font-size: 24px; font-weight: 800;
  letter-spacing: -0.5px; margin: 36px 0 12px;
  color: var(--ink);
}
.avs-dispatch .edition-body h2:first-child { margin-top: 0; }
.avs-dispatch .edition-body h3 {
  font-size: 17px; font-weight: 700; letter-spacing: -0.3px;
  margin: 28px 0 8px;
  color: var(--ink-soft);
}
.avs-dispatch .edition-body p {
  color: var(--ink-muted); margin: 0 0 14px;
  font-size: 15px; line-height: 1.7;
}
.avs-dispatch .edition-body a {
  color: var(--dispatch-blue); text-decoration: none;
  border-bottom: 1px solid var(--dispatch-blue-10);
  transition: border-color 0.2s;
}
.avs-dispatch .edition-body a:hover { border-bottom-color: var(--dispatch-blue); }
.avs-dispatch .edition-body code {
  font-family: "Consolas", "JetBrains Mono", monospace; font-size: 13px;
  background: var(--dispatch-blue-05);
  padding: 2px 6px; border-radius: 4px;
}
.avs-dispatch .edition-body pre {
  margin: 18px 0;
  padding: 16px 18px;
  overflow-x: auto;
  border: 1px solid rgba(74, 109, 167, 0.14);
  border-radius: var(--radius);
  background: var(--dispatch-blue-05);
}
.avs-dispatch .edition-body pre code {
  display: block;
  padding: 0;
  border-radius: 0;
  background: transparent;
  color: var(--ink-soft);
  font-size: 13px;
  line-height: 1.65;
  white-space: pre;
}
.avs-dispatch .edition-body blockquote {
  border-left: 3px solid var(--dispatch-blue);
  padding: 14px 20px; margin: 20px 0;
  background: var(--dispatch-blue-05);
  border-radius: 0 var(--radius) var(--radius) 0;
  font-style: italic; color: var(--ink-muted);
}
.avs-dispatch .edition-body table {
  width: 100%; border-collapse: collapse;
  margin: 20px 0; font-size: 13px;
}
.avs-dispatch .edition-body th {
  font-family: "Consolas", "JetBrains Mono", monospace;
  font-size: 10px; font-weight: 500;
  letter-spacing: 1px; text-transform: uppercase;
  color: var(--ink-faint); text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid var(--parchment-dark);
  background: var(--parchment-light);
}
.avs-dispatch .edition-body td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--parchment);
  color: var(--ink-muted);
}
.avs-dispatch .edition-body ul { margin: 14px 0; padding-left: 20px; }
.avs-dispatch .edition-body li {
  color: var(--ink-muted); font-size: 15px;
  line-height: 1.7; margin-bottom: 6px;
}
.avs-dispatch .edition-body li strong { color: var(--ink-soft); }
.avs-dispatch .edition-body hr {
  border: none; border-top: 1px solid var(--parchment-dark);
  margin: 32px 0;
}
.avs-dispatch .edition-body strong { color: var(--ink-soft); }
.avs-dispatch .edition-body em { color: var(--ink-soft); }
.avs-dispatch .edition-figure {
  margin: 24px 0; text-align: center;
}
.avs-dispatch .edition-figure img {
  max-width: 100%; height: auto; border-radius: var(--radius);
}
.avs-dispatch .edition-figure figcaption {
  font-size: 12px; color: var(--ink-faint);
  margin-top: 8px; font-style: italic;
}
@media (max-width: 640px) {
  .avs-dispatch .edition-header { padding: 16px 20px; }
  .avs-dispatch .edition-body { padding: 24px 20px; }
  .avs-dispatch .edition-body h2 { font-size: 20px; }
}
""".strip()


# ───────────────────────────────────────────────────────────────────────────────
# HTML wrapper — body-only, no <html>/<head>/<body>
# ───────────────────────────────────────────────────────────────────────────────

def absolutize_local_urls(html: str, origin: str = PUBLIC_SITE_ORIGIN) -> str:
    """Rewrite root-relative src/href (e.g. "/editions/.../img.png") to absolute
    URLs on the public site. Protocol-relative (//) and already-absolute URLs
    (http://, https://, mailto:, data:, #fragment) are left alone."""
    def _sub(match: re.Match) -> str:
        attr, quote, path = match.group(1), match.group(2), match.group(3)
        return f'{attr}={quote}{origin}{path}{quote}'
    return re.sub(r'\b(src|href)=(["\'])(/[^/][^"\']*)\2', _sub, html)


def ascii_safe(html: str) -> str:
    """Encode all non-ASCII characters as numeric HTML entities.

    SharePoint document libraries usually serve HTML with charset=utf-8, but
    Page Viewer / Content Query / pasted-content scenarios sometimes strip or
    override the Content-Type header, producing mojibake (em-dashes appear as
    "â€"", etc.). Converting to numeric entities makes the file ASCII-safe so
    it renders correctly regardless of how SharePoint serves it.
    """
    return html.encode("ascii", "xmlcharrefreplace").decode("ascii")


def build_body_html(*, slug: str, kicker: str, edition_label: str, inner_html: str) -> str:
    """Wrap rendered edition HTML in a scoped Dispatch container."""
    body = (
        f'<!-- AVS AI Dispatch \u2014 {edition_label} ({kicker}) -->\n'
        f'<!-- Scoped to .avs-dispatch; no JavaScript; body-only HTML. -->\n'
        f'<style>\n{SCOPED_CSS}\n</style>\n'
        f'<div class="avs-dispatch">\n'
        f'  <div class="edition-header">\n'
        f'    <div>\n'
        f'      <span class="edition-badge">{slug}</span>\n'
        f'      <span class="edition-date">{edition_label}</span>\n'
        f'    </div>\n'
        f'    <div class="edition-kicker">{kicker}</div>\n'
        f'  </div>\n'
        f'  <div class="edition-body">\n'
        f'{inner_html}\n'
        f'  </div>\n'
        f'</div>\n'
    )
    return ascii_safe(absolutize_local_urls(body))


def format_edition_label(slug: str) -> str:
    """Convert 2026-04-17 → 'Week of April 17, 2026'."""
    try:
        dt = datetime.strptime(slug, "%Y-%m-%d")
        return f"Week of {dt.strftime('%B %-d, %Y')}"
    except ValueError:
        return slug


# ───────────────────────────────────────────────────────────────────────────────
# Main
# ───────────────────────────────────────────────────────────────────────────────

def build_edition(slug: str) -> None:
    full_md_path = os.path.join(EDITIONS_DIR, f"{slug}.md")
    simple_md_path = os.path.join(EDITIONS_DIR, f"{slug}-simplified.md")

    if not os.path.exists(full_md_path):
        print(f"  ✗ Missing: {full_md_path}", file=sys.stderr)
        return

    out_dir = os.path.join(OUT_ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    edition_label = format_edition_label(slug)

    with open(full_md_path, "r", encoding="utf-8") as f:
        full_md = f.read()
    full_inner = markdown_to_html(full_md)
    full_html = build_body_html(
        slug=slug, kicker="Full Edition",
        edition_label=edition_label, inner_html=full_inner,
    )
    full_out = os.path.join(out_dir, f"{slug}-full.html")
    with open(full_out, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"  ✓ {full_out}  ({len(full_html):,} chars)")

    if os.path.exists(simple_md_path):
        with open(simple_md_path, "r", encoding="utf-8") as f:
            simple_md = f.read()
        simple_inner = markdown_to_html(simple_md)
        simple_html = build_body_html(
            slug=slug, kicker="Quick Summary",
            edition_label=edition_label, inner_html=simple_inner,
        )
        simple_out = os.path.join(out_dir, f"{slug}-summary.html")
        with open(simple_out, "w", encoding="utf-8") as f:
            f.write(simple_html)
        print(f"  ✓ {simple_out}  ({len(simple_html):,} chars)")
    else:
        print(f"  - No simplified source for {slug} (skipping summary)")


def discover_editions() -> list:
    slugs = set()
    if not os.path.isdir(EDITIONS_DIR):
        return []
    for name in os.listdir(EDITIONS_DIR):
        m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})(?:-simplified)?\.md", name)
        if m:
            slugs.add(m.group(1))
    return sorted(slugs)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build SharePoint-ready HTML body files.")
    parser.add_argument("slug", nargs="?", help="Edition slug, e.g. 2026-04-17")
    parser.add_argument("--all", action="store_true", help="Rebuild every edition")
    args = parser.parse_args()

    if args.all:
        slugs = discover_editions()
        if not slugs:
            print("No editions found.", file=sys.stderr)
            return 1
        print(f"Building {len(slugs)} edition(s):")
        for slug in slugs:
            print(f"\n{slug}:")
            build_edition(slug)
    elif args.slug:
        print(f"Building {args.slug}:")
        build_edition(args.slug)
    else:
        parser.print_help()
        return 2

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
