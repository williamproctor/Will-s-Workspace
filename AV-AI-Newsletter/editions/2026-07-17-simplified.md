# The AVS AI Dispatch — Week of July 17, 2026

> **AI media tools are moving from impressive output toward correctable production objects.** SmartRoto returns editable splines. Lucy 2.5 keeps a live video stream open to direction. MultiRef-Compass tests whether people, objects, actions, and sounds remain correctly connected. Dubbing 2.0 allows segment-level correction, and Aiode produces editable stems from licensed recordings. Kimi K3 and the late-breaking Qwen3.8-Max-Preview add a broader reminder: the general-model frontier is widening faster than launch-day rankings can settle.

---

## The Big Story

### SmartRoto Produces Editable Splines, Not a Flat Mask

Foundry released **SmartRoto** for Nuke on July 17. An artist creates roto keyframes, and the plugin propagates the shape through the shot while preserving an editable spline.

That is the practical difference from a flat AI mask. A compositor can adjust points, preserve artist-created keyframes, and continue working inside the existing Roto node.

SmartRoto costs:

- **$499 per year** at the introductory price
- **$599 per year** at the regular price
- A separate **Nuke-family license** is also required

Inference runs locally. Foundry says the training data is licensed and customer footage is not transmitted for processing. The plugin requires Nuke 16.1 or later, and Foundry recommends more than 8GB of VRAM.

Foundry advertises roto work that is **up to four times faster**. fxguide’s independent reporting adds an important qualification: Foundry’s testing lead said **roughly two times faster was the more consistent result**, while four times was the high end. These remain vendor test figures rather than a broad production benchmark.

The larger point is the deliverable. SmartRoto uses AI to create something an artist can inspect and correct inside a familiar professional workflow.

**Source:** [Foundry](https://www.foundry.com/products/nuke-family/smartroto) · [fxguide](https://www.fxguide.com/fxfeatured/foundrys-smartroto-ai-assisted-roto-that-aims-to-work-the-way-you-do/) · July 17, 2026

---

## Other Stories

### Lucy 2.5 Edits Video While It Streams

Decart’s **Lucy 2.5** accepts text and reference images while a video stream continues. It can replace a subject, add or remove objects, change an environment, and keep edits active over time.

Decart’s release page says **1080p at 30 FPS**, but the current API documentation lists **1280×720**. No independent latency, consistency, or quality benchmark was available during the research window.

The interaction is the main story: the image remains responsive during playback instead of becoming fixed after a render.

**Source:** [Decart release](https://decart.ai/publications/lucy-2-5-raising-the-bar-for-live-ai) · [API documentation](https://docs.platform.decart.ai/models/realtime/lucy-2.5) · July 16, 2026

### MultiRef-Compass Measures Reference Correctness

The **MultiRef-Compass** benchmark evaluates eight audio-video systems across **350 curated samples**. Its four dimensions are basic quality, reference consistency, audio-visual consistency, and instruction following.

The authors reported Gemini Omni leading visual quality and lip sync, while Kling narrowly led entity fidelity. The comparison has important limits: safety filters reduced the available samples for two systems, some metrics use another model as a judge, and there has been no independent replication.

The useful idea is to review whether the correct face, object, action, voice, and sound remain attached to one another—not only whether the clip looks polished.

**Source:** [Paper](https://arxiv.org/abs/2607.14189) · [Code](https://github.com/zxhhh0201/MultiRef-Compass) · July 15, 2026

### Dubbing 2.0 Allows Segment-Level Correction

**Synthesia Dubbing 2.0** adds revised lip sync, voice, translation, glossary support, and timing preservation across more than 130 languages.

Editors can review the transcript and translation, then regenerate a failed segment without rerendering the full video. The service is live for all customers, while Enterprise plans unlock the complete editing workflow and unlimited dubbing.

Synthesia’s description of a publishable first pass is a vendor claim. No blind comparison, numerical error rate, or independent evaluation was supplied.

**Source:** [Synthesia](https://www.synthesia.io/post/introducing-dubbing-2-0) · July 15, 2026

### BandLab Acquires Aiode

BandLab Technologies acquired **Aiode**, whose standalone web and desktop beta will continue.

Aiode supports section-level direction, alternate takes, and separate **48kHz/24-bit stereo WAV stems**. The company says its training recordings are licensed and traceable, participating musicians help create individual models, and those musicians receive revenue share.

Those are company statements. Revenue-share percentages and acquisition terms were not disclosed, and several digital-audio-workstation features remain planned.

**Source:** [BandLab Technologies](https://bandlabtechnologies.com/news/bandlab-technologies-announces-acquisition-ai-powered-digital-music-studio-aiode/) · [Aiode](https://aiode.com/product/) · July 15, 2026

---

## Frontier Watch

### Kimi K3

Moonshot AI launched **Kimi K3** on July 16 with:

- **2.8 trillion total parameters**
- **16 of 896 experts active** for each token
- Native image and video input
- A **one-million-token context window**

Kimi K3 is hosted now through Kimi products and the API. Full weights are **scheduled for July 27** and were not downloadable during this edition’s research window.

API pricing is **$0.30 per million cached input tokens, $3 per million fresh input tokens, and $15 per million output tokens**.

Kimi K3 is an understanding and agent model, **not a native video generator**. Moonshot showed it examining footage, selecting clips, creating motion-graphics code, making cuts, synchronizing edits to beats, processing audio, and revising through tools. That demonstration is vendor-reported.

The parameter count shows scale, not proof of quality. Evaluation results change with hardware, harnesses, reasoning effort, and fallback behavior, so launch-day rankings remain unsettled.

**Source:** [Moonshot AI](https://www.kimi.com/blog/kimi-k3) · [API documentation](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) · [Independent launch reporting](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems) · July 16, 2026

### Qwen3.8-Max-Preview

Alibaba officially announced **Qwen3.8-Max-Preview** on **July 19**, two days outside the newsletter’s research window.

Alibaba reports **2.4 trillion parameters** and multimodal capability. Preview access is available through Token Plan, Qoder, and QoderWork. Open weights are promised, but no release date has been published.

Alibaba says the model is “second only to Fable 5.” That vendor claim did not have independent validation at announcement. As with Kimi K3, scale and a launch-day ranking do not establish production quality.

**Source:** [South China Morning Post](https://www.scmp.com/tech/article/3361119/alibaba-says-newest-qwen-ai-model-second-only-anthropics-claude-fable-5) · July 19, 2026 · late-breaking

---

## Quick Hits

- **Griptape Enterprise** adds permissions, versioning, provenance records, and private deployment around multi-model media workflows. Foundry assigns customers responsibility for verifying the rights terms of connected models. [Source](https://www.foundry.com/products/griptape) · July 17
- **Google Vids** added Gemini Omni editing and personal avatars for eligible paid accounts. This is a partial repeat of earlier Omni coverage; the Vids integration is new. Generated clips receive SynthID. [Source](https://workspace.google.com/blog/product-announcements/introducing-gemini-omni-flash-in-google-vids) · July 16
- **Gemini Notebook** is the new name for NotebookLM. Google is positioning it as a broader source-to-audio, video, and interactive workspace; this is primarily a rebrand. [Source](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/) · July 16
- **VideoChat3** is a 4-billion-parameter long-video understanding model with 16-times spatiotemporal compression. Its benchmark results are author-reported. [Source](https://arxiv.org/abs/2607.14935) · July 16
- **LALAL.AI Lynx** isolates dialogue from surrounding sound. It uses cloud processing, and no independent quality comparison was available. [Source](https://www.lalal.ai/blog/lynx-voice-isolation-neural-network/) · July 14
- **GPT-Red** searches for prompt-injection weaknesses in connected agents. OpenAI’s performance claim is internally measured. [Source](https://openai.com/index/unlocking-self-improvement-gpt-red/) · July 15

---

## Voices This Week

- **Connie He and Márcia Mayer** described rough animation, storyboards, and artist-defined source material carrying timing and framing more precisely than text alone. Localized refinement and repeated shot review remained part of the process. [Discussion](https://themakingof.substack.com/p/filmmaker-connie-he-google-deepminds) · [Production account](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/dear-upstairs-neighbors/)
- **Nathaniel Whittemore** emphasized the agent harness around a model: tools, permissions, memory, evaluation, workflow rules, and recovery. The idea is commentary, not a measured forecast. [Discussion](https://aidailybrief.ai/e/2026-07-15)
- **Terrence O’Brien** reported that input safeguards and a paid commercial plan did not necessarily resolve final-output rights and distribution risk. Product behavior can change, and the legal questions remain unsettled. [Discussion](https://www.theverge.com/podcast/965581/suno-ai-music-vergecast) · [Supporting investigation](https://www.theverge.com/ai-artificial-intelligence/906896/sunos-copyright-ai-music-covers)

---

## Common Threads

### Editable Deliverables

SmartRoto returns splines, Dubbing 2.0 isolates correctable segments, and Aiode exports separate stems. The useful output is an artifact that fits the next production step.

### Continuous, Multimodal Control

Lucy 2.5 combines a live stream with text and image references. Rough animation can carry timing, pose, framing, and performance. The prompt box is becoming one part of a larger control surface.

### Rights and Provenance Inside the Workflow

Aiode links models to licensed recordings and participating musicians. Griptape records provenance and controls model access. Google Vids adds SynthID. Rights review is moving closer to model selection, generation, and export.

### Production-Specific Evaluation

MultiRef-Compass tests identity binding and sound-source assignment. A general preference ranking cannot answer every production question.

### Harness and Infrastructure

Permissions, storage, networking, versioning, evaluation, and recovery affect whether a model can perform reliably inside a real workflow.

### A Widening Frontier

Kimi K3 and Qwen3.8-Max-Preview arrived within days with trillion-parameter scale and multimodal claims. Their access, weights, hardware needs, and evaluation conditions differ, so the pace is clearer than the ranking.

---

## Novel Ideas Worth Watching

- **Rough animation as a control language:** blocked motion can carry timing, gesture, camera movement, and performance more precisely than a longer written prompt.
- **The live stream as an editable canvas:** Lucy 2.5 keeps generated video responsive while it plays.
- **Multi-reference binding as quality assurance:** identity, attribute, action, voice, and sound can be checked as separate review targets.

---

## Tip of the Week

### Back to Basics, Week 8: Separate Drafting From Review

Use one pass to create and a second pass to critique.

1. Ask for the first draft without requesting criticism in the same instruction.
2. Begin a separate review pass.
3. Check facts, omissions, names, dates, numbers, timecodes, formatting, preservation rules, and unsupported certainty.
4. Ask for a list of findings before requesting a rewrite.
5. Keep the draft, findings, and revision as an audit trail.

Use this review instruction:

```text
Review this draft. Do not rewrite it yet.

Check the facts against the supplied sources.
Identify missing information and formatting problems.
Verify names, dates, numbers, and timecodes.
Flag anything stated with more certainty than the evidence supports.

List each issue and cite the relevant source.
Wait for approval before revising.
```

The separate pass is especially useful for edit notes, transcript summaries, captions, metadata, production documents, and client-facing material.

Next week, Back to Basics Week 9: **Turn recurring review criteria into a reusable checklist.**

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
