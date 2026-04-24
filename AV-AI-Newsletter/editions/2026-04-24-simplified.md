# The AVS AI Dispatch — Week of April 24, 2026

> Quick Summary: OpenAI shipped two step-change products in 48 hours — **GPT-5.5**, a new top-of-the-benchmarks AI model, and **ChatGPT Images 2.0**, which opened the largest launch-day lead in AI image-generation history. Kling's video AI now outputs 4K directly with no upscaling. Blackmagic released **DaVinci Resolve 21** with over a dozen new AI tools including voice cloning, age/de-age, and searchable clip libraries. **NAB 2026** confirmed that every major editing app — Premiere, Avid, Resolve — is now AI-native. And Chinese lab DeepSeek matched GPT-5.5 on benchmarks at 86% lower cost just nine hours after OpenAI's announcement.

---

## The Big Stories This Week

### OpenAI Ships GPT-5.5 — The Biggest Single Jump Since GPT-4.5

OpenAI released **GPT-5.5** on April 23, the first fully retrained base model since GPT-4.5 — not an incremental update. The benchmark gains are substantial: it tops the Artificial Analysis Intelligence Index, scores 82.7% on Terminal-Bench 2.0 (up from 75.1% on GPT-5.4), and handles a 922,000-token context window at the same per-token speed as the previous model.

Two data points that stand out from the pre-release period:

- NVIDIA rolled Codex (powered by GPT-5.5) to more than **10,000 engineers internally** and reports that debugging cycles compressed from days to hours.
- OpenAI says the model can run **independently for more than seven hours** on complex coding tasks without losing the thread.

**Pricing doubled** to $5 per million input tokens and $30 per million output. A new GPT-5.5 Pro tier is available for harder reasoning work. Available now to Plus, Pro, Business, and Enterprise subscribers in ChatGPT and Codex; API access coming soon.

Community reception has been mixed — developers call it "completely cracked" for coding, while heavy users burned through their weekly session limits in 15 minutes of agentic use. Claude Opus 4.7 still leads on one major benchmark (SWE-Bench Pro), and the restricted Claude Mythos Preview leads on several others.

### ChatGPT Images 2.0 Posts the Biggest Launch-Day Lead in Image AI History

On April 21 — two days before GPT-5.5 — OpenAI shipped **ChatGPT Images 2.0**, the successor to GPT-image-1.5. The model is now standalone rather than a subsystem of GPT-4o, and it posted a result that required reading twice to believe: on the Arena.ai text-to-image leaderboard, it scored **1,512 — 241 points above the second-place model** (Google's Nano Banana Pro). For context, the entire previous top-15 spanned roughly 130 points. This is the largest launch-day lead any image model has ever held in Arena's history.

![Arena.ai Text-to-Image leaderboard at launch — GPT Image 2 scores 1,512, 241 points above Nano Banana 2 in second place. The rest of the top 15 are clustered within roughly 130 points of each other.](/editions/2026-04-24/arena-leaderboard.png)

What actually changed:

- **Text rendering jumped from ~90–95% to 99%+ accuracy**, across dozens of languages including Chinese, Japanese, Korean, Hindi, and Bengali. The long-standing weakness around menus, signs, infographics, and UI mockups is effectively solved.
- The model now **reasons before rendering** — planning composition, resolving spatial relationships, and interpreting complex multi-part instructions.
- **Up to 8 consistent images per prompt**, aspect ratios from 3:1 to 1:3, native 2K with experimental 4K.
- Free-tier access for every ChatGPT user in Instant mode; Thinking mode (with web search and verification) for paid tiers.

**Limitations matter**: no transparent PNG output, generation is slow (15–60 seconds per image), brand logo reproduction is still unreliable, and the artistic style range is narrower than Midjourney for abstract or painterly work.

Designer reception was unusual for its consistency — poster and flyer designers are saying text-in-image is finally production-ready, and several reported skipping Photoshop for first-pass marketing assets.

### Kling Video 3.0 Adds Native 4K Direct Output

Kuaishou's Kling AI announced on April 23 that its Video 3.0 series now supports **native 4K direct output** — generating at full 4K resolution rather than upscaling from lower-res. The company is marketing this as the first video model to deliver native 4K without post-processing, targeting film, advertising, and professional production work.

This sits on top of Kling 3.0's existing capabilities — 15-second clips, multi-shot sequencing, native audio across multiple languages, and one unified pipeline for text-to-video, image-to-video, reference-to-video, and in-video editing. Kling 3.0 and Kling 3.0 Omni were also added to **Adobe Firefly's model roster** during NAB week.

Kuaishou posted a [4K native-output reel on YouTube](https://www.youtube.com/watch?v=I7tMTopo6xk) alongside the announcement. Worth a look less for the question of whether Kling specifically becomes the best video generation model, and more for what it signals about where the whole category is converging on image quality and motion coherence. If this is now the floor, it resets expectations for what **Veo 4** (expected at Google I/O on May 19–20) and the next Sora-successor will need to clear.

### DaVinci Resolve 21 Lands With a Full AI Toolkit

Blackmagic Design released the **public beta of DaVinci Resolve 21** on April 13 — over 100 new features in a single release. The AI additions alone close most of the gap that had opened up against Premiere on AI tooling:

- **AI IntelliSearch** — natural-language search in the Media Pool by object, face, or dialogue keyword
- **AI CineFocus** — synthetic depth-of-field after the fact, with keyframeable rack focus and selectable bokeh
- **AI Face Age Transformer** — age or de-age a tracked subject
- **AI Face Reshaper** — adjust facial features on moving subjects
- **AI Blemish Removal** — skin retouching that preserves texture
- **AI Slate ID** — automatic metadata extraction from clapperboards, even dark or out-of-focus
- **AI UltraSharpen** and **AI Motion Deblur** — rescue soft or motion-blurred footage
- **AI Speech Generator** — voice cloning from just 10 seconds of source audio

There's also a brand-new **Photo page** that brings DaVinci's full color grading stack to still photography, with tethered shooting support for Sony and Canon. The public beta is free.

### NAB 2026 Confirmed Every Major NLE Is Now AI-Native

NAB Show 2026 (April 18–22 in Las Vegas) surfaced the clearest signal yet that the era of "AI as an NLE plugin" is over — it's now part of the base product:

- **Avid × Google Cloud** announced a multi-year partnership embedding Gemini and Vertex AI directly into Media Composer. Editors can query footage using natural language ("find the emotional moment when the lead character reacts"), auto-generate B-roll, and automate metadata logging. Avid Content Core — their new cloud-native media data layer — reached general availability and won the NAB Product of the Year in Media Supply Chain.
- **Adobe** debuted **Premiere Color Mode** (editor-first color grading, won Product of the Year in Graphics/VFX), **AI Object Matte** in After Effects (roto work in minutes instead of hours), **Frame.io Drive** (mount cloud projects like local drives), and previewed the **Firefly AI Assistant** — an agentic layer that orchestrates work across Premiere, Photoshop, Lightroom, and the rest of Creative Cloud from a single conversational interface. Adobe confirmed the assistant will extend to Anthropic's Claude and other third-party models.
- **DaVinci Resolve 21** (above) is the third major NLE to go AI-native this month.
- **TwelveLabs** showed Pegasus 1.5, a video intelligence model that extracts structured metadata against a customer-defined schema and outperforms Gemini 2.5 Pro by 30% on segmentation quality. Already in production with one major broadcast network.
- **Amplify's KAI** is an AI story-building panel inside Premiere — editors search footage by story beats and moments rather than by filename.
- **MediaPET 2.1** launched a fully agentic video system where you direct the project conversationally from your phone rather than working clip-by-clip in a timeline.

### DeepSeek V4 Matches GPT-5.5 at 86% Lower Cost — Nine Hours Later

Roughly nine hours after OpenAI announced GPT-5.5, Chinese AI lab **DeepSeek** released **V4**, a fully open-source model with a 1-million-token context window that matches or exceeds GPT-5.5 on several benchmarks — at approximately 86% lower cost. This is now the third time in eighteen months that DeepSeek has released a frontier-competitive open model within days of a flagship US launch. The practical implication: whatever advantage a new proprietary model has at launch is now measured in days, not months.

---

## Why This Week Matters

A few patterns worth noting:

- **"Agentic AI" is now the default frame.** Every major launch this week — GPT-5.5, Firefly AI Assistant, Avid × Gemini, MediaPET 2.1, Amplify KAI — led with the word "agentic." What that actually means varies, but the marketing category is converging faster than the technology. The gap between "demo that runs agentically" and "agent that works reliably in production" is still the biggest risk.

- **Text-in-image is effectively solved.** ChatGPT Images 2.0 at 99%+ accuracy, along with Flux 2 and Nano Banana Pro scoring in the 80s and 90s, closes a three-year-old weakness. The practical consequence: designers asking an AI for mocked-up posters, menus, signage, or infographics now get something usable on the first pass rather than a placeholder that has to be rebuilt with correct text composited on top.

- **Every major NLE is now AI-native.** Premiere, Avid Media Composer, and DaVinci Resolve all shipped significant AI feature drops in a 30-day window. If you've been waiting for AI to be part of your editing tool rather than a separate workflow, that happened this month.

- **Proprietary model leads are measured in days.** GPT-5.5 held the top spot on the main intelligence leaderboard for roughly nine hours before DeepSeek V4 matched it at 86% lower cost. ChatGPT Images 2.0 opened a 241-point lead on April 21; the assumption inside the industry is that Nano Banana Pro 2 is weeks away, not months.

- **The timeline itself is being argued against.** MediaPET, Amplify KAI, and the Firefly AI Assistant all argue — from different angles — that clip-by-clip editing is a legacy interface and conversational project direction is the next mental model. Whether any of them prove out at feature-length production scale is an open question, but three independent companies arguing the same thesis in one month is a signal worth tracking.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. This is the quick summary — the full edition has the complete technical breakdown and sources. Curated with AI assistance. Questions or suggestions? Reply to this message.*
