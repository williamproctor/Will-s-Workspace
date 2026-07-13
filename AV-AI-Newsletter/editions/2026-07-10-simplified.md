# The AVS AI Dispatch — Week of July 10, 2026

> **Uber provided this week’s clearest example of AI adoption moving from individual tasks into departmental workflows.** Its “Agentic Pods” pair AI-proficient engineers with business experts for two weeks of observation, building, validation, and deployment. In media, **Runway Dev** brought first- and third-party image, video, and audio models into one enterprise platform. **Meta launched Muse Image and previewed Muse Video** with native audio. **GPT-5.6 became generally available**, accompanied by ChatGPT Work for long-running tasks. And **LucidLink connected Frame.io footage with external production storage** without moving or duplicating files.

---

## The Big Story

### Uber’s Agentic Pods Focus on Complete Workflows

Uber CTO **Praveen Neppalli Naga** shared company-reported figures showing how deeply AI has entered its engineering organization:

- 99 percent of engineers use AI tools
- More than 70 percent of pull requests are attributed to local or cloud agents
- Engineers have created more than 2,500 agent skills

The figures have not been independently audited. The more useful part of the story is how Uber is taking AI into finance, legal, operations, marketing, support, HR, procurement, and other departments.

Uber selected approximately 30 AI-proficient engineers and paired each one with a departmental expert. Each **Agentic Pod** received two weeks:

- Days 1–2: Observe and document the work
- Day 3: Prioritize opportunities
- Days 4–5: Build an agent with the expert
- Days 6–9: Validate it with more users
- Day 10: Ship

Naga said Uber ran 16 pods across 16 business functions in two months. Reported results included:

- Capital allocation analysis: 15 hours to 30 minutes
- Financial pacing reports: two days to 10 minutes
- Marketing website QA: two weeks to 50 minutes
- Support workflow creation: 9,000 manual workflows moved to self-service automation

The main lesson was not simply faster tasks. Uber found larger gains by redesigning whole workflows, including handoffs, approvals, tools, and cross-team steps.

For AV departments, that pattern is relevant to work spanning intake, scheduling, recording, editing, review, captions, metadata, publishing, archiving, and support. Uber’s approach begins by observing the people doing the work rather than trying to automate from documentation alone.

**Source:** [Praveen Neppalli Naga](https://x.com/praveenTweets/status/2074605343439810922) · [Business Insider](https://www.businessinsider.com/uber-cto-bets-on-agentic-pods-make-ai-more-efficient-2026-7) · July 7, 2026

---

## Other Stories

### Runway Dev Puts Multiple Media Models Behind One API

Runway launched **Runway Dev**, an enterprise media platform that combines its own models with third-party options.

The initial catalog includes:

- Runway Gen-4.5
- Runway Aleph 2.0
- Runway Act-Two
- ByteDance Seedance
- OpenAI GPT Image 2
- ElevenLabs models

Runway says developers can change models with one line of code and monitor spending through one dashboard.

The platform also includes vendor-stated enterprise controls such as no-training commitments, zero-data-retention support, SOC 2 Type II compliance, IP indemnification, moderation, cost controls, and a 99.9 percent uptime commitment.

The larger pattern: professional media systems are starting to assume that different models will handle different parts of the workflow.

**Source:** [Runway](https://runwayml.com/news/introducing-runway-dev) · July 8, 2026

### Meta Launches Muse Image and Previews Muse Video

Meta released **Muse Image**, an image generation and editing model that can compose from multiple references, use tools, and refine its own output.

Meta also introduced **Content Seal**, an invisible provenance signal designed to survive cropping, compression, resizing, and screenshots.

**Muse Video** remains a preview. Meta says it generates native audio with video, while acknowledging that audio-video synchronization and physically accurate fast motion still need improvement.

The immediate story is not a finished new video platform. It is Meta combining media generation, editing, references, tool use, and provenance in one model family.

**Source:** [Meta](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) · July 7, 2026

### GPT-5.6 Is Now Generally Available

OpenAI moved **GPT-5.6 Sol, Terra, and Luna** from limited preview into general availability across ChatGPT, Codex, and the API.

The release includes:

- Ultra mode with parallel subagents
- Program Calling for coordinating tools
- A multi-agent API capability entering beta
- Stronger computer-use and design performance

OpenAI also launched **ChatGPT Work**, an agent that can remain with a project for hours, gather information across connected applications and files, and create finished documents, spreadsheets, slides, or web applications.

The operational questions remain permissions, connected systems, review controls, and data handling—not only benchmark results.

**Source:** [OpenAI GPT-5.6](https://openai.com/index/gpt-5-6/) · [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) · July 9, 2026

### LucidLink Connect Unifies Frame.io and Production Storage

LucidLink introduced a workflow that places Frame.io Camera-to-Cloud footage beside assets held in other cloud and storage systems.

It does not move or duplicate the files. Editors access them through one filespace and can work in Premiere, Resolve, or Avid.

The system streams only the portions of media needed for playback and editing. It is currently available to enterprise accounts.

This matters to AI workflows because agents and media models need reliable access to the right assets, paths, permissions, and versions.

**Source:** [LucidLink](https://www.lucidlink.com/blog/lucidlink-connect-frame-io) · July 7, 2026

---

## Quick Hits

- **GPT-Live** brings full-duplex voice to ChatGPT, allowing the system to listen and speak at the same time. API access is planned. Voice with video or screen sharing is not supported at launch.
- **Runway AVTensor** is an open-source media decoder designed to keep audio and video aligned from the same time origin in model-training pipelines.

---

## Common Threads

### The Workflow Is Becoming the Unit of AI Adoption

Uber’s pods redesign full departmental workflows. ChatGPT Work operates across applications. Runway Dev connects multiple models. LucidLink connects media stored across systems.

The model is becoming one part of a longer chain of work.

### Model Choice Is Moving Behind a Platform

Runway Dev provides multiple media models. GPT-5.6 has capability and cost tiers. Meta connects reasoning and media generation.

This places more importance on routing, permissions, cost tracking, retention, and reliability.

### Data Access Matters as Much as Model Capability

Agents cannot complete work without access to the correct files and systems. Media models cannot produce reliable results from misaligned audio and video. The data layer remains part of the production system.

---

## Tip of the Week

### Back to Basics, Week 7: Give It Examples Before You Ask for Output

When a format matters, give AI two representative examples before requesting a new output.

Use this pattern:

```text
Here are two examples of the output format I want.

Example 1:
[Paste a strong example]

Example 2:
[Paste another strong example]

Create a new version using the same:
- Structure
- Level of detail
- Tone
- Labeling pattern
- Approximate length

Do not copy the subject matter or wording.
Use the examples only as format references.
```

For AV work, examples can establish the format for edit notes, timecodes, equipment summaries, captions, production documentation, client updates, show notes, and QA reports.

Remove confidential names, links, credentials, and project details before sharing examples with an AI system.

The small habit: provide two examples and clearly identify what the model should imitate—and what it should not copy.

Next week: **Separate Drafting From Review**.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
