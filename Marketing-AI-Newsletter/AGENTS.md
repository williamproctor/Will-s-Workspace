# Signal & Scale — Production Runbook

> Working title. The brand name, tagline, and domain live in `config.json` — change them there and rebuild; nothing else needs to be edited. This newsletter is completely separate from The AVS AI Dispatch (`AV-AI-Newsletter/`). Do not cross-reference content, branding, or domains between the two.

## Purpose

Signal & Scale is a weekly intelligence briefing for the GrowthX team. Its job is to keep the team current on AI and tech news **as it relates to marketing** — with a strong bias toward the conversations actually blowing up on X and LinkedIn — so the team can comment on highly topical things while they're live, and so social posts, client conversations, and thought leadership stay timely and authoritative.

Two outcomes define success each week:

1. Every reader knows what marketing/AI X and LinkedIn are talking about right now — who said what, why it's spreading, and where the comment window still is.
2. Every reader leaves with at least one grounded angle they could turn into a post or a point of view this week, backed by real numbers and sources.

## Audience

Growth marketers, content strategists, and operators at GrowthX. They are AI-literate practitioners (AEO/GEO, content systems, AI-led growth) who publish publicly and advise clients. Write for a sharp colleague, not a beginner: no explaining what a large language model is, no hype, no filler.

## Voice & Tone

- **Scannable first, deep second.** The site renders every story headline as an expandable card — collapsed by default. Headlines must carry the news on their own; bodies are for the reader who clicks. Write headlines like a sharp colleague summarizing the story in one line, not like SEO titles.
- **Tight.** Story bodies run 120–250 words. Conversation items run 80–180 words. If a story needs more, it's two stories or it's overwritten. The lede blockquote is 3–4 sentences, never more.
- **Observational reporting, clearly separated from angle-making.** News sections report what happened with evidence. **The Conversation** reports what people are saying and why it's spreading. **Angles for the Week** is the one place the newsletter suggests how the team might use it all.
- **Operator perspective, anti-hype.** Written by someone who uses these tools and channels. Honest about limitations. This matches the GrowthX voice.
- **Label the evidence.** Distinguish vendor claims, company-reported figures, platform announcements, independent studies, and practitioner anecdotes. Readers will repeat what we print — the qualifier is part of the fact.

## What to Include

Developments from the past 7 days, in this priority order:

1. **The live conversation** — what marketing/AI X and LinkedIn are actually arguing about: viral campaigns and backlashes, executive posts and dunks, platform drama, discourse moments. Who started it, the key posts/quotes (attributed), why it's spreading, and whether the window to comment is still open. This is the section the newsletter exists for; never miss the week's main character.
2. **AI search and answer engines** — Google AI Mode/AI Overviews, ChatGPT, Perplexity: ranking changes, ads in AI answers, citation behavior, referral-traffic data. GrowthX's home turf.
3. **Ad platforms' AI** — Google, Meta, Amazon, TikTok, LinkedIn, Reddit: automated campaign types, creative generation, targeting and measurement shifts.
4. **Models and tools that change marketing work** — new models/agents when (and only when) they change how marketing content, ads, video, or analysis gets produced.
5. **Martech and adtech industry** — launches, funding, acquisitions, shutdowns, pricing changes.
6. **Data, studies, and benchmarks** — adoption surveys, traffic studies, spend forecasts. Thought-leadership fuel; always report methodology and sample size.

## Content Standards

- **Accuracy over completeness.** Every factual claim traceable to a source in the Sources section. If a number can't be verified, qualify it explicitly or cut it.
- **Preserve qualifiers.** "Company-reported," "vendor-stated," "preview," "reported by" — never let a plan become a product or a claim become a finding.
- **Viral ≠ verified.** The Conversation section reports discourse; keep the distinction between what someone claimed in a viral post and what is independently established. Quote posts accurately and attribute to the named person.
- **Professional, publishable tone.** No profanity (paraphrase around it when quoting), no cheap shots at named individuals, no rumor as fact. Everything should survive being screenshotted.
- **Competitors and clients.** Report on marketing-industry vendors (including GrowthX competitors) factually and neutrally.
- **Speculation is labeled.**

## Structure

Each edition follows this structure:

1. **Lede** — A 3–4 sentence blockquote: the week's conversation, the biggest hard-news story, and the pattern connecting them.
2. **The Conversation** — 3–5 things blowing up on X/LinkedIn among marketers. Each gets its own H3 (expandable on the site). Per item: what happened, the key posts and quotes attributed by name, why it's spreading, and a one-line **Comment window** note — what a smart contribution looks like and how long the moment has left.
3. **This Week in Marketing AI** — 4–6 hard-news stories with source links. Each story gets its own H3. Lead with the most consequential story for marketers.
4. **Platform & Tool Watch** — Bulleted quick hits: smaller platform changes, model releases, martech launches. One to three sentences each with source link and date.
5. **Common Threads** — 3–4 patterns across the week, each an H3 with a 2–4 sentence observation.
6. **Angles for the Week** — 3–5 thought-leadership angles grounded in this edition's reporting, biased toward conversations that are still live. Each angle: **the hook** (one line), **the evidence** (facts from this edition), **why now** (what makes it timely, and how long the window stays open). Raw material, not finished posts.
7. **Sources** — Numbered list with publication, date, and what each source supports. (Rendered collapsed on the site.)

Retired sections: *Voices This Week* (folded into The Conversation — attributed posts are the voices) and *Tip of the Week* (dropped 2026-07-27; the newsletter informs and arms, the team decides what to do with it).

## Mandatory Pre-Build Review (every edition)

After drafting the full and simplified editions — and before building the site or committing:

1. **Claims audit.** Re-verify every number, date, price, quote, and product-status claim against its source. Confirm each link resolves and supports the claim it's attached to.
2. **Qualifier audit.** Hunt for vendor claims reading as findings, previews reading as shipped products, viral claims reading as verified facts.
3. **Reputation audit.** The team echoes this content publicly. Flag anything that could embarrass GrowthX if quoted: unverifiable stats, one-sided competitor framing, angles that overreach the evidence, quotes with profanity not yet paraphrased.
4. Report the result explicitly ("Review: N claims verified, no flags" or a flag list with fixes) before building.

## NotebookLM Producer Briefs (each edition, after review)

Generate two NotebookLM source documents immediately after the review pass:

- `notebooklm/YYYY-MM-DD-podcast.md` — Audio Overview producer brief
- `notebooklm/YYYY-MM-DD-video.md` — Video Overview producer brief

```bash
python3 scripts/generate_notebooklm_briefs.py YYYY-MM-DD --video-title "Short editorial episode title"
```

The generator maps the edition (conversation → lead story → supporting stories → threads → angles) into podcast and video act structures, embeds audience and house-style constraints, strips URLs, and validates both files. Validate with `--check`. Upload only the matching brief to NotebookLM — never the raw edition markdown as a second source. Audio goes to `site/audio/YYYY-MM-DD.m4a` plus an ffmpeg MP3 copy at `site/audio/mp3/YYYY-MM-DD.mp3`; video to `site/video/YYYY-MM-DD.mp4`. Media is optional per edition — set the manifest flags when files ship.

## Build System (one manifest, one builder)

This project deliberately avoids the per-edition build scripts and scattered metadata of the AV newsletter (see TEAM-MEMORY 2026-07-19).

- **`config.json`** — the single brand surface: name, tagline, description, domain, publisher. Renaming or attaching the purchased domain is a one-file change.
- **`editions/manifest.json`** — the single edition registry: slug, title, hook, description, media flags. Newest first; featured automatically.
- **`scripts/build_site.py`** — the only builder. Regenerates every edition page, the homepage, robots.txt, and sitemap in one pass:

```bash
cd Marketing-AI-Newsletter
python3 scripts/build_site.py            # build everything
python3 scripts/build_site.py --check    # validate without writing
```

The site renders each H3 as an expandable story card (collapsed by default, with expand/collapse-all controls) and collapses the Sources section — this is implemented in `site/shared.js`/`site/shared.css` and applies to every edition automatically. Write headlines accordingly.

### Weekly workflow

1. **Research** (four artifacts under `research/YYYY-MM-DD/`):
   - `conversation-YYYY-MM-DD.md` — the X/LinkedIn discourse sweep: viral campaigns, executive posts, dunks, debates, platform drama. Capture exact quotes, dates, view/engagement counts where reported, and who's driving each thread. (If the XAgent X/Twitter MCP is configured with a key, use it for this track; otherwise web-search the discourse and its trade coverage.)
   - `platforms-YYYY-MM-DD.md` — primary-source announcements: ad platforms, search/answer engines, model vendors.
   - `industry-YYYY-MM-DD.md` — martech/adtech industry news, studies, funding, data.
   - `analysis-YYYY-MM-DD.md` — synthesis: what leads, what connects, candidate angles, comment windows.
2. **Draft** `editions/YYYY-MM-DD.md` (full) and `editions/YYYY-MM-DD-simplified.md` (quick summary). Respect the length budgets.
3. **Review** (claims, qualifiers, reputation).
4. **Briefs** — generate and validate both NotebookLM briefs.
5. **Manifest** — prepend the edition entry with its hook.
6. **Build** — `python3 scripts/build_site.py`, preview with `python3 serve.py` (port 8092).
7. **Commit and push.** Vercel deploys `site/` when connected.

## Technical Notes

- Editions are Markdown in `editions/`, named `YYYY-MM-DD.md` with the **Monday publication date** (covering the previous 7 days). A `-simplified.md` sibling powers the Quick Summary toggle.
- The site renders markdown client-side (`site/shared.js`), then wraps each H3 block into an expandable card and collapses the Sources section. Numbered lists render as plain paragraphs (renderer parity with the AV site) — keep Sources as `1. [..]` lines.
- Images: place under `site/editions/YYYY-MM-DD/` and reference root-relative. Never hardcode a domain in markdown.
- No subscribe CTAs and no email-send integration yet. Distribution starts as a shareable site plus the markdown itself.
