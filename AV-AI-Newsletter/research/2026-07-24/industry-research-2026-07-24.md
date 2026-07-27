# Primary-Source AV AI Research — Week of July 24, 2026

Research window: July 18–24, 2026.

## Lead — Black Forest Labs FLUX 3

- **Announcement:** July 23
- **Primary:** https://bfl.ai/blog/flux-3
- **Independent:** https://venturebeat.com/technology/black-forest-labs-launches-flux-3-capable-of-generating-images-and-20-second-video-with-audio-but-in-limited-release-to-start
- **Status:** FLUX 3 Video and Action entered gated early access. Image early access, APIs, private weights, and FLUX 3 Dev are planned.

### What FLUX 3 is

FLUX 3 is a jointly trained multimodal flow-matching backbone spanning images, video, and audio, with the same foundation extended toward action prediction. It is Black Forest Labs’ first public video-generation model family.

Announced lines:

1. **FLUX 3 Video:** video/audio generation and editing; gated early access.
2. **FLUX 3 Image:** synthesis/editing; early access promised in following weeks.
3. **FLUX 3 Action / FLUX-mimic:** selected research/commercial partners.
4. **FLUX 3 Dev:** planned open-weight multimodal backbone; no date or license.

### Video capabilities

- Up to **20 seconds** in one generation
- Text-to-video
- Image-to-video from opening frames or looser references
- Video-to-video
- Video/audio continuation
- Keyframe-to-video transitions
- Multilingual dialogue
- Native audio
- Multiple aspect ratios/styles
- Typography and animated design
- Agentic chaining into longer multi-shot sequences

Unknown:

- Maximum video resolution
- Frame rate
- Codec/container/bit depth
- Audio format/sample rate/channels
- Maximum reference count
- Identity-retention metrics
- Public latency and hardware requirements

### Image capabilities

BFL promises synthesis, natural-language editing, complex prompts, multiple resolutions/aspect ratios/styles, and multilingual text. FLUX 3 Image was not released during the window, and no image benchmark or API contract was published.

### Pricing, weights, and licensing

- Public price: not announced
- Public API: not available during the window
- Open weights: FLUX 3 Dev promised later in 2026
- Dev license: not announced
- Parameter count: not announced
- Generation hardware/VRAM: not announced
- Production SLA: not announced

Do not transfer FLUX.2 reference limits, pricing, licenses, or hardware requirements to FLUX 3.

### Preliminary vendor evaluation

BFL compared early-checkpoint 10-second, 720p clips with audio:

- Luma Ray 3.2: 93% preference
- Runway Gen-4.5: 77%
- Grok Imagine Video: 69%
- Kling v3 Pro: 60%
- Happy Horse v1: 59%
- Happy Horse 1.1: 57%
- Seedance 2.0: 52%
- Gemini Omni Flash: 52%

Missing: prompt set, sample count, rater details, confidence intervals, randomization, inference settings, separate audio/picture scores, and evidence that the early checkpoint matches the early-access system. The 52% comparisons may represent ties.

### Independent status

No independent hands-on test or benchmark existed by July 24. Early practitioner posts were vendor-seeded or had undisclosed access. VentureBeat verified launch status and omissions but did not evaluate output.

### Accurate lead framing

FLUX 3 moves Black Forest Labs from still-image generation toward one image/video/audio/action backbone. Its technical ambition is broad; its current access, pricing, specifications, licensing, and independent evidence remain narrow.

## 2. Qwen-Audio-3.0 voice stack

- **Date:** July 21–24
- **Primary:** https://www.alibabacloud.com/blog/qwen-audio-3-0-tts-more-multilingual-easier-to-direct_603379
- **Independent:** https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice
- **Variants:** Flash for latency; Plus for quality
- **Capabilities:** 16 languages, natural-language delivery control, nonverbal tags, imperfect-reference voice cloning, up to three minutes per pass
- **Independent snapshot:** Plus at 1,234 Elo ±16 from 1,517 samples, effectively tied with Simba 3.2
- **Availability:** Hosted Model Studio API; no weights
- **Caveat:** Full language/48kHz support was rolling out; vendor multilingual and cloning claims need independent review.

## 3. Runway Media Router

- **Date:** July 23
- **Primary:** https://runwayml.com/news/company-news/introducing-runway-media-router
- **Documentation:** https://docs.dev.runwayml.com/model-routers/configuration/
- **Independent:** https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/
- **Capabilities:** Route image/video/audio requests by one preference—cost, latency, or quality—with allow/deny lists, credit ceilings, immutable config IDs, versioning, realized costs, and dry runs.
- **Price:** No routing surcharge; underlying model rates apply; Runway credit = $0.01.
- **Availability:** Live through Runway Dev.
- **Caveat:** Quality scores and selection methods are internal; routing decisions need logging for provenance/reproducibility.
- **Repeat check:** Valid follow-up to July 10’s planned routing layer.

## 4. Sonilo Sound Effects 1.0

- **Date:** July 21
- **Primary:** https://www.prnewswire.com/news-releases/sonilo-and-fal-launch-sound-effects-1-0-for-realistic-sound-effects-from-video-and-text-302830490.html
- **API:** https://fal.ai/models/sonilo/v1.1/video-to-sound-effects/llms.txt
- **Capabilities:** Video-conditioned synchronized sound-effects track from up to three minutes of footage; optional prompt direction; text-to-sound effects from 1–180 seconds; AAC/MP3/WAV/FLAC output.
- **Pricing:** Video $0.009/sec; text $0.0018/sec.
- **Availability:** Initial exclusive API launch on fal.
- **Caveat:** Launch says 1.0 while endpoints use v1.1. No independent synchronization benchmark or disclosed methodology.
- **Repeat check:** Video-to-music was covered June 26; this is a separate sound-effects model.

## 5. Qwen-Image-3.0

- **Date:** July 21–22
- **Primary:** https://www.alibabacloud.com/blog/qwen-image-3-0-rich-content-authentic-details-deep-knowledge_603385
- **Independent:** https://decrypt.co/374084/alibaba-qwen-image-3-ai-useful-not-just-pretty
- **Claims:** 4,500-token prompts, text down to 10 pixels, 12 languages, dense multi-panel layouts, formulas, UI mockups, editing, optional retrieval.
- **Availability:** Qwen Chat; API access limited/trial-based.
- **Unknown:** parameter count, weights, license, model card, benchmark, latency, stable API contract.
- **Why it matters:** Structured storyboards, production diagrams, title graphics, presentations, and UI/reference layouts.

## 6. ElevenMusic References, Vocals, and Finetunes

- **Dates:** July 22–23
- **Primary:** https://elevenlabs.io/blog/introducing-references-sound-control-for-music-v2
- **Vocals:** https://elevenlabs.io/blog/introducing-vocals-a-consistent-voice-for-your-elevenmusic-songs
- **References:** 10 seconds to five minutes of owned audio to steer style/instrumentation/feel.
- **Vocals:** reusable singing identity from owned recordings or supplied library.
- **Finetunes:** private style models; up to 50 tracks in current documentation.
- **Pricing:** $0.15/min generated music; $1.50 per finetune.
- **Caveat:** Copyright matching is not proof of ownership/consent. Documentation has Music v1/v2 migration ambiguity.

## 7. NVIDIA Cosmos3-Super Image2Video 4Step

- **Date:** July 20
- **Model:** https://huggingface.co/nvidia/Cosmos3-Super-Image2Video-4Step
- **Independent:** https://artificialanalysis.ai/video/leaderboard/image-to-video?audio-output=false&open-weights=true
- **Facts:** 64B parameters, four denoising steps, claimed up to 25× acceleration, 256p/480p/720p, five to 400 frames, MP4 with optional 48kHz AAC stereo.
- **Independent snapshot:** approximately 1,271 Elo, first among open-weight image-to-video models without audio.
- **Caveat:** Hardware tested mainly on data-center or professional GPUs; acceleration claim remains vendor-measured.

## 8. SANA-Video 2.0

- **Date:** July 23–24
- **Paper:** https://arxiv.org/abs/2607.21553
- **Project:** https://nvlabs.github.io/Sana/Video2/
- **Facts:** 5B/14B hybrid models; 75% linear attention; author-reported five-second 720p generation in 13.06 seconds on one H100; claimed 120× speed over Wan comparison.
- **Availability:** Paper/project code; new weights absent during scan.
- **Caveat:** Author-run metrics, H100 hardware, no independent replication.

## 9. ShotPlan

- **Date:** July 20
- **Paper:** https://arxiv.org/abs/2607.17675
- **Code/weights:** https://github.com/Pensioner-11/ShotPlan
- **Facts:** Planning tokens direct hard cuts, soft transitions, and local camera movement; authors report hard-cut timing error below one frame.
- **Availability:** Apache-2.0 code/weights; public data research-only.
- **Caveat:** Five-second training clips, full 14B fine-tune, author evaluation, dataset-size discrepancy between paper and repository.

## 10. Runway AI Media Report

- **Date:** July 20
- **Primary:** https://runway.com/news/company-news/ai-media-report
- **Claims:** large reported cost reductions, 800–1,000 ads from a five-person team, 46,000 saved hours, approximately 8,000 property videos, 210 products/day.
- **Caveat:** Customer-reported, anonymized, self-selected, unaudited, and lacking definitions, controls, failure rates, or full methodology.
- **Use:** Supporting adoption signal only, never independent proof.

## 11. Luma AMD/TensorWave inference migration

- **Date:** July 22
- **Primary:** https://lumalabs.ai/news/luma-runs-production-inference-on-amd-and-tensorwave
- **Facts:** Thousands of MI325X GPUs serve Ray3.2, Uni-1, and Luma Agents; Luma reports rapid migration with small engineering teams.
- **Caveat:** No independent performance audit or throughput/cost/power comparison.
- **Why it matters:** Production video inference is becoming less tied to one accelerator vendor.

## 12. Fusion Embedding

- **Date:** July 21
- **Paper:** https://arxiv.org/abs/2607.18666
- **Code:** https://github.com/Eximius-Labs/fusion-embedding
- **Facts:** Adds audio to a frozen visual/text embedding model using small connectors/adapters.
- **Availability:** Preview weights; Apache-2.0 code and non-commercial preview weights.
- **Why it matters:** Unified archive search across transcripts, frames, footage, and sound.
- **Caveat:** Research preview, no independent replication.

## Exclusions

- Qwen3.8, Google Vids/Omni, Seedance 2.5, Meta Muse, and earlier Luma releases: repeats or outside the window.
- Wan-Streamer and ABot-World: first release dates outside the window.
- Resolve 21.0.3: maintenance release, not a new AI story.
- Premiere, After Effects, Frame.io, Avid, Veo/Flow: no qualifying in-window AI release.
- Kling MCP: insufficient official implementation documentation.
- Consumer/social-first or unsuitable creative stories.
- Fundraising-only announcements.

Content review: no sensitivity issues identified in the recommended stories.
