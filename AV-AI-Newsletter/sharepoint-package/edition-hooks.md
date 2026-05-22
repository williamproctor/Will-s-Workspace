# AVS AI Dispatch — Edition Hooks

Reference sheet of the **`Hook`** field for every published edition. Use these when entering rows into the SharePoint list manually, or when QA'ing what was imported via `samples/list-import-all-editions.csv`.

- **SharePoint field:** `Hook` — Multiple lines of text (plain text, 1 line shown)
- **Length guidance:** 1–3 sentences. No HTML. No line breaks.
- **Where it shows up:** archive tile preview + the featured "Latest" card on the homepage.

These are the same hooks shown on the public site's homepage card and archive list (`https://avaidispatch.com/`), so SharePoint and the public site stay in sync.

---

## 2026-05-22 — Week of May 22, 2026

> Google I/O 2026: Gemini Omni Flash ships a multimodal video model with conversational editing to the Gemini app, Flow, and free to YouTube Shorts. Gemini 3.5 Flash claims 4× speed and < ½ cost vs Claude Opus 4.7 and GPT-5.5. Flow becomes a creative copilot with Flow Agent and vibe-coded Flow Tools. Lyria 3 + Pro ship for developers. Karpathy joins Anthropic to accelerate pre-training research. OpenAI disproves an 80-year-old Erdős conjecture. Cannes 2026 wraps: AI "came out of the closet."

---

## 2026-05-15 — Week of May 15, 2026

> OpenAI ships three Realtime voice models — streaming transcription at $1.02/hour, live translation at $2.04/hour, and a GPT-5-class voice agent with parallel tool calling. Anthropic locks down 220K GPUs via SpaceX and doubles Claude Code rate limits. Cannes 2026 launches Human Provenance — the first open-license AI disclosure standard — while Soderbergh premieres an AI-assisted Lennon documentary. Krea 2 ships a style-first foundation image model. Flick raises $6M. Vertigo + Federation spin out amersia + Woven from "Critterz."

---

## 2026-05-08 — Week of May 8, 2026

> Cannes 2026 opens with the AI question split clean down the middle: AGC boards "Critterz" while the festival bans AI from Palme d'Or competition. OpenAI ships GPT-5.5 Instant as the new ChatGPT default with a 52.5% reduction in hallucinated claims. xAI's Grok 4.3 lands with strong agentic benchmarks at half the price. Topaz adds Hyperion 2 + a native Premiere panel. Twinnin raises $3M to license actor likenesses while YouTube's deepfake-detection rolls out to Hollywood.

---

## 2026-05-01 — Week of May 1, 2026

> Insta360 + Splatica's Project Eternal turns a 360 camera walk-through into a navigable Gaussian splat. Whittemore's Agent OS framework argues the model matters less than the personal infrastructure underneath it. Alibaba's HappyHorse 1.0 takes the #1 video model crown. ElevenLabs ships ElevenMusic with a style-royalty deal. Topaz rebuilds its stack. Anthropic ships persistent memory for Claude agents.

---

## 2026-04-24 — Week of April 24, 2026

> OpenAI ships GPT-5.5 and ChatGPT Images 2.0 in 48 hours — Images 2.0 opens the biggest Arena leaderboard lead in history. Kling adds native 4K output. DaVinci Resolve 21 lands with 10+ AI tools. NAB 2026 confirms every major NLE is now AI-native. DeepSeek V4 matches GPT-5.5 at 86% lower cost.

---

## 2026-04-17 — Week of April 17, 2026

> Anthropic ships Claude Opus 4.7 and narrowly retakes the LLM lead. OpenAI updates Codex with background computer use, an in-app browser, and built-in image generation. Wonder Project and Luma launch Innovative Dreams with Ben Kingsley as Moses. Midjourney V8.1 Alpha makes HD 3x faster and cheaper.

---

## 2026-04-10 — Week of April 10, 2026

> Anthropic's Mythos model triggered an emergency meeting between the Treasury Secretary, the Fed Chair, and Wall Street bank CEOs. Seedance 2.0 hit #1 on every video benchmark. Netflix open-sourced physics-aware video object removal. Anthropic hit $30B run rate.

---

## 2026-04-03 — Week of April 3, 2026

> OpenAI killed Sora — it was burning $1M a day. Anthropic finds 171 emotion-like patterns in Claude. Cursor 3 goes agent-first. Microsoft ships three in-house AI models without OpenAI. Google drops Gemma 4 for agents.

---

## 2026-03-27 — Week of March 27, 2026

> Anthropic's most powerful model leaks by accident, Adobe opens Firefly Custom Models to everyone, Idomoo ships a video AI that generates layers instead of pixels, and Jensen Huang tells Lex Fridman he thinks we've already achieved AGI — sort of.

---

## 2026-03-20 — Week of March 20, 2026

> A $15 million ad campaign recreated in 40 hours for under $20K, ByteDance's video model shelved by Disney's lawyers, and a new open-source voice model that lets you direct emotional delivery word by word.

---

## 2026-03-13 — Week of March 13, 2026

> ElevenLabs just launched a node-based production canvas that combines 35+ visual AI models with voice, music, and sound effects — and it might be the first tool that actually deserves the label "AI production platform."

---

## Going forward

Each new Friday edition will include a hook here as part of the standard build. The hook lives in three coordinated places — keep all three in sync if a hook is ever revised:

1. `sharepoint-package/samples/list-import-all-editions.csv` — `Hook` column.
2. `sharepoint-package/edition-hooks.md` — this file.
3. `site/index.html` — the `EDITIONS` array's `hook` field.
