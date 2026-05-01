# The AVS AI Dispatch — Week of May 1, 2026

> Quick Summary: **Insta360 + Splatica's Project Eternal** turns a single 360 camera walk-through into a navigable Gaussian splat — volumetric capture migrating from purpose-built rigs to consumer hardware. The week's most useful framing came from Nathaniel Whittemore's argument that **the model matters less than the personal "Agent OS"** you build underneath it, with an AI chief of staff as the entry point. **Alibaba's HappyHorse 1.0** seized the #1 spot on the Artificial Analysis Video Arena, built in five months by the architect of Kling 1.0 and 2.0. **ElevenLabs shipped ElevenMusic** with a first-of-its-kind style-royalty deal through Believe and TuneCore. **Topaz Labs released Next-Gen**, a full rebuild of its image and video stack. And **Anthropic moved Claude's persistent memory** for managed agents to public beta — closing what builders call the biggest infrastructure gap in agentic AI.

---

## The Big Stories This Week

### Insta360 + Splatica Launch Project Eternal — Consumer 360 Cameras Become Volumetric Capture Devices

Insta360 and Splatica announced **Project Eternal** on April 28 — a joint pipeline that converts footage from a consumer 360 camera (Insta360 X5 or One RS 1-inch 360) into a **fully navigable Gaussian splat**. The capture step collapses to a single handheld camera the operator walks through the space with. Splatica's cloud processes the footage in roughly 1.5× the capture duration, and the output exports as standard `.splat` and `.ply` files that drop directly into Unreal Engine 5.6, Unity 6, Blender 4.5, Niantic Scaniverse, Apple Vision Pro, and Meta Horizon OS.

The Verge's hands-on framed it bluntly: until this week, getting a Gaussian splat into a film, game, or training simulation meant hiring a specialist. Insta360 just shipped the consumer version. **Pricing**: $29/month subscription or $0.50/minute pay-as-you-go for the cloud processing, separate from the camera hardware (X5 retails $549). Up to 30 minutes of source footage per scene with automatic stitching across multiple captures, and native depth alignment using parallax between dual sensors rather than pure photogrammetric inference.

**For AV teams**, the practical implication is that locations that used to require a scout, a lighting plan, and re-shoots can now be captured once and walked through forever. The output quality is currently "convincing real-time game environment" rather than "indistinguishable from camera negative" — strong enough for previs, second-unit reference, training data, and immersive installations, not yet good enough for hero shots in feature work.

### The Agent OS Shift: Why the Model Matters Less Than What You Build Underneath It

The most useful framing of agentic AI this week came from **Nathaniel Whittemore's AI Daily Brief on April 25**, where guest **Nufar Gaspar** walked through a **seven-layer "Agent OS"** designed to be platform- and model-agnostic. The argument, in one sentence: every agentic tool — Cursor, Claude Code, OpenClaw, Codex — is converging on the same set of capabilities, so the system you build underneath the tool is what compounds.

**The seven layers**, briefly:

1. **Identity** — who you are, your communication style, values, the rules the agent should never break
2. **Context** — three to five focused single-page files: team, product, customers, current quarter, stakeholders
3. **Skills** — reusable instruction sets ("when I say X, do Y using Z, output format")
4. **Memory** — deliberate capture of decisions, priority changes, and relationship context
5. **Connections** — read-only access to email, calendar, Slack via MCPs/CLIs/APIs (write access only after weeks of trust)
6. **Verification** — quick tone/fact/accuracy checks plus periodic system audits
7. **Automations** — scheduled tasks; start with draft outputs for review, not direct external sends

**The compounding mechanic is the headline.** Building the first agent — a chief of staff that reviews inbox, prepares meeting pre-reads, tracks commitments, drafts weekly updates — takes a weekend, because you're building the OS foundation along with the agent. Each subsequent specialist agent (research, post-production triage, content production) takes only an afternoon, because it inherits the layers. Gaspar's framing: people who build that foundation now have it compound; everyone else keeps starting over with new tools.

**For AV teams**, the relevance is direct. Every new launch — Premiere's Firefly Assistant, Avid × Gemini, DaVinci IntelliSearch, Topaz Astra, Sora, Veo, Kling, ChatGPT, Claude — comes with its own context window and memory model. Switch tools and accumulated context resets to zero. An Agent OS layer is the argument that the same underlying system can drive a chief-of-staff agent in Claude this quarter and a post-production-triage agent in Codex the next, with identity, skills, and memory carrying across.

### Alibaba HappyHorse 1.0 Takes the #1 Spot on the Video Arena

**Alibaba shipped HappyHorse 1.0** on April 27, a 15-billion-parameter video generation model that took the **#1 Elo ranking on the Artificial Analysis Video Arena** in both text-to-video and image-to-video categories — surpassing ByteDance's Seedance 2.0 by roughly **115 Elo points** in text-to-video.

What makes this an industry story rather than a benchmark story:

- **The team is led by Zhang Di**, the architect of Kling 1.0 and 2.0, who left Kuaishou in fall 2025 and joined Alibaba in November. Five months from team formation to a #1 leaderboard launch is unusual.
- **Three-channel distribution**: Free consumer access via the Qwen App (300M+ MAU); enterprise API via Alibaba Cloud Bailian at 0.9 yuan/sec (720p) or 1.6 yuan/sec (1080p); international API via fal at $0.14/sec (720p) and $0.28/sec (1080p), available globally from launch.
- **Open-source base model** with paid commercial premium tier — the same playbook Alibaba ran on Qwen and DeepSeek runs on V4.

**The capabilities**: 15-second multi-shot sequences in a single generation, native 1080p output, aspect ratios across 16:9, 9:16, 1:1, 4:3, and 3:4 in one model. Caveats: Seedance 2.0 still leads on synchronized lip-sync and Foley audio work, and the model performs best with concise prompts rather than long, complex ones. Full commercial GA is scheduled for May 2026.

### ElevenLabs Ships ElevenMusic With a Style-Royalty Licensing Deal

**ElevenLabs launched ElevenMusic** on April 29 — its first dedicated music generation model — paired with a licensing arrangement through **Believe** and **TuneCore** that's structured differently from any prior AI-music release. The deal pays artists when the model references their style, not just when their sound recordings are used in training.

**What ElevenMusic generates**: Up to four minutes of music per generation, vocals included, in 30+ genres and 20+ languages. Native stem separation produces aligned drums, bass, melody, vocals, and atmosphere as 24-bit WAV. Tempo, key, time signature, and song structure are controllable through structured prompts.

**The licensing structure** is the interesting part. Through Believe/TuneCore, opted-in artists get paid based on style attribution — every generation is run through a similarity-scoring pipeline, and if the output draws meaningfully from an opted-in artist's catalog, that artist receives a per-generation royalty out of a pool funded by ElevenMusic subscription revenue. This contrasts with Suno and Udo's position that training is fair use and per-track licensing isn't required.

**Pricing**: included in existing Creator ($22/mo) and Pro ($99/mo) tiers. The practical implication for AV producers: ElevenMusic is the first generative music tool with four-minute output, native stems, and licensing that survives a label-side audit. Quality is strong on stem alignment and structural coherence; genre-specific timbres in jazz, classical, and acoustic folk are still less convincing than dedicated genre models.

### Topaz Labs Ships "Next-Gen" — A Full Rebuild of the Image and Video Stack

**Topaz Labs released Topaz Next-Gen** on April 28 — a complete rebuild that replaces Photo AI, Gigapixel, and Video AI with a single unified application built on a new foundation model. The release closes the gap that had opened against newer competitors (Magnific, Runway Refine, Krea, Recraft).

The headline numbers:

- **Up to 16K upscaling** for stills (previous max: 8K from a 4K source)
- **Up to 10× video upscaling** with consistent temporal coherence (Proteus topped out at 4×)
- **120fps frame interpolation** with new frame-aware optical flow
- **Real-time preview** on Apple Silicon M3 Max+ and NVIDIA RTX 50-series
- **Native Apple ProRes RAW input**

**Pricing**: $299 one-time license with one year of updates, or $15/month for ongoing updates. Existing Photo AI / Video AI / Gigapixel customers get 50% off the upgrade. Topaz is also adding **Topaz Astra** (its dedicated video generation model) to **Adobe Firefly's roster** alongside Runway, Veo, Kling, and Sora.

### Buzzy Launches "AI Video Photoshop" With $20M From Sequoia and Ribbit

**Buzzy** — founded by ex-Runway and ex-Adobe engineers — exited stealth on April 30 with **$20M Series A** led by Sequoia. The product is positioned as **"Photoshop for AI video"** — direct manipulation editing on AI-generated clips at the pixel and timeline level, rather than re-prompting and re-generating.

**What's actually new**: AI video tools have largely worked on a generate-then-replace loop. Buzzy's pitch is that this is the wrong abstraction — once a generation is "almost right," the natural next step is direct edit. Object-level masking with consistent appearance across frames, local prompt edits with brush tools (paint a region, type what should be there), camera-path retargeting on existing generations, and multi-clip continuity that enforces character/lighting/prop consistency across cuts.

**Founding team is notable**. CEO Anya Singh was a senior PM on Runway Gen-3 and Gen-4. CTO Marcus Chen led Adobe's Project SuperSonic team and worked on the Firefly Video Editor. Their bet is that the next phase of AI video is editing tools, not better base models. Closed beta is open at $79/month with broader launch in summer 2026.

### Anthropic Moves Claude Persistent Memory for Managed Agents to Public Beta

**Anthropic shipped persistent memory for Claude Managed Agents** to public beta on April 27 — addressing what builders are calling the single biggest infrastructure gap in agentic AI. Agents now remember decisions, context, and accumulated knowledge across sessions, projects, and model upgrades, rather than starting from a blank slate every time.

**What's in the release**:

- **Long-term episodic memory** — agents store summaries of conversations and decisions in a managed memory store
- **Cross-session continuity** — an agent invoked a month after a project inherits the full context without re-priming
- **Selective forgetting** — flag stale memories, delete entries, set retention policies (30/90 days/indefinite)
- **Cross-model portability** — memories accumulated under Claude Opus 4.7 carry forward to future Claude releases

**Pricing**: free for the first 10MB per agent per month; $0.50/GB-month thereafter. Memory queries during inference cost the same per-token rate as standard input tokens.

**The thread to the Agent OS feature is direct**. With managed memory in the model provider's stack, the "memory" layer of Gaspar's framework moves from custom markdown files and external storage to a managed primitive — and the compounding effect (the second agent inheriting the foundation in an afternoon rather than a weekend) becomes meaningfully easier to realize.

### Quick Hits

- **AutoCut April update** — the popular Premiere/Resolve/Final Cut plugin shipped a new **Caption AI** module ($19/mo above base) for speaker-attributed captions across mixed multi-language interviews
- **Creo + Google Cloud** — Omnicom's influencer arm launched agentic content vetting using Gemini Enterprise and Veo, compressing review cycles from days to same-day
- **Sora API GA confirmed for September 24, 2026** — five-month countdown
- **Google I/O 2026 — May 19–20** — expectations include Veo 4, Imagen 5, Gemini 3.5

---

## Why This Week Matters

A few patterns worth noting:

- **Memory is the missing infrastructure layer — and it's finally shipping.** Whittemore/Gaspar's Agent OS framework and Anthropic's persistent memory release are arguing the same thing from opposite sides of the stack. From the user side: build a system that captures context, identity, and decisions in human-readable files. From the provider side: ship managed memory so users don't have to. Both arrive in the same week because both are responding to the same gap.

- **The capture layer of AV production is migrating to consumer hardware.** Volumetric capture used to require a dedicated rig. It now runs on a single 360 camera and a cloud subscription. Photogrammetry has been migrating in the same direction (Polycam, Luma's capture apps). Color and exposure science migrated from in-camera to log + post grading years ago. The pattern is consistent: capture sophistication moves from rig to device, and the post-side software gets the new complexity.

- **The open-weights model strategy is now standard for Chinese labs releasing AV models.** HappyHorse 1.0's open-source base with a paid commercial premium is the same playbook Alibaba ran on Qwen, that DeepSeek runs on V4, and that Kuaishou ran on the Kling 1.x base. The pattern is consistent enough that Western labs releasing closed models look like the exception rather than the norm.

- **Video models compete on total workflow now, not just model quality.** HappyHorse is the #1 video model, but the launch story is the Qwen + Bailian + fal three-channel distribution and the open-source play. Topaz Next-Gen rolls upscale, denoise, and frame interpolation into one model. Buzzy is positioning around editing a generation, not generating better. Adobe's Firefly Video Editor includes Kling, Veo, Sora, and Topaz Astra in one product. The unit of competition is no longer the model — it's the workflow that wraps the model, and that workflow increasingly includes multiple models from multiple vendors on one timeline.

- **Direct manipulation is the next phase of AI video tools.** Buzzy's "Photoshop for AI video" framing — and Adobe's parallel investments in the Firefly Video Editor's local-edit tools — suggest the field is entering its second phase. Phase one was generate from text. Phase two is generate something close, then edit directly. The same arc happened in still images (Stable Diffusion → ControlNet → inpainting → Photoshop integration), and there's no obvious reason video shouldn't follow.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. This is the quick summary — the full edition has the complete technical breakdown and sources. Curated with AI assistance. Questions or suggestions? Reply to this message.*
