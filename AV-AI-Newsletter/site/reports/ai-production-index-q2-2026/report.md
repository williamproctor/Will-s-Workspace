# The AVS AI Production Index — Q2 2026

> A quarterly assessment of what AI can and can't do in audio/video production. No hype. Just what works, what's close, and what's still a demo. This Q2 edition is a snapshot as of June 2026.

The Q1 edition ended with a simple pattern: AI could already handle a large share of repetitive AV work, but the final quality pass still belonged to people. Q2 did not overturn that conclusion. It sharpened it.

The biggest change this quarter is that AI production stopped looking like a collection of isolated generators and started looking like a set of production workspaces. Video tools gained timelines, keyframes, memory, shot-level revision, and stronger handoff paths. Audio tools moved from "generate a clip" toward realtime conversation, open-weight music generation, and targeted editing. Agents moved from chat windows into Microsoft 365, code repositories, local runtimes, and controlled production environments.

The headline shift is not that AI can now replace a production team. It still cannot. The shift is that the "middle 70%" of many workflows is getting compressible: rough cut assembly, transcript cleanup, captioning, search, media routing, versioning, background music, voice drafts, code scaffolding, documentation, and first-pass variations. The last 10-30% still decides whether the work is good.

That is the Q2 story: more leverage, more context, more integration, and still a clear need for human judgment.

---

## If You Only Read One Section

**What changed since Q1:**

- **Video editing became the strongest AI video category.** Runway Aleph 2.0, Threadline, VidMuse 2.0, and PAI 2.0 all focus on revision and control, not just generation.
- **Enterprise agents moved into real work systems.** Microsoft Build introduced Scout, Work IQ APIs, Windows Agent Framework, and Microsoft Execution Containers.
- **Audio moved in two directions at once:** realtime voice agents on one side, open-weight local music and sound generation on the other.
- **Creative apps became hubs.** Adobe Firefly, Google Flow, PAI, and VidMuse are all trying to be workspaces that connect models, assets, timelines, and revision loops.
- **Open-weight models became more credible for AV.** Stable Audio 3 and AVTR-1 show that local or self-hosted options are no longer limited to text models.

**What you can do right now:**

- Generate or edit short video clips for concept work, supplemental visuals, and controlled revisions.
- Use AI inside professional post tools for search, masking, focus adjustment, cleanup, captions, and audio repair.
- Produce usable background music, voice drafts, and realtime voice interactions with human review.
- Build internal tools and workflow automations with coding agents and Microsoft 365-connected agents.
- Use transcript- and shot-based tools to compress rough-cut and review workflows.

**What you still can't do reliably:**

- Produce a polished long-form narrative video from prompts alone.
- Trust AI-generated video with exact text, hands, complex physics, or long continuity.
- Replace a human editor, sound designer, composer, animator, or production lead.
- Deploy autonomous agents into production workflows without permissions, logs, and human checkpoints.

Every section below follows the same frame: **what's ready, what's close, what's not there yet**, and a practical takeaway.

---

## The Basics: Models, Agents, and Context

Q1 explained the difference between chatbots and agents. In Q2, that distinction became more important.

A **chatbot** answers. An **agent** acts. The difference is not just intelligence; it is access. An agent can use tools, retrieve files, write code, edit documents, trigger workflows, and check its own work. That access creates leverage, but it also creates risk. The better the agent, the more important the boundaries around it become.

### The Q2 frontier model picture

| Provider | Primary Surface | Q2 Position | AV Relevance |
|---|---|---|---|
| OpenAI | ChatGPT, Codex, Realtime API | Strongest general-purpose and realtime voice stack | Voice agents, coding, transcription, live translation |
| Anthropic | Claude, Claude Code, Managed Agents | Strong reasoning and tool-use; enterprise deployment improvements | Coding agents, secure internal agents, long-context analysis |
| Google | Gemini, Flow, Antigravity, Vertex AI | Gemini 3.5 Flash available; 3.5 Pro pending | Video/audio generation, workflow agents, coding |
| xAI | Grok, Grok Imagine | Strong model competition; new image-to-video preview | Early video model evaluation and chatbot alternative |
| Meta / open-weight ecosystem | Llama and related models | Strong self-hosting option | Sensitive data workflows, internal tools |
| Stability AI | Stable Audio 3 | Open-weight audio generation arrives | Local music and sound generation |

### What changed in Q2

The model layer became less interesting by itself. The important change is what providers wrapped around the models:

- **Microsoft Work IQ** gives agents workplace context across Microsoft 365.
- **Google Flow** turns multimodal generation into a creative workspace.
- **Runway Edit Studio** wraps Aleph 2.0 in an editing-first workflow.
- **Adobe Firefly** increasingly acts as a hub for Adobe and partner models.
- **Antigravity, Codex, Claude Code, Cursor, and Windsurf** turn models into development harnesses.

The takeaway from Q2 is clear: **the model matters, but the operating context matters more.** A slightly weaker model with the right files, tools, permissions, and review loop often beats a stronger model operating blind.

---

## Video Generation and Video Editing

This is the category that changed most since Q1. The Q1 question was "can AI generate usable video?" The Q2 question is "can AI help revise video without starting over?"

### The field right now

| Tool / Model | Primary Use | Resolution / Duration | Production Readiness |
|---|---|---|---|
| Runway Aleph 2.0 | In-context editing of existing footage | Up to 30s at 1080p | Strong for targeted revisions |
| Gemini Omni Flash | Multimodal video generation and conversational editing | Short clips through Gemini / Flow / YouTube surfaces | Promising, still early for API workflows |
| Seedance 2.0 | Production-friendly text/image/video generation | Short-form video, strong references | Strong general-purpose generation |
| Kling 3.0 | Cinematic generation and controls | Up to 4K in supported modes | Strong for API-driven shot generation |
| Grok Imagine 1.5 Preview | Image-to-video API | Up to 720p | Early preview |
| PAI 2.0 | AI video workspace | 15-second segments, keyframe workflow, 4K claims | Promising workspace model |
| VidMuse 2.0 | Storyboard/timeline revision | Shot-level revision and timeline tools | Promising for iterative workflows |

### Ready to use

- **Targeted video edits on existing footage.** Aleph 2.0 is the clearest Q2 jump. Editing one keyframe and propagating that change across a short clip is a real production workflow for variations, fixes, and controlled visual changes.
- **Image-to-video for concept shots.** Starting from a reference image remains more reliable than pure text-to-video. Grok Imagine 1.5, Seedance, Kling, and other tools reinforce that pattern.
- **Short-form concept and B-roll generation.** The 5-15 second range remains the reliable zone.
- **Conversational revisions inside workspaces.** Flow, PAI, and VidMuse are moving toward project-level revision instead of one-off generations.

### Close but not reliable

- **Longer scene continuity.** Multi-shot support is improving, but continuity still degrades as scenes get longer or more complex.
- **Precise action direction.** Camera movement and mood are easier than exact blocking, timing, or physical interaction.
- **Project-level style consistency.** Tools can maintain a look across some shots, but longer sequences still need human control.
- **Native audio-video generation.** Models with native audio are improving, but audio timing, dialogue, and visual sync still need review.

### Not there yet

- **Prompt-only long-form production.** A complete polished minute-long sequence from prompts alone remains unreliable.
- **Stable text inside generated video.** Add text in post.
- **Complex hands, tools, and fine physical interactions.** Still a common failure point.
- **Final delivery without human review.** Generated or edited video still needs a quality pass.

**The takeaway:** Q2 made AI video more useful by making it more editable. The best use today is not "make the whole video." It is "make the first version faster, revise a controlled shot, or create variations without a reshoot."

---

## Video Editing and Post-Production

Post-production remains the highest-confidence category for immediate AV value.

### Ready to use

- **DaVinci Resolve 21.** The official Q2 release adds the Photo page, IntelliSearch, CineFocus, speech generation, slate tools, improved noise reduction, motion deblur, and expanded scripting hooks for AI analysis. The important point is not one feature; it is that AI is now woven through search, finishing, still images, audio, and metadata.
- **AI subject isolation and masks.** Premiere, Resolve, Final Cut, and plugins continue to make rotoscoping and subject isolation faster.
- **Transcript-based editing.** Descript-style editing remains highly effective for spoken-word work. It is not a replacement for timeline editing, but it compresses rough assembly and cleanup.
- **Topaz enhancement.** Hyperion 2 converts standard dynamic range or 8-bit AI-generated material into higher-bit-depth HDR-friendly outputs, improving finishing latitude for the right source footage.
- **Threadline.** The new intonation-based editing approach is promising for interviews, internal communications, training, and spoken-word material where pacing and emphasis matter.

### Close but not reliable

- **AI-created rough cuts.** Useful as a starting point, but not a final edit.
- **Shot-level revision inside AI workspaces.** VidMuse 2.0 and PAI 2.0 show the right direction, but they still need testing against real production feedback.
- **Automatic B-roll recommendations.** Helpful for discovery, not yet a substitute for editorial taste.

### Not there yet

- **Creative editorial judgment.** Pacing, emphasis, tone, and emotional structure still require a human editor.
- **Unsupervised client-ready outputs.** AI can assemble and clean; humans still decide.
- **Complex multi-format delivery without QC.** Captioning, aspect ratios, loudness, and export settings still need verification.

**The takeaway:** If a team wants reliable time savings, start with post-production. Search, cleanup, captions, masking, focus tools, audio repair, transcript workflows, and enhancement are ready enough to matter.

---

## Capture, 3D, and Spatial Workflows

Q2 also showed movement in capture and spatial workflows. This category is still uneven, but the capture layer is getting more accessible.

### Ready to use

- **Consumer 360 capture for spatial reconstruction.** The Insta360 + Splatica Project Eternal pattern shows how a consumer walk-through can become a navigable spatial asset.
- **Gaussian splat experiments.** Useful for location capture, previsualization, and interactive reference spaces.
- **Consumer 3D scanning.** Revopoint POP 4 and similar devices make object capture more accessible for reference, previs, and lightweight production support.

### Close but not reliable

- **Splat-native editing.** Capture is becoming easier; editing the resulting spatial assets is still a fragmented workflow.
- **Production-quality 3D reconstruction from casual capture.** Good enough for references and internal use, not always good enough for final delivery.
- **Cross-tool pipelines.** Moving from capture to edit to delivery still requires manual glue.

### Not there yet

- **Fully automated volumetric production.** Capture, cleanup, retopology, lighting, and delivery still need specialist oversight.
- **Reliable real-time spatial editing for non-specialists.** The tools are improving, but the workflow is not yet simple.

**The takeaway:** Spatial capture is becoming more available, but the production workflow around it is still early. Use it for references, planning, documentation, and experiments before treating it as a final-output pipeline.

---

## Voice, Realtime Audio, and Text-to-Speech

Q2 was a major quarter for realtime audio and voice agents.

### Ready to use

- **OpenAI Realtime API.** The Q2 release stack covers streaming transcription, live translation, and realtime voice agents with tool use. This makes live voice interfaces more practical than they were in Q1.
- **ElevenLabs expressive voice.** ElevenLabs' newer voice controls make emotion and delivery more steerable, especially for short-form narration and character voice drafts.
- **Short narration and voice drafts.** AI text-to-speech remains ready for internal drafts, scratch narration, and some final informational content with review.
- **Streaming transcription.** Real-time transcription is now mature enough for many production and operations workflows.

### Close but not reliable

- **Long-form narration.** Drift in pacing and emphasis still appears over longer reads.
- **Realtime voice agents with production responsibility.** They can respond, use tools, and translate, but they need clear boundaries and logs.
- **Fine emotional direction.** Voice models respond to tags and prompts, but subtle delivery still needs human performance or careful review.

### Not there yet

- **Replacing premium voice performance.** AI can produce good narration; it does not replace a skilled voice actor where nuance matters.
- **Unsupervised realtime agents in sensitive contexts.** Human escalation and guardrails remain necessary.
- **Perfect pronunciation of specialized terms.** Custom dictionaries and review still matter.

**The takeaway:** Realtime audio crossed from demo into practical tooling this quarter. The safest near-term use is transcription, translation, draft narration, and controlled voice-agent workflows with clear human oversight.

---

## Music and Sound

Music and sound generation improved sharply in Q2, especially because open-weight options became more credible.

### Ready to use

- **Background music and underscore.** AI-generated music is usable for drafts, internal projects, and some low-risk background contexts.
- **Stable Audio 3 small and medium.** Open-weight models can generate music and sound effects locally or self-hosted, with small models able to run on consumer hardware and medium models supporting longer outputs.
- **Lyria 3.** Google's Q2 music stack adds structured music generation, lyric timing, and developer access through Google surfaces.
- **Music in production workspaces.** Google Flow and Adobe Firefly-style hubs increasingly connect video, music, voice, and visual generation inside one workspace.

### Close but not reliable

- **Distinctive musical identity.** Models can produce polished genre outputs, but memorable themes still need human composition.
- **Targeted audio edits.** Inpainting and continuation are improving, especially in Stable Audio 3, but final mixes still need ears.
- **Commercial-use certainty across every provider.** Licensing and training-data policies vary. Document the model and terms used.

### Not there yet

- **Replacing a composer for signature work.** AI music remains strongest as background, reference, or temp material.
- **Final sound design without review.** AI sound effects still need timing, layering, and mix decisions.
- **Complex adaptive scores.** Dynamic music that follows long-form narrative changes remains difficult.

**The takeaway:** Q2 made music generation more useful and more controllable, but the best use remains background, temp, reference, and draft work. For final signature music, keep people in the loop.

---

## Avatars and Synthetic Presenters

This category split into two clearer lanes in Q2: pre-rendered avatar video and realtime interactive avatars.

### Ready to use

- **Pre-rendered training and informational videos.** Synthesia and HeyGen remain viable for structured scripts, training content, and repeatable internal communication.
- **Multilingual variants.** Avatar platforms are useful when the same controlled message needs to appear in multiple languages.
- **Custom avatars for controlled contexts.** Quality is good enough for some internal and instructional uses when expectations are clear.

### Close but not reliable

- **Realtime interactive avatars.** HeyGen's separate realtime product, Tavus-style systems, and Avaturn AVTR-1 point to a real category. AVTR-1 is especially notable because it is open-weight and designed for low-latency duplex interaction.
- **High-trust presenter replacement.** Audiences still respond differently to real people and synthetic presenters.
- **Expressive gestures and listening behavior.** Improving, but still easy to overuse.

### Not there yet

- **Replacing filmed human presenters for high-trust messages.** Use caution.
- **Unsupervised interactive avatars.** Realtime systems need guardrails, logs, fallback paths, and clear disclosure.
- **Natural long-form performance.** Short, structured content works better than nuanced delivery.

**The takeaway:** Avatar video is useful for repeatable, controlled, informational content. Realtime avatars are promising but early. The safest use is internal training, guided demos, and controlled simulations, not high-trust public messages.

---

## End-to-End Production Platforms

Q1 said true end-to-end production was not here. Q2 did not change that, but it made the direction clearer.

### The platforms to watch

| Platform | Q2 Direction | Best Read |
|---|---|---|
| Google Flow | Multimodal creative workspace with agentic assistance | Strongest ecosystem direction |
| Adobe Firefly | Partner-model hub inside Adobe workflows | Strong integration path |
| Runway Edit Studio | Editing-first surface around Aleph 2.0 | Strong for controlled revision |
| PAI 2.0 | AI video workspace with keyframes and Canvas | Early but aligned with production needs |
| VidMuse 2.0 | Timeline, memory, shot-level revision | Early but useful pattern |
| OttoBox | Local media indexing and rough-cut assistance | Interesting for sensitive footage |
| Project Nara | Studio-internal AI production platform | Important signal, not broadly available |

### Ready to use

- **Multi-tool pipelines.** Script in an LLM, generate assets in specialized tools, edit in a professional NLE, finish with human review.
- **Creative workspaces for ideation and variants.** Flow, Firefly, Runway, PAI, and VidMuse are useful for controlled experiments and early production stages.
- **Model hubs.** Adobe's partner-model approach is increasingly practical because it keeps multiple capabilities inside one creative surface.

### Close but not reliable

- **Single-platform production.** The pieces are assembling, but most serious work still requires several tools.
- **Agent-led creative workflows.** Agents can help organize and generate, but human taste still drives the work.
- **Studio-grade provenance.** Standards are improving, but implementation varies.

### Not there yet

- **One-click production.** Still a demo phrase, not a dependable workflow.
- **Fully autonomous creative direction.** Tools can propose; people decide.
- **Universal asset handoff.** Exports, metadata, versioning, and review still need better standards.

**The takeaway:** The right mental model is not "one tool replaces the pipeline." It is "the pipeline gains AI workspaces at several points."

---

## AI Agents for Production Operations

Q2's biggest non-creative shift was the arrival of governed workplace agents.

### Ready to use

- **Structured automation.** File routing, transcription jobs, metadata cleanup, notification flows, and repeatable publishing steps remain strong candidates.
- **Microsoft 365-connected agents in controlled preview.** Scout and Work IQ show where enterprise agents are going: context-aware, permission-aware, logged, and connected to the systems people already use.
- **Documentation and reporting agents.** Agents are useful for gathering scattered notes, summarizing project state, and producing first drafts of reports.

### Close but not reliable

- **Always-on agents for production coordination.** The idea is strong, but deployment needs policy, access control, and human checkpoints.
- **Agents with internal media access.** Useful only if storage, permissions, and logging are handled properly.
- **Multi-agent workflows.** Promising for operations, but failure modes are harder to inspect.

### Not there yet

- **Autonomous production management.** Agents cannot own stakeholder judgment, priority conflicts, or final approvals.
- **Unrestricted access to files and communications.** Permissions must be narrow, logged, and reversible.
- **Creative decision-making.** Agents can organize options; people choose.

**The takeaway:** Agents are most useful where the workflow is structured and the risk is bounded. Give them context, tools, and narrow permissions; keep humans at approval points.

---

## AI Coding Agents and Internal Tool Building

Q2 confirmed that coding agents are no longer a side category. For AV teams building internal tools, dashboards, web pages, asset workflows, or automation infrastructure, this is one of the highest-leverage areas.

### The field right now

| Tool | Primary Paradigm | Best For |
|---|---|---|
| Cursor | IDE-native model-agnostic agent | Polished day-to-day development |
| Claude Code | Terminal / codebase reasoning agent | Deep refactors, careful interactive work |
| OpenAI Codex | Desktop and ChatGPT-connected coding agent | Fast execution and broad distribution |
| Google Antigravity 2.0 | Multi-agent development platform | Parallel agents and browser-connected workflows |
| Jules | Asynchronous task agent | PR-driven background work |
| Windsurf | Agentic IDE | Multi-file editing and project memory |

### Ready to use

- **Internal tools and websites.** A developer with Cursor, Claude Code, Codex, or Antigravity can build and maintain internal tools faster than in Q1.
- **Automation scripts.** Agents handle scaffolding, API glue, tests, and documentation well when requirements are clear.
- **Bug fixes and small features.** Well-scoped issues are a strong fit.
- **Repository guidance files.** `AGENTS.md` has become a common way to tell coding agents how a project works.

### Close but not reliable

- **Broad refactors.** Agents can help, but require human planning and review.
- **Parallel agent work.** Antigravity and Cursor-style multi-agent workflows are powerful, but coordination overhead remains.
- **Async pull requests.** Useful for repeatable work; risky for ambiguous work.

### Not there yet

- **Autonomous architecture decisions.** People still need to own design, tradeoffs, and system boundaries.
- **Shipping code without review.** Agent output still needs human code review and testing.
- **Understanding organizational context by default.** Agents need project instructions and examples.

**The takeaway:** Coding agents are ready for AV teams that build internal tools. They do not replace developers; they compress the repetitive parts of development and make small tools cheaper to create.

---

## Transcription, Captioning, and Accessibility

This remains one of the most mature AI categories.

### Ready to use

- **Batch transcription.** Whisper-class systems, AssemblyAI, Deepgram, and cloud transcription tools are mature enough for most production workflows.
- **Live transcription.** Latency and accuracy are good enough for many internal and event-support use cases.
- **Auto-captioning.** First-pass captions are reliable enough to speed workflows, but still need review.
- **Speaker and topic search.** Transcript search is one of the simplest ways to make media libraries more usable.

### Close but not reliable

- **Speaker diarization with many speakers.** Accuracy drops with overlap, noise, and large groups.
- **Specialized names and terminology.** Custom dictionaries and review remain important.
- **Automatic caption styling.** Placement and readability still require a human pass.

### Not there yet

- **Final captions without review.** Accessibility work requires accuracy.
- **Perfect live captions in difficult audio.** Room noise, crosstalk, and accents still affect results.

**The takeaway:** Transcription and captioning should be standard AI-assisted workflows, with human review for anything published or accessibility-critical.

---

## Legal, Disclosure, and Trust

Q2 made provenance and disclosure more concrete.

### Ready to use

- **Watermarking and metadata where available.** Google, Adobe, and other major platforms increasingly attach provenance signals.
- **Disclosure practices for AI-assisted content.** The industry is converging on clearer labeling, especially for synthetic media.
- **Human review logs.** Teams can document which tools were used, what was generated, and who approved final outputs.

### Close but not reliable

- **Universal provenance.** Standards are improving, but compatibility across platforms is uneven.
- **Detection tools.** Useful as signals, not definitive proof.
- **Rights handling for likeness and voice.** Policies and products are improving, but consent remains the central issue.

### Not there yet

- **One universal AI disclosure standard.** The ecosystem is still fragmented.
- **Automatic rights clearance.** Teams need process, not just tools.
- **Trust without transparency.** Sensitive or public-facing work should make AI use clear when it materially affects the output.

**The takeaway:** Treat disclosure and provenance as production paperwork, not a last-minute legal concern. Document tools, inputs, edits, approvals, and final human review.

---

## The Cheat Sheet

### Use now — clear ROI

| Use Case | Best-Fit Tools / Patterns |
|---|---|
| Audio cleanup | iZotope RX, Adobe Podcast Enhance, NLE audio tools |
| Transcription and captions | Whisper-class tools, AssemblyAI, Deepgram, NLE caption tools |
| Subject isolation and masking | Premiere, Resolve, Final Cut, specialist plugins |
| Short concept video | Runway, Kling, Seedance, Gemini/Flow, Grok Imagine preview |
| Controlled video revision | Runway Aleph 2.0, VidMuse shot revision, PAI workspace |
| Background music and temp tracks | Stable Audio 3, Lyria 3, Suno/Udio-style tools with review |
| Voice drafts and realtime voice | ElevenLabs, OpenAI Realtime, cloud TTS tools |
| Internal tool development | Cursor, Claude Code, Codex, Antigravity |
| Production documentation | LLMs and agents with project context |
| Microsoft 365 workflow context | Work IQ / Copilot / Scout-style agents as they become available |

### Watch closely — promising but early

| Use Case | Tools / Patterns |
|---|---|
| Image-to-video with native audio | Grok Imagine 1.5 Preview and comparable models |
| AI video workspaces | PAI 2.0, VidMuse 2.0, Google Flow |
| Local media indexing | OttoBox-style local search and rough-cut tools |
| Open-weight realtime avatars | AVTR-1 and similar models |
| Studio AI platforms | Project Nara-style production systems |
| Cross-app creative agents | Adobe Firefly AI Assistant, Microsoft agent stack |

### Don't count on yet

- Prompt-only long-form video production.
- Final AI-generated video without human QC.
- Fully autonomous production agents.
- Premium voice acting replacement.
- Signature music composition replacement.
- Universal AI provenance across every platform.
- Final captions or localization without review.
- Coding agents making architecture decisions without a developer.

---

## Q2 Bottom Line

Q1 established that AI was already useful across AV production, but uneven. Q2 shows the unevenness getting more organized.

The strongest categories are still the practical ones: transcription, captioning, audio cleanup, masking, search, rough assembly, and internal tool building. The fastest-moving categories are video editing, realtime voice, workplace agents, and AI video workspaces. The most important constraint remains unchanged: people still own quality, taste, approvals, and trust.

The safest operating principle for Q3 is simple:

**Use AI to make the first version faster. Use people to make the final version worthy.**

---

## Methodology

This assessment draws from Q2 2026 product announcements, vendor documentation, public model cards, trade coverage, and the weekly AVS AI Dispatch archive from April through early June 2026. Where marketing claims conflict with conservative production experience, the report takes the conservative position. Pricing and access details reflect public information as of June 2026 and may vary by plan, region, and enterprise agreement.

**Shelf life:** roughly 3-6 months. The Q3 2026 edition should revisit video workspaces, workplace agents, realtime voice, open-weight media models, and provenance standards.

---

## References

1. [Runway — Introducing Aleph 2.0 and Edit Studio](https://runwayml.com/news/introducing-aleph-2-and-edit-studio) — May 21, 2026.
2. [Google — Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/) — May 19, 2026.
3. [Google DeepMind — Gemini Omni Flash model card](https://deepmind.google/models/model-cards/gemini-omni-flash/) — May 2026.
4. [xAI — Grok Imagine 1.5 Preview](https://x.ai/news/grok-imagine-1-5) — June 3, 2026.
5. [xAI Docs — Grok Imagine Video 1.5 Preview](https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview) — June 2026.
6. [WaveSpeed — Gemini Omni Flash vs Seedance 2.0 vs Kling 3.0](https://wavespeed.ai/blog/posts/gemini-omni-flash-vs-seedance-2-kling-3/) — May/June 2026.
7. [Newsshooter — DaVinci Resolve 21 final release](https://www.newsshooter.com/2026/06/02/davinci-resolve-21-final-release/) — June 2, 2026.
8. [Digital Production — DaVinci Resolve 21 leaves beta](https://digitalproduction.com/2026/06/05/davinci-resolve-21-leaves-beta/) — June 5, 2026.
9. [Topaz Labs — Hyperion 2 documentation](https://docs.topazlabs.com/topaz-video/filters/sdr-to-hdr/hyperion-2) — May 2026.
10. [Topaz Labs — Expansion Update press release](https://www.prnewswire.com/news-releases/topaz-labs-announces-new-video-enhancement-model-features-and-model-access-as-part-of-larger-company-wide-expansion-302766318.html) — May 7, 2026.
11. [Stability AI — Stable Audio 3 technical report](https://arxiv.org/html/2605.17991) — May 2026.
12. [Stability AI — Stable Audio 3 repository](https://github.com/stability-ai/stable-audio-3) — May 2026.
13. [TechCrunch — Stability AI releases new audio model](https://techcrunch.com/2026/05/20/stability-ai-release-a-new-audio-model-that-can-create-six-minute-songs/) — May 20, 2026.
14. [Google Cloud — Lyria 3 and Lyria 3 Pro on Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/lyria-3-and-lyria-3-pro-on-vertex-ai) — May 2026.
15. [OpenAI — Realtime API documentation](https://platform.openai.com/docs/guides/realtime) — May/June 2026.
16. [ElevenLabs — Voice and music product documentation](https://elevenlabs.io/) — Q2 2026.
17. [Microsoft — Introducing Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) — June 2, 2026.
18. [Microsoft — Build 2026: Be yourself at work](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/) — June 2, 2026.
19. [Microsoft 365 Developer Blog — Work IQ: production-ready intelligence for every agent](https://devblogs.microsoft.com/microsoft365dev/work-iq-production-ready-intelligence-for-every-agent/) — June 2026.
20. [Microsoft — Announcing the new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/) — June 2, 2026.
21. [The New Stack — Claude Code vs Cursor vs Codex vs Antigravity](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/) — June 2026.
22. [Digital Applied — Claude Code vs Codex vs Jules Q2 2026 benchmark matrix](https://www.digitalapplied.com/blog/claude-code-vs-codex-vs-jules-q2-2026-matrix) — Q2 2026.
23. [Avaturn — AVTR-1 open-weight realtime avatar model](https://www.einnews.com/pr_news/914997722/avaturn-releases-avtr-1-first-open-weights-ai-avatar-duplex-model) — May 26, 2026.
24. [Adobe — Topaz Astra Video Upscaling in Firefly Boards](https://www.adobe.com/mena_en/products/firefly/partner-models/topaz.html) — 2026.
25. [Adobe — ElevenLabs voice generation in Firefly](https://www.adobe.com/products/firefly/partner-models/elevenlabs.html) — 2026.
26. [Variety — Utopai Studios launches PAI 2.0](https://variety.com/2026/biz/tech/ai-utopai-studios-pai-2-generative-video-platform-1236764434/) — June 2026.
27. [VidMuse — VidMuse 2.0 release](https://vidmuse.ai/blog/vidmuse-2-0-release) — June 1, 2026.
28. [LavX News — OmAI unveils OttoBox](https://news.lavx.hu/article/omai-unveils-ottobox-ai-video-creation-assistant-at-beyond-expo-2026) — June 1, 2026.
29. [HeyGen / Synthesia / D-ID 2026 comparison](https://pikvue.com/synthesia-vs-heygen-vs-d-id-2026-best-ai-avatar-video-generator-compared/) — 2026.
30. [Kompozy — AI avatar video in 2026](https://kompozy.io/ai-content/avatar-video) — 2026.

---

*Published by The AVS AI Dispatch · Q2 2026*
