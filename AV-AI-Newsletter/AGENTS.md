# AVS AI Dispatch — Writing Guidelines

## Purpose

The AVS AI Dispatch is a weekly awareness newsletter for the Audio/Video Services department. Its sole purpose is to keep the team informed about what is happening on the frontier of AI as it relates to AV workflows. It is not a strategy document, a recommendations engine, or a roadmap.

## Voice & Tone

- **Observational, not prescriptive.** Report what happened and why it matters. Do not tell the reader what to do. No directives like "stop evaluating X," "migrate your workflows," "benchmark these tools," or "start with Y." The reader is an informed professional who can draw their own conclusions.
- **Informational, not advisory.** The newsletter answers "what happened this week?" — not "what should we do about it?" Avoid "What this means for us:" callout blocks that prescribe actions. If a development has obvious implications, state the implication as an observation, not an instruction.
- **Conversational but precise.** Write the way a well-informed colleague talks — direct, concrete, no jargon for its own sake. Use specific numbers, dates, and sources. Avoid vague hedging ("could potentially," "may possibly").
- **Operator perspective.** Write from the perspective of someone who uses these tools, not someone selling them. Be honest about limitations. Don't hype.

## What to Include

- Developments from the past 7 days that are relevant to audio/video production, AI tooling, or the broader AI landscape that contextualizes AV-specific changes.
- Concrete facts: pricing, benchmarks, release dates, capabilities, limitations.
- Voices from notable individuals (attributed to the person, not the show or publication they appeared on).
- Forward-looking context where grounded in evidence — e.g., confirmed event dates, announced product roadmaps, credible industry speculation. Label speculation clearly.
- Tool and model comparisons when multiple options launched in the same window.

## Content Standards & Audience Sensitivity (non-negotiable)

The Dispatch is produced for an Audio/Video Services department inside a faith-based / religious organization. All content must be **PG at most** — appropriate for every member of that audience, including the most conservative reader.

- **Quotes must be clean.** Never include a quote — even a verbatim, well-sourced, "best quote of the year" one — that is sexual, profane, crude, violent, blasphemous, or otherwise potentially offensive. When a notable figure's only memorable quote is inappropriate, either paraphrase the underlying point in neutral language or omit the quote entirely. Do not fabricate a clean substitute quote and attribute it to the person.
- **No R-rated films or filmmakers known for that body of work.** Do not feature, profile, or build stories around R-rated/explicit films, or directors/creators primarily known for explicit, violent, or sexual content. Family-friendly work by an otherwise family-friendly creator is fine (e.g., a kids' animated series). Use judgment: the test is whether highlighting the person/work could reasonably make a conservative religious reader uncomfortable.
- **Topics to handle carefully or avoid:** sexual content, graphic violence, profanity, drugs, gambling, religion/politics framed provocatively, and anything that mocks faith or values. Report adjacent industry news factually and neutrally; do not dwell on or quote the objectionable parts.
- **When in doubt, leave it out** and surface it in the content-review flag (below) so a human can decide.

## Mandatory Content-Review Step (every edition)

After completing the **initial draft pass** of the full and simplified editions — and **before** building the site/SharePoint outputs or committing — perform an explicit content-sensitivity review:

1. Re-read both drafts specifically hunting for anything that could be deemed offensive, sexual, profane, crude, violent, blasphemous, or otherwise inappropriate for a PG, faith-based audience — including quotes, film/filmmaker references, jokes, idioms, and double entendres.
2. **Produce a content-review flag list** for the user: each potentially sensitive item, where it appears, why it's flagged, and a proposed fix (paraphrase, soften, or cut).
3. **Stop and get the user's review/approval** on the flagged items before proceeding to build and deploy. If nothing is flagged, state that explicitly ("Content review: no sensitivity issues found") and proceed.

This step is required even when the week's news seems benign. Last-mile review is cheaper than a published faux pas.

## What to Avoid

- **Directives or calls to action.** Never tell the reader to adopt, migrate, benchmark, evaluate, or stop using a tool. The newsletter informs; the reader decides.
- **"What this means for us" prescription blocks.** If you want to draw a connecting thread, do it as observation ("The practical consequence is more competition, which tends to lower prices") not instruction ("Start with the workflows that are most repetitive").
- **Podcast references.** Do not mention podcasts by name. Attribute quotes and insights to the individual speaker.
- **Subscribe CTAs.** No subscription functionality exists. Do not reference it.
- **Social content framing.** The organization does not produce short-form social content and has no social media presence. Do not frame applications around social distribution.

## Structure

Each edition follows this structure:

1. **Lede** — A one-paragraph blockquote summarizing the 3–5 biggest stories.
2. **This Week in AI** — Individual stories with source links. Each story gets its own H3.
3. **Voices This Week** — Notable quotes or threads from individuals, attributed by name.
4. **Common Threads** — Patterns across the week's stories. Observational analysis, not strategy recommendations.
5. **Novel Ideas Worth Watching** — Emerging tools, techniques, or shifts that are early but interesting.
6. **Tip of the Week** — A single practical tip designed to help AV personnel adopt AI tools in their personal workflows. Format: a clear actionable tip, why it works for AVS specifically, what to do (concrete steps), and a link or pointer if relevant. Bias toward tips that are doable in a weekend, work across multiple AI tools, and compound over time. (Earlier editions used "Tool of the Week" — that format was retired in May 2026.)
7. **Sources** — Numbered list of all cited sources with publication, date, and brief description.

## Source Policy

- Every factual claim should be traceable to a source in the Sources section.
- Attribute quotes to individuals by name, not to publications or shows.
- When speculating (e.g., about upcoming releases), label it explicitly as speculation and provide the evidence basis.

## Technical Notes

- Newsletter content is authored in Markdown (`.md`) in the `editions/` directory.
- The markdown is JSON-escaped and injected into the HTML page's `EDITION_MD` constant via a Python script.
- Edition dates follow a Friday publication schedule.
- Images can be placed in the edition's site directory (e.g., `site/editions/2026-04-03/`) and referenced from the markdown using **root-relative paths** (e.g., `![alt](/editions/2026-04-03/chart.png)`). Root-relative paths work on both localhost and production, and `sharepoint-package/build_sharepoint.py` automatically rewrites them to absolute `https://avaidispatch.com/...` URLs during the SharePoint build so images still resolve when the HTML body is embedded inside a SharePoint page. Do **not** hardcode the `https://avaidispatch.com` origin in the markdown — it will break local preview.

## Audio Pipeline (required for every new edition)

Every edition ships with two audio formats so downstream platforms (SharePoint, email clients, legacy players) always have a compatible option:

1. The original `.m4a` file (NotebookLM export) is placed at `site/audio/YYYY-MM-DD.m4a`.
2. **An MP3 copy MUST be generated and placed at `site/audio/mp3/YYYY-MM-DD.mp3`** alongside the m4a. This is not optional — do it as part of the same step that copies the audio into `site/audio/`.

**Conversion command** (uses `ffmpeg`, VBR quality 2 ≈ 190 kbps, which typically halves file size while preserving audio quality):

```bash
ffmpeg -i site/audio/YYYY-MM-DD.m4a -codec:a libmp3lame -qscale:a 2 site/audio/mp3/YYYY-MM-DD.mp3 -y
```

Create the `site/audio/mp3/` directory if it does not already exist. After conversion, verify both files exist before committing.

## Thumbnail / Image Generation Pipeline

All AI-generated images (video thumbnails, in-edition illustrations) go through `scripts/generate_thumbnail.py`, which calls OpenAI's **`gpt-image-2`** model. Never use the legacy Gemini/Imagen path — it's retired.

- **API key location:** `../.env` at the workspace root (sibling of `AV-AI-Newsletter/`). The key is stored as `OPENAI_API_KEY=...`. The file is gitignored at the workspace level — never commit it and never print its full value.
- **Default output path:** `site/video/thumbs/YYYY-MM-DD.png` when you pass `--slug YYYY-MM-DD`. Pass `--out <path>` for ad-hoc uses.
- **Default params:** `model=gpt-image-2`, `size=1536x1024` (3:2, plays cleanly as a 16:9 poster), `quality=high`.
- **Prompt files:** Keep prompts in `scripts/prompts/YYYY-MM-DD-thumb.txt` so the prompt that shipped the asset is version-controlled alongside everything else.

Invoke using the workspace venv so the `openai` SDK is present:

```bash
../.venv/bin/python scripts/generate_thumbnail.py \
  --slug YYYY-MM-DD \
  --prompt-file scripts/prompts/YYYY-MM-DD-thumb.txt
```

**Design direction — stay on brand.** The Dispatch visual identity is editorial, not sci-fi. Prompts should bias toward: warm parchment backgrounds (`#faf8f3` / `#f5f0e8`), muted dispatch blue (`#4a6da7`) as the sole accent, flat 2D vector aesthetic, generous negative space, monospace corner typography, and a reference to magazine/newspaper design (Monocle, The Economist, NYT Opinion). Explicitly avoid: neon, glow effects, gradients, wireframes, 3D renders, particle effects, dark Tron-style backgrounds, or anything that could be described as "sci-fi."

## Dual Delivery: Public Site + SharePoint Package (required for every new edition)

Every edition ships to two destinations. Both MUST be built before committing.

### 1. Public site (interactive, JavaScript-enabled)

The site build renders markdown client-side, embeds audio/video players, and supports the Full Edition / Quick Summary reading toggle.

- **Source:** `editions/YYYY-MM-DD.md` and `editions/YYYY-MM-DD-simplified.md`
- **Output:** `site/editions/YYYY-MM-DD/index.html`
- **How:** Author or reuse a small per-edition build script (e.g. `build_apr17.py`) that reads both markdown files, JSON-escapes them into `EDITION_MD` / `EDITION_SIMPLIFIED` JS constants, injects them into the HTML template, and sets `HAS_AUDIO` / `HAS_VIDEO` / `VIDEO_TITLE`.
- **Also update:**
  - `site/index.html` — prepend the new entry to the `EDITIONS` array at the top and update the `hook` on the latest-edition card.
  - `site/sitemap.xml` — add a `<url>` entry for the new edition and bump the homepage `lastmod`.

### 2. SharePoint package (body-only HTML, no JavaScript)

SharePoint modern pages cannot run JavaScript, so a separate sister build renders markdown **server-side** to body-only HTML with a scoped `<style>` block. This is non-negotiable — the SharePoint team deploys from this package, not the public site.

- **Source:** Same `editions/YYYY-MM-DD.md` and `editions/YYYY-MM-DD-simplified.md` files (no duplication of content).
- **Output:**
  - `sharepoint-package/editions/YYYY-MM-DD/YYYY-MM-DD-full.html`
  - `sharepoint-package/editions/YYYY-MM-DD/YYYY-MM-DD-summary.html` (only if a `-simplified.md` source exists)
- **How:**
  ```bash
  cd sharepoint-package
  python3 build_sharepoint.py YYYY-MM-DD
  ```
  The generator has no dependencies and uses the same markdown-to-HTML rules as the site's client-side renderer.
- **Also update:**
  - `sharepoint-package/samples/list-import-all-editions.csv`
    - Flip the previous edition's `Featured` column from `Yes` to `No`.
    - Prepend a new row for this edition with `Status=Published`, `Featured=Yes`, the hook (same hook used on the site's homepage card), and URLs using the `{SITE_URL}` token.
    - Leave `SummaryUrl` blank if no simplified source; leave media URLs blank if no media shipped this week.
  - `sharepoint-package/edition-hooks.md` — prepend a section for the new edition with the same hook used in the CSV and the homepage `EDITIONS` array. The SharePoint deployment team uses this as a copy-paste reference when entering rows manually.

### Deployment summary each week

1. Source markdown (full + simplified).
2. **Content-review step** (see "Mandatory Content-Review Step"): flag potentially sensitive content and get user sign-off before building.
3. Site build: `build_<month>.py` → archive entry → sitemap entry.
4. Media: m4a + mp3 pair; video + thumbnail.
5. SharePoint build: `build_sharepoint.py YYYY-MM-DD` + CSV row + feature flip.
6. One commit, one push. Vercel deploys the site; SharePoint team pulls the package folder.
