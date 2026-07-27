# The AVS AI Dispatch — Week of July 24, 2026

> **FLUX 3 proposes one backbone for image, video, audio, and action, but its ambition is ahead of its current access and evidence.** Video and Action are gated, Image and developer access are still coming, and basic production specifications remain unpublished. Qwen added directed voice and structured-image systems, Runway launched model routing, Sonilo tied effects to picture timing, and ElevenMusic expanded reference-driven control.

---

## The Big Story

### FLUX 3: One Backbone, Narrow Current Access

FLUX 3 was announced on July 23 as a jointly trained backbone across image, video, and audio, extended toward action prediction. The goal is one learned foundation that can generate and revise still images, motion, sound, and actions.

Only part of that plan is available:

- **Video:** gated early access
- **Action:** gated early access for selected research and commercial partners
- **Image:** promised in the following weeks
- **API access and private weights:** planned for later, with no public dates
- **FLUX 3 Dev open weights:** planned for later in 2026, with no published license

FLUX 3 Video can generate up to **20 seconds** with native audio. It accepts text, images, video, and keyframes and supports text-to-video, image-to-video, video-to-video, keyframe transitions, and continuation of both video and audio.

The developer also claims multilingual dialogue, typography, animated design, and chaining across multiple shots. The announced scope therefore extends beyond a single silent clip toward a sequence in which picture and sound remain connected.

The preliminary comparisons need careful qualification. They used **early-checkpoint 10-second, 720p clips with audio**. FLUX 3 was preferred over Luma Ray 3.2 in **93%** of comparisons, Runway Gen-4.5 in **77%**, Grok Imagine Video in **69%**, Kling v3 Pro in **60%**, Happy Horse v1 in **59%**, Happy Horse 1.1 in **57%**, and Seedance 2.0 and Gemini Omni Flash in **52%** each.

No sample size, prompt set, rater details, confidence intervals, randomization procedure, or separate picture and audio scores were published. A **52% result may be a tie**, and there is no published evidence that the tested checkpoint matches the gated system.

There is also **no public pricing, license, parameter count, hardware profile, service-level agreement, maximum resolution, output-format specification, reference limit, or independent hands-on test**.

The important story is the gap: FLUX 3 describes one image, video, audio, and action production layer, while current access, specifications, and evidence cover only a narrow part of that ambition.

**Source:** [FLUX 3 developer announcement](https://bfl.ai/blog/flux-3) · [Independent launch reporting](https://venturebeat.com/technology/black-forest-labs-launches-flux-3-capable-of-generating-images-and-20-second-video-with-audio-but-in-limited-release-to-start) · July 23, 2026

---

## Other Stories

### Qwen-Audio-3.0

Qwen-Audio-3.0-TTS launched in Flash and Plus variants. Flash targets lower latency; Plus prioritizes quality.

The hosted service supports:

- **16 languages**
- Natural-language delivery direction
- Inline nonverbal tags
- Voice cloning from imperfect references
- Up to **three minutes per pass**

An independent leaderboard snapshot placed Plus at **1,234 Elo ±16 from 1,517 samples**, effectively tied with Simba 3.2 in that evaluation. The result does not cover every language or production setting.

Access is through the hosted Model Studio API; no weights were released. Full language coverage and 48kHz support were still rolling out.

**Source:** [Qwen announcement](https://www.alibabacloud.com/blog/qwen-audio-3-0-tts-more-multilingual-easier-to-direct_603379) · July 21 · [Independent leaderboard](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice) · accessed July 27

### Runway Media Router

Runway Media Router selects an image, video, or audio model according to one preference: **cost, latency, or quality**.

Configurations can include model allowlists or denylists, credit ceilings, fixed configuration IDs, version history, realized costs, and dry runs. There is no routing surcharge; the selected model’s rate applies.

The quality scores and selection method are internal. Reproducibility still depends on recording the selected model, router version, and active policy.

**Source:** [Runway announcement](https://runwayml.com/news/company-news/introducing-runway-media-router) · [Documentation](https://docs.dev.runwayml.com/model-routers/configuration/) · [Independent reporting](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/) · July 23

### Sonilo Sound Effects 1.0

Sonilo generates a synchronized sound-effects track from up to **three minutes of video**, using picture as the event and timing guide. An optional prompt adds direction. A separate text mode generates **one to 180 seconds** of sound.

Output formats are AAC, MP3, WAV, and FLAC. Pricing is **$0.009 per second** for video-conditioned generation and **$0.0018 per second** for text-only generation.

The launch calls the model 1.0 while current endpoints use v1.1. No independent synchronization benchmark or published methodology was available.

**Source:** [Launch announcement](https://www.prnewswire.com/news-releases/sonilo-and-fal-launch-sound-effects-1-0-for-realistic-sound-effects-from-video-and-text-302830490.html) · [API documentation](https://fal.ai/models/sonilo/v1.1/video-to-sound-effects/llms.txt) · July 21

### Qwen-Image-3.0

Qwen-Image-3.0 targets structured material as well as standalone images. The developer claims:

- Prompts up to **4,500 tokens**
- Text down to **10 pixels**
- **12 languages**
- Dense multi-panel layouts, formulas, and user-interface mockups
- Editing and optional retrieval

The model is available in Qwen Chat, while API access remained limited or trial-based. No public weights, parameter count, license, model card, blind benchmark, latency profile, or stable API contract accompanied the examples.

**Source:** [Qwen announcement](https://www.alibabacloud.com/blog/qwen-image-3-0-rich-content-authentic-details-deep-knowledge_603385) · [Independent launch reporting](https://decrypt.co/374084/alibaba-qwen-image-3-ai-useful-not-just-pretty) · July 21–22

### ElevenMusic References, Vocals, and Finetunes

**References** uses **10 seconds to five minutes** of audio to guide style, instrumentation, and feel. **Vocals** creates a reusable singing identity from supplied recordings or uses a voice from the service’s library.

**Finetunes** creates a private style model. Current documentation allows up to **50 tracks**, each 10 seconds to 10 minutes long, with 250 minutes of total audio.

The developer says uploads are checked for recorded matches. That screening is a vendor safeguard, not proof of ownership or performer consent.

**Source:** [References announcement](https://elevenlabs.io/blog/introducing-references-sound-control-for-music-v2) · [Vocals announcement](https://elevenlabs.io/blog/introducing-vocals-a-consistent-voice-for-your-elevenmusic-songs) · [Finetunes documentation](https://elevenlabs.io/docs/eleven-creative/products/music/finetunes.mdx) · July 22–23

---

## Quick Hits

- **Cosmos3-Super Image2Video 4Step** is a 64-billion-parameter open-weight model. An independent snapshot placed it around **1,271 Elo** at the top of the filtered open-weight image-to-video list without audio. Its acceleration claim is vendor-measured, and published testing centers on data-center or professional GPUs. [Model](https://huggingface.co/nvidia/Cosmos3-Super-Image2Video-4Step) · [Leaderboard](https://artificialanalysis.ai/video/leaderboard/image-to-video?audio-output=false&open-weights=true) · July 20
- **SANA-Video 2.0** reports five seconds of 720p video in 13.06 seconds on one H100. The comparison is author-run, has no independent replication, and the new weights were not available during the scan. [Paper](https://arxiv.org/abs/2607.21553) · [Project](https://nvlabs.github.io/Sana/Video2/) · July 23–24
- **ShotPlan** uses planning tokens for hard cuts, soft transitions, and local camera movement. The authors report hard-cut timing error below one frame; the evaluation has not been independently replicated. [Paper](https://arxiv.org/abs/2607.17675) · [Repository](https://github.com/Pensioner-11/ShotPlan) · July 20
- **Luma moved production inference to AMD and TensorWave infrastructure.** The company says thousands of MI325X GPUs now serve its products. No independent throughput, cost, power, or quality audit was published. [Source](https://lumalabs.ai/news/luma-runs-production-inference-on-amd-and-tensorwave) · July 22
- **Gemini Flash variants** target agent execution, throughput, and security. Their AV relevance is in multimodal understanding, logging, metadata, quality checks, and production-system operation—not native media generation. Access differs by variant. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) · July 21
- **Runway’s AI Media Report** cites 800–1,000 ads from a five-person team, 46,000 saved hours, approximately 8,000 property videos, and 210 products per day. These are anonymized, self-selected, unaudited customer claims without shared definitions, controls, failure rates, or full methodology. [Source](https://runway.com/news/company-news/ai-media-report) · July 20

---

## Voices This Week

- **Eiso Kant** said persistence, verification, backtracking, and avoiding premature completion may matter more to practical system gains than model scale alone. He kept people responsible for ideas and debugging. This is practitioner interpretation, not a controlled media study. [July 23 discussion](https://www.latent.space/p/poolside)
- **Chris Benson** observed that machine-facing agent connections make identity, permissions, resource controls, and recovery part of the product. The point applies to media systems that connect scheduling, assets, rendering, quality checks, and publishing without a person navigating every screen. [July 23 discussion](https://practicalai.show/365)
- **Brooks Jensen** described AI authorship as a set of choices about source material, generation, enhancement, editing, and human decisions—not one universal boundary. His comments are philosophical, not legal analysis. [July 20 discussion](https://www.lenswork.com/indexhome.html)
- **Tony Doe** noted that open RSS feeds make media easy to distribute and discover, while also making automated retrieval easier. Public accessibility does not settle training permission, licensing, consent, or ownership. [July 22 discussion](https://rss.com/podcasts/into-the-podverse-innovation-challenges-opportunities/3012821/)

---

## Common Threads

### One Model Is Absorbing More Modalities

FLUX 3 joins picture, motion, sound, and action in one architectural claim. Qwen’s coordinated audio and image launches cover adjacent parts of the same production sequence. One architecture does not guarantee equal quality in every mode.

### References and Revision Are Replacing One-Shot Prompting

FLUX 3 uses images, video, and keyframes. ElevenMusic uses reference recordings, reusable vocals, and finetunes. Qwen-Image-3.0 and ShotPlan add more defined structure and correction.

### Routing Is Moving Behind Infrastructure

Runway turns model selection into a cost, latency, or quality policy. Luma’s migration shows that accelerator choice can also change underneath a stable service.

### Audio Is Becoming Picture-Aware and Controllable

FLUX 3 joins native audio to video, Sonilo derives timing from picture, Qwen-Audio directs speech delivery, and ElevenMusic carries reference-based identity.

### Release Pace Is Outrunning Evidence

FLUX 3, Qwen-Image-3.0, SANA-Video 2.0, and ShotPlan all arrived with meaningful claims and incomplete independent evaluation. Availability status and evidence type are becoming as important as the feature list.

### Accessibility Does Not Settle Rights or Provenance

Upload screening does not prove permission. Public feeds do not grant training rights. Router provenance still depends on recording which model handled an asset.

**Source basis:** [FLUX 3](https://bfl.ai/blog/flux-3) · [Runway Media Router](https://runwayml.com/news/company-news/introducing-runway-media-router) · [Sonilo](https://www.prnewswire.com/news-releases/sonilo-and-fal-launch-sound-effects-1-0-for-realistic-sound-effects-from-video-and-text-302830490.html) · [ElevenMusic References](https://elevenlabs.io/blog/introducing-references-sound-control-for-music-v2) · [Tony Doe discussion](https://rss.com/podcasts/into-the-podverse-innovation-challenges-opportunities/3012821/)

---

## Novel Ideas Worth Watching

- **A multimodal backbone as a production layer:** FLUX 3’s larger claim is that stills, motion, sound, and actions can share context across more of a production sequence. Current access does not yet demonstrate the complete claim. [Source](https://bfl.ai/blog/flux-3)
- **Video as sound timing:** Sonilo treats visible events and edit timing as the foundation for generated effects, with text as added direction. [Source](https://www.prnewswire.com/news-releases/sonilo-and-fal-launch-sound-effects-1-0-for-realistic-sound-effects-from-video-and-text-302830490.html)
- **Model routing as editorial policy:** different routing rules can represent the priorities of a preview, review copy, or final. A model-and-version record remains necessary. [Source](https://docs.dev.runwayml.com/model-routers/configuration/)
- **Verification over raw scale:** Eiso Kant’s emphasis on persistence, checking, and backtracking suggests that dependable completion behavior may matter more than a larger model that stops at a plausible first answer. This remains a practitioner hypothesis. [Source](https://www.latent.space/p/poolside)

---

## Tip of the Week

### Back to Basics, Week 9: Turn Recurring Review Criteria Into a Reusable Checklist

Move repeated review criteria out of memory and into one reusable checklist.

1. Gather the checks that recur across captions, edit notes, metadata, graphics, equipment briefs, and delivery records.
2. Write each check as a yes-or-no question.
3. Add a field for evidence: source link, file location, timecode, or specification.
4. Label vendor, author, customer, and independent evidence correctly.
5. Record missing inputs, uncertain rights, and absent approvals as open findings.
6. Save a baseline version and add project-specific checks without removing the core list.

A compact checklist can cover:

- Facts, names, dates, numbers, timecodes, and links
- Required wording, dimensions, channels, file names, and sections
- Unknowns, unavailable features, and evidence limits
- Audience fit, rights, consent, provenance, and human approval

The result is a visible review record rather than a pass based on memory.

Next week, Back to Basics Week 10: **Test the checklist against a finished task.**

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
