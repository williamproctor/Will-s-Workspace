# The Monday Signal

A weekly intelligence briefing that keeps the GrowthX team current on AI and tech news **as it relates to marketing** — so social posts, client conversations, and thought leadership stay timely and authoritative.

This project is completely separate from The AVS AI Dispatch (`AV-AI-Newsletter/`). It borrows the production method — researched weekly markdown editions, a static site, NotebookLM audio/video briefs — but shares no content, branding, or domain.

## Status

- **Name:** The Monday Signal (decided 2026-07-28; previously working-titled "Signal & Scale"). All branding lives in `config.json`; a rename is a one-file change followed by `python3 scripts/build_site.py`.
- **Domain:** `mondaysignal.com` (purchased 2026-07-28, configured in `config.json` — the build emits canonical/OG URLs and the sitemap from it). Hosting: Vercel project with root directory `Marketing-AI-Newsletter/site`.
- **Cadence:** Mondays. Each edition covers the previous 7 days, so the team starts the week with fresh material.
- **Delivery:** static site + the markdown itself. No email integration yet.

## Quick start

```bash
cd Marketing-AI-Newsletter

# Build the site (edition pages + homepage + sitemap) from the manifest
python3 scripts/build_site.py

# Validate without writing
python3 scripts/build_site.py --check

# Generate NotebookLM producer briefs for an edition
python3 scripts/generate_notebooklm_briefs.py 2026-07-27 --video-title "..."

# Preview locally at http://localhost:8092
python3 serve.py
```

## Layout

```
Marketing-AI-Newsletter/
├── AGENTS.md              ← production runbook (read this first)
├── config.json            ← the single branding surface
├── SOURCES.md             ← curated research source list
├── editions/
│   ├── manifest.json      ← the single edition registry
│   ├── YYYY-MM-DD.md      ← full edition (Monday date)
│   └── YYYY-MM-DD-simplified.md
├── research/YYYY-MM-DD/   ← weekly research artifacts (4 files)
├── notebooklm/            ← podcast + video producer briefs
├── scripts/
│   ├── build_site.py      ← the only builder
│   └── generate_notebooklm_briefs.py
├── serve.py               ← local preview (port 8092)
└── site/                  ← deployable static site (generated pages committed)
```

## Producing an edition

See `AGENTS.md` for the full runbook. Short version: research (four artifacts) → draft full + simplified markdown → claims/qualifier/reputation review → NotebookLM briefs → prepend manifest entry → `build_site.py` → commit.
