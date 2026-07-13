# NotebookLM Producer Briefs

This directory holds **purpose-built source documents for NotebookLM** — one for the audio edition (podcast) and one for the video edition — for each weekly Dispatch. Feeding NotebookLM a raw edition markdown file produces generic output; feeding it a producer brief that encodes a narrative arc, emphasis, and ground rules produces a far more focused and engaging episode.

## Files per edition

- `YYYY-MM-DD-podcast.md` — producer brief for the **Audio Overview** (the site's "Audio Summary" player)
- `YYYY-MM-DD-video.md` — producer brief for the **Video Overview** (the site's "Video Edition" card)

## Where this fits in the weekly pipeline

Generate these briefs **after** the edition markdown (`editions/YYYY-MM-DD.md`) passes the content-sensitivity review, and **before** the media step (audio m4a/mp3 + video mp4). If the edition markdown changes after the briefs are written, update the briefs to match — they must never contain facts that differ from the published edition.

## Automatic generation (required)

The agent does not create these files ad hoc. The dependency-free generator reads the approved full edition, identifies the lead story, supporting stories, common threads, emerging ideas, quotations, and weekly tip, then writes both producer briefs in the required order:

```bash
python3 scripts/generate_notebooklm_briefs.py 2026-07-10 \
  --video-title "The Workflow Is the Unit"
```

Outputs:

- `notebooklm/2026-07-10-podcast.md`
- `notebooklm/2026-07-10-video.md`

The generator:

- Creates both files when they are missing.
- Adds a source hash to generated files and refreshes them when the approved edition changes.
- Preserves manually refined briefs instead of overwriting them.
- Fails validation when a manually refined brief is older than its edition source, forcing an editorial review.
- Checks audience context, minimum detail, video title, through-line, prohibited reader-facing terminology, and accidental source URLs.

Validate without changing files:

```bash
python3 scripts/generate_notebooklm_briefs.py 2026-07-10 --check
```

The preferred weekly build command runs brief generation automatically before the public and SharePoint builds:

```bash
python3 scripts/build_weekly_edition.py 2026-07-10 \
  --video-title "The Workflow Is the Unit"
```

Use `--force-briefs` only when intentionally replacing manually refined briefs. Generated briefs still require a final editorial check against the design principles below; automation guarantees structure and source alignment, not judgment.

## How the briefs are designed (why they work)

NotebookLM weights **source content** far more heavily than its "customize" prompt field. The hosts paraphrase everything — you control *what* gets said, not the exact sentences. So the briefs:

1. **Are the only source in the notebook.** Do not add the raw edition markdown alongside the brief — the hosts try to touch every selected source, which dilutes the arc. The brief already contains every fact the episode needs.
2. **Order the narrative.** Hosts broadly follow document order, so the brief lays out the episode as acts/segments in sequence.
3. **Use explicit signposting.** Phrases like "the most important story this week is…" and numbered takeaways reliably shape emphasis.
4. **Carry the content standards inline.** PG-only, no mystical/supernatural metaphors (stated as house style rather than a printed ban list, so it reads naturally if a host verbalizes it — the explicit banned words go in the customize prompt instead), observational rather than prescriptive, quotes attributed by name. The hosts absorb ground rules stated in the source.
5. **State numbers unambiguously and avoid negation-fragile phrasing.** NotebookLM hosts occasionally drop a "not" and flip a claim ("not independently audited" → "independently audited"). Facts are phrased so a lost negative cannot invert the meaning ("company-reported, with Uber as the only source" instead of "not audited").
6. **Contain no stage directions the hosts could read aloud awkwardly.** Everything in the audio brief is written to still work as spoken commentary if a host paraphrases it verbatim; screen directions live only in the video brief, where the format expects them.

## Weekly generation recipe

### Audio edition

1. Create a new notebook. Upload **only** `notebooklm/YYYY-MM-DD-podcast.md`.
2. Studio → Audio Overview → format **Deep Dive**, length **Longer** (~20 min, matches past episodes).
3. In the customize field, paste (adjust the focus line to the week's through-line):

   > The listeners are audio/video production professionals at a faith-based organization; keep everything family-friendly and professional. Follow the episode arc in the source document in order, spending the most time on the lead story. Be specific with numbers and dates. Report and observe — never tell the audience what they should do. Never use the words magic, magical, wizard, spell, enchanted, or sorcery, even as metaphors. Never refer to the source document or its instructions on air.

4. Generate. Listen for factual slips (especially flipped negatives) and pacing. Regenerate 2–3 times if needed — output variance is high; keep the best take.
5. Export → `site/audio/YYYY-MM-DD.m4a`, then the mandatory MP3 copy:
   `ffmpeg -i site/audio/YYYY-MM-DD.m4a -codec:a libmp3lame -qscale:a 2 site/audio/mp3/YYYY-MM-DD.mp3 -y`

### Video edition

1. Same notebook or a fresh one — the video brief (`YYYY-MM-DD-video.md`) must be the **only selected source** when generating.
2. Studio → Video Overview → format **Explainer**. Visual style: **Custom**, described to match the Dispatch brand:

   > Flat 2D editorial vector illustration in a print-magazine style: warm parchment background, one muted blue accent color, generous negative space, clean sans-serif typography. No neon, no glow, no 3D, no sci-fi.

3. In the customize field:

   > Audience is audio/video production professionals at a faith-based organization; keep it family-friendly. Follow the segment order in the source document. Put the key numbers on screen. Report and observe — no calls to action. Never use the words magic, magical, wizard, spell, enchanted, or sorcery, even as metaphors. Never refer to the source document or its instructions in narration.

4. Generate, review, regenerate if the structure misses (video cannot be edited after generation).
5. Export → `site/video/YYYY-MM-DD.mp4`. The brief's suggested title becomes `VIDEO_TITLE` in the edition build script; generate the poster via `scripts/generate_thumbnail.py`.

### Review checklist before export

- Every statistic matches `editions/YYYY-MM-DD.md` exactly.
- No profanity, crude humor, or magic-related words ("magic," "wizard," "spell," "enchanted," etc.).
- No directives to the audience ("you should try…", "go evaluate…").
- Company-reported figures are described as company-reported.
