# AVS AI Dispatch — SharePoint Package

Sister build output of the public site. This folder produces **body-only HTML
files** (no JavaScript) that drop into a SharePoint document library and are
referenced from a SharePoint list. The SharePoint site then renders the
newsletter via a Content Query / Highlighted Content web part plus an Embed or
Page Viewer web part for the edition body.

## Why this exists

JavaScript does not run reliably inside SharePoint modern pages. The public
site build (`AV-AI-Newsletter/site/`) is a fully interactive single-page
experience with a client-side markdown renderer, audio player, video player,
and reading-mode toggle. None of that works in SharePoint.

This package produces the same content, rendered server-side, as plain HTML
that any SharePoint surface can display:

- **No `<script>` tags.** Markdown is rendered to HTML at build time.
- **No external CSS.** A scoped `<style>` block is embedded at the top of each
  file, namespaced to `.avs-dispatch` so it cannot collide with SharePoint's
  own page CSS.
- **No `<html>`/`<head>`/`<body>` wrappers.** Each file is a body-only
  fragment, safe to drop into a Page Viewer web part, Content Query XSLT, or
  SPFx component.
- **No audio/video embeds in the body.** SharePoint's native audio/video web
  parts handle media, driven off the list columns (`AudioUrl`, `VideoUrl`).

## What AVS delivers each week

For each edition date `YYYY-MM-DD` the team receives:

| File | Where it goes |
|---|---|
| `editions/YYYY-MM-DD/YYYY-MM-DD-full.html` | `AVSDispatchContent/editions/` in the doc library |
| `editions/YYYY-MM-DD/YYYY-MM-DD-summary.html` | `AVSDispatchContent/editions/` in the doc library |
| `audio/YYYY-MM-DD.mp3` | `AVSDispatchContent/audio/` in the doc library |
| `video/YYYY-MM-DD.mp4` | `AVSDispatchContent/video/` in the doc library |
| `thumbs/YYYY-MM-DD.png` | `AVSDispatchContent/thumbs/` in the doc library |

Plus one new row in the `AVS AI Dispatch Editions` list pointing at those
URLs. See [`SHAREPOINT_LIST_SCHEMA.md`](./SHAREPOINT_LIST_SCHEMA.md) for the
full list schema and weekly workflow.

## Build (for the AVS editorial side)

```bash
# Build a single edition
python3 build_sharepoint.py 2026-04-17

# Build every edition we have markdown for
python3 build_sharepoint.py --all
```

Requires Python 3 only — no dependencies. The script reads markdown source
from `../editions/` and writes HTML output to `./editions/`.

## Folder layout

```
sharepoint-package/
├── README.md                       # This file
├── SHAREPOINT_LIST_SCHEMA.md       # List columns, views, CQWP config, weekly workflow
├── build_sharepoint.py             # Generator (body-only HTML, no JS)
├── editions/
│   └── YYYY-MM-DD/
│       ├── YYYY-MM-DD-full.html
│       └── YYYY-MM-DD-summary.html (if a simplified source exists)
└── samples/
    └── list-import-all-editions.csv  # Ready-to-import rows for every edition
```

## Editions currently packaged

All editions to date are built and ready to deploy. Media columns are left
blank where no audio/video exists for that week yet.

| Edition | Full HTML | Summary HTML | Audio (mp3) | Video (mp4) | Thumbnail |
|---|---|---|---|---|---|
| 2026-04-17 | yes | yes | yes | yes | yes |
| 2026-04-10 | yes | yes | yes | yes | yes |
| 2026-04-03 | yes | yes | yes | yes | yes |
| 2026-03-27 | yes | — | — | — | — |
| 2026-03-20 | yes | — | yes | yes | yes |
| 2026-03-13 | yes | — | — | — | — |

## Importing the archive into the SharePoint list

`samples/list-import-all-editions.csv` contains one row per edition with hooks,
URLs, and status. Before importing:

1. Do a find/replace on `{SITE_URL}` and replace with your SharePoint site URL
   root (e.g. `https://tenant.sharepoint.com/sites/AVSDispatch`). The CSV uses
   that token so the file is portable across environments.
2. In SharePoint, open the `AVS AI Dispatch Editions` list → **Integrate →
   Power Automate → See your flows** → *or* **Quick Edit** mode → paste rows
   directly. (SharePoint Online supports pasting tabular data into Quick Edit.)
3. Alternatively, use `Import-SPListItems` in PowerShell or the Microsoft Lists
   "Import from Excel" option if you save the CSV as `.xlsx` first.
4. Confirm exactly one row has `Featured = Yes` (should be the latest edition).

## Notes on styling

The scoped `<style>` block uses Dispatch colors and the `Segoe UI` font stack
(SharePoint's native family) with `Plus Jakarta Sans` as a fallback if the
team decides to load a custom font. Layout is responsive and degrades to a
semantic HTML appearance if SharePoint sandboxes the `<style>` tag.

If a SharePoint surface strips inline `<style>` tags entirely, the content
still renders correctly — it just looks like plain themed SharePoint content
instead of Dispatch-branded.
