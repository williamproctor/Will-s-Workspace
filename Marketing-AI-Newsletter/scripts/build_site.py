#!/usr/bin/env python3
"""Build the newsletter site from config.json and editions/manifest.json.

One manifest, one builder: regenerates every edition page, the homepage,
robots.txt, and (when a domain is configured) sitemap.xml in a single pass.
No per-edition build scripts.

Usage:
  python3 scripts/build_site.py            # build everything
  python3 scripts/build_site.py --check    # validate inputs and outputs, write nothing
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.json"
MANIFEST_PATH = ROOT / "editions" / "manifest.json"
EDITIONS_DIR = ROOT / "editions"
SITE_DIR = ROOT / "site"
TEMPLATES_DIR = SITE_DIR / "templates"

SLUG_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TOKEN_RE = re.compile(r"\{\{[A-Z_]+\}\}")

ARROW_SVG = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
)


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def display_date(slug: str) -> str:
    d = datetime.strptime(slug, "%Y-%m-%d")
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def site_name_html(name: str) -> str:
    return esc(name).replace("&amp;", '<span class="amp">&amp;</span>')


def load_inputs() -> tuple[dict, list[dict]]:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    editions = manifest.get("editions", [])
    editions.sort(key=lambda e: e.get("slug", ""), reverse=True)
    return config, editions


def validate(config: dict, editions: list[dict]) -> list[str]:
    errors: list[str] = []

    for key in ("name", "tagline", "description", "publisher", "footerLine"):
        if not str(config.get(key, "")).strip():
            errors.append(f"config.json is missing '{key}'")

    if not editions:
        errors.append("manifest has no editions")

    seen: set[str] = set()
    for edition in editions:
        slug = edition.get("slug", "")
        label = slug or "<missing slug>"
        if not SLUG_RE.match(slug):
            errors.append(f"{label}: slug must be YYYY-MM-DD")
            continue
        if slug in seen:
            errors.append(f"{label}: duplicate slug")
        seen.add(slug)

        if not (EDITIONS_DIR / f"{slug}.md").exists():
            errors.append(f"{label}: editions/{slug}.md not found")
        if edition.get("hasSimplified") and not (EDITIONS_DIR / f"{slug}-simplified.md").exists():
            errors.append(f"{label}: hasSimplified is true but editions/{slug}-simplified.md not found")
        for key in ("title", "hook", "description"):
            if not str(edition.get(key, "")).strip():
                errors.append(f"{label}: manifest entry is missing '{key}'")
        if edition.get("hasVideo") and not str(edition.get("videoTitle", "")).strip():
            errors.append(f"{label}: hasVideo is true but videoTitle is empty")
        if edition.get("hasAudio") and not (SITE_DIR / "audio" / f"{slug}.m4a").exists():
            errors.append(f"{label}: hasAudio is true but site/audio/{slug}.m4a not found")
        if edition.get("hasVideo") and not (SITE_DIR / "video" / f"{slug}.mp4").exists():
            errors.append(f"{label}: hasVideo is true but site/video/{slug}.mp4 not found")

    for template in ("edition.template.html", "index.template.html"):
        if not (TEMPLATES_DIR / template).exists():
            errors.append(f"missing template site/templates/{template}")

    return errors


def og_url_block(config: dict, path: str) -> str:
    domain = str(config.get("domain", "")).rstrip("/")
    if not domain:
        return ""
    lines = [
        f'  <link rel="canonical" href="{domain}{path}">',
        f'  <meta property="og:url" content="{domain}{path}">',
    ]
    if (SITE_DIR / "og-image.png").exists():
        lines.append(f'  <meta property="og:image" content="{domain}/og-image.png">')
        lines.append('  <meta name="twitter:card" content="summary_large_image">')
    return "\n".join(lines)


# Brand mark: concentric signal rings with an offset satellite dot
# (per Will's 2026-08-18 logo redesign).
LOGO_MARK_SVG = """<svg viewBox="0 0 72 72" fill="none" aria-hidden="true">
        <circle cx="33" cy="39" r="28" stroke="#79d3a3" stroke-opacity="0.26" stroke-width="2"/>
        <circle cx="33" cy="39" r="19.5" stroke="#a5e8c0" stroke-opacity="0.55" stroke-width="2.6"/>
        <circle cx="33" cy="39" r="11.5" stroke="#d2f2da" stroke-opacity="0.9" stroke-width="3"/>
        <circle cx="33" cy="39" r="4" fill="#e9f8ea"/>
        <circle cx="62" cy="10" r="6.5" fill="#79d3a3"/>
      </svg>"""


def common_tokens(config: dict, build_version: str) -> dict[str, str]:
    year = datetime.now(timezone.utc).year
    return {
        "SITE_NAME": esc(config["name"]),
        "SITE_NAME_HTML": site_name_html(config["name"]),
        "LOGO_MARK": LOGO_MARK_SVG,
        "BUILD_VERSION": build_version,
        "FOOTER_COPYRIGHT": esc(f"© {year} {config['publisher']} — {config['name']}"),
    }


def fill(template: str, tokens: dict[str, str]) -> str:
    out = template
    for key, value in tokens.items():
        out = out.replace("{{" + key + "}}", value)
    return out


def build_edition_page(config: dict, edition: dict, template: str, build_version: str) -> str:
    slug = edition["slug"]
    md = (EDITIONS_DIR / f"{slug}.md").read_text(encoding="utf-8")
    simplified = ""
    if edition.get("hasSimplified"):
        simplified = (EDITIONS_DIR / f"{slug}-simplified.md").read_text(encoding="utf-8")

    tokens = common_tokens(config, build_version)
    tokens.update(
        {
            "PAGE_TITLE": esc(f"{config['name']} — {edition['title']}"),
            "OG_TITLE": esc(f"{config['name']} — {edition['title']}"),
            "META_DESCRIPTION": esc(edition["description"]),
            "OG_URL_BLOCK": og_url_block(config, f"/editions/{slug}"),
            "SLUG": slug,
            "EDITION_TITLE": esc(edition["title"]),
            "EDITION_TITLE_JS": json.dumps(edition["title"]),
            "EDITION_MD_JS": json.dumps(md),
            "EDITION_SIMPLIFIED_JS": json.dumps(simplified),
            "HAS_AUDIO": "true" if edition.get("hasAudio") else "false",
            "HAS_VIDEO": "true" if edition.get("hasVideo") else "false",
            "AUDIO_TITLE_JS": json.dumps(f"{config['name']} — Audio Briefing"),
            "VIDEO_TITLE_JS": json.dumps(edition.get("videoTitle") or edition["title"]),
        }
    )
    return fill(template, tokens)


def featured_card(config: dict, edition: dict) -> str:
    slug = edition["slug"]
    host = str(config.get("domain", "")).rstrip("/").replace("https://", "").replace("http://", "") or "monday-signal.local"
    return f"""      <a class="featured-card" href="/editions/{slug}">
        <div class="browser-bar">
          <span class="browser-dots"><i></i><i></i><i></i></span>
          <span class="browser-url">{esc(host)}/editions/{slug}</span>
        </div>
        <div class="featured-body">
          <div class="edition-meta-row">
            <span class="edition-badge">{slug}</span>
            <span class="edition-tag">Newest edition &middot; {esc(display_date(slug))}</span>
          </div>
          <h3>{esc(edition["title"])}</h3>
          <p>{esc(edition["hook"])}</p>
          <span class="card-cta">Read the full briefing {ARROW_SVG}</span>
        </div>
      </a>"""


def archive_card(edition: dict) -> str:
    slug = edition["slug"]
    return f"""        <a class="archive-card" href="/editions/{slug}">
          <div class="edition-meta-row" style="margin-bottom:0;">
            <span class="edition-badge">{slug}</span>
          </div>
          <h3>{esc(edition["title"])}</h3>
          <p>{esc(edition["hook"])}</p>
          <span class="card-cta">Read edition {ARROW_SVG}</span>
        </a>"""


def build_homepage(config: dict, editions: list[dict], template: str, build_version: str) -> str:
    latest = editions[0]
    day = config.get("publicationDay", "Monday")
    count = len(editions)

    tokens = common_tokens(config, build_version)
    tokens.update(
        {
            "PAGE_TITLE": esc(f"{config['name']} — {config['tagline']}"),
            "OG_TITLE": esc(f"{config['name']} — {config['tagline']}"),
            "META_DESCRIPTION": esc(config["description"]),
            "OG_URL_BLOCK": og_url_block(config, "/"),
            "HERO_INTRO": config.get("heroIntroHtml") or esc(config["tagline"]),
            "HERO_DISPLAY": config.get("heroDisplayHtml") or site_name_html(config["name"]),
            "HERO_SUB": esc(config["description"]),
            "HERO_META": esc(f"Every {day} · {config.get('audienceNote', '')} · Curated with AI assistance".strip(" ·")),
            "STATEMENT_HTML": config.get("statementHtml", ""),
            "LATEST_URL": f"/editions/{latest['slug']}",
            "CADENCE_LABEL": esc(f"Published {day}s"),
            "FEATURED_CARD": featured_card(config, latest),
            "ARCHIVE_CARDS": "\n".join(archive_card(e) for e in editions),
            "EDITION_COUNT": str(count),
            "EDITION_COUNT_PLURAL": "" if count == 1 else "s",
            "ABOUT_WHY": esc(
                config.get(
                    "aboutWhy",
                    "To keep the team current on AI and tech news as it relates to marketing.",
                )
            ),
        }
    )
    return fill(template, tokens)


def build_sitemap(config: dict, editions: list[dict]) -> str | None:
    domain = str(config.get("domain", "")).rstrip("/")
    if not domain:
        return None
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = [f"""  <url>
    <loc>{domain}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""]
    for edition in editions:
        urls.append(f"""  <url>
    <loc>{domain}/editions/{edition['slug']}</loc>
    <lastmod>{edition['slug']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")
    body = "\n".join(urls)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


def build_robots(config: dict) -> str:
    domain = str(config.get("domain", "")).rstrip("/")
    lines = ["User-agent: *", "Allow: /"]
    if domain:
        lines.append(f"Sitemap: {domain}/sitemap.xml")
    return "\n".join(lines) + "\n"


def scan_for_tokens(paths: list[Path]) -> list[str]:
    errors = []
    for path in paths:
        if not path.exists():
            errors.append(f"expected output missing: {path.relative_to(ROOT)}")
            continue
        leftover = sorted(set(TOKEN_RE.findall(path.read_text(encoding="utf-8"))))
        if leftover:
            errors.append(
                f"{path.relative_to(ROOT)} contains unreplaced tokens: {', '.join(leftover)}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing.")
    args = parser.parse_args()

    config, editions = load_inputs()
    errors = validate(config, editions)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    build_version = datetime.now(timezone.utc).strftime("%Y%m%d")
    edition_template = (TEMPLATES_DIR / "edition.template.html").read_text(encoding="utf-8")
    index_template = (TEMPLATES_DIR / "index.template.html").read_text(encoding="utf-8")

    outputs: list[Path] = [SITE_DIR / "index.html"]
    for edition in editions:
        outputs.append(SITE_DIR / "editions" / edition["slug"] / "index.html")

    if args.check:
        token_errors = scan_for_tokens([p for p in outputs if p.exists()])
        if token_errors:
            print("Output check failed:", file=sys.stderr)
            for error in token_errors:
                print(f"  - {error}", file=sys.stderr)
            return 1
        print(f"Check passed: {len(editions)} edition(s), config and manifest valid.")
        return 0

    written: list[Path] = []
    for edition in editions:
        out_dir = SITE_DIR / "editions" / edition["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "index.html"
        out_path.write_text(
            build_edition_page(config, edition, edition_template, build_version),
            encoding="utf-8",
        )
        written.append(out_path)

    index_path = SITE_DIR / "index.html"
    index_path.write_text(build_homepage(config, editions, index_template, build_version), encoding="utf-8")
    written.append(index_path)

    robots_path = SITE_DIR / "robots.txt"
    robots_path.write_text(build_robots(config), encoding="utf-8")
    written.append(robots_path)

    sitemap = build_sitemap(config, editions)
    sitemap_path = SITE_DIR / "sitemap.xml"
    if sitemap:
        sitemap_path.write_text(sitemap, encoding="utf-8")
        written.append(sitemap_path)
    elif sitemap_path.exists():
        sitemap_path.unlink()
        print("note: no domain configured — removed stale sitemap.xml")
    else:
        print("note: no domain configured — skipping sitemap.xml (set 'domain' in config.json)")

    token_errors = scan_for_tokens([p for p in written if p.suffix == ".html"])
    if token_errors:
        print("Build produced invalid output:", file=sys.stderr)
        for error in token_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    for path in written:
        print(f"  wrote {path.relative_to(ROOT)}")
    print(f"Built {len(editions)} edition(s) for {config['name']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
