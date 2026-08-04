# Primary-Source AV AI Research — Week of July 31, 2026

Research window: July 25–31, 2026.

## 1. MiniMax H3

- **Date:** July 31
- **Primary:** https://www.minimax.io/blog/minimax-h3
- **API:** https://platform.minimaxi.com/docs/guides/video-generation?ready=6
- **Independent:** https://artificialanalysis.ai/video/leaderboard/video-editing
- **Capabilities:** Text/image/video/audio conditioning; reference generation; editing; motion transfer; 4–15 seconds; 768p or 2K; native stereo audio; up to 9 images, 3 videos, 3 audio clips, 12 files total.
- **Pricing:** CNY 0.80/sec at 2K, CNY 0.50/sec at 768p in China docs; global API tracked at $7.80/minute.
- **Independent snapshot:** 1,130 Elo ±6 from 8,208 editing samples; 1,239 Elo ±10 from 6,026 text-to-video samples.
- **Availability:** Hosted API live; weights promised but not released by July 31.
- **Limits:** Technical report pending; codec/frame rate unclear; provenance watermark optional and off by default; vendor notes visual-detail weaknesses.

## 2. Seedance 2.5 official rollout

- **Date:** July 31
- **Primary:** https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- **Capabilities:** Native 30-second audio-video; multiple extensions; up to 30 images, 10 videos, 10 audio references; timestamp, camera, green-screen, and reference editing; 3D blocking references.
- **Availability:** Jimeng AI and Doubao Pro; BytePlus API coming.
- **Unknown:** public API schema/model ID/price, resolution, frame rate, codec, bit depth, output watermark, independent benchmark.
- **Limits:** ByteDance names complex-motion plausibility and multi-subject stability.
- **Repeat:** Preview covered June 26; official rollout is the new event.

## 3. OpenAI GPT Transcribe and Live Transcribe

- **Date:** July 28
- **Primary:** https://developers.openai.com/cookbook/examples/migrating_from_whisper_to_gpt_transcribe
- **Models:** `gpt-transcribe` for completed/committed audio; `gpt-live-transcribe` for continuous low-latency audio.
- **Capabilities:** Context prompts, literal keyword hints, expected-language arrays, streamed file results, Realtime transport.
- **Pricing:** $0.0045/minute file/turn; $0.017/minute live.
- **Independent:** Artificial Analysis measured 3.3% WER versus 4.0% for GPT-4o Transcribe on its test.
- **Limits:** JSON only; no native SRT/VTT, word timestamps, English translation, or speaker diarization. Separate models remain necessary.

## 4. xAI Imagine Video 1.5 references update

- **Date:** July 31
- **Primary:** https://x.ai/news/grok-imagine-video-1-5-references
- **Capabilities:** Text-only generation, native 1080p, up to seven visual references, image-plus-voice reference.
- **Pricing/spec:** $0.08/output second; 1–15 seconds. Reference and editing modes limited to 720p.
- **Access:** Text/1080p broad; image/voice references staged to selected paid users and gated API.
- **Provenance:** Mandatory vendor watermark; no C2PA/SynthID found.
- **Limits:** No independent 1080p or identity/voice retention benchmark.

## 5. Luma Layers

- **Date:** July 29
- **Primary:** https://lumalabs.ai/news/introducing-layers
- **Capabilities:** Generate independently editable layers or decompose flat images into text/object/background/transparent elements; rearrange, reuse, localize, regenerate.
- **Pricing:** 75 credits at 1K; 150 credits at 2K; plans from $30/month.
- **Access:** Live in Luma Agents.
- **Limits:** No stated PSD/interchange format; preservation/decomposition claims vendor-only.

## 6. Google Lyria 3.5

- **Date:** July 29
- **Primary:** https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/
- **Capabilities:** Better musical structure, lyric adherence, pronunciation, vocal expression, tempo/duration control; up to three-minute requested length.
- **Access:** Google Flow Music; no weights or public API announced.
- **Provenance:** SynthID watermark.
- **Independent:** Hands-on testing found M4A/MP3/WAV output plus some pronunciation and download failures.
- **Limits:** No blind listening benchmark or published licensed-corpus inventory.

## 7. OpenAI SynthID audio and verification API

- **Date:** July 31
- **Primary:** https://openai.com/index/advancing-content-provenance/
- **Capabilities:** SynthID in supported generated audio; web verifier and content-provenance API for images/audio.
- **Audio formats:** MP3, Opus, AAC, FLAC, WAV, PCM; 50MiB and 60-second check limit.
- **Limits:** OpenAI signals only; non-detection does not prove human origin; compression/editing can weaken signals; checks not Zero Data Retention eligible.

## 8. AutoCut Angles

- **Date:** July 29
- **Primary:** https://www.autocut.com/en/blogs/july-autocut-updates-2026/
- **Capabilities:** Builds an editable switching sequence from supplied camera tracks and one audio track for single-speaker footage.
- **Hosts:** Premiere 2023–2026 and Resolve 18.6+, free and Studio.
- **Pricing:** $9.90/month, $19.80/month, team tier around $19.90; 14-day trial.
- **Limits:** Single-speaker workflow; not speaker-directed multicam; model/training/provenance undisclosed.

## 9. ElevenLabs Character Casting

- **Date:** July 30
- **Primary:** https://elevenlabs.io/blog/introducing-character-casting-in-audiobooks
- **Capabilities:** Detect manuscript characters, suggest voices, preview real dialogue, replace globally, prefill pronunciations, control breaks.
- **Scale:** 90+ languages, 10,000+ voices.
- **Rights:** Paid commercial use; free non-commercial; professional clones limited to verified account-holder voice.
- **Limits:** No independent detection/casting/cleanup/language test; no flat feature price.

## 10. Grok Voice Think Fast 2.0

- **Date:** July 29
- **Primary:** https://x.ai/news/grok-voice-think-fast-2
- **Price:** $0.08/audio minute.
- **Independent snapshot:** 82.9% overall, 56.5% agentic, 0.70s first audio.
- **Capabilities:** Speech-to-speech, transcription, turn-taking, reasoning, tools.
- **Limits:** Vendor multilingual comparisons and operational A/B claims lack full methodology; no provenance mechanism disclosed.

## 11. Kimi K3 weights

- **Date:** July 27
- **Primary:** https://huggingface.co/moonshotai/Kimi-K3
- **Release:** Approximately 1.56TB MXFP4 weights, code, report, custom Kimi license.
- **Architecture:** 2.8T total, 104B active, 1,048,576 context.
- **License:** Separate agreement for large model-as-a-service operators; attribution conditions for very large products.
- **Limits:** Specialized multi-GPU deployment; model card modality table conflicts with README’s video-understanding claim.
- **Repeat:** Actual weight release is new after July 17 launch coverage.

## 12. C2PA guidance for AI-modified media

- **Date:** July 30
- **Primary:** https://c2pa.org/wp-content/uploads/sites/33/2026/07/Use-of-Content-Credentials-to-Identify-Synthetic-and-Non-Synthetic-Content.pdf
- **Scope:** Maps generated and AI-modified workflows to source types, actions, disclosure fields, Regions of Interest, prompts, and reference ingredients.
- **Limits:** Guidance, not normative requirement; records signed claims but does not detect or prove truth.

## 13. Pangram Image research preview

- **Date:** July 29
- **Primary:** https://www.pangram.com/blog/introducing-pangram-image-detection
- **Access:** Web preview; invitation API; 3 free scans/day; JPG/PNG/WebP, 512×512 minimum, 30MB max.
- **Claims:** 99.5% internal accuracy, >99% AUROC on several datasets, 0.16% false positives on pre-2022 images.
- **Limits:** Vendor-run measurements; limited hands-on found a miss; deepfakes/face swaps out of scope; statistical detection, not provenance.

## 14. Qwen-Audio-3.0-Gen-Preview

- **Date:** July 30
- **Paper:** https://arxiv.org/abs/2607.27011
- **Claim:** One non-autoregressive path for dialogue, ambience, localized effects, and longer mixed audio at 48kHz stereo.
- **Availability:** Paper only; no weights, API, demo, price, license, or parameter count.
- **Limits:** Author-run in-house benchmarks; no independent replication.

## 15. Valiant Finance audio-production case

- **Date:** July 29
- **Primary:** https://elevenlabs.io/blog/valiant-finance
- **Claims:** 10 radio-ad variants across two campaigns in one week versus a prior month-long cycle; other contact-center metrics.
- **Evidence:** Vendor-hosted customer story, early-stage and unaudited.
- **Use:** Adoption signal, not independent proof.

## Exclusions

- FLUX 3: no qualifying public API, price, weights, or independent test; temporary partner preview only.
- Kling: no official in-window model launch.
- Veo/Flow video/Vids: no qualifying video release.
- Runway Router, Qwen Image 3.0, Qwen-Audio TTS, Sonilo SFX, ElevenMusic controls: covered July 24 without material new event.
- MiniMax H3 weights shipped August 3, after cutoff.
- Adobe/Avid: no qualifying AI release.
- Resolve 21.0.3: maintenance, not a new AI story.
- Consumer/social-first, fundraising-only, union, provocative political, or unsuitable entertainment stories.

Content review: no sensitivity issues in recommended stories.
