# AVS AI Dispatch — Edition Hooks

Reference sheet of the **`Hook`** field for every published edition. Use these when entering rows into the SharePoint list manually, or when QA'ing what was imported via `samples/list-import-all-editions.csv`.

- **SharePoint field:** `Hook` — Multiple lines of text (plain text, 1 line shown)
- **Length guidance:** 1–3 sentences. No HTML. No line breaks.
- **Where it shows up:** archive tile preview + the featured "Latest" card on the homepage.

These are the same hooks shown on the public site's homepage card and archive list (`https://avaidispatch.com/`), so SharePoint and the public site stay in sync.

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
