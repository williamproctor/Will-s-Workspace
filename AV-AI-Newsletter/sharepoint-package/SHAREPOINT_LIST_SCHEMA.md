# AVS AI Dispatch — SharePoint List Schema

This list drives the newsletter archive and the weekly featured edition on the
SharePoint page. Create it once; add one row per edition going forward.

**Recommended list name:** `AVS AI Dispatch Editions`
**Recommended internal name:** `AVSDispatchEditions`

---

## Columns

| Column display name | Internal name | Type | Required | Notes |
|---|---|---|---|---|
| Title | `Title` | Single line of text (255) | Yes | Edition headline, e.g. `Week of April 17, 2026`. Used as the list item title and page heading. |
| Edition Date | `EditionDate` | Date and time (date only) | Yes | The Friday of the edition. Used for sorting the archive newest-first. |
| Slug | `Slug` | Single line of text (20) | Yes | `YYYY-MM-DD` format, e.g. `2026-04-17`. Must match the filenames in the document library. |
| Hook | `Hook` | Multiple lines of text (plain text, 1 line shown) | Yes | 1–3 sentence preview used on the archive tile and the homepage. No HTML. |
| Full Edition URL | `FullEditionUrl` | Hyperlink or Picture | Yes | Link to `YYYY-MM-DD-full.html` in the document library. |
| Summary URL | `SummaryUrl` | Hyperlink or Picture | No | Link to `YYYY-MM-DD-summary.html` in the document library. Omit if no summary was produced. |
| Audio URL | `AudioUrl` | Hyperlink or Picture | No | Link to the `.mp3` in the document library. Drives the SharePoint audio web part for that edition page. |
| Video URL | `VideoUrl` | Hyperlink or Picture | No | Link to the `.mp4` in the document library. Drives the SharePoint video web part for that edition page. |
| Video Thumbnail URL | `VideoThumbUrl` | Hyperlink or Picture | No | Link to the `.png` thumbnail in the document library. |
| Status | `Status` | Choice | Yes | `Draft`, `Published`, `Archived`. Default `Draft`. Only `Published` items appear on the public newsletter page. |
| Featured | `Featured` | Yes/No | No | Exactly one item should be `Yes` at a time — this is the "latest edition" on the landing page. |

---

## Views

Create at least these two views:

**Archive** (default)
- Filter: `Status = 'Published'`
- Sort: `EditionDate` descending
- Columns shown: Title, Edition Date, Hook, Full Edition URL, Summary URL
- Used by the Content Query web part on the archive page.

**Featured**
- Filter: `Status = 'Published' AND Featured = Yes`
- Limit: 1 item
- Columns shown: Title, Edition Date, Hook, Full Edition URL, Summary URL, Audio URL, Video URL, Video Thumbnail URL
- Used by the Content Query web part on the homepage / latest edition page.

---

## Content Query Web Part configuration

When configuring the Content Query (or Highlighted Content) web part on the
SharePoint page, point it at this list and use these options:

- **Source:** This list → `AVS AI Dispatch Editions`
- **List type:** Custom list
- **Presentation → Grouping:** none
- **Presentation → Sorting:** `EditionDate` descending
- **Presentation → Item limit:** 20 (archive) or 1 (featured)
- **Fields to display:** `Title`, `EditionDate`, `Hook`, `FullEditionUrl`

For the edition body itself, use one of two approaches:

1. **Page Viewer / Embed web part** pointing at `FullEditionUrl` — renders the
   HTML body file inside a frame on a SharePoint page. Simplest option. The
   file is self-contained (scoped CSS, no JS) so it renders cleanly.

2. **Content Query + XSLT** pulling the HTML file contents into the page
   directly — requires a small XSLT template that fetches the file body from
   the document library and injects it. More native look, slightly more setup.

---

## Document library structure

Create a single document library (recommended name: `AVSDispatchContent`) with
this folder layout. The SharePoint list columns above reference files by URL
within this library.

```
AVSDispatchContent/
├── editions/
│   ├── 2026-04-17-full.html
│   ├── 2026-04-17-summary.html
│   ├── 2026-04-10-full.html
│   └── 2026-04-10-summary.html
├── audio/
│   ├── 2026-04-17.mp3
│   └── 2026-04-10.mp3
├── video/
│   ├── 2026-04-17.mp4
│   └── 2026-04-10.mp4
└── thumbs/
    ├── 2026-04-17.png
    └── 2026-04-10.png
```

AVS will deliver these files weekly. Your team uploads them to the library and
adds a row to the list pointing at the uploaded URLs.

---

## Weekly update workflow (for the SharePoint team)

1. Receive the weekly package from AVS:
   - `editions/YYYY-MM-DD/YYYY-MM-DD-full.html`
   - `editions/YYYY-MM-DD/YYYY-MM-DD-summary.html`
   - `audio/YYYY-MM-DD.mp3`
   - `video/YYYY-MM-DD.mp4`
   - `thumbs/YYYY-MM-DD.png`
2. Upload files to the matching folders in `AVSDispatchContent/`.
3. In the `AVS AI Dispatch Editions` list:
   - Set the previously-featured item's `Featured` to `No`.
   - Add a new list item with the new edition's metadata (see column table above).
   - Set `Status = Published`, `Featured = Yes`.
4. The homepage and archive refresh automatically via the Content Query web parts.
