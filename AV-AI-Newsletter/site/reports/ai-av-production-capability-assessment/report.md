# What AI Can and Can't Do in AV Production — March 2026

> A grounded enterprise assessment of AI capabilities across video, audio, and production pipeline tooling. No hype. No speculation. Just what works, what partially works, and what doesn't — right now.

---

## Executive Summary

AI has crossed meaningful thresholds in audio/video production. Text-to-speech passes for human narration in controlled scenarios. Short-form video generation is production-usable. Post-production AI (noise removal, rotoscoping, transcript editing) is saving real hours today. But the gap between demos and reliable enterprise output remains wide.

**The pattern across every category:** AI gets you 70–90% of the way there, fast. The last 10–30% still needs human judgment, and that gap matters enormously at enterprise quality.

**The bottom line:** You can now generate 5–15 seconds of impressive video footage, produce broadcast-quality background music, clone voices with near-human fidelity, and automate tedious post-production tasks. You cannot yet produce a coherent 60-second narrative scene, replace a composer for distinctive music, or trust any AI output without a human QA pass.

---

## Video Generation

### The Landscape

| Tool | Max Resolution | Max Duration | Character Consistency | Price Range |
|------|---------------|-------------|----------------------|-------------|
| Runway Gen-4.5 | 4K | 60s | Good (reference images) | $12–$127/mo |
| Kling 3.0 | 4K at 60fps | 15s | Good (multi-shot mode) | $6–$48/mo |
| Seedance 2.0 | 2K cinema | 15s | Good (multi-shot) | TBD |
| Sora 2 Pro | 1080p | 20s | Weak | $20–$200/mo |
| Pika 2.5 | 1080p | 10s (25s w/ Pikaframes) | Weak | $8–$76/mo |
| Veo 2 | 720p | 8s | Weak | Vertex pricing |
| Luma Uni-1 | Up to 4K | Varies | Moderate | Enterprise |

### What Works

- **Short-form clips (5–15s)** for social media, ads, and B-roll. All major tools produce usable footage at this duration.
- **Image-to-video animation.** Starting from a reference image consistently beats text-to-video quality.
- **Style, mood, and camera movement.** Cinematic lighting, color grading, and camera moves are well-handled by the top three tools.
- **Concept visualization and pre-vis.** Over 14,000 enterprises use these tools for storyboarding, cutting pre-production time by ~40%.
- **Lip-sync in controlled settings.** Seedance 2.0 and Kling 3.0 produce serviceable lip-sync for talking-head shots.

### What Partially Works

- **Character consistency across shots.** Kling 3.0's multi-shot mode and Seedance's reference system are the best available, but character drift compounds beyond 3–4 shots. Expect heavy curation and re-generation.
- **Extended duration (30–60s).** Runway Gen-4.5 claims 60s continuous generation. In practice, coherence degrades past ~20 seconds, particularly with multiple subjects.
- **Physics simulation.** Rigid body physics look reasonable. Fluid dynamics, cloth draping, and fine motor interactions fail routinely.
- **Multi-character scenes.** Two characters interacting is achievable. Three or more reliably introduces spatial confusion and identity mixing.

### What Doesn't Work

- **Text rendering in video.** Every tool fails at generating readable, stable text within frames. Add text in post.
- **Complex hand/finger interactions.** Extra fingers, impossible joint angles, objects phasing through hands — the Achilles' heel persists.
- **Narrative coherence over 30+ seconds.** No tool produces a reliable minute-long scene with consistent spatial reasoning, cause-and-effect continuity, and character motivation.
- **Precise prompt control.** "A woman picks up the red cup with her left hand, turns 90 degrees clockwise, and places it on the shelf" — this level of specificity is beyond current capabilities.
- **Photorealistic humans under scrutiny.** Close-up faces in motion still trigger uncanny valley. Wide shots and stylized aesthetics hide limitations better.

### Recommendation

**Adopt now** for pre-visualization, social B-roll, and concept work. **Evaluate carefully** for multi-shot narrative sequences. **Don't rely on** AI-only video for hero brand content or anything requiring precise human representation.

---

## Video Editing & Post-Production

### What Works

- **Transcript-based editing (Descript).** Edit video by editing text. Filler word removal, silence trimming, and rough-cut assembly are production-proven. 60–70% time savings for spoken-word content.
- **AI-powered clipping (Opus Clip).** 70–80% of generated clips are usable without further editing. Converting long-form to short-form is the strongest use case.
- **Object masking and tracking (Premiere Pro).** Adobe's AI Object Mask is a workflow accelerator — hover, click, tracked mask in seconds. Production-ready.
- **AI audio cleanup (DaVinci Resolve, Descript).** Fairlight Voice Isolation and Descript Studio Sound reliably improve bad audio to acceptable levels.
- **Auto-captioning.** 92–95% accuracy for clear English audio. Dramatically faster than manual captioning.

### What Partially Works

- **AI-assembled timelines from scripts (DaVinci IntelliScript).** First-draft quality requiring significant editorial judgment for pacing and shot selection.
- **Generative Extend (Premiere Pro).** Subtle clip extensions work. Quality degrades with longer extensions or moving subjects.
- **AI translation and dubbing (Descript).** 30+ languages with lip-sync. Strong for major European languages, weak for tonal languages.

### What Doesn't Work

- **Creative editorial judgment.** No AI tool replaces an editor's sense of pacing, emotional arc, or comedic timing.
- **Brand-consistent editing at scale.** Maintaining a consistent editorial voice across dozens of AI-assisted videos requires human oversight.
- **Complex narrative editing.** Multi-act structure, parallel storylines, non-linear timelines — entirely human-driven.

### Best Value

DaVinci Resolve's free version includes most AI features and is a legitimate professional tool. The $295 Studio upgrade is a one-time purchase — exceptional value compared to subscription models.

---

## VFX & Compositing

### What Works

- **AI rotoscoping.** The single most production-ready AI capability in VFX. DaVinci Magic Mask v2, Premiere Object Mask, and Slapshot (up to 8K, 400 shots/day) produce results that previously required hours of manual work per shot.
- **CG character compositing (Wonder Studio).** 80–90% of the VFX pipeline automated — character tracking, lighting matching, shadow casting, compositing. Exports to Maya, Blender, Unreal. Cuts turnaround from one week to one day. ~$1,000/year.
- **Simple object removal.** Static or slow-moving objects (wires, boom mics, unwanted signage) — reliable.

### What Partially Works

- **AI de-aging.** 94% realism in controlled shots. Varied lighting, fast head turns, and partial occlusions still produce artifacts. Production-grade results still require artist intervention.
- **Complex object removal.** Moving objects from busy scenes produce visible temporal smearing and edge bleeding.
- **Dynamic background replacement.** Fast-moving subjects with complex edges (hair, flowing fabric) still hallucinate edge detail.

### What Doesn't Work

- **Fully automated VFX shots.** No tool produces broadcast-ready VFX without human supervision.
- **Photorealistic digital doubles.** Beyond AI-only pipelines for arbitrary lighting conditions.
- **Real-time AI compositing for live production.** Processing latency makes this unreliable.

---

## Animation

### What Works

- **AI-assisted keyframe animation (Cascadeur).** AutoPosing generates physically plausible poses. AutoPhysics calculates weight, balance, and momentum. 2–3x faster blocking than traditional methods.
- **Motion capture cleanup.** Rokoko Studio and Cascadeur convert noisy mocap data into clean, editable keyframes — minutes instead of days.
- **Single-camera mocap for previz.** Rokoko Vision's webcam/phone-based capture is usable for previsualization.

### What Partially Works

- **Video-based markerless motion capture.** Approaches marker-based quality for body motion, but finger tracking, facial capture, and ground contact precision lag behind dedicated hardware.
- **AI-generated in-betweens.** Physically plausible but artistically generic — needs animator refinement.
- **2D animation from AI.** Useful for animatics and concept exploration, not for production-quality output.

### What Doesn't Work

- **Fully automated character animation.** No AI tool produces broadcast-quality animation without animator input.
- **AI lip-sync for 3D characters.** "Approximation" quality — not production-grade.
- **Complex multi-character choreography.** Fight scenes, dance sequences, group conversations remain manual.

---

## Text-to-Speech & Voice Synthesis

### What Works

- **Short-to-medium narration (under 10 minutes).** ElevenLabs, Azure Neural TTS, and Fish Audio S2 produce speech indistinguishable from human narration for corporate/explainer content, IVR, and eLearning.
- **Voice cloning.** Production-viable. ElevenLabs requires ~30 minutes of studio audio. Fish Audio S2 needs only 15 seconds. Near-human fidelity.
- **Word-level emotion control (Fish Audio S2).** Tag individual words with `[excited]`, `[whispered]`, `[somber]` — a genuine breakthrough in TTS control.

### What Partially Works

- **Long-form narration (30+ minutes).** Prosody drift and pacing inconsistencies accumulate. Audiobook narration benefits from human direction.
- **Complex emotional arcs.** Irony, subtle sarcasm, building tension require manual prompt engineering and splicing.
- **Domain jargon pronunciation.** Custom pronunciation dictionaries help but require upfront investment.

### What Doesn't Work

- **Replacing professional voice actors for premium content.** Feature film narration, AAA game characters, high-emotion advertising — the last 5% of human vocal nuance remains out of reach.
- **Singing voice synthesis at production quality.** A separate unsolved problem.

### Pricing

| Tier | Tool | Cost |
|------|------|------|
| Quality leader | ElevenLabs Enterprise | ~$0.05–$0.12/min |
| Open-source leader | Fish Audio S2 | Self-host (free) or API |
| Cloud-native budget | Azure / Google Cloud TTS | ~$0.016/1K chars |

---

## Music Generation

### What Works

- **Background music, mood beds, podcast intros, social media content.** AI music has crossed the "good enough for production" threshold for non-focal music. Suno V5 produces broadcast-quality 48kHz tracks with natural-sounding vocals. 2 million paid subscribers generating 7 million tracks/day.
- **Genre coverage.** Pop, hip-hop, electronic, lo-fi, ambient, corporate/upbeat — all reliable.

### What Partially Works

- **Full songs as primary content.** Suno V5 can produce releasable tracks, but vocals can drift, structures collapse in the second half, and genre shifts randomly. Export stems and finish in a DAW.
- **Specific production control.** You can prompt for genre and mood, but fine-grained arrangement control is limited.

### What Doesn't Work

- **Replacing a composer for distinctive music.** AI music is competent but generic — no distinctive artistic voice.
- **Complex arrangements with multiple movements.** Extended compositions with dynamic shifts remain unreliable.
- **Udio.** Post-UMG settlement, downloads are disabled. Music lives on Udio's platform only — unusable for production workflows.

### Critical Legal Note

Purely AI-generated music (prompt-only, no editing) likely cannot be copyrighted and enters the public domain. To strengthen claims: edit, mix, arrange, and add human performance. Document your creative process.

---

## Sound Design & SFX

The weakest AI audio category.

### What Works

Simple ambient textures, basic UI sounds, and atmospheric backgrounds. ElevenLabs Sound Effects is the current leader — handles rain, wind, footsteps, door creaks, crowd ambience, and simple impacts.

### What Doesn't Work

- **Replacing a sound library or foley artist.** AI SFX are useful for prototyping and temp tracks. Not reliable enough to ship without significant curation.
- **Complex foley.** Lacks the micro-variations and timing precision of professional foley.
- **Cinematic sound design.** Simple whooshes and risers work. Complex, layered trailer design does not.

### Practical Guidance

Use AI SFX for rapid prototyping and temp tracks. Maintain a curated stock SFX library (Epidemic Sound, Artlist) and a sound designer for anything customer-facing.

---

## Audio Post-Production

The most production-ready AI audio category.

### What Works

- **Noise removal (iZotope RX 11).** Industry gold standard. ML-based Repair Assistant analyzes and fixes clipping, clicks, hum, noise, reverb, and sibilance. Non-negotiable for professional audio work. $99–$1,199.
- **Free speech enhancement (Adobe Podcast Enhance v2).** Advanced source separation with independent speech/noise/music sliders. Rivals entry-level professional tools for spoken word cleanup. Free (1hr/day).
- **Stem separation (LALAL.AI).** 10-stem separation (vocals, drums, bass, guitars, piano, synth, strings, wind). No competitor matches that breadth. 14.8M hours processed in 2025.
- **Transcript-based editing (Descript).** Studio Sound one-click cleanup, AI filler word removal, regenerate audio for corrections.

### What Doesn't Work

- **AI mastering for premium releases.** LANDR and eMastered produce 80% solutions — fine for most use cases, insufficient where mastering decisions affect artistic outcome.
- **Fully automated podcast/video post.** Pacing, narrative editing, and tonal consistency still need a human editor.

---

## Dubbing & Localization

### What Works

- **AI dubbing with human QA pipelines for corporate/informational content.** Deepdub (5,000+ titles, Hollywood studio trust), Papercup/RWS (1,800 in-house linguists, patented QA pipeline), and ElevenLabs Dubbing (best raw voice quality) all deliver broadcast-acceptable results through hybrid AI+human workflows.

### What Partially Works

- **Entertainment dubbing for streaming.** Being used by platforms, but premium scripted content still sounds noticeably AI-dubbed. Emotional performances and comedic timing lose fidelity.
- **Lip-sync matching.** Frame-accurate for simple dialogue, noticeably off for rapid speech or singing.

### What Doesn't Work

- **Fully automated dubbing without human review.** Every enterprise provider includes mandatory human QA. Skip it at your own risk — the errors are embarrassing.
- **Premium entertainment dubbing.** Feature films and prestige TV still need human voice actors.
- **Singing/musical numbers.** AI dubbing handles dialogue only.

---

## End-to-End Production Platforms

### The Honest Answer

**No single platform handles a full production pipeline at enterprise quality.** The market is strong point solutions that need orchestration.

| Platform | What It Actually Does | Enterprise-Ready? |
|----------|----------------------|-------------------|
| ElevenLabs Flows | Chains audio, image, and video models in a visual canvas | No — alpha, no API yet |
| Luma Agents | Multi-modal asset generation from a single brief | No — launched March 5, 2026 |
| Synthesia | Script-to-avatar video for training and corporate comms | Yes — for talking-head content only |
| HeyGen | Avatar video with best-in-class lip-sync and voice cloning | Yes — for talking-head content only |

**The realistic production pipeline today:**
1. Script via LLM (Claude/GPT)
2. Avatar video via Synthesia/HeyGen OR generative video via Runway/Kling
3. Audio/voice via ElevenLabs
4. Editing in a traditional NLE or Descript
5. Delivery via existing infrastructure

This is a 4–5 tool pipeline, not end-to-end.

---

## AI Agents for Production

### The Reality

AI agents work for structured, repeatable tasks (ingest → transcribe → tag → distribute). They fail at creative judgment and anything requiring visual quality assessment.

- **Claude Computer Use:** ~60% success rate on simple tasks, ~45% on complex workflows. Anthropic cut their own productivity forecasts in half.
- **Make.com / n8n:** ~50% time reduction for trigger-based workflows. Reliable for multi-platform publishing, template-based video creation, and file routing.
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

## Legal & Copyright Landscape

### The Definitive Ruling

The U.S. Supreme Court declined certiorari on March 2, 2026, confirming that AI-generated content without meaningful human authorship is **not copyrightable**.

### Key Risks

- **70+ new copyright lawsuits** filed since January 2026 targeting enterprises using AI-generated assets.
- **EU AI Act** mandates AI content labeling by August 2026. Fines up to 3% of global turnover.
- **Voice cloning** is now regulated under the AI Fraud Accountability Act and state-level likeness laws.
- **Training data lawsuits** (Runway, OpenAI, Suno/Udio settlements) create derivative liability risk for enterprise customers.

### Mitigation Requirements

1. **Document human involvement** in every AI-assisted deliverable — shot selection, editing, creative direction.
2. **Negotiate IP indemnification** with vendors. Adobe Firefly and Sora offer the strongest protections.
3. **Label AI content proactively** — even outside the EU, norms are shifting.
4. **Do not use consumer AI tools** for confidential content — courts treat AI as a "third party" waiving privilege.

---

## Enterprise Cost Modeling

### 100 Videos/Month (Corporate Training)

| Component | Tool | Monthly Cost |
|-----------|------|-------------|
| Script generation | Claude/GPT API | $50–$200 |
| Avatar video | Synthesia Enterprise | ~$2,500 |
| Voice/audio | ElevenLabs Scale | $99–$330 |
| Transcription/captions | Whisper API | $3 |
| Content repurposing | Opus Clip Pro | $15 |
| QC automation | Telestream/Venera | $800–$2,000 |
| Workflow automation | n8n Cloud | $24–$80 |
| **Total** | | **$3,500–$5,200** |

### 500 Marketing Videos/Month (Mixed Formats)

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

## Recommendations

### Adopt Now (Clear ROI)

| Use Case | Best Tools |
|----------|-----------|
| Short-form social clips from long-form | Opus Clip + Descript |
| Concept/pre-visualization | Runway Gen-4.5 or Kling 3.0 |
| Rotoscoping and masking | DaVinci Resolve Magic Mask or Premiere Object Mask |
| Audio cleanup | iZotope RX 11 or Adobe Podcast Enhance (free) |
| Transcript-based editing | Descript |
| Background music | Suno V5 |
| Voice synthesis (short-form) | ElevenLabs or Fish Audio S2 |
| Corporate talking-head video | Synthesia or HeyGen |
| Animation blocking and mocap cleanup | Cascadeur + Rokoko |
| CG character compositing | Wonder Studio (~$1K/yr) |

### Evaluate Carefully (Promising but Unproven)

| Use Case | Watch Closely |
|----------|---------------|
| Agent-based creative workflows | Luma Agents, ElevenLabs Flows |
| Multi-shot narrative generation | Kling 3.0 multi-shot, Seedance 2.0 |
| AI dubbing at scale | Deepdub, Papercup, ElevenLabs |
| End-to-end video from brief | CapCut AI Suite |

### Don't Rely On (Yet)

- AI-only long-form video generation (>30s coherent narrative)
- Automated editorial decision-making for brand content
- AI text rendering within generated video
- Unsupervised VFX compositing
- AI-only character animation for broadcast
- Fully autonomous production agents
- AI music as hero content for premium releases
- AI sound effects for final production delivery

---

## Methodology

This assessment is based on research conducted March 20, 2026, cross-referencing manufacturer documentation, third-party benchmarks (Artificial Analysis), trade press reporting, enterprise case studies, and independent product reviews. Where marketing claims conflict with independent assessments, the more conservative position is taken. Pricing reflects publicly available rates and may not reflect negotiated enterprise agreements.

**Shelf life:** This document has a useful life of roughly 3–6 months before material updates are needed. Re-evaluate quarterly.

---

*Published by The AV AI Dispatch · March 2026*
