# The AV AI Production Index — Q1 2026

> A quarterly assessment of what AI can and can't do in audio/video production. No hype. Just what works, what's close, and what's still a demo. This is the inaugural edition.

In 1986, a headquarters staff member told a writer, "It's sure great that you have MEPS. Now writing must be easy for you." The writer had to explain that [people, not machines, do the writing](https://wol.jw.org/en/wol/d/r1/lp-e/101986170).¹ Forty years later, the technology is different, but the punchline is the same.

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

---

## AI Agents for Production

AI agents work for structured, repeatable tasks (ingest → transcribe → tag → distribute). They fail at creative judgment and visual quality assessment.

- **Make.com / n8n:** ~50% time reduction for trigger-based workflows. Reliable for template-based video creation and file routing.²⁷
- **No agent is ready for autonomous production.** Every workflow needs human checkpoints.

---

## Transcription & Captioning

The most mature AI category in production.

| Provider | English Accuracy | Price | Best For |
|----------|-----------------|-------|----------|
| AssemblyAI Universal-3 Pro²⁸ | 94.1% | $0.0035/min | Audio intelligence, PII redaction |
| OpenAI Whisper | ~92% | $0.006/min | Budget batch, 100+ languages |
| Deepgram Nova-3²⁹ | ~92% | $0.0043/min | Real-time (<300ms latency) |

**Speaker diarization** remains the weak point: 85–90% accuracy in typical conditions, dropping to 75–80% with noise or 5+ speakers.

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

### Watch closely — promising but unproven

| Use Case | Tools to Evaluate |
|----------|---------------|
| Agent-based creative workflows | Luma Agents, ElevenLabs Flows |
| Multi-shot narrative generation | Kling 3.0 multi-shot, Seedance 2.0 |
| AI dubbing at scale | Deepdub, Papercup, ElevenLabs |
| End-to-end video from brief | CapCut AI Suite |

### Don't count on — not yet

- AI-only long-form video generation (>30s coherent narrative)
- Automated editorial decision-making
- AI text rendering within generated video
- Unsupervised VFX compositing
- AI-only character animation for broadcast
- Fully autonomous production agents
- AI music as hero content
- AI sound effects for final delivery

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
---

*Published by The AV AI Dispatch · Q1 2026*
