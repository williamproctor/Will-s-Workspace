# AI in AV Production: What Actually Works Right Now

> An honest look at every major AI capability in audio/video production — what's ready for enterprise use, what's close, and what's still hype. Updated March 2026.

In 1986, a headquarters staff member told a writer, "It's sure great that you have MEPS. Now writing must be easy for you." The writer had to explain that [people, not machines, do the writing](https://wol.jw.org/en/wol/d/r1/lp-e/101986170). Forty years later, the technology is different, but the punchline is the same.

---

## The Short Version

AI is real in AV production now. But the gap between impressive demos and reliable enterprise output is still wide.

**The pattern across every category:** AI handles 70–90% of the work, fast. The final 10–30% still needs a human — and that last stretch is where quality lives.

Here's where things stand:

- **You can** generate 5–15 seconds of usable video footage, produce broadcast-quality background music, clone voices with near-human fidelity, and automate tedious post-production tasks.
- **You can't** produce a coherent 60-second narrative scene, replace a composer for distinctive music, or ship any AI output without a human QA pass.

---

## Video Generation

### Who's in the game

| Tool | Max Resolution | Max Duration | Character Consistency | Price Range |
|------|---------------|-------------|----------------------|-------------|
| Runway Gen-4.5 | 4K | 60s | Good (reference images) | $12–$127/mo |
| Kling 3.0 | 4K at 60fps | 15s | Good (multi-shot mode) | $6–$48/mo |
| Seedance 2.0 | 2K cinema | 15s | Good (multi-shot) | TBD |
| Sora 2 Pro | 1080p | 20s | Weak | $20–$200/mo |
| Pika 2.5 | 1080p | 10s (25s w/ Pikaframes) | Weak | $8–$76/mo |
| Veo 2 | 720p | 8s | Weak | Vertex pricing |
| Luma Uni-1 | Up to 4K | Varies | Moderate | Enterprise |

### Ready to use

- **Short clips (5–15s)** for B-roll, interstitials, and supplemental website/app content. Every major tool produces usable footage at this length.
- **Image-to-video animation.** Starting from a reference image consistently beats text-to-video in quality.
- **Style, mood, and camera movement.** Cinematic lighting, grading, and camera moves are well-handled by the top tools.
- **Concept visualization and pre-vis.** Over 14,000 enterprises already use these tools for storyboarding, cutting pre-production time by ~40%.
- **Lip-sync in controlled settings.** Seedance 2.0 and Kling 3.0 produce serviceable lip-sync for talking-head shots.

### Getting there

- **Character consistency across shots.** Kling 3.0's multi-shot mode and Seedance's reference system are the best available, but character drift compounds beyond 3–4 shots. Expect heavy curation.
- **Extended duration (30–60s).** Runway Gen-4.5 claims 60s continuous generation. In practice, coherence falls apart past ~20 seconds, especially with multiple subjects.
- **Physics simulation.** Rigid body physics look reasonable. Fluid dynamics, cloth, and fine motor interactions fail routinely.
- **Multi-character scenes.** Two characters interacting is achievable. Three or more reliably causes spatial confusion and identity mixing.

### Not there yet

- **Text rendering in video.** Every tool fails at generating readable, stable text within frames. Add text in post.
- **Complex hand/finger interactions.** Extra fingers, impossible joint angles, objects phasing through hands — the Achilles' heel persists.
- **Narrative coherence over 30+ seconds.** No tool produces a reliable minute-long scene with consistent spatial reasoning and cause-and-effect continuity.
- **Precise prompt control.** "A woman picks up the red cup with her left hand, turns 90 degrees clockwise, and places it on the shelf" — this level of specificity is beyond current capabilities.
- **Photorealistic humans under scrutiny.** Close-up faces in motion still trigger uncanny valley. Wide shots and stylized aesthetics hide limitations better.

### Bottom line

**Use now** for pre-visualization, supplemental B-roll, and concept work. **Be cautious** with multi-shot narrative sequences. **Don't ship** AI-only video for published content requiring precise human representation.

---

## Video Editing & Post-Production

### Ready to use

- **Transcript-based editing (Descript).** Edit video by editing text. Filler word removal, silence trimming, and rough-cut assembly are production-proven. 60–70% time savings for spoken-word content.
- **Object masking and tracking (Premiere Pro).** Adobe's AI Object Mask — hover, click, tracked mask in seconds. Production-ready.
- **AI audio cleanup (Descript).** Studio Sound reliably improves bad audio to acceptable levels.
- **Auto-captioning.** 92–95% accuracy for clear English audio. Dramatically faster than manual captioning.

### Getting there

- **Generative Extend (Premiere Pro).** Subtle clip extensions work. Quality degrades with longer extensions or moving subjects.
- **AI translation and dubbing (Descript).** 30+ languages with lip-sync. Strong for major European languages, weak for tonal languages.

### Not there yet

- **Creative editorial judgment.** No AI tool replaces an editor's sense of pacing, emotional arc, or comedic timing.
- **Brand-consistent editing at scale.** Maintaining a consistent editorial voice across dozens of AI-assisted videos requires human oversight.
- **Complex narrative editing.** Multi-act structure, parallel storylines, non-linear timelines — entirely human-driven.

---

## VFX & Compositing

### Ready to use

- **AI rotoscoping.** The single most production-ready AI capability in VFX. Premiere Object Mask and Slapshot (up to 8K, 400 shots/day) produce results that previously required hours of manual work per shot.
- **CG character compositing (Wonder Studio).** 80–90% of the VFX pipeline automated — character tracking, lighting matching, shadow casting, compositing. Exports to Maya, Blender, Unreal. Cuts turnaround from one week to one day. ~$1,000/year.
- **Simple object removal.** Static or slow-moving objects (wires, boom mics, unwanted signage) — reliable.

### Getting there

- **AI de-aging.** 94% realism in controlled shots. Varied lighting, fast head turns, and partial occlusions still produce artifacts. Production-grade results still require artist intervention.
- **Complex object removal.** Moving objects from busy scenes produce visible temporal smearing and edge bleeding.
- **Dynamic background replacement.** Fast-moving subjects with complex edges (hair, flowing fabric) still hallucinate edge detail.

### Not there yet

- **Fully automated VFX shots.** No tool produces broadcast-ready VFX without human supervision.
- **Photorealistic digital doubles.** Beyond AI-only pipelines for arbitrary lighting conditions.
- **Real-time AI compositing for live production.** Processing latency makes this unreliable.

---

## Animation

### Ready to use

- **AI-assisted keyframe animation (Cascadeur).** AutoPosing generates physically plausible poses. AutoPhysics calculates weight, balance, and momentum. 2–3x faster blocking than traditional methods.
- **Motion capture cleanup.** Rokoko Studio and Cascadeur convert noisy mocap data into clean, editable keyframes — minutes instead of days.
- **Single-camera mocap for previz.** Rokoko Vision's webcam/phone-based capture is usable for previsualization.

### Getting there

- **Video-based markerless motion capture.** Approaches marker-based quality for body motion, but finger tracking, facial capture, and ground contact precision lag behind dedicated hardware.
- **AI-generated in-betweens.** Physically plausible but artistically generic — needs animator refinement.
- **2D animation from AI.** Useful for animatics and concept exploration, not for production-quality output.

### Not there yet

- **Fully automated character animation.** No AI tool produces broadcast-quality animation without animator input.
- **AI lip-sync for 3D characters.** "Approximation" quality — not production-grade.
- **Complex multi-character choreography.** Fight scenes, dance sequences, group conversations remain manual.

---

## Voice Synthesis & Text-to-Speech

### Ready to use

- **Short-to-medium narration (under 10 minutes).** ElevenLabs, Azure Neural TTS, and Fish Audio S2 produce speech indistinguishable from human narration for explainer content, educational material, and eLearning.
- **Voice cloning.** Production-viable. ElevenLabs requires ~30 minutes of studio audio. Fish Audio S2 needs only 15 seconds. Near-human fidelity.
- **Word-level emotion control (Fish Audio S2).** Tag individual words with `[excited]`, `[whispered]`, `[somber]` — a genuine breakthrough in TTS control.

### Getting there

- **Long-form narration (30+ minutes).** Prosody drift and pacing inconsistencies accumulate. Audiobook narration benefits from human direction.
- **Complex emotional arcs.** Irony, subtle sarcasm, building tension require manual prompt engineering and splicing.
- **Domain jargon pronunciation.** Custom pronunciation dictionaries help but require upfront investment.

### Not there yet

- **Replacing professional voice actors for premium content.** Feature film narration, dramatic performances, and emotionally nuanced storytelling — the last 5% of human vocal nuance remains out of reach.
- **Singing voice synthesis at production quality.** A separate unsolved problem.

### What it costs

| Tier | Tool | Cost |
|------|------|------|
| Quality leader | ElevenLabs Enterprise | ~$0.05–$0.12/min |
| Open-source leader | Fish Audio S2 | Self-host (free) or API |
| Cloud-native budget | Azure / Google Cloud TTS | ~$0.016/1K chars |

---

## Music Generation

### Ready to use

- **Background music, mood beds, and underscore.** AI music has crossed the "good enough" threshold for non-focal music — tracks that support visuals rather than being the primary product. Suno V5 produces broadcast-quality 48kHz tracks with natural-sounding vocals. 2 million paid subscribers generating 7 million tracks/day.
- **Genre coverage.** Pop, hip-hop, electronic, lo-fi, ambient, corporate/upbeat — all reliable.

### Getting there

- **Full songs as primary content.** Suno V5 can produce releasable tracks, but vocals can drift, structures collapse in the second half, and genre shifts randomly. Export stems and finish in a DAW.
- **Specific production control.** You can prompt for genre and mood, but fine-grained arrangement control is limited.

### Not there yet

- **Replacing a composer for distinctive music.** AI music is competent but generic — no distinctive artistic voice.
- **Complex arrangements with multiple movements.** Extended compositions with dynamic shifts remain unreliable.
- **Udio.** Post-UMG settlement, downloads are disabled. Music lives on Udio's platform only — unusable for production workflows.

### Legal note worth knowing

Purely AI-generated music (prompt-only, no editing) likely cannot be copyrighted and enters the public domain. To strengthen IP claims: edit, mix, arrange, and add human performance. Document your creative process.

---

## Sound Design & SFX

The weakest AI audio category.

### Ready to use

Simple ambient textures, basic UI sounds, and atmospheric backgrounds. ElevenLabs Sound Effects is the current leader — handles rain, wind, footsteps, door creaks, crowd ambience, and simple impacts.

### Not there yet

- **Replacing a sound library or foley artist.** AI SFX are useful for prototyping and temp tracks. Not reliable enough to ship without significant curation.
- **Complex foley.** Lacks the micro-variations and timing precision of professional foley.
- **Cinematic sound design.** Simple whooshes and risers work. Complex, layered trailer design does not.

### What to do

Use AI SFX for rapid prototyping and temp tracks. Maintain a curated stock SFX library (Epidemic Sound, Artlist) and a sound designer for anything customer-facing.

---

## Audio Post-Production

The most production-ready AI audio category.

### Ready to use

- **Noise removal (iZotope RX 11).** Industry gold standard. ML-based Repair Assistant analyzes and fixes clipping, clicks, hum, noise, reverb, and sibilance. $99–$1,199.
- **Free speech enhancement (Adobe Podcast Enhance v2).** Advanced source separation with independent speech/noise/music sliders. Rivals entry-level professional tools for spoken word cleanup. Free (1hr/day).
- **Stem separation (LALAL.AI).** 10-stem separation (vocals, drums, bass, guitars, piano, synth, strings, wind). No competitor matches that breadth. 14.8M hours processed in 2025.
- **Transcript-based editing (Descript).** Studio Sound one-click cleanup, AI filler word removal, regenerate audio for corrections.

### Not there yet

- **AI mastering for premium releases.** LANDR and eMastered produce 80% solutions — fine for most use cases, insufficient where mastering decisions affect artistic outcome.
- **Fully automated podcast/video post.** Pacing, narrative editing, and tonal consistency still need a human editor.

---

## Dubbing & Localization

### Ready to use

- **AI dubbing with human QA for informational content.** Deepdub (5,000+ titles, Hollywood studio trust), Papercup/RWS (1,800 in-house linguists, patented QA pipeline), and ElevenLabs Dubbing (best raw voice quality) all deliver broadcast-acceptable results through hybrid AI+human workflows.

### Getting there

- **Entertainment dubbing for streaming.** Being used by platforms, but premium scripted content still sounds noticeably AI-dubbed. Emotional performances and comedic timing lose fidelity.
- **Lip-sync matching.** Frame-accurate for simple dialogue, noticeably off for rapid speech or singing.

### Not there yet

- **Fully automated dubbing without human review.** Every enterprise provider includes mandatory human QA. Skip it at your own risk — the errors are embarrassing.
- **Premium entertainment dubbing.** Feature films and prestige TV still need human voice actors.
- **Singing/musical numbers.** AI dubbing handles dialogue only.

---

## End-to-End Production Platforms

### The honest answer

**No single platform handles a full production pipeline at enterprise quality.** The market is strong point solutions that need orchestration.

| Platform | What It Actually Does | Enterprise-Ready? |
|----------|----------------------|-------------------|
| ElevenLabs Flows | Chains audio, image, and video models in a visual canvas | No — alpha, no API yet |
| Luma Agents | Multi-modal asset generation from a single brief | No — launched March 5, 2026 |
| Synthesia | Script-to-avatar video for training and corporate comms | Yes — for talking-head content only |
| HeyGen | Avatar video with best-in-class lip-sync and voice cloning | Yes — for talking-head content only |

**What a realistic production pipeline looks like today:**
1. Script via LLM (Claude/GPT)
2. Avatar video via Synthesia/HeyGen OR generative video via Runway/Kling
3. Audio/voice via ElevenLabs
4. Editing in a traditional NLE or Descript
5. Delivery via existing infrastructure

This is a 4–5 tool pipeline, not end-to-end.

---

## AI Agents for Production

### The reality

AI agents work for structured, repeatable tasks (ingest → transcribe → tag → distribute). They fail at creative judgment and anything requiring visual quality assessment.

- **Claude Computer Use:** ~60% success rate on simple tasks, ~45% on complex workflows. Anthropic cut their own productivity forecasts in half.
- **Make.com / n8n:** ~50% time reduction for trigger-based workflows. Reliable for template-based video creation, file routing, and automated distribution to web platforms.
- **No agent is ready for autonomous production.** Every workflow needs human checkpoints.

---

## Transcription & Captioning

The most mature category.

| Provider | English Accuracy | Price/Min | Best For |
|----------|-----------------|-----------|----------|
| AssemblyAI Universal-3 Pro | 94.1% | $0.006 | Audio intelligence, PII redaction |
| OpenAI Whisper | 92.4% | $0.006 | Cheapest batch, 100+ languages |
| Deepgram Nova-3 | 92.1% | $0.004 | Real-time (<300ms latency) |

**Speaker diarization** remains the weak point: 85–90% accuracy in typical conditions, dropping to 75–80% with noise or 5+ speakers.

---

## Legal & Copyright

### The ruling that matters

The U.S. Supreme Court declined certiorari on March 2, 2026, confirming that AI-generated content without meaningful human authorship is **not copyrightable**.

### Risks to know

- **70+ new copyright lawsuits** filed since January 2026 targeting enterprises using AI-generated assets.
- **EU AI Act** mandates AI content labeling by August 2026. Fines up to 3% of global turnover.
- **Voice cloning** is now regulated under the AI Fraud Accountability Act and state-level likeness laws.
- **Training data lawsuits** (Runway, OpenAI, Suno/Udio settlements) create derivative liability risk for enterprise customers.

### What to do about it

1. **Document human involvement** in every AI-assisted deliverable — shot selection, editing, creative direction.
2. **Negotiate IP indemnification** with vendors. Adobe Firefly and Sora offer the strongest protections.
3. **Label AI content proactively** — even outside the EU, norms are shifting.
4. **Do not use consumer AI tools** for confidential content — courts treat AI as a "third party" waiving privilege.

---

## What It Costs at Scale

### 100 Videos/Month (Educational/Instructional)

| Component | Tool | Monthly Cost |
|-----------|------|-------------|
| Script generation | Claude/GPT API | $50–$200 |
| Avatar video | Synthesia Enterprise | ~$2,500 |
| Voice/audio | ElevenLabs Scale | $99–$330 |
| Transcription/captions | Whisper API | $3 |
| QC automation | Telestream/Venera | $800–$2,000 |
| Workflow automation | n8n Cloud | $24–$80 |
| **Total** | | **$3,500–$5,100** |

### 500 Videos/Month (Mixed Formats, Web & App Distribution)

| Component | Tool | Monthly Cost |
|-----------|------|-------------|
| Script + creative direction | Claude/GPT API + human | $500–$1,500 |
| Video generation | HeyGen Enterprise + Luma API | $3,000–$8,000 |
| Audio production | ElevenLabs Enterprise | $500–$1,500 |
| Transcription/captions | AssemblyAI | $150–$300 |
| QC + compliance | Enterprise QC suite | $2,000–$5,000 |
| Human review/editing | Staff editors | $5,000–$15,000 |
| **Total** | | **$12,000–$34,000** |

The largest cost in any AI production pipeline remains **human review and editing**, which currently cannot be eliminated.

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
| Animation blocking and mocap cleanup | Cascadeur + Rokoko |
| CG character compositing | Wonder Studio (~$1K/yr) |

### Watch closely — promising but unproven

| Use Case | Tools to Evaluate |
|----------|---------------|
| Agent-based creative workflows | Luma Agents, ElevenLabs Flows |
| Multi-shot narrative generation | Kling 3.0 multi-shot, Seedance 2.0 |
| AI dubbing at scale | Deepdub, Papercup, ElevenLabs |
| End-to-end video from brief | CapCut AI Suite |

### Don't count on — not yet

- AI-only long-form video generation (>30s coherent narrative)
- Automated editorial decision-making for brand content
- AI text rendering within generated video
- Unsupervised VFX compositing
- AI-only character animation for broadcast
- Fully autonomous production agents
- AI music as hero content for premium releases
- AI sound effects for final production delivery

---

## How We Built This

This assessment draws from research conducted March 2026, cross-referencing manufacturer documentation, third-party benchmarks (Artificial Analysis), trade press reporting, enterprise case studies, and independent product reviews. Where marketing claims conflict with independent assessments, the more conservative position is taken. Pricing reflects publicly available rates and may not reflect negotiated enterprise agreements.

**Shelf life:** This document is useful for roughly 3–6 months before material updates are needed. Re-evaluate quarterly.

---

*Published by The AV AI Dispatch · March 2026*
