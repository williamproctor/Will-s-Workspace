# Primary-Source AV AI Research — Week of July 17, 2026

Research window: July 11–17, 2026. Sixteen candidates screened; twelve retained below.

## 1. Foundry SmartRoto

- **Date:** July 17
- **Primary:** https://www.foundry.com/products/nuke-family/smartroto
- **Independent:** https://www.fxguide.com/fxfeatured/foundrys-smartroto-ai-assisted-roto-that-aims-to-work-the-way-you-do/
- **What shipped:** A Nuke plugin that propagates editable roto splines from artist-created keyframes inside the existing Roto node.
- **Price:** $499/year introductory; $599/year regular. Separate Nuke-family license required. Unrestricted 90-day trial.
- **Hardware:** Nuke 16.1+, recommended over 8GB VRAM; lower-resolution work recommended on weaker GPUs.
- **Measurement:** Foundry advertises up to 4× faster. Its testing lead told fxguide that approximately 2× was consistent and 4× represented the high end.
- **Data:** Licensed training data, local inference, no footage transmission.
- **Why it matters:** AI produces the editable spline deliverable compositors already use rather than a flattened mask.

## 2. Decart Lucy 2.5

- **Date:** July 16
- **Primary:** https://decart.ai/publications/lucy-2-5-raising-the-bar-for-live-ai
- **API:** https://docs.platform.decart.ai/models/realtime/lucy-2.5
- **What shipped:** Real-time text- and reference-image editing of streaming video, including subject replacement, object addition/removal, environment changes, and persistent edits.
- **Transport:** WebRTC; landscape and portrait.
- **Resolution conflict:** Release copy says 1080p at 30 FPS; current API specifications list 1280×720.
- **Measurement:** Vendor-reported; no independent latency, consistency, or quality benchmark found.
- **Why it matters:** Generative editing moves from render/export toward live camera processing.

## 3. Gemini Omni Flash and personal avatars in Google Vids

- **Date:** July 16–17
- **Primary:** https://workspace.google.com/blog/product-announcements/introducing-gemini-omni-flash-in-google-vids
- **Independent:** https://www.theverge.com/ai-artificial-intelligence/966644/google-vids-will-now-let-you-generate-ai-videos-of-yourself
- **Capabilities:** Conversational clip editing, background replacement, lighting repair, appearance changes, revised voiceovers/text, and account-linked personal avatars.
- **Availability:** Eligible paid Workspace/Google AI plans; staged rollout.
- **Limits:** Avatar users must meet age, language, region, and account requirements; admin controls apply.
- **Provenance:** SynthID on generated video.
- **Measurement:** More than seven million monthly Vids users is a Google-reported figure.
- **Repeat check:** Gemini Omni and Vids appeared previously; the personal-avatar and Omni-in-Vids integration is new.

## 4. Synthesia Dubbing 2.0

- **Date:** July 15
- **Primary:** https://www.synthesia.io/post/introducing-dubbing-2-0
- **Capabilities:** Revised lip sync, voice, translation, glossary support, timing preservation, transcript review, and segment-level regeneration across more than 130 languages.
- **Availability:** Live for all customers; Enterprise unlocks the full editing workflow and unlimited dubbing.
- **Limits:** No blind test, numerical error rate, or independent evaluation. “Publishable first pass” is a vendor claim.
- **Why it matters:** Localization behaves more like editable post-production; failed segments can be corrected without rerendering the complete video.

## 5. MultiRef-Compass

- **Date:** July 15
- **Paper:** https://arxiv.org/abs/2607.14189
- **Code:** https://github.com/zxhhh0201/MultiRef-Compass
- **Scope:** 350 curated multi-reference audio-video samples, four evaluation dimensions, and eight tested systems.
- **Automatic results:** Gemini Omni led reported visual quality (0.2373) and lip-sync (4.5333); Kling led entity fidelity (0.6160), narrowly ahead of Seedance (0.6104).
- **Important limits:** Safety filters reduced Seedance to 282 samples and Gemini Omni to 245, making some comparisons partial. Several metrics use Gemini 3.1 Pro as a judge. No independent replication yet.
- **Why it matters:** Aggregate visual scores miss identity splitting, role swaps, attribute leakage, and incorrect sound-source assignments.

## 6. BandLab acquires Aiode

- **Date:** July 15
- **Primary:** https://bandlabtechnologies.com/news/bandlab-technologies-announces-acquisition-ai-powered-digital-music-studio-aiode/
- **Product:** https://aiode.com/product/
- **Capabilities:** Audio-to-audio musician and style models; section-level direction; alternate takes; 48kHz/24-bit stereo WAV stems.
- **Licensing:** Aiode states that all training audio is licensed and traceable, individual musician models are built with participating performers, and musicians receive revenue share.
- **Availability:** Standalone web/desktop beta continues.
- **Limits:** Revenue-share percentages and acquisition terms were not disclosed; several DAW capabilities remain planned.
- **Why it matters:** A licensed, musician-participatory model produces editable musical parts rather than a complete opaque song.

## 7. Foundry Griptape Enterprise

- **Date:** July 17
- **Primary:** https://www.foundry.com/products/griptape
- **Independent:** https://www.awn.com/news/foundry-launches-griptape-enterprise-secure-ai-accelerated-vfx-workflows
- **Capabilities:** Node-based orchestration for text, image, video, audio, and 3D models; Python workflows; MCP connections to Nuke, Maya, Blender, and Flow Production Tracking.
- **Controls:** Permissions, versioning, provenance metadata, on-premises/private-cloud deployment.
- **Price:** Professional $40/month or $400/year per user, up to three users; Enterprise custom.
- **Limits:** Foundry says customers must verify each connected model’s training-data and licensing status.
- **Why it matters:** Model experimentation moves behind studio permissions, repeatable graphs, and provenance records.

## 8. VideoChat3

- **Date:** July 16
- **Paper:** https://arxiv.org/abs/2607.14935
- **Code:** https://github.com/MCG-NJU/VideoChat3
- **Capabilities:** 4B-parameter long/streaming video understanding model with 16× spatiotemporal compression.
- **Reported scores:** 70.1 Video-MME, 61.7 MotionBench, 75.6 TempCompass, 56.7 LVBench.
- **Limits:** Author-run benchmarks; training code was not yet available during the scan; long-video tests used H200-class hardware.
- **Why it matters:** Archive search, logging, temporal retrieval, media QA, and stream monitoring.

## 9. LALAL.AI Lynx

- **Date:** July 14
- **Primary:** https://www.lalal.ai/blog/lynx-voice-isolation-neural-network/
- **Independent:** https://www.prosoundweb.com/lalal-ai-launches-new-lynx-neural-network-for-speech-denoising/
- **Capabilities:** Purpose-built dialogue isolation from music, crowds, engines, footsteps, and environmental noise.
- **Availability:** Default in Voice Cleaner and Voice & Noise across browser, mobile, desktop cloud mode, and API.
- **Limits:** Cloud processing; no independent quality benchmark; group vocals and distant microphones remain improvement targets.
- **Why it matters:** Cleaner dialogue inputs for transcription, dubbing, and voice replacement.

## 10. Gemini Omni leads current preference leaderboards

- **Date:** July 13 snapshot
- **Text-to-video:** https://artificialanalysis.ai/video/leaderboard/text-to-video
- **Image-to-video:** https://artificialanalysis.ai/video/leaderboard/image-to-video
- **Reported snapshot:** Text-to-video with audio 1,240 Elo; image-to-video with audio 1,204 Elo.
- **Limits:** Elo measures blind viewer preference, not editability, licensing, consistency, prompt reliability, or professional output formats. Rankings change continuously.
- **Why it matters:** Current preference quality and production usefulness remain separate measurements.

## 11. Thinking Machines Inkling

- **Date:** July 15
- **Primary:** https://thinkingmachines.ai/news/introducing-inkling/
- **Capabilities:** Open-weights multimodal understanding model; 975B total parameters, 41B active, up to 1M-token context, audio input and text output.
- **Reported audio scores:** 91.4 VoiceBench, 77.2 MMAU, 56.6 Audio MC.
- **Limits:** Extremely large checkpoint; no video input in the released path; vendor-run evaluations.
- **Why it matters:** Contextualizes future agents that reason over recordings, images, transcripts, and tools.

## 12. Verbatik MCP voice tools

- **Date:** July 16
- **Primary:** https://verbatik.com/mcp
- **Capabilities:** TTS, SSML, voice design, music generation, and short-sample voice cloning through MCP-compatible agents.
- **Limits:** Pricing and character-limit documentation conflict; no independent quality measurement; consent verification was not prominent.
- **Why it matters:** Narration and audio generation become callable steps in larger production agents.

## Frontier Watch: Kimi K3

- **Date:** July 16
- **Primary:** https://www.kimi.com/blog/kimi-k3
- **API:** https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
- **Independent:** https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems
- **Scale:** 2.8 trillion total parameters with 16 of 896 experts active, native vision, video input, and a one-million-token context window.
- **Availability:** Hosted now through Kimi products and API. Full weights are scheduled for July 27, so it is not yet independently downloadable.
- **API price:** $0.30/M cached input, $3/M fresh input, $15/M output.
- **AV relevance:** Kimi says the model can understand video, generate motion-graphics code, select from source clips, make motion-matched cuts, synchronize edits to beats, process audio, and revise an edit through tools. These are vendor demonstrations of an understanding/agent model, not native video generation.
- **Benchmark nuance:** Moonshot’s tables mix harnesses, hardware, and fallback conditions. Independent evaluations place K3 near the frontier and particularly strong in frontend/code tasks, but not universally first.
- **Operational caveat:** Moonshot recommends 64 or more accelerators for deployment. “Open weight” does not mean practical local use on ordinary workstations.
- **Why it matters:** The gap between hosted frontier models and downloadable systems is narrowing quickly, while model scale and infrastructure requirements are also rising.

## Late-Breaking Frontier Watch: Qwen3.8-Max-Preview

- **Date:** July 19, two days after the edition window
- **Reporting:** https://www.scmp.com/tech/article/3361119/alibaba-says-newest-qwen-ai-model-second-only-anthropics-claude-fable-5
- **Status:** Officially announced preview, not Qwen4 and not merely a leak.
- **Scale:** Alibaba reports 2.4 trillion parameters and multimodal capability.
- **Availability:** Preview access through Token Plan, Qoder, and QoderWork. Open weights are promised, with no published date.
- **Benchmark nuance:** Alibaba says the model is second only to Claude Fable 5, but no independent benchmark package was available at announcement.
- **Why it matters:** Kimi K3 and Qwen3.8 arrived within days of each other, showing how quickly open-weight and hosted frontier claims are moving. The timing is the story; the rankings remain unverified.

## Excluded

- **Seedance 2.5 launch:** no verified target-week availability; official surfaces still list 2.0.
- **Runway Agent 2.0 engineering interview:** retrospective on a June launch; useful context, not new availability.
- **Amap ABot-World:** open release occurred July 9, outside the window.
- **YouCam Video AI MV:** consumer/social-first positioning and limited professional workflow relevance.
- **Adobe Premiere/After Effects/Frame.io, Avid, Resolve, ElevenLabs, Kling, Luma:** no sufficiently novel qualifying product launch found in the date window.

Content review: no sensitivity issues identified in the recommended stories. Reader-facing copy must avoid unsuitable phrasing present on some source pages.
