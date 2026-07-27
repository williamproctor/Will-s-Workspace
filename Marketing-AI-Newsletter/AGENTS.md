# Signal & Scale — Production Runbook

> Working title. The brand name, tagline, and domain live in `config.json` — change them there and rebuild; nothing else needs to be edited. This newsletter is completely separate from The AVS AI Dispatch (`AV-AI-Newsletter/`). Do not cross-reference content, branding, or domains between the two.

## Purpose

Signal & Scale is a weekly intelligence briefing for the GrowthX team. Its job is to keep the team current on AI and tech news **as it relates to marketing** — so that social posts, client conversations, and thought leadership are timely, informed, and authoritative. It is a working input for people who publish, not a strategy document and not a public-relations digest.

Two outcomes define success each week:

1. Every reader can speak fluently about the week's most consequential marketing-relevant AI developments — with real numbers, dates, and sources.
2. Every reader leaves with at least one grounded angle they could turn into a post, a client note, or a point of view this week.

## Audience

Growth marketers, content strategists, and operators at GrowthX. They are AI-literate practitioners (AEO/GEO, content systems, AI-led growth) who publish publicly and advise clients. Write for a sharp colleague, not a beginner: no explaining what a large language model is, no hype, no filler.

## Voice & Tone

- **Observational reporting, clearly separated from angle-making.** News sections report what happened with evidence. The **Angles for the Week** section is the one place where the newsletter suggests how the team might use the news. Keep the two modes separate so facts stay clean.
- **Conversational but precise.** Direct, concrete, specific numbers, dates, and sources. No vague hedging ("could potentially," "may possibly").
- **Operator perspective.** Written by someone who uses these tools and channels, not someone selling them. Honest about limitations. Anti-hype — this matches the GrowthX voice.
- **Label the evidence.** Distinguish vendor claims, company-reported figures, platform announcements, independent studies, and practitioner anecdotes. A pitch deck stat and a peer-reviewed study are not the same thing, and readers will repeat what we print — so the qualifier is part of the fact.

## What to Include

Developments from the past 7 days that touch marketing, in roughly this priority order:

1. **AI search and answer engines** — Google AI Mode/AI Overviews, ChatGPT, Perplexity, Copilot: ranking changes, ads in AI answers, citation behavior, referral-traffic data. This is GrowthX's home turf; never miss a story here.
2. **Ad platforms' AI** — Google, Meta, Amazon, TikTok, LinkedIn, Reddit: automated campaign types, creative generation, targeting changes, measurement shifts.
3. **Models and tools that change marketing work** — new frontier or media models when (and only when) they change how marketing content, ads, video, or analysis gets produced; agent capabilities that touch commerce or buying.
4. **Martech and adtech industry** — launches, funding, acquisitions, shutdowns, pricing changes that shift what stacks look like.
5. **Distribution and platform shifts** — social algorithm changes, email/deliverability changes, creator-economy moves, browser/agent behavior that changes how people find and buy things.
6. **Data, studies, and benchmarks** — adoption surveys, spend forecasts, traffic studies, CTR/conversion research. These are thought-leadership fuel; always report methodology and sample size.
7. **Voices** — what notable operators, executives, and researchers said this week, attributed to the person.

## Content Standards

- **Accuracy over completeness.** Every factual claim traceable to a source in the Sources section. If a number can't be verified, either qualify it explicitly or cut it.
- **Preserve qualifiers.** "Company-reported," "vendor-stated," "preview," "waitlist," "announced but not shipped" — never let a plan become a product or a claim become a finding.
- **Professional, publishable tone.** No profanity, no cheap shots at named individuals, no rumor presented as fact. Team members may quote this newsletter publicly — write everything so it survives being screenshotted.
- **Competitors and clients.** Report on marketing-industry vendors (including GrowthX competitors) factually and neutrally. No trash talk, no promotion.
- **Speculation is labeled.** Forward-looking statements need an evidence basis and an explicit "speculation" or "expected" label.

## Structure

Each edition follows this structure:

1. **Lede** — A one-paragraph blockquote summarizing the 3–5 biggest stories and the week's pattern.
2. **This Week in Marketing AI** — 4–6 individual stories with source links. Each story gets its own H3. Lead with the most consequential story for marketers, not the loudest launch.
3. **Platform & Tool Watch** — Bulleted quick hits: smaller platform changes, model releases, martech launches, funding. One to three sentences each, each with a source link and date.
4. **Voices This Week** — Notable quotes or arguments from individuals, attributed by name (person, not publication or show).
5. **Common Threads** — Patterns across the week's stories. Observational analysis of where things are heading.
6. **Angles for the Week** — 3–5 thought-leadership angles grounded in this edition's reporting. Each angle has three parts: **the hook** (the contrarian or clarifying one-liner), **the evidence** (which facts from this edition support it), and **why now** (what makes it timely this week). These are raw material for the team's own POV — starting points, not finished posts, and never fabricated beyond what the reporting supports.
7. **Tip of the Week** — One practical, doable-this-week tip for using AI in marketing work. Format: the tip, why it works, concrete steps, and a pointer if relevant. Bias toward tips that compound and work across tools.
8. **Sources** — Numbered list of all cited sources with publication, date, and a one-line description of what each source supports.

## Mandatory Pre-Build Review (every edition)

After drafting the full and simplified editions — and before building the site or committing — perform an explicit review pass:

1. **Claims audit.** Re-verify every number, date, price, and product-status claim against its source. Confirm each source link resolves and actually supports the claim it's attached to.
2. **Qualifier audit.** Hunt for places where a vendor claim reads like an independent finding, a preview reads like a shipped product, or speculation reads like reporting. Fix in place.
3. **Reputation audit.** The team will echo this content publicly. Flag anything that could embarrass GrowthX if quoted: unverifiable stats, one-sided framing of a competitor, or angles that overreach the evidence.
4. Report the result explicitly ("Review: N claims verified, no flags" or a flag list with proposed fixes) before building.

## NotebookLM Producer Briefs (each edition, after review)

Generate two NotebookLM source documents immediately after the review pass:

- `notebooklm/YYYY-MM-DD-podcast.md` — Audio Overview producer brief
- `notebooklm/YYYY-MM-DD-video.md` — Video Overview producer brief

```bash
python3 scripts/generate_notebooklm_briefs.py YYYY-MM-DD --video-title "Short editorial episode title"
```

The generator maps the edition into podcast and video act structures, embeds audience and house-style constraints, strips URLs (NotebookLM reads them aloud), and validates both files. Validate with `--check`. Upload only the matching brief to NotebookLM — never the raw edition markdown as a second source. Audio (m4a exported from NotebookLM) goes to `site/audio/YYYY-MM-DD.m4a` plus an ffmpeg MP3 copy at `site/audio/mp3/YYYY-MM-DD.mp3`; video goes to `site/video/YYYY-MM-DD.mp4`. Media is optional per edition — set the flags in the manifest when files ship.

## Build System (one manifest, one builder)

This project deliberately avoids the per-edition build scripts and scattered metadata of the AV newsletter (see TEAM-MEMORY 2026-07-19: the audit found 14 copied builders and 6+ repeated metadata surfaces there).

- **`config.json`** — the single brand surface: name, tagline, description, domain, publisher. Renaming the newsletter or attaching the purchased domain is a one-file change.
- **`editions/manifest.json`** — the single edition registry: slug, title, hook, description, media flags. The newest edition is listed first and is featured on the homepage automatically.
- **`scripts/build_site.py`** — the only builder. It reads the config, the manifest, and the markdown sources, then regenerates every edition page, the homepage archive, and `sitemap.xml` in one pass:

```bash
cd Marketing-AI-Newsletter
python3 scripts/build_site.py            # build everything
python3 scripts/build_site.py --check    # validate without writing
```

No per-edition scripts. To ship a new edition: add the markdown files, prepend one entry to the manifest, run the builder.

### Weekly workflow

1. **Research** (three parallel tracks, saved under `research/YYYY-MM-DD/`):
   - `platforms-YYYY-MM-DD.md` — primary-source announcements: ad platforms, search/answer engines, social platforms, model vendors.
   - `industry-YYYY-MM-DD.md` — martech/adtech industry news, studies, funding, data.
   - `voices-YYYY-MM-DD.md` — practitioner and executive commentary worth attributing.
   - `analysis-YYYY-MM-DD.md` — cross-source synthesis: what leads, what connects, candidate angles.
2. **Draft** `editions/YYYY-MM-DD.md` (full) and `editions/YYYY-MM-DD-simplified.md` (quick summary).
3. **Review** (claims, qualifiers, reputation — see above).
4. **Briefs** — generate and validate both NotebookLM briefs.
5. **Manifest** — prepend the edition entry with its hook.
6. **Build** — `python3 scripts/build_site.py`, then preview with `python3 serve.py` (port 8092).
7. **Commit and push.** One commit per edition once media flags are final. Vercel deploys `site/` when the project is connected.

## Technical Notes

- Editions are Markdown in `editions/`, named `YYYY-MM-DD.md` with the **Monday publication date** (the edition covers the previous 7 days). A `-simplified.md` sibling powers the Quick Summary toggle.
- The site renders markdown client-side (`site/shared.js`), same rules as the AV site renderer. Body-only HTML for other destinations (email paste, Notion, Slack) can be added later without changing the sources.
- Images: place under `site/editions/YYYY-MM-DD/` and reference root-relative (`/editions/YYYY-MM-DD/chart.png`). Never hardcode a domain in markdown — the domain is not final.
- No subscribe CTAs and no email-send integration yet. Distribution starts as a shareable site plus the markdown itself; an ESP can be layered on once the name/domain are settled.
