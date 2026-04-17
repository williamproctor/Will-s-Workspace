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
6. **Tool of the Week** — A single tool highlighted with structured fields (What it does / Who it's for / Pricing / Worth trying? / Link).
7. **Sources** — Numbered list of all cited sources with publication, date, and brief description.

## Source Policy

- Every factual claim should be traceable to a source in the Sources section.
- Attribute quotes to individuals by name, not to publications or shows.
- When speculating (e.g., about upcoming releases), label it explicitly as speculation and provide the evidence basis.

## Technical Notes

- Newsletter content is authored in Markdown (`.md`) in the `editions/` directory.
- The markdown is JSON-escaped and injected into the HTML page's `EDITION_MD` constant via a Python script.
- Edition dates follow a Friday publication schedule.
- Images can be placed in the edition's site directory (e.g., `site/editions/2026-04-03/`) and referenced with relative paths in the markdown.

## Audio Pipeline (required for every new edition)

Every edition ships with two audio formats so downstream platforms (SharePoint, email clients, legacy players) always have a compatible option:

1. The original `.m4a` file (NotebookLM export) is placed at `site/audio/YYYY-MM-DD.m4a`.
2. **An MP3 copy MUST be generated and placed at `site/audio/mp3/YYYY-MM-DD.mp3`** alongside the m4a. This is not optional — do it as part of the same step that copies the audio into `site/audio/`.

**Conversion command** (uses `ffmpeg`, VBR quality 2 ≈ 190 kbps, which typically halves file size while preserving audio quality):

```bash
ffmpeg -i site/audio/YYYY-MM-DD.m4a -codec:a libmp3lame -qscale:a 2 site/audio/mp3/YYYY-MM-DD.mp3 -y
```

Create the `site/audio/mp3/` directory if it does not already exist. After conversion, verify both files exist before committing.
