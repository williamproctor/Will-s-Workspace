# Signal & Scale (working title)

A weekly intelligence briefing that keeps the GrowthX team current on AI and tech news **as it relates to marketing** — so social posts, client conversations, and thought leadership stay timely and authoritative.

This project is completely separate from The AVS AI Dispatch (`AV-AI-Newsletter/`). It borrows the production method — researched weekly markdown editions, a static site, NotebookLM audio/video briefs — but shares no content, branding, or domain.

## Status

- **Name:** "Signal & Scale" is a working title. All branding lives in `config.json`; renaming is a one-file change followed by `python3 scripts/build_site.py`.
- **Domain:** not yet purchased. The site builds domain-agnostic (relative URLs). Set `"domain"` in `config.json` when one is registered and rebuild to emit canonical/OG URLs.
- **Cadence:** Mondays. Each edition covers the previous 7 days, so the team starts the week with fresh material.
- **Delivery:** static site (Vercel-ready) + the markdown itself. No email integration yet.

### Name alternates considered

If "Signal & Scale" doesn't stick: The Marketing Frontier, The Growth Signal, The Relevance Report, Demand Signal, The Distribution. Check domain availability before committing.

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
