# The AVS AI Dispatch — Week of July 31, 2026

> **MiniMax H3 and Seedance 2.5 launched on July 31 with different strengths and different evidence.** H3 had a live hosted API, pricing, documented limits, and independent preference snapshots. Seedance offered 30-second audio-video generation and up to 50 references, but its API, price, output specifications, watermark details, and independent evaluation were still unavailable.

---

## The Big Story

### MiniMax H3 vs. Seedance 2.5

Both new models combine video, audio, references, and editing. The important difference at launch was what could be measured.

#### MiniMax H3

H3 generates **4–15 seconds** of video at **768p or 2K** with native stereo audio. It accepts text, images, video, and audio as context and supports generation, editing, reference control, and motion transfer.

The category limits are below, subject to a **12-file overall cap**:

- Up to **nine images**
- Up to **three video clips**
- Up to **three audio files**

The hosted API was live. China pricing was **CNY 0.80 per second at 2K** and **CNY 0.50 per second at 768p**.

Artificial Analysis recorded two independent preference snapshots:

- **Video editing:** **1,130 Elo ±6 from 8,208 samples**
- **Text-to-video:** **1,239 Elo ±10 from 6,026 samples**

These are blind-preference results, not tests of reliability, rights, consistency, or total workflow cost.

H3’s promised downloadable weights had **not shipped by the July 31 cutoff**. Its technical report was pending, frame rate and codec were unclear, and its optional provenance watermark was off by default.

#### Seedance 2.5

Seedance 2.5 officially rolled out with **30-second audio-video generation**, multi-round extensions, and up to:

- **30 images**
- **10 video clips**
- **10 audio clips**

It also includes timestamp revision, camera changes, green-screen and reference editing, and textureless 3D blocking references for composition, poses, motion paths, and camera angles.

Initial access was through **Jimeng AI and Doubao Pro**. A BytePlus API was coming later.

At launch, there was no public API schema or model identifier, price, resolution, frame rate, codec, bit depth, watermark specification, or independent Seedance 2.5 benchmark. ByteDance also notes continuing limits with complex motion and multiple subjects.

H3 therefore had stronger launch evidence for access, price, limits, and independent preference. Seedance presented a longer format and broader reference system, but more of its case remained vendor-demonstrated.

**Sources:** [H3 announcement](https://www.minimax.io/blog/minimax-h3) · [H3 API documentation](https://platform.minimaxi.com/docs/guides/video-generation?ready=6) · [Independent editing snapshot](https://artificialanalysis.ai/video/leaderboard/video-editing) · [Independent text-to-video snapshot](https://artificialanalysis.ai/video/leaderboard/text-to-video) · [Seedance 2.5 announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) · July 31

---

## Other Stories

### OpenAI GPT Transcribe and Live Transcribe

OpenAI split transcription into two models:

- **GPT Transcribe:** completed or committed audio at **$0.0045 per minute**
- **GPT Live Transcribe:** continuous low-latency audio at **$0.017 per minute**

Both support context prompts, literal keyword hints, and expected-language arrays. An independent evaluation measured GPT Transcribe at **3.3% word error rate**, compared with **4.0%** for GPT-4o Transcribe.

Output is JSON only. The models do not provide native SRT or VTT captions, word-level timestamps, English translation, or speaker diarization, so those jobs still require separate processing or models.

**Sources:** [OpenAI migration guide](https://developers.openai.com/cookbook/examples/migrating_from_whisper_to_gpt_transcribe) · [Independent evaluation](https://artificialanalysis.ai/speech-to-text/models/openai-gpt-transcribe) · July 28–29

### xAI Imagine Video 1.5 References

xAI added native **1080p** text generation, up to **seven visual references**, and an image-plus-voice reference mode. Clips run **1–15 seconds** at **$0.08 per output second**.

Text and 1080p access were broad, while image and voice references were staged for selected paid users and gated API access. Reference and editing modes remained limited to **720p**.

Outputs carry a mandatory vendor watermark. No independent test of the new 1080p, identity-retention, or voice-retention features was available.

**Source:** [xAI update](https://x.ai/news/grok-imagine-video-1-5-references) · July 31 · vendor announcement

### Luma Layers

Luma Layers can generate independently editable image components or decompose a flat image into text, objects, backgrounds, and transparent elements. Those parts can be rearranged, reused, localized, or regenerated.

The feature was live in Luma Agents at **75 credits for 1K** and **150 credits for 2K**, with plans starting at **$30 per month**.

No PSD or other interchange format was specified, and no independent decomposition test was published.

**Source:** [Luma Layers announcement](https://lumalabs.ai/news/introducing-layers) · July 29 · vendor announcement

### Google Lyria 3.5

Lyria 3.5 launched in Flow Music with vendor-reported improvements in musical structure, lyrics, pronunciation, vocal expression, tempo, and requested duration. It can target tracks of up to **three minutes**.

Generated audio includes a **SynthID watermark**. No downloadable weights or public Lyria 3.5 API model identifier were announced, and no blind independent listening benchmark was available.

**Sources:** [Google announcement](https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/) · [Model card](https://deepmind.google/models/model-cards/lyria-3-5/) · July 29 · vendor and model-author evidence

### OpenAI Audio Provenance

OpenAI added SynthID watermarks to supported generated audio and expanded its verifier and Content Provenance API to check audio.

The API accepts MP3, Opus, AAC, FLAC, WAV, and PCM, with a **50 MiB** limit and a **60-second** decoded-duration limit. It checks supported OpenAI signals only.

A non-detected result does not prove human origin, and the check does not establish rights or ownership. Compression and editing can also weaken a watermark.

**Sources:** [OpenAI announcement](https://openai.com/index/advancing-content-provenance/) · [API guide](https://developers.openai.com/api/docs/guides/content-provenance) · July 31

---

## Quick Hits

- **AutoCut Angles** builds an editable switching sequence from supplied camera tracks and one audio track in Premiere or Resolve. It is for single-speaker footage, not speaker-directed multicamera switching. [Source](https://www.autocut.com/en/blogs/july-autocut-updates-2026/) · July 29
- **ElevenLabs Character Casting** detects manuscript characters, suggests voices, previews lines, and changes a selected voice across a project. The company lists more than 90 languages and more than 10,000 voices; no independent casting or cleanup test was published. [Source](https://elevenlabs.io/blog/introducing-character-casting-in-audiobooks) · July 30
- **Kimi K3 weights shipped** on July 27: approximately **1.56 TB** of MXFP4 weights, code, and a report for a **2.8-trillion-parameter model with 104 billion active parameters**. The custom license and specialized multi-GPU requirements still apply. [Source](https://huggingface.co/moonshotai/Kimi-K3)
- **C2PA guidance** maps generated, partially modified, and later human-edited media to source types, actions, disclosure fields, ingredients, and regions. It is guidance, not a new mandatory rule, and signed claims do not prove every assertion. [Source](https://c2pa.org/wp-content/uploads/sites/33/2026/07/Use-of-Content-Credentials-to-Identify-Synthetic-and-Non-Synthetic-Content.pdf) · July 30
- **Pangram Image** is a statistical detector preview. Pangram reports high internal accuracy, but the measurements are vendor-run and the detector cannot provide signed provenance. [Source](https://www.pangram.com/blog/introducing-pangram-image-detection) · July 29
- **Grok Voice Think Fast 2.0** costs **$0.08 per audio minute**. An independent snapshot recorded **82.9% overall**, **56.5% agentic performance**, and **0.70 seconds to first audio** under the tested conditions. [Announcement](https://x.ai/news/grok-voice-think-fast-2) · [Independent snapshot](https://artificialanalysis.ai/speech-to-speech) · July 29
- **Qwen-Audio-3.0-Gen-Preview** describes one research path for dialogue, ambience, localized effects, and longer mixed audio at **48 kHz stereo**. It remains paper-only, with author-run benchmarks and no weights, API, demo, price, license, or parameter count. [Paper](https://arxiv.org/abs/2607.27011) · July 30

---

## Voices This Week

- **Victor Riparbelli** described video that can answer, demonstrate, draw, and test comprehension. His company perspective treats video as a stateful application rather than only a rendered file. [July 28 discussion](https://aneyeonai.libsyn.com/video-is-about-to-stop-being-one-way-and-that-changes-everything-victor-riparbelli-synthesia)
- **Colin Smith** argued that easier tools do not create taste. Editing knowledge still helps correct a small defect instead of regenerating an entire result, while provenance may increase the need to demonstrate authentic capture. This is practitioner judgment. [July 30 discussion](https://shows.acast.com/camera-shake-photography-podcast/episodes/25-years-of-photoshop-the-skills-ai-cant-replace-with-colin)
- **Thais Castello Branco** separated objectively checkable quality from creative preference shaped by audience, brand, context, and taste. Her frame combines fixed checks with contextual human review. [July 31 discussion](https://www.youtube.com/watch?v=4x_gN7XMIcE)
- **Daniel Whitenack and Chris Benson** examined how tool access, credentials, package proxies, network policy, uploads, monitoring, and human approval combine into agent containment. One incident illustrates a failure mode but does not predict every agent. [July 30 discussion](https://share.transistor.fm/s/9d74230b)
- **Akshay Nathan** separated visible activity from meaningful progress and described how one agent foundation can support task-specific interfaces and sandboxes. **Nathaniel Whittemore** described models as routine drivers, specialists, sub-agents, or fallbacks rather than one winner for every task. [Akshay Nathan](https://www.latent.space/p/chatgpt-work) · [Nathaniel Whittemore](https://aidailybrief.ai/e/2026-07-27)

---

## Common Threads

### Video Models Are Becoming Audiovisual Editors

H3, Seedance, and xAI now compete on references, audio, revision, duration, and preservation—not only first-generation appearance.

### Evidence Levels Differ at Launch

A callable API, pricing, vendor demonstrations, and independent measurements answer different questions. “Available,” “documented,” “priced,” and “independently measured” are separate claims.

### Media Is Becoming an Interface

Interactive video can respond during a session. Luma Layers makes image parts addressable. Character Casting treats narration as a project-wide system of roles and voices. A deliverable may include state, tools, and permissions as well as an exported file.

### Provenance Starts at Intake

OpenAI verifies supported audio signals, C2PA can describe partial edits, and Pangram estimates image origin statistically. Detection, provenance, rights, and ownership remain different records.

### Judgment Becomes Scarcer

Faster generation increases the value of selection, audience fit, factual review, continuity, and approval. More output is not the same as more progress.

### Agents Need Contained Tools

Media agents can touch uploads, storage, codecs, rendering, publishing, and credentials. Human approval, network policy, tool boundaries, monitoring, and automated checks all remain part of the system.

**Source basis:** [H3](https://www.minimax.io/blog/minimax-h3) · [Seedance](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) · [Luma Layers](https://lumalabs.ai/news/introducing-layers) · [OpenAI provenance](https://openai.com/index/advancing-content-provenance/) · [C2PA](https://c2pa.org/wp-content/uploads/sites/33/2026/07/Use-of-Content-Credentials-to-Identify-Synthetic-and-Non-Synthetic-Content.pdf) · [Agent-containment discussion](https://share.transistor.fm/s/9d74230b)

---

## Novel Ideas Worth Watching

- **Interactive video as an application runtime:** a video that answers, demonstrates, draws, and checks understanding also needs state, permissions, logging, and recovery. [Source](https://aneyeonai.libsyn.com/video-is-about-to-stop-being-one-way-and-that-changes-everything-victor-riparbelli-synthesia)
- **Creative quality as conditional preference:** fixed checks can verify objective requirements, while audience, context, brand, and taste require qualified preference examples and review. [Source](https://www.youtube.com/watch?v=4x_gN7XMIcE)
- **Partial-edit provenance:** C2PA regions can associate a claim with one part or interval rather than labeling a complete asset uniformly. [Source](https://c2pa.org/wp-content/uploads/sites/33/2026/07/Use-of-Content-Credentials-to-Identify-Synthetic-and-Non-Synthetic-Content.pdf)
- **Trained weights as reusable assets:** downloadable weights can become production inputs under their license and hardware constraints, while broader weight-space methods remain early research. [Kimi K3 release example](https://huggingface.co/moonshotai/Kimi-K3)

---

## Tip of the Week

### Back to Basics, Week 10: Test the Checklist Against a Finished Task

Use one completed AV task to learn whether the Week 9 checklist catches real issues.

1. Choose a finished caption file, edit, graphic package, equipment brief, metadata set, or delivery record.
2. Run the checklist without changing the finished work.
3. Mark each check as pass, finding, unclear, or not applicable.
4. Compare the results with the task’s actual review history.
5. Record missed issues, false alarms, and criteria that require human judgment.
6. Revise and version the checklist so the change remains traceable.

A simple test record can use:

```text
Check | Result | Evidence | Checklist change
```

The test shows whether the checklist reflects real production work rather than only appearing complete on paper.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. Curated with AI assistance. Questions or suggestions? Reply to this message.*
