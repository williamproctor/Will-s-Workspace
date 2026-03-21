# The AV AI Production Index — Q1 2026

> A quarterly assessment of what AI can and can't do in audio/video production. No hype. Just what works, what's close, and what's still a demo. This is the inaugural edition.

In 1986, the Multilanguage Electronic Publishing System — MEPS — was the most advanced technology our organization had ever built. It could typeset dozens of scripts on a single machine, a genuine breakthrough at a time when most publishers couldn't handle more than one alphabet. A staff member marveled at the system and told a writer, "It's sure great that you have MEPS. Now writing must be easy for you." The writer had to gently correct the assumption: [people, not machines, do the writing](https://wol.jw.org/en/wol/d/r1/lp-e/101986170).¹

That exchange happened in a world where the internet didn't exist, a "computer" meant a room-sized mainframe, and the idea of a machine generating video from a text prompt would have sounded like science fiction. Forty years later, the technology has leapt so far that MEPS would be unrecognizable — but the misunderstanding hasn't budged an inch. People still look at a powerful new tool and assume the hard part is over. It never is. The tool changes what's possible; it doesn't change what's difficult.

---

## If You Only Read One Section

AI handles 70–90% of the work in most AV categories — fast. The final 10–30% still requires a human, and that's where quality lives.

**What you can do right now:**
- Generate 5–15 seconds of usable video footage for B-roll and concept work
- Produce broadcast-quality background music indistinguishable from stock libraries
- Clone voices with near-human fidelity from as little as 15 seconds of audio
- Cut post-production time in half with AI-powered cleanup, captioning, and masking

**What you still can't do:**
- Produce a coherent 60-second narrative scene
- Replace a composer for distinctive, memorable music
- Ship any AI-generated output without a human quality pass

Every section below follows the same structure: **what's ready, what's close, what's not there yet**, and a one-line recommendation.

---

## The Basics: Frontier LLMs and Why They Matter

Before we get into cameras, microphones, and timelines, it helps to understand the foundation everything else is built on. Every AI tool in this report — from video generators to voice cloners to coding agents — is powered by a **large language model** (LLM). The companies building these models are in an intense race, and the landscape changes quarterly.

### Chatbots vs. Agents — one distinction that matters

A **chatbot** is a conversation interface. You type a question, it gives an answer. It's reactive — it waits for you, responds, and stops. Think of it as a very knowledgeable colleague who only speaks when spoken to. ChatGPT, Claude, Gemini, and Grok are all chatbots at their core.

An **agent** is a chatbot that can *do things*. It doesn't just answer — it reasons about a goal, breaks it into steps, uses tools (web search, file editing, code execution, API calls), checks its own work, and iterates until the task is done. The same underlying model powers both; the difference is whether it's given autonomy and tools.

In practice: when you ask ChatGPT "how do I fix this audio sync issue?" — that's a chatbot. When you tell Codex "fix the audio sync bug in this repo, run the tests, and open a PR" — that's an agent. Same brain, different level of autonomy.

Most AV teams will interact with these models as chatbots first (research, brainstorming, drafting) and as agents later (automating workflows, building tools). Understanding which model sits behind which product helps you make informed choices about cost, capability, and data privacy.

### The frontier model lineup — March 2026

| Provider | Chatbot | Flagship Model | Context Window | Pricing |
|----------|---------|----------------|----------------|---------|
| OpenAI³⁵ | ChatGPT | GPT-5.4 | Up to 1M tokens | Free tier; Plus $20/mo; Pro $200/mo |
| Anthropic³⁶ | Claude | Claude Opus 4.6 | 1M tokens (beta) | Free tier; Pro $20/mo; Max $100/mo or $200/mo |
| Google³⁷ | Gemini | Gemini 3.1 Pro | 1M tokens | Free tier; AI Plus $5/mo; Pro $20/mo; Ultra $250/mo |
| xAI³⁸ | Grok | Grok 4.20 | 256K tokens | Free tier; SuperGrok $30/mo; Heavy $300/mo |
| Meta³⁹ | — (no chatbot) | Llama 4 Maverick | 10M tokens (Scout) | Open-weight; free to download and self-host |
| DeepSeek⁴⁰ | DeepSeek Chat | DeepSeek V3.2 | 128K tokens | Free tier; API ~$0.28/M tokens |
| Mistral⁴¹ | Le Chat | Mistral Large 3 | 256K tokens | Free tier; Pro $15/mo; Team $25/user/mo |

### What each column means

- **Chatbot** is the consumer-facing product — the thing you open in a browser or app to have a conversation.
- **Flagship Model** is the provider's most capable general-purpose model as of this writing.
- **Context Window** is how much text the model can process in a single conversation. 1 million tokens is roughly 750,000 words — enough to analyze an entire book or a full production bible.

### Open-weight vs. closed

Meta's Llama 4, DeepSeek, and Mistral release model weights publicly — meaning your organization can download, host, and run them on your own infrastructure. No data leaves your network. OpenAI, Anthropic, Google, and xAI keep their weights proprietary — you access them through APIs or their chatbot interfaces, and your data passes through their servers.

For AV teams handling sensitive production material, this distinction matters. Open-weight models give you full data control at the cost of managing your own infrastructure. Closed models are easier to start with but require trust in the provider's data handling policies.

### Why this matters for AV production

Every specialized AI tool in the sections below is either:
1. **Built on top of** a frontier LLM (e.g., Descript uses Whisper for transcription, ElevenLabs uses custom models for voice)
2. **Orchestrated by** a frontier LLM (e.g., AI agents use Claude or GPT to plan and execute multi-step workflows)
3. **Enhanced by** a frontier LLM (e.g., Cursor uses Claude/GPT to understand your codebase and write code)

Understanding the model layer helps you evaluate vendor claims, anticipate capability jumps (when a new model drops, every tool built on it gets better), and make strategic build-vs-buy decisions.

---

## Video Generation

The most visible category — and the one with the widest gap between demos and production reality.

### The field right now

| Tool | Resolution | Duration | Consistency | Price |
|------|-----------|----------|------------|-------|
| Runway Gen-4.5² | 4K | Up to 60s | Good | $12–$76/mo |
| Kling 3.0³ | 4K at 60fps | 15s | Good (multi-shot) | $6–$48/mo |
| Seedance 2.0⁴ | 2K | 15s | Good (multi-ref) | TBD |
| Google Veo 3.1⁵ | Up to 4K (upscaled) | 4–8s | Moderate | Vertex pricing |
| Sora 2⁶ | 1080p | 20s | Weak | $20–$200/mo |
| Pika 2.5⁷ | 1080p | 10s (25s via Pikaframes) | Weak | $8–$76/mo |
| Luma Ray 3.14⁸ | 1080p native | 5–10s (ext. to 30s) | Moderate | Enterprise |

### Ready to use

- **Short clips (5–15s) for B-roll and supplemental content.** Every major tool produces usable footage at this length.
- **Image-to-video animation.** Starting from a reference image consistently beats text-to-video in quality.
- **Cinematic style, mood, and camera movement.** The top tools handle lighting, grading, and camera moves well.
- **Concept visualization and pre-vis.** Over 14,000 enterprises use these tools for storyboarding, reducing pre-production time by roughly 40%.⁹
- **Lip-sync in controlled settings.** Seedance 2.0 and Kling 3.0 produce serviceable results for talking-head shots.

### Close but not reliable

- **Character consistency across shots.** Kling 3.0's multi-shot mode is the best available, but drift compounds beyond 3–4 shots.
- **Extended duration (30–60s).** Runway Gen-4.5 claims 60s, but coherence falls apart past ~20 seconds with multiple subjects.
- **Physics simulation.** Rigid body physics look reasonable. Fluid dynamics and fine motor interactions fail routinely.

### Not there yet

- **Text rendering in video.** Every tool fails at stable, readable text. Add text in post.
- **Complex hand/finger interactions.** The Achilles' heel persists across all models.
- **Narrative coherence over 30 seconds.** No tool produces a reliable minute-long scene.
- **Precise prompt control.** Specific multi-step physical instructions remain beyond current capabilities.

**The takeaway:** Use now for pre-vis, supplemental B-roll, and concept work. Don't ship AI-only video for anything requiring precise human representation.

> *Also in this space:* Vidu (anime/stylized), Hailuo/MiniMax (motion quality), CapCut AI (consumer-grade), Genmo Mochi (open-source), Higgsfield, Haiper

---

## Video Editing & Post-Production

Where AI delivers the most immediate, measurable time savings today.

### Ready to use

- **Transcript-based editing (Descript).** Edit video by editing text. 60–70% time savings for spoken-word content.¹⁰
- **Object masking and tracking (Premiere Pro).** Adobe's AI Object Mask: hover, click, tracked mask in seconds.
- **AI audio cleanup (Descript).** Studio Sound reliably lifts bad audio to usable levels.
- **Auto-captioning.** 92–95% accuracy for clear English. Dramatically faster than manual captioning.

### Close but not reliable

- **Generative Extend (Premiere Pro).** Subtle clip extensions work. Quality degrades with longer extensions or moving subjects.
- **AI translation and dubbing (Descript).** 30+ languages with lip-sync. Strong for major European languages, weak for tonal languages.

### Not there yet

- **Creative editorial judgment.** No AI replaces an editor's sense of pacing, emotional arc, or comedic timing.
- **Brand-consistent editing at scale.** Consistent editorial voice across dozens of AI-assisted videos still needs a human.
- **Complex narrative editing.** Multi-act structures and parallel storylines — entirely human-driven.

**The takeaway:** The strongest ROI in this entire report. If you edit spoken-word content, transcript-based editing alone justifies the tool cost.

> *Also in this space:* VEED.IO (browser-based transcript editing), Choppity (podcast-focused), Flixier (browser-based with AI B-roll), PlayPlay (enterprise), ScreenApp, Mocha Pro 2026 (AI masking/tracking plugin for After Effects, Premiere, Nuke — $48/mo)

---

## VFX & Compositing

AI rotoscoping is the single most production-ready AI capability in all of VFX.

### Ready to use

- **AI rotoscoping.** Premiere Object Mask and Slapshot (up to 8K, 400 shots/day¹¹) produce results that previously required hours of manual work per shot.
- **CG character compositing (Wonder Studio).** 80–90% of the VFX pipeline automated — tracking, lighting, shadows, compositing. Exports to Maya, Blender, Unreal. Plans from $19.99/mo.¹²
- **Simple object removal.** Wires, boom mics, unwanted signage — reliable for static or slow-moving objects.

### Close but not reliable

- **AI de-aging.** 94% realism in controlled shots. Varied lighting and fast head turns still produce artifacts.
- **Complex object removal.** Moving objects in busy scenes cause temporal smearing.
- **Dynamic background replacement.** Complex edges (hair, flowing fabric) still hallucinate detail.

### Not there yet

- **Fully automated VFX shots.** No tool produces broadcast-ready VFX without human supervision.
- **Photorealistic digital doubles.** Beyond AI-only pipelines for arbitrary lighting.
- **Real-time AI compositing for live production.** Latency makes this unreliable.

**The takeaway:** Rotoscoping and simple compositing are ready to deploy today. Everything else still needs an artist in the loop.

> *Also in this space:* Mocha Pro 2026/Boris FX (planar tracking, 3D camera solve), Runway Inpainting/Gen Remove, HitFilm (free VFX compositor)

---

## Animation

### Ready to use

- **AI-assisted keyframe animation (Cascadeur).** AutoPosing generates physically plausible poses; AutoPhysics calculates weight and momentum. 2–3x faster blocking.¹³
- **Motion capture cleanup.** Rokoko Studio and Cascadeur convert noisy mocap data into clean keyframes in minutes instead of days.
- **Single-camera mocap for previz.** Rokoko Vision's webcam/phone-based capture is usable for previsualization.

### Close but not reliable

- **Video-based markerless motion capture.** Approaches marker-based quality for body motion; finger tracking and facial capture lag behind.
- **AI-generated in-betweens.** Physically plausible but artistically generic — needs animator refinement.

### Not there yet

- **Fully automated character animation.** No tool produces broadcast-quality animation without animator input.
- **AI lip-sync for 3D characters.** "Approximation" quality — not production-grade.
- **Complex multi-character choreography.** Fight scenes, dance sequences, group conversations remain manual.

**The takeaway:** Cascadeur and Rokoko are genuine time multipliers for blocking and cleanup. Final animation still needs human artistry.

> *Also in this space:* DeepMotion (web-based markerless mocap), Move.ai (multi-person studio mocap), Plask (browser-based mocap + retargeting), Wonder Dynamics (body mocap in Wonder Studio), RADiCAL (phone/webcam mocap), KinectA.I., Motorica (game locomotion AI)

---

## Voice Synthesis & Text-to-Speech

The category where AI most consistently passes for human output.

### Ready to use

- **Short-to-medium narration (under 10 minutes).** ElevenLabs, Azure Neural TTS, and Fish Audio S2 produce speech indistinguishable from human narration for explainer and educational content.¹⁴
- **Voice cloning.** ElevenLabs requires ~30 minutes of studio audio; Fish Audio S2 needs only 15 seconds. Both achieve near-human fidelity.¹⁵
- **Word-level emotion control (Fish Audio S2).** Tag individual words with natural-language descriptions like `[whispered]` or `[voice breaking]` — a genuine breakthrough in TTS control.¹⁶

### Close but not reliable

- **Long-form narration (30+ minutes).** Prosody drift and pacing inconsistencies accumulate over time.
- **Complex emotional arcs.** Irony, subtle sarcasm, and building tension require manual prompt engineering.
- **Domain jargon pronunciation.** Custom dictionaries help but require upfront work.

### Not there yet

- **Replacing professional voice actors for premium content.** The last 5% of human vocal nuance remains out of reach.
- **Singing voice synthesis at production quality.** A separate unsolved problem.

### What it costs

| Tier | Tool | Cost |
|------|------|------|
| Quality leader | ElevenLabs Enterprise¹⁷ | Custom (from ~$0.12/1K chars) |
| Open-source leader | Fish Audio S2¹⁶ | Self-host (free) or API |
| Cloud budget | Azure / Google Cloud TTS | ~$0.016/1K chars |

**The takeaway:** For narration under 10 minutes, AI TTS is production-ready today. Voice cloning is viable for consistent brand voices. Premium dramatic performance still needs a human.

> *Also in this space:* PlayHT 3.0 (ultra-low-latency streaming TTS), WellSaid Labs (enterprise brand voices), Murf.ai (studio-grade TTS), Resemble AI (voice cloning + deepfake detection), Coqui/XTTS (open-source multilingual), Tortoise TTS (open-source, slow but high quality), Bark (Suno's open-source TTS), Amazon Polly, Google Cloud TTS

---

## Music Generation

### Ready to use

- **Background music, mood beds, and underscore.** AI music has crossed the "good enough" threshold for non-focal music. Suno V5 produces 48kHz tracks with natural-sounding vocals. The platform has 2 million paid subscribers generating 7 million tracks per day.¹⁸
- **Genre coverage.** Pop, hip-hop, electronic, lo-fi, ambient, corporate/upbeat — all reliable.

### Close but not reliable

- **Full songs as primary content.** Suno V5 can produce releasable tracks, but vocals drift, structures collapse, and genre shifts randomly. Export stems and finish in a DAW.
- **Specific production control.** Genre and mood prompts work. Fine-grained arrangement control is limited.

### Not there yet

- **Replacing a composer for distinctive music.** AI music is competent but generic — no distinctive artistic voice.
- **Complex arrangements with multiple movements.** Extended compositions with dynamic shifts remain unreliable.

### Legal note

Purely AI-generated music (prompt-only, no human editing) likely cannot be copyrighted and enters the public domain.¹⁹ To strengthen IP claims: edit, mix, arrange, and add human performance. Document your creative process.

**The takeaway:** Strong for underscore and mood beds. Not a replacement for a composer when the music needs to be memorable.

> *Also in this space:* Udio (comparable to Suno, stronger on vocals), AIVA (classical/orchestral focus, copyright-clear), Soundraw (customizable loops), Boomy (consumer-grade), Loudly, Beatoven.ai (mood-based scoring), Stability Audio (open-weight model), MusicFX (Google's experimental tool)

---

## Sound Design & SFX

The weakest AI audio category.

### Ready to use

Simple ambient textures, basic UI sounds, and atmospheric backgrounds. ElevenLabs Sound Effects handles rain, wind, footsteps, door creaks, crowd ambience, and simple impacts.

### Not there yet

- **Replacing a sound library or foley artist.** AI SFX are useful for prototyping and temp tracks — not reliable enough to ship.
- **Complex foley.** Lacks the micro-variations and timing precision of professional foley work.
- **Cinematic sound design.** Simple whooshes and risers work. Complex, layered designs do not.

**The takeaway:** Use for rapid prototyping. Keep your stock SFX library (Epidemic Sound, Artlist) and sound designer for anything that ships.

> *Also in this space:* Stable Audio (Stability AI, text-to-audio), AudioCraft/AudioGen (Meta, open-source), Soundful, Splash Pro, MusicLM/SoundStorm (Google), Lovo SFX

---

## Audio Post-Production

The most production-ready AI audio category. If you adopt nothing else from this report, start here.

### Ready to use

- **Noise removal (iZotope RX 11).** Industry gold standard. ML-based Repair Assistant fixes clipping, clicks, hum, noise, reverb, and sibilance.²⁰
- **Free speech enhancement (Adobe Podcast Enhance v2).** Source separation with independent speech/noise/music sliders. Free (1hr/day).²¹
- **Stem separation (LALAL.AI).** 10-stem separation using proprietary neural networks trained on 20TB+ of studio recordings. 14.8M hours processed.²²
- **Transcript-based editing (Descript).** One-click cleanup, filler word removal, and audio regeneration for corrections.

### Not there yet

- **AI mastering for premium releases.** LANDR and eMastered produce 80% solutions — insufficient where mastering decisions affect artistic outcome.
- **Fully automated podcast/video post.** Pacing, narrative editing, and tonal consistency still need a human editor.

**The takeaway:** Audio post is where AI saves the most hours per dollar spent. iZotope RX 11 and Descript should be in every production toolkit.

> *Also in this space:* Accusonus ERA Bundle (one-knob audio cleanup), Audo.ai (browser-based noise removal), Krisp (real-time noise cancellation), Auphonic (automated podcast mastering), LANDR (AI mastering), eMastered (AI mastering), Acon Digital (restoration plugins), CrumplePop (AI audio plugins for FCPX/Premiere), Moises.ai (stem separation)

---

## Dubbing & Localization

### Ready to use

- **AI dubbing with human QA for informational content.** Deepdub (5,000+ titles²³), Papercup/RWS (1,800 in-house linguists), and ElevenLabs Dubbing (best raw voice quality) deliver broadcast-acceptable results through hybrid AI+human workflows.

### Close but not reliable

- **Entertainment dubbing for streaming.** Being used by platforms, but premium scripted content still sounds noticeably AI-dubbed.
- **Lip-sync matching.** Frame-accurate for simple dialogue, noticeably off for rapid speech or singing.

### Not there yet

- **Fully automated dubbing without human review.** Every enterprise provider includes mandatory human QA. Skip it at your own risk.
- **Premium entertainment dubbing.** Feature films and prestige TV still need human voice actors.
- **Singing/musical numbers.** AI dubbing handles dialogue only.

**The takeaway:** Viable now for corporate and instructional content with a human QA layer. Not ready for premium entertainment.

> *Also in this space:* Translated (RWS/Papercup parent company), Dubverse.ai, Rask.ai (video-native dubbing), Flawless AI (TrueSync lip-sync for film), Camb.ai, AppTek, TransPerfect, AI Studios/DeepBrain AI

---

## End-to-End Production Platforms

**No single platform handles a full production pipeline at enterprise quality.** The market is strong point solutions that need orchestration.

| Platform | What It Does | Production-Ready? |
|----------|-------------|-------------------|
| ElevenLabs Flows²⁴ | Chains 35+ audio/image/video models in a visual canvas | Alpha — no API yet |
| Luma Agents⁸ | Multi-modal asset generation from a single brief | Just launched |
| Synthesia²⁵ | Script-to-avatar video for instructional content | Yes — talking-head only |
| HeyGen²⁶ | Avatar video with lip-sync and voice cloning | Yes — talking-head only |

**What a realistic pipeline looks like today:**
1. Script via LLM (Claude/GPT)
2. Avatar video via Synthesia/HeyGen OR generative video via Runway/Kling
3. Audio/voice via ElevenLabs
4. Editing in a traditional NLE or Descript
5. Delivery via existing infrastructure

This is a 4–5 tool pipeline. True end-to-end is not here yet.

> *Also in this space:* Colossyan (enterprise avatar video), D-ID (live avatar API), Tavus (personalized video), Elai.io, Vidnoz, Hour One, DeepBrain AI, Runway Orchestration (emerging), Descript Storyboard (emerging)

---

## AI Agents for Production

AI agents work for structured, repeatable tasks (ingest → transcribe → tag → distribute). They fail at creative judgment and visual quality assessment.

- **Make.com / n8n:** ~50% time reduction for trigger-based workflows. Reliable for template-based video creation and file routing.²⁷
- **No agent is ready for autonomous production.** Every workflow needs human checkpoints.

> *Also in this space:* Zapier (mainstream automation), Activepieces (open-source alternative to Make), Pipedream (developer-focused), Bardeen.ai (browser automation), CrewAI (multi-agent framework), LangChain/LangGraph (agent orchestration), AutoGen (Microsoft, multi-agent)

---

## AI Coding Agents & Development Harnesses

A separate category that matters for any AV team building internal tools, web platforms, or automation infrastructure. Two layers have emerged: **IDE harnesses** (where a developer steers the agent in real time) and **autonomous agents** (where the AI works independently and returns finished code).

### IDE harnesses — developer-in-the-loop

| Harness | Model | Key Capability | Price |
|---------|-------|----------------|-------|
| Cursor³⁰ | Multi-model (Claude, GPT-5, Gemini) | Agent mode with multi-file editing, cloud agents, up to 8 parallel agents on isolated branches | $20–$200/mo individual; $40/user/mo teams |
| Windsurf³¹ | Multi-model (via Cascade) | Cascade agent writes ~90% of code; persistent "Memories" learn project conventions; Turbo Mode for autonomous execution | $15–$200/mo; enterprise on-prem available |
| Google Antigravity³² | Gemini 3.1 Pro | Agent-first platform: plan → execute → test → verify across editor, terminal, and browser. Google Stitch integration for design-to-code | Free preview; paid tiers emerging |

These are not autocomplete tools — they are agentic environments where you describe intent in natural language and the AI plans, writes, tests, and debugs multi-file changes. Over half the Fortune 500 now use Cursor alone.³⁰

### Autonomous agents — asynchronous, no IDE required

| Agent | Provider | How It Works | Access |
|-------|----------|-------------|--------|
| OpenAI Codex³³ | OpenAI | Cloud-based agent that clones your repo, writes code, runs tests, and returns a pull request. Powered by GPT-5.3-Codex — 25% faster than predecessor, highest SWE-Bench Pro scores | Included with ChatGPT Plus ($20/mo) through Pro ($200/mo) |
| Claude Code | Anthropic | Terminal-based agent that reads your codebase, plans multi-step implementations, and executes them. Ships as CLI | Claude Max ($100–$200/mo) |
| Jules 3.0³⁴ | Google | Asynchronous agent powered by Gemini 2.5 Pro. Assign tasks from browser/Slack, returns completed PRs. API access for CI/CD integration | Free preview; Google AI Pro/Ultra tiers |
| Claude Cowork | Anthropic | Extends Claude's agentic capability to knowledge work — file management, spreadsheet creation, report synthesis. Not code-specific but relevant for production ops | Claude Max ($100–$200/mo), macOS/Windows |

### Use cases for AV teams

**Internal software development.** Build and maintain asset management systems, review/approval workflows, project dashboards, and metadata tagging tools. A developer paired with Cursor or Windsurf can build internal web apps at 2–4x the speed of traditional development — what once took a team of three might take one developer and an agent.

**Web development & publishing.** Build and iterate on websites, content management interfaces, and distribution platforms. Agents handle the scaffolding, responsive layouts, API integrations, and deployment pipelines while the developer focuses on design intent and business logic.

**Automation infrastructure.** Connect production tools via APIs — ingest pipelines, transcription routing, automated QC checks, and notification systems. Codex and Jules can work asynchronously on GitHub issues, returning working PRs while your team focuses on creative work.

**Production operations.** Claude Cowork handles the non-code side: organizing project files, compiling reports from scattered notes, generating formatted spreadsheets from raw data, and managing documentation — tasks that consume hours of an operations team's week.

### Ready to use

- **IDE harnesses for web/tool development.** Cursor and Windsurf deliver genuine productivity multipliers for any team building internal software. The learning curve is low for any developer already in VS Code.
- **Autonomous agents for well-scoped tasks.** Bug fixes, documentation, unit tests, and small features with clear specifications.

### Not there yet

- **Autonomous agents for complex, ambiguous work.** Architectural decisions, creative problem-solving, and anything requiring deep domain knowledge still needs a human driving.
- **Production-critical code without review.** No agent output should ship to production without human code review — the error rate on complex tasks is still too high.

**The takeaway:** IDE harnesses like Cursor and Windsurf are the fastest path to building internal tools and web platforms. Autonomous agents (Codex, Jules, Claude Code) handle well-defined tasks asynchronously. Neither replaces a developer — they replace the repetitive 70% of development work so your team can focus on the hard 30%.

> *Also in this space:* GitHub Copilot (agent mode now available), JetBrains AI (Junie agent), Tabnine (enterprise-focused), Codeium (free tier), Replit Agent (full-stack from prompt), Bolt.new (Stackblitz), Lovable (UI-focused), Devin (Cognition, autonomous SWE), Sweep AI (junior dev tasks)

---

## Transcription & Captioning

The most mature AI category in production.

| Provider | English Accuracy | Price | Best For |
|----------|-----------------|-------|----------|
| AssemblyAI Universal-3 Pro²⁸ | 94.1% | $0.0035/min | Audio intelligence, PII redaction |
| OpenAI Whisper | ~92% | $0.006/min | Budget batch, 100+ languages |
| Deepgram Nova-3²⁹ | ~92% | $0.0043/min | Real-time (<300ms latency) |

**Speaker diarization** remains the weak point: 85–90% accuracy in typical conditions, dropping to 75–80% with noise or 5+ speakers.

> *Also in this space:* Rev.com (hybrid AI+human), Otter.ai (meeting transcription), Sonix, Trint (journalist-focused), Verbit (enterprise/legal), Speechmatics (on-prem option), Gladia (real-time API), Amazon Transcribe, Google Cloud Speech-to-Text, Transkriptor

---

## The Cheat Sheet

### Use now — clear ROI

| Use Case | Best Tools |
|----------|-----------|
| Concept/pre-visualization | Runway Gen-4.5 or Kling 3.0 |
| Rotoscoping and masking | Premiere Object Mask or Slapshot |
| Audio cleanup | iZotope RX 11 or Adobe Podcast Enhance (free) |
| Transcript-based editing | Descript |
| Background music | Suno V5 |
| Voice synthesis (short-form) | ElevenLabs or Fish Audio S2 |
| Instructional talking-head video | Synthesia or HeyGen |
| Animation blocking + mocap cleanup | Cascadeur + Rokoko |
| CG character compositing | Wonder Studio |
| Internal tool / web development | Cursor or Windsurf (IDE harness) |
| Async bug fixes & small features | OpenAI Codex or Jules 3.0 |

### Watch closely — promising but unproven

| Use Case | Tools to Evaluate |
|----------|---------------|
| Agent-based creative workflows | Luma Agents, ElevenLabs Flows |
| Multi-shot narrative generation | Kling 3.0 multi-shot, Seedance 2.0 |
| AI dubbing at scale | Deepdub, Papercup, ElevenLabs |
| End-to-end video from brief | CapCut AI Suite |
| Autonomous agents for complex dev work | Codex, Claude Code, Jules |
| AI-assisted production ops | Claude Cowork |

### Don't count on — not yet

- AI-only long-form video generation (>30s coherent narrative)
- Automated editorial decision-making
- AI text rendering within generated video
- Unsupervised VFX compositing
- AI-only character animation for broadcast
- Fully autonomous production agents for creative work
- AI music as hero content
- AI sound effects for final delivery
- Autonomous coding agents for complex architecture decisions

---

## Methodology

This assessment draws from manufacturer documentation, third-party benchmarks (Artificial Analysis), trade press, enterprise case studies, and independent product reviews as of March 2026. Where marketing claims conflict with independent testing, the conservative position is taken. Pricing reflects publicly available rates and may not match negotiated enterprise agreements.

**Shelf life:** Roughly 3–6 months. The Q2 2026 edition will follow.

---

## References

1. "MEPS — What It Can and Cannot Do," *Awake!*, March 8, 1986, pp. 24–27. [wol.jw.org](https://wol.jw.org/en/wol/d/r1/lp-e/101986170)
2. Runway Gen-4.5 product page and API pricing. [runwayml.com/pricing](https://www.runwayml.com/pricing); [docs.dev.runwayml.com](https://docs.dev.runwayml.com/guides/pricing/)
3. "Kling 3.0 Makes AI Video Feel Like a Real Production Tool," COEY, March 11, 2026. [coey.com](https://coey.com/resources/blog/2026/03/11/kling-3-0-makes-ai-video-feel-like-a-real-production-tool/)
4. "Official Launch of Seedance 2.0," ByteDance Seed Team, February 12, 2026. [seed.bytedance.com](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0)
5. "Veo 3.1 Ingredients to Video," Google Blog, January 13, 2026. [blog.google](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video); Vertex AI documentation. [cloud.google.com](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate)
6. "Sora 2 Is Here," OpenAI, September 30, 2025. [openai.com](https://www.openai.com/index/sora-2/); "OpenAI Opens Sora 2 Video API to All Developers," VO3 AI, March 13, 2026. [vo3ai.com](https://www.vo3ai.com/blog/openai-opens-sora-2-video-api-to-all-developers-what-this-means-for-ai-filmmakin-2026-03-13)
7. Pika 2.5 pricing and features. [pikaais.com](https://pikaais.com/subscription/); [app-pika.art](https://app-pika.art/pika-2-5-pricing/)
8. Luma Ray 3.14 and Luma Agents announcements. [lumalabs.ai](https://lumalabs.ai/blog/luma-ray-2-release)
9. Based on aggregated vendor case studies from Runway, Kling, and Pika enterprise marketing materials, cross-referenced with independent reviews.
10. Descript product documentation. [descript.com](https://www.descript.com)
11. Slapshot VFX product specifications.
12. Wonder Studio pricing and features. [wonderdynamics.com](https://wonderdynamics.com); Overview at [powerusers.ai](https://powerusers.ai/ai-tool/wonder-studio/)
13. Cascadeur AutoPosing and AutoPhysics documentation. [cascadeur.com](https://cascadeur.com/)
14. ElevenLabs product documentation. [elevenlabs.io](https://elevenlabs.io)
15. Fish Audio S2 voice cloning specifications. [fish.audio](https://fish.audio/blog/fish-audio-s2-fine-grained-ai-voice-control-at-the-word-level/)
16. "Fish Audio S2: Fine-Grained AI Voice Control at the Word Level," Fish Audio Blog, March 2026. [fish.audio](https://fish.audio/blog/fish-audio-s2-fine-grained-ai-voice-control-at-the-word-level/)
17. ElevenLabs pricing tiers. [elevenlabs.io/pricing](https://elevenlabs.io/pricing)
18. Suno V5 usage statistics per Blake Crosley, "Suno AI Music Generation: The Definitive Technical Reference." [blakecrosley.com](https://blakecrosley.com/guides/suno)
19. *Thaler v. Perlmutter*, U.S. Supreme Court certiorari denied March 2, 2026. Reuters coverage. [reuters.com](https://www.reuters.com/legal/government/us-supreme-court-declines-hear-dispute-over-copyrights-ai-generated-material-2026-03-02); Lexology analysis. [lexology.com](https://www.lexology.com/library/detail.aspx?g=6c1c89e9-778d-4407-8167-996e4dad0f23)
20. iZotope RX 11 features and editions. [izotope.com](https://www.izotope.com/en/products/rx/features.html)
21. Adobe Podcast Enhance. [podcast.adobe.com](https://podcast.adobe.com)
22. LALAL.AI 10-stem separation. [lalal.ai](https://www.lalal.ai); AI Spectrum India coverage. [aispectrumindia.com](https://aispectrumindia.com/analysis/48/124/lalal-ai-redefines-enterprise-audio-splitting-with-10-stem-ai-separation-restoration-and-api-integration.html)
23. Deepdub enterprise dubbing platform.
24. "Introducing Flows, the AI Creative Canvas," ElevenLabs Blog. [elevenlabs.io](https://elevenlabs.io/blog/introducing-flows-in-elevencreative)
25. Synthesia enterprise pricing and features. [synthesia.io](https://synthesia.io/pricing); CheckThat.ai analysis. [checkthat.ai](https://checkthat.ai/brands/synthesia/pricing)
26. HeyGen enterprise pricing. [heygen.com](https://www.heygen.com/enterprise/pricing)
27. Make.com and n8n workflow automation platforms.
28. AssemblyAI Universal-3 Pro benchmarks and pricing. [assemblyai.com](https://www.assemblyai.com/universal-3-pro); [assemblyai.com/benchmarks](https://www.assemblyai.com/benchmarks)
29. Deepgram Nova-3 pricing and latency. [deepgram.com](https://deepgram.com/pricing-test-page)
30. Cursor AI IDE features, pricing, and enterprise adoption. [cursor.com/pricing](https://cursor.com/pricing); "Cursor AI IDE Complete Guide 2026." [crazyrouter.com](https://crazyrouter.com/en/blog/cursor-ai-ide-complete-guide-2026)
31. Windsurf AI IDE features, Cascade agent, and enterprise metrics. [windsurf.ai/enterprise](https://windsurf.ai/enterprise); "Windsurf Review: Is the AI-First IDE Worth $15/Month?" [agentrank.tech](https://www.agentrank.tech/blog/windsurf-review-ai-ide-2026)
32. Google Antigravity agent-first development platform. [antigravity.codes/tutorial](https://antigravity.codes/tutorial); "Cursor vs Antigravity 2026." [antigravity.codes](https://antigravity.codes/blog/cursor-vs-antigravity)
33. OpenAI Codex and GPT-5.3-Codex. "OpenAI Launches GPT-5.3-Codex." [awesomeagents.ai](https://awesomeagents.ai/news/gpt-5-3-codex-openai-agentic-coding/); Codex developer documentation. [developers.openai.com](https://developers.openai.com/codex/)
34. Google Jules 3.0 coding agent. "Jules, Google's asynchronous AI coding agent, is out of public beta." [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/jules-now-available/); Jules documentation. [jules.google/docs](https://jules.google/docs/)
35. OpenAI model release notes and GPT-5.4 announcement. "Introducing GPT-5.4." [openai.com](https://openai.com/index/introducing-gpt-5-4/); "Introducing o3 and o4-mini." [openai.com](https://openai.com/index/introducing-o3-and-o4-mini/)
36. Anthropic Claude models overview. "Claude Opus 4.6." [anthropic.com](https://www.anthropic.com/claude/opus); "Introducing Sonnet 4.6." [anthropic.com](https://www.anthropic.com/news/claude-sonnet-4-6); Models documentation. [docs.anthropic.com](https://docs.anthropic.com/en/docs/models-overview)
37. Google Gemini models. "Gemini 3.1 Pro." [blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro); "Gemini 2.5 updates." [deepmind.google](https://deepmind.google/blog/gemini-25-updates-to-our-family-of-thinking-models/)
38. xAI Grok models. "Grok 3 Beta — The Age of Reasoning Agents." [x.ai](https://x.ai/news/grok-3); Release notes. [docs.x.ai](https://docs.x.ai/docs/release-notes)
39. Meta Llama 4. "The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation." [ai.meta.com](https://ai.meta.com/blog/llama-4-multimodal-intelligence); Model cards. [llama.meta.com](https://llama.meta.com/docs/model-cards-and-prompt-formats/llama4/)
40. DeepSeek V3.2 and R1. "DeepSeek V3.2: Frontier Reasoning at 6x Lower Cost." [largo.dev](https://largo.dev/tutorials/transformers/deepseek-v3-architecture/); DeepSeek R1 documentation. [deepseeksr1.com](https://deepseeksr1.com/r1-model/)
41. Mistral Small 4 and model lineup. "Mistral Small 4." [docs.mistral.ai](https://docs.mistral.ai/models/mistral-small-4-0-26-03); Models overview. [docs.mistral.ai](https://docs.mistral.ai/models/)
---

*Published by The AV AI Dispatch · Q1 2026*
