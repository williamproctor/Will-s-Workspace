# The AVS AI Dispatch — Week of July 3, 2026

> **This week, AI video became more editable and more audio-aware.** Google brought **Veo 3.1** into Flow with audio support across Ingredients to Video, Frames to Video, and Extend. Anthropic released **Claude Sonnet 5**, a lower-cost model focused on agentic coding, tool use, and multi-step work. Runway expanded its partnership with Bertelsmann, showing AI video moving deeper into large media workflows. Adobe's Topaz deal also reminded the industry that enhancement, restoration, and upscaling are becoming central to AI production.

---

## The Big Story

### Google Brings Veo 3.1 Into Flow

Google updated Flow with **Veo 3.1**, adding richer audio, better prompt adherence, more realistic textures, and more precise editing controls.

The most important change is audio support across more Flow modes:

- Ingredients to Video
- Frames to Video
- Extend

These are the modes that use more than a text prompt. Ingredients to Video works from reference materials. Frames to Video uses a starting or ending image. Extend continues an existing clip.

Adding audio to those modes makes the output more production-like. The model is not only creating a silent clip; it can carry visual references, timing, motion, and sound together.

Google also added more editing control with **Insert**, a feature that adds an element to an existing scene while preserving the surrounding clip. Object removal is planned next.

Veo 3.1 is available through Flow, the Gemini API, Vertex AI, the Gemini app, and Google Vids. Some audio features are still experimental, so review and editing remain part of the process.

**Source:** [Google](https://blog.google/innovation-and-ai/products/veo-updates-flow/) · [Google Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/veo-3-1-gemini-api/) · July 2026

---

## Other Stories

### Claude Sonnet 5 Is About Agentic Work

Anthropic released **Claude Sonnet 5** on June 30.

Anthropic describes it as the most agentic Sonnet model yet. The model is built for planning, tool use, coding, terminal workflows, and longer multi-step tasks.

Key details:

- Available across Claude plans
- Available in Claude Code
- Available through the Claude API as `claude-sonnet-5`
- Introductory API price: **$2 input / $10 output per 1M tokens** through August 31
- Standard price after that: **$3 input / $15 output per 1M tokens**

Anthropic reports **63.2% on SWE-bench Pro** and **80.4% on Terminal-Bench 2.1**.

For AV teams, the relevance is mostly around workflow support: scripts, file organization, metadata cleanup, QA passes, SharePoint packaging, publishing workflows, and small internal tools.

**Source:** [Anthropic](https://www.anthropic.com/news/claude-sonnet-5) · June 30, 2026

### Runway Expands Its Bertelsmann Partnership

Runway announced a creative partnership with **Bertelsmann** on July 1.

The agreement brings Runway models into Bertelsmann businesses including RTL Group, BMG, and Bertelsmann Marketing Services. Runway says the relationship began through the Bertelsmann AI Hub in 2024 and is now expanding into broader creative workflow development.

The important pattern: AI video tools are moving from individual browser experiments into operational media workflows.

**Source:** [Runway](https://runwayml.com/news/runway-announces-creative-partnership-with-bertelsmann) · July 1, 2026

### Adobe's Topaz Deal Highlights AI Enhancement

Late last week, Adobe announced a definitive agreement to acquire **Topaz Labs**.

Topaz is known for AI image and video enhancement: sharpening, denoising, restoring, upscaling, and improving existing footage or images.

Adobe says Topaz technology will come into Firefly, Firefly Services, and Creative Cloud apps, while Topaz products will continue as standalone offerings. Adobe also highlighted Topaz's **Neurostream** technology for running large image and video models locally on consumer hardware.

The useful reminder: AI production is not only generation. Finishing, restoration, and enhancement are becoming part of the same tool stack.

**Source:** [Adobe](https://news.adobe.com/news/2026/06/adobe-to-acquire-topaz-labs) · [TechCrunch](https://techcrunch.com/2026/06/25/adobe-acquires-image-and-video-enhancement-tool-maker-topaz-labs/) · June 25, 2026

---

## Quick Hits

- **Seedance 2.5 moved into early-access coverage.** Since we covered the preview last week, the main update is workflow positioning: longer clips, more references, region-level editing, and native audio-video generation.
- **LTX 2.3 keeps pushing open audio-video generation.** LTX emphasizes synchronized audio-video output, cleaner audio, native portrait output, and audio-to-video workflows. Older LTX 2.0 LoRAs need retraining because the latent space changed.
- **Video leaderboards remain task-dependent.** Artificial Analysis shows Seedance 2.0 leading among text-to-video models with audio output, but different rankings weigh Veo, Kling, HappyHorse, and Runway differently.

---

## Common Threads

### Video Is Becoming Editable After Generation

Veo 3.1 in Flow, Seedance 2.5's region-level editing, Runway's workflow partnerships, and LTX's retake/extend-style tooling all point toward the same direction: generation is becoming only the first step.

### Audio Is Becoming Part of the Video Model

Google is adding audio across more Flow modes. LTX continues to emphasize synchronized audio-video generation. Seedance is also framed around native audio-video output. The old pattern of silent clips first and sound later is starting to change.

### Enterprise AI Is About Workflow Fit

Runway with Bertelsmann, Adobe with Topaz, and Google through Vertex AI all show the same pattern. The tool has to fit into production, review, enhancement, and deployment workflows.

---

## Tip of the Week

### Back to Basics, Week 6: Use Checklists as Guardrails

When asking AI to revise, summarize, or review something, give it a checklist first.

Example:

```text
Before you revise, use this checklist:

- Preserve all names, dates, and timecodes.
- Keep technical terms unchanged unless they are clearly wrong.
- Remove repeated ideas.
- Make the wording clearer and shorter.
- Do not add new claims.
- Flag anything uncertain instead of guessing.

After the revision, show:
- Revised version
- Checklist results
- Items that need human review
```

For AV work, this helps with edit notes, equipment summaries, captions, SharePoint copy, scripts, documentation, asset lists, and QA passes.

The small habit: before asking AI to improve something, tell it how you will judge the result.

Next week: **Give It Examples Before You Ask for Output**.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
