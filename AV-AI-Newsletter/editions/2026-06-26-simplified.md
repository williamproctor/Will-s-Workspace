# The AVS AI Dispatch — Week of June 26, 2026

> **This week, AI video control moved beyond prompts.** Creators are using Blender camera paths, depth passes, edge passes, pose passes, grey-box scenes, and 3D blocking to guide AI video models with precise camera movement. ByteDance previewed **Seedance 2.5** with claims of native 30-second clips, up to 50 reference inputs, regional editing, and 3D preview controls, though independent benchmarks are not available yet. OpenAI announced **GPT-5.6 Sol, Terra, and Luna** in limited preview, with the strongest benchmark story around long-horizon agent work. Sonilo also brought licensed video-to-music generation to fal.ai, showing audio tools becoming more timeline-aware.

---

## The Big Story

### Blender Is Becoming a Camera-Control Layer for AI Video

The most interesting AI video trend this week is a workflow pattern: create the camera move in Blender first, then use that 3D reference to guide the AI video model.

Instead of asking a model for a "slow dolly in" and hoping it understands the shot, creators can build the move in Blender and export a control reference:

- A camera path
- A grey-box scene
- A depth pass
- An outline pass
- A pose pass
- A low-detail reference animation

RunComfy's **Blender to ComfyUI AI Renderer 2.0** is one example. It uses depth, outline, or pose passes to drive Wan VACE video generation so the final video follows the original layout and motion.

Other projects point in the same direction. ComfyUI Blender temporal nodes use Blender EXR depth and normal passes as ControlNet conditioning. LooseControlVideo uses spatial blocking with 3D boxes to control object placement and movement.

The takeaway: the rough 3D scene is becoming more than a planning tool. It can become the control track for generation.

**Source:** [RunComfy](https://www.runcomfy.com/comfyui-workflows/blender-to-comfyui-ai-renderer-2-0-workflow-cinematic-video-output) · [ComfyUI Blender temporal nodes](https://github.com/12georgiadis/comfyui-blender-temporal) · [LooseControlVideo](https://arxiv.org/html/2606.19495v1) · June 2026

---

## Other Stories

### Seedance 2.5 Preview Shows Where AI Video Is Heading

ByteDance previewed **Seedance 2.5** on June 23 at its Volcano Engine FORCE conference.

The headline claim is a single native 30-second clip, generated directly instead of stitched together from shorter clips. Reports also describe support for up to **50 multimodal reference inputs**, including images, audio clips, 3D white-box models, and style references.

Other preview claims include:

- Native 4K output and 10-bit color depth
- Around 20 percent better prompt adherence
- Audio generated in the same system as the video
- Region-level editing
- 3D preview controls before full rendering

Important caveat: Seedance 2.5 is not broadly available yet. It is in enterprise beta, with public launch targeted for early July. There are no independent Seedance 2.5 benchmark results yet.

The practical story is control. Seedance 2.5 appears designed around more references, longer clips, local edits, and more structured direction.

**Source:** [The Next Web](https://thenextweb.com/news/bytedance-seedance-2-5-ai-video-4k-30-seconds) · [The Decoder](https://the-decoder.com/bytedances-seedance-2-5-breaks-the-30-second-barrier-for-ai-video-generation/) · [Tosea](https://tosea.ai/blog/seedance-2-5-bytedance-ai-video-model-guide) · June 2026

### GPT-5.6 Is About Long-Horizon Agent Work

OpenAI announced the **GPT-5.6** series on June 26:

- **Sol** — flagship model
- **Terra** — balanced model
- **Luna** — fast, lower-cost model

Access is limited at first to selected partners through the API and Codex, with broader availability planned in the coming weeks.

The benchmark story is agentic work, not ordinary chat. OpenAI says GPT-5.6 Sol sets a new state of the art on **Terminal-Bench 2.1**, which measures command-line tasks requiring planning, iteration, and tool coordination. VentureBeat reported OpenAI-provided figures of **91.91%** in `ultra` mode and **88.76%** in `max` mode.

OpenAI also introduced:

- `max` reasoning effort for deeper work
- `ultra` mode, which uses subagents for complex tasks
- More predictable prompt caching with named cache breakpoints

For AV teams, GPT-5.6 matters mostly around internal tools, publishing scripts, metadata cleanup, QA passes, and workflow agents.

**Source:** [OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/) · [VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov) · June 26, 2026

### Sonilo Brings Video-to-Music to fal.ai

Sonilo announced that its licensed video-to-music model is now available on **fal.ai**.

The model analyzes a video and generates an original soundtrack matched to the clip's length, pacing, and emotional arc. It delivers the music as a separate audio track, so editors can adjust it without changing dialogue, voiceover, or sound effects.

Through fal.ai, Sonilo says it can score videos up to **600 seconds** long.

The important pattern: the video itself becomes the timing reference. Audio generation is becoming more connected to the actual edit, not just a separate prompt.

**Source:** [Morningstar / PR Newswire](https://www.morningstar.com/news/pr-newswire/20260622cn86889/sonilo-launches-licensed-ai-music-generator-for-video-on-falai) · [Sonilo](https://sonilo.com/) · June 22, 2026

---

## Quick Hits

- **Runway Aleph 2.0 is now in Figma Weave.** Users can extract a frame, edit it, connect it back to the Aleph node with a timestamp, and carry that edit through the video while preserving the rest of the shot.
- **Seed Audio 1.0 surfaced in ByteDance's model stack.** It is described as a unified audio model for speech, music, and ambient sound.
- **GPT-5.6 adds named prompt-cache controls.** OpenAI says GPT-5.6 supports cache breakpoints and a 30-minute minimum cache life, which matters for repeated long-context agent workflows.

---

## Common Threads

### Text Prompts Are Not Precise Enough by Themselves

The strongest workflows this week use more than text: Blender camera paths, depth passes, 3D blockouts, reference images, audio timing, masks, and timelines.

### References Are Becoming the Main Control Surface

Seedance 2.5's preview claim of up to 50 reference inputs points to a broader shift. AI tools are becoming more useful when they can accept the materials production teams already have.

### Agent Benchmarks Are Getting Closer to Real Work

GPT-5.6's benchmark story focuses on tool use, planning, command-line workflows, and long-running tasks. That is closer to practical production support than a single-answer test.

---

## Tip of the Week

### Back to Basics, Week 5: Ask for a Delta

When AI revises something, ask it to tell you what changed.

Use a prompt like this:

```text
Revise this production note for clarity.

Preserve exactly:
- Speaker names
- Timecodes
- Technical terms
- Approved wording

After the revised version, include a delta:
- What changed
- What stayed the same
- Anything that still needs human review
```

For AV work, this helps with scripts, captions, edit notes, show notes, equipment summaries, SharePoint copy, and documentation.

The simple version:

```text
After the revision, list the exact changes you made.
```

That gives the reviewer a short change trail instead of forcing them to compare every line by hand.

Next week: **Use Checklists as Guardrails**.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
