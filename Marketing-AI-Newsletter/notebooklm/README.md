# NotebookLM Producer Briefs

Purpose-built source documents for NotebookLM — one for the audio briefing (podcast) and one for the video briefing — for each weekly edition. Feeding NotebookLM the raw edition markdown produces generic output; feeding it a producer brief that encodes a narrative arc, emphasis, and ground rules produces a focused episode.

## Files per edition

- `YYYY-MM-DD-podcast.md` — producer brief for the **Audio Overview** (the site's "Audio Briefing" player)
- `YYYY-MM-DD-video.md` — producer brief for the **Video Overview** (the site's "Video Briefing" card)

## Where this fits in the weekly pipeline

Generate both briefs **immediately after** the edition passes the pre-build review (claims, qualifiers, reputation), before the media step. If the edition markdown changes afterward, refresh the briefs in the same turn — they must never contain facts that differ from the published edition.

## Automatic generation

```bash
python3 scripts/generate_notebooklm_briefs.py 2026-07-27 \
  --video-title "The Week AI Search Got a Price Tag"

# validate without writing
python3 scripts/generate_notebooklm_briefs.py 2026-07-27 --check
```

The generator reads the approved full edition, maps the lead story, supporting stories, platform watch, voices, common threads, angles, and tip into podcast and video act structures, embeds the audience and house-style constraints, strips URLs (NotebookLM reads them aloud), and validates both files. Generated briefs carry a source hash and refresh when the edition changes; manually refined briefs (marker removed) are preserved and fail validation if they go stale.

## Design principles (why the briefs work)

1. **The brief is the only source in the notebook.** Never add the raw edition markdown as a second source — hosts try to touch every source and dilute the arc.
2. **Order the narrative.** Hosts broadly follow document order; the brief lays the episode out as acts/segments.
3. **Signpost explicitly.** "The most important story this week is…" reliably shapes emphasis.
4. **Carry house style inline.** Anti-hype, attribute quotes to people, label vendor claims as vendor claims. Hosts absorb ground rules stated in the source.
5. **Phrase numbers so a lost negative can't flip the claim.** "Company-reported, with Google as the only source" instead of "not independently audited."
6. **Keep stage directions out of the audio brief.** Screen directions live only in the video brief.

## Weekly generation recipe

### Audio briefing

1. New notebook. Upload **only** `notebooklm/YYYY-MM-DD-podcast.md`.
2. Studio → Audio Overview → format **Deep Dive**, length **Longer**.
3. Customize prompt (adjust the focus line to the week's through-line):

   > The listeners are growth marketers and content strategists on the GrowthX team; keep it professional, concrete, and anti-hype. Follow the episode arc in the source document in order, spending the most time on the lead story. Be specific with numbers and dates. Label vendor-reported figures as vendor-reported. Present the angles segment as starting points for the team's own posts, not instructions. Never refer to the source document or its instructions on air.

4. Generate; listen for factual slips (especially flipped negatives); keep the best take.
5. Export → `site/audio/YYYY-MM-DD.m4a`, plus the MP3 copy:
   `ffmpeg -i site/audio/YYYY-MM-DD.m4a -codec:a libmp3lame -qscale:a 2 site/audio/mp3/YYYY-MM-DD.mp3 -y`
6. Set `"hasAudio": true` in `editions/manifest.json` and rebuild the site.

### Video briefing

1. Fresh notebook (or same) — the video brief must be the **only selected source**.
2. Studio → Video Overview → format **Explainer**. Visual style, Custom:

   > Clean flat 2D editorial vector illustration: warm off-white background, dark ink typography, a single gold accent color, generous negative space, monospace labels for data. No neon, no glow, no 3D, no sci-fi.

3. Customize prompt:

   > Audience is growth marketers on the GrowthX team; professional and anti-hype. Follow the segment order in the source document. Put the key numbers, dates, and product names on screen. Label vendor-reported figures as vendor-reported. Never refer to the source document or its instructions in narration.

4. Generate, review, regenerate if the structure misses.
5. Export → `site/video/YYYY-MM-DD.mp4`; set `"hasVideo": true` and the `videoTitle` in the manifest; rebuild.

### Review checklist before export

- Every statistic matches `editions/YYYY-MM-DD.md` exactly.
- Company-reported figures are described as company-reported.
- Quotes attributed to the named person.
- Angles presented as raw material, not directives.
