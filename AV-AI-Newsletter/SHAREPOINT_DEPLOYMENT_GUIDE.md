# AVS AI Dispatch — SharePoint Deployment Guide

**Prepared for:** SharePoint Development / Web Team
**From:** Audio/Video Services
**Date:** April 2026

---

## What You're Receiving

Each week, AVS will deliver a **self-contained newsletter package** for the AVS AI Dispatch. The package consists of the following files:

### Per-Edition Delivery (weekly)

| File | Description | Size (typical) |
|------|-------------|----------------|
| `editions/YYYY-MM-DD/index.html` | The newsletter page — a single HTML file containing all content, metadata, and inline JavaScript | 25–40 KB |
| `audio/YYYY-MM-DD.m4a` | Audio summary (NotebookLM-generated) | 30–95 MB |
| `video/YYYY-MM-DD.mp4` | Video companion piece | 30–70 MB |
| `video/thumbs/YYYY-MM-DD.png` | Video poster/thumbnail image | ~1 MB |

### Shared Assets (one-time setup, updated occasionally)

| File | Description |
|------|-------------|
| `shared.css` | All styling — typography, layout, colors, audio/video player UI, responsive breakpoints |
| `shared.js` | All JavaScript — audio player, video player, markdown renderer, reading mode toggle |
| `favicon.svg` | Site icon |
| `og-image.png` | Open Graph thumbnail for link previews (1200×630px) |

### Static Pages (one-time setup)

| File | Description |
|------|-------------|
| `index.html` | Landing page with edition archive, research section, experiments section |
| `brand-guidelines.html` | Brand reference page |
| `reports/ai-av-production-capability-assessment/index.html` | Research report page |
| `reports/ai-av-production-capability-assessment/slide-deck.html` | Slide deck version of the research report |

---

## How the Newsletter Works (Technical Summary)

Each edition is a **single HTML file** that:

1. Loads `shared.css` and `shared.js` via relative paths (`/shared.css`, `/shared.js`)
2. Contains the full newsletter content as a JavaScript string constant (`EDITION_MD`) in JSON-escaped Markdown
3. Contains a simplified version as a second constant (`EDITION_SIMPLIFIED`) for the "Quick Summary" toggle
4. Renders the Markdown to HTML client-side via the `markdownToHtml()` function in `shared.js`
5. Initializes an audio player if `HAS_AUDIO = true` (points to `/audio/YYYY-MM-DD.m4a`)
6. Initializes a video player if `HAS_VIDEO = true` (points to `/video/YYYY-MM-DD.mp4` with poster from `/video/thumbs/YYYY-MM-DD.png`)
7. Initializes a "Full Edition / Quick Summary" reading mode toggle if `EDITION_SIMPLIFIED` is present

**External dependencies** (loaded from CDN, no local files needed):
- Google Fonts: Plus Jakarta Sans, JetBrains Mono
- Vercel Analytics script (can be removed for SharePoint)

**No server-side processing is required.** Everything renders in the browser.

---

## Deployment Options

### Option A: Embed via Iframe (Recommended Starting Point)

**How it works:** Upload the entire file set to a SharePoint Document Library. Use an Embed web part on each page to iframe the HTML file.

**Setup steps:**

1. Create a Document Library (e.g., `AVSAIDispatch`) on your SharePoint site
2. Replicate the folder structure inside it:
   ```
   AVSAIDispatch/
   ├── shared.css
   ├── shared.js
   ├── favicon.svg
   ├── og-image.png
   ├── index.html
   ├── brand-guidelines.html
   ├── audio/
   │   ├── 2026-04-03.m4a
   │   └── 2026-04-10.m4a
   ├── video/
   │   ├── 2026-04-03.mp4
   │   ├── 2026-04-10.mp4
   │   └── thumbs/
   │       ├── 2026-04-03.png
   │       └── 2026-04-10.png
   ├── editions/
   │   ├── 2026-04-03/index.html
   │   └── 2026-04-10/index.html
   └── reports/
       └── ai-av-production-capability-assessment/
           ├── index.html
           └── slide-deck.html
   ```
3. **Critical:** Update the `<link>` and `<script>` paths in each HTML file from absolute (`/shared.css`) to relative paths that resolve within your Document Library. For example:
   - In `editions/2026-04-10/index.html`, change `/shared.css` → `../../shared.css`
   - Change `/shared.js` → `../../shared.js`
   - Change `/audio/2026-04-10.m4a` → `../../audio/2026-04-10.m4a`
   - Change `/video/2026-04-10.mp4` → `../../video/2026-04-10.mp4`
4. Add an **Embed** web part to a SharePoint page
5. Set the URL to the Document Library path of the HTML file
6. The newsletter renders inside the iframe with full JavaScript support

**Weekly update process:** Upload the new edition folder (`editions/YYYY-MM-DD/`) and its media files (`audio/`, `video/`, `video/thumbs/`). No changes to shared assets unless notified.

| Pros | Cons |
|------|------|
| Fastest to deploy (hours, not days) | Renders inside an iframe — won't inherit SharePoint theme |
| Full JavaScript support (audio player, video player, toggle) | URL paths need manual adjustment (one-time, then templated) |
| No build tools or development environment required | iframe height may need manual sizing or a resize script |
| Media files (audio/video) work with native HTML5 players | Large media files count against Document Library storage |
| Easy to update weekly — just upload new files | Users see SharePoint chrome around the embedded content |

---

### Option B: JW Content Editor Web Part

**How it works:** Use the existing JW Content Editor web part (component ID `4662ace2-ce6b-4f17-8dae-9945cdf4439c`) to inject the HTML directly into a SharePoint page.

**Setup steps:**

1. Upload `shared.css`, `shared.js`, and media files to **Site Assets** or a Document Library
2. Create a new SharePoint page
3. Add a JW Content Editor web part
4. Either:
   - Reference the HTML file URL directly, or
   - Paste the HTML content with `wysiwygOn: false` in the web part configuration
5. Update all asset paths to point to the uploaded locations in Site Assets

**Weekly update process:** Create a new page for each edition, add the JW Content Editor web part, reference or paste the new HTML.

| Pros | Cons |
|------|------|
| Content lives natively on the SharePoint page (no iframe) | JW Content Editor **may strip JavaScript** — must test thoroughly |
| Can inherit some SharePoint page styling | If JS is stripped, audio player, video player, and reading toggle will not work |
| Familiar workflow for SharePoint content authors | CSS conflicts with SharePoint's own styles are possible |
| No build tools required | Each edition requires manual page creation and configuration |
| | Content editor has character/size limits that may affect large editions |

**Important:** Test the first edition thoroughly before committing to this option. If the Content Editor strips the `<script>` tags, the audio player, video player, markdown renderer, and reading mode toggle will all fail silently — the page will show "Loading edition..." and never render.

---

### Option C: Full SPFx Web Part (Production-Grade)

**How it works:** Build a custom SharePoint Framework (SPFx) web part that renders the newsletter content natively within SharePoint.

**Prerequisites:**

```bash
npm install -g yo @microsoft/generator-sharepoint
```

**Scaffold:**

```bash
yo @microsoft/sharepoint
# Project name: avs-ai-dispatch
# Framework: React
# Web part name: AVSAIDispatch
```

**Architecture:**

```
src/webparts/avsAIDispatch/
├── AVSAIDispatchWebPart.ts          # Entry point, web part properties
├── components/
│   ├── Dispatch.tsx                   # Main container
│   ├── EditionRenderer.tsx            # Markdown → HTML renderer
│   ├── AudioPlayer.tsx                # Custom audio player (port from shared.js)
│   ├── VideoPlayer.tsx                # Custom video player
│   ├── ReadingToggle.tsx              # Full Edition / Quick Summary toggle
│   └── EditionArchive.tsx             # Archive listing for landing page
├── services/
│   └── ContentService.ts             # Fetches edition data from SP list or library
├── models/
│   └── IEdition.ts                    # Edition metadata interface
└── styles/
    └── Dispatch.module.scss           # Port of shared.css to SCSS modules
```

**Key conversion work:**

1. **Port `shared.css` to SCSS modules** — Convert CSS custom properties to SCSS variables. Map brand colors to SPFx theme slots where appropriate (e.g., `[theme:themePrimary]` for `--dispatch-blue`).
2. **Port `shared.js` to React components** — The `buildPodcastPlayer()`, `initPodcastPlayer()`, `buildReadingToggle()`, `initReadingToggle()`, and `markdownToHtml()` functions become React components with state hooks.
3. **Content storage** — Store the Markdown content in a SharePoint List (one item per edition with columns for date, standard markdown, simplified markdown, audio URL, video URL, thumbnail URL) or in individual files in a Document Library.
4. **Media hosting** — Upload audio and video files to a Document Library. Reference them by SharePoint URL. Ensure the library supports HTTP Range Requests for audio/video seeking (SharePoint Online does this natively).
5. **Build and deploy:**
   ```bash
   gulp bundle --ship
   gulp package-solution --ship
   ```
   Upload the `.sppkg` from `sharepoint/solution/` to the tenant App Catalog.

**Weekly update process:** Add a new item to the SharePoint List (or upload new markdown/media files to the Document Library). The web part reads the latest content automatically. No code changes needed week to week.

| Pros | Cons |
|------|------|
| Fully native SharePoint experience — no iframe, no workarounds | Requires SPFx development skills (TypeScript, React, SCSS) |
| Inherits SharePoint theming and responsive behavior | Initial build is 2–4 weeks of development |
| Deployable across multiple sites via App Catalog | Requires a Node.js development environment and build pipeline |
| Content updates are data-only (no HTML changes needed weekly) | Audio/video player components need to be ported from vanilla JS to React |
| Proper SharePoint authentication for any future API calls | Testing requires a SharePoint workbench or dedicated test site |
| Best long-term maintainability | Any changes to the newsletter format require a code update and redeployment |

---

## Recommendation

| Scenario | Recommended Option |
|----------|--------------------|
| Need it live this week | **Option A** (Iframe Embed) |
| Want native SharePoint pages, team is comfortable testing | **Option B** (JW Content Editor) — but test JS support first |
| Building a long-term, multi-site deployment | **Option C** (Full SPFx) |
| Not sure yet | Start with **Option A**, validate the content and audience, then invest in **Option C** if the newsletter proves valuable |

---

## What AVS Delivers Weekly

Each Friday, AVS will provide:

1. **Edition HTML file** — `editions/YYYY-MM-DD/index.html`
2. **Audio summary** — `audio/YYYY-MM-DD.m4a`
3. **Video file** — `video/YYYY-MM-DD.mp4`
4. **Video thumbnail** — `video/thumbs/YYYY-MM-DD.png`
5. **Edition markdown** (raw) — `editions/YYYY-MM-DD.md` and `editions/YYYY-MM-DD-simplified.md` (if the team prefers to work with the source markdown directly rather than the pre-built HTML)

Files are delivered via the GitHub repository at `github.com/williamproctor/Will-s-Workspace` under `AV-AI-Newsletter/`. The team can pull from the repo directly or receive the files via an agreed-upon delivery method.

---

## Questions?

Contact Audio/Video Services. This guide will be updated as the deployment path is finalized.
