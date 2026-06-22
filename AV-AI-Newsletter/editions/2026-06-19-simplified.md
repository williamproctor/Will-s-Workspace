# The AVS AI Dispatch — Week of June 19, 2026

> **This week, AI moved closer to the actual creative workspace.** Adobe is putting Firefly AI Assistant inside Premiere, Photoshop, Illustrator, InDesign, and Frame.io. Google Vids can now make longer Veo clips and generate multiple clips at once. Palmier Pro is a new open-source Mac video editor that lets AI agents operate the timeline through MCP. Claude Fable 5 reaction remains focused on hard coding and long-running agent work. LTX Trainer gives teams a way to customize the open LTX-2 audio-video model. Mistral's Voxtral TTS adds another multilingual voice model to the growing audio stack.

---

## The Big Story

### Adobe Puts AI Assistant Inside Creative Cloud Apps

Adobe announced that **Firefly AI Assistant** is now in public beta across major creative apps, including Premiere, Photoshop, Illustrator, InDesign, and Frame.io.

For AV work, Premiere and Frame.io are the most important pieces. Adobe describes assistant tasks like sorting assets into bins, batch-renaming clips, identifying interview questions, adding markers, and helping prepare raw footage for a first cut.

The important shift is context. The assistant is not just a separate prompt box. It is moving into the app where the production work already lives.

Adobe also previewed an upgraded Firefly studio with **Projects**, **Elements**, storyboard-to-video, product-video tools, and **Quick Cut**, which can assemble raw footage into a structured first cut for a person to refine.

The takeaway: Adobe is trying to make AI part of the production layer, not just the generation layer.

**Source:** [Adobe](https://blog.adobe.com/en/publish/2026/06/18/adobe-firefly-introduces-new-agentic-capabilities-and-an-upgraded-creative-ai-studio-built-for-the-way-you-work) · [TechCrunch](https://techcrunch.com/2026/06/18/adobe-adds-its-ai-assistant-to-premiere-illustrator-and-indesign/) · June 18, 2026

---

## Other Stories

### Google Vids Adds Longer Veo Clips

Google Vids now supports longer Veo clips and parallel generation.

That means users can extend an existing AI-generated clip and start multiple video generations at the same time. This is useful for comparing prompt options and building short internal videos more quickly.

Google Vids is not replacing a professional editor. But it is becoming more useful for internal communication, training support, project updates, and rough video explainers.

**Source:** [Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/06/create-longer-veo-videos-and-generate-multiple-at-once-in-Google-Vids.html) · June 17, 2026

### Palmier Pro Lets Agents Edit a Timeline

Palmier Pro is an open-source Mac video editor designed for AI agents.

The app exposes a local MCP server, which means tools like Claude, Codex, or Cursor can connect to the project and operate the timeline. An agent can work with clips, tracks, and project context instead of only responding to a prompt outside the editor.

Palmier is still early, macOS-only, and not a replacement for mature editing software. But it shows an important idea: media tools can become agent-accessible.

**Source:** [Y Combinator](https://www.ycombinator.com/launches/QtT-palmier-pro-an-open-source-video-editor-your-agents-can-operate) · [Palmier Pro GitHub](https://github.com/palmier-io/palmier-pro/blob/main/README.md) · June 2026

### LTX Trainer Makes Open Video Models Easier to Customize

Lightricks released **LTX Trainer**, a training framework for LTX-2.

It supports LoRA training, audio-video LoRA, IC-LoRA for video-to-video work, and full fine-tuning. In plain terms, it gives technical teams more ways to adapt LTX-2 to specific needs.

The requirements are still serious. Many workflows need Linux, CUDA, and high-end Nvidia GPUs. But the direction matters: open video models are becoming more customizable, not just downloadable.

**Source:** [LTX](https://ltx.io/newsroom/introducing-the-new-ltx-trainer-one-framework-every-training-mode) · [GitHub](https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer) · June 17, 2026

### Mistral Voxtral TTS Adds Another Voice Option

Mistral's **Voxtral TTS** is a 4B-parameter text-to-speech model that supports nine languages.

It is designed for low-latency voice applications, with Mistral listing 70ms model latency for a typical request and API pricing at $0.016 per 1,000 characters. The open-weight version is available for non-commercial use.

For AV teams, this adds another option to the voice stack alongside ElevenLabs, OpenAI, and other audio tools. Voice AI is splitting into several categories: narration, realtime assistants, localization, cloning, and local experimentation.

**Source:** [Mistral](https://mistral.ai/news/voxtral-tts) · [Hugging Face](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) · 2026

---

## Quick Hits

- **Premiere Pro 26.3 shipped** with just-in-time upgrades for Productions, object masking, and fixes around captions, relinking, and exports.
- **Claude Fable 5 reaction remains strong** around hard coding, long-running agent work, and difficult automation. The tradeoff is that it is slower, more expensive, and more tightly guarded than everyday models.
- **IK Multimedia released ReSing Doubling**, an add-on that creates doubled vocals and ensemble-style vocal layers from one performance.
- **Gemini 3.5 Pro is still worth watching**, but broad public access still appears pending as of this research pass.

---

## Common Threads

### AI Is Moving Into the File

Adobe's assistant in Premiere and Frame.io, and Palmier's agent-accessible timeline, point in the same direction. AI tools are moving closer to the actual project files, clips, comments, and timelines.

### First Cuts Are Becoming Automatable

Quick Cut, Google Vids clip extension, and agentic timeline tools all focus on rough assembly and early structure. The final edit still needs human judgment, but the first-pass layer is becoming more automated.

### Open Models Need Training Tools

Open video models are more useful when teams can adapt them. LTX Trainer matters because it gives technical users a clearer path to customize LTX-2 instead of only running it as-is.

---

## Voices This Week

### Zeev Farbman on Open Audio-Video Models

Lightricks co-founder and CEO Zeev Farbman said:

> "LTX-2 is the first truly open audio-video model, released with open weights and training code, and designed to run locally on consumer GPUs."

He also said:

> "It delivers the kind of quality and performance teams usually associate with closed systems, without giving up control, transparency, or the ability to customize."

The important idea: open-weight audio-video models become more useful when teams also get training code and customization paths.

### Simon Willison on Claude Fable 5

Developer Simon Willison described Fable 5 as "slow, expensive" while also saying it was capable enough that the challenge was finding tasks it could not handle.

That matches the broader reaction: Fable 5 is not being treated as a cheap everyday model. It is being treated as a high-ceiling model for hard, long-running work.

---

## Tip of the Week

### Back to Basics, Week 4: Tell It What Not to Change

When asking AI to revise something, most people explain what they want changed. They forget to explain what must stay the same.

That can create problems. A model may clean up the writing but change a timecode, paraphrase a quote, remove a safety note, or alter an approved phrase.

Add a preservation block to your prompt:

```text
Your task: revise this script for clarity and pacing.

Preserve exactly:
- All names and titles.
- All timecodes.
- Any safety instructions.
- Any quoted language.
- The three-section structure.
- The target runtime of 90 seconds.

You may change:
- Sentence length.
- Transitions.
- Repeated wording.
- Jargon that can be simplified.

Return:
1. Revised script.
2. Brief list of what changed.
```

For AV work, this is useful with timecodes, speaker names, captions, technical terms, runtime limits, file names, and stakeholder-approved wording.

The exercise: take one revision prompt you already use and add two blocks: **Preserve exactly** and **You may change**.

Next week: **Ask for a Delta** — why a short list of changes can be as useful as the revised output itself.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
