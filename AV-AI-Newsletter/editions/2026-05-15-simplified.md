# The AVS AI Dispatch — Week of May 15, 2026

> Quick Summary: **OpenAI shipped three Realtime voice models on May 11** and the pricing rewrites what's possible for AV teams that handle voice: streaming transcription at **$1.02/hour**, live translation across 70+ input languages at **$2.04/hour**, and a GPT-5-class voice agent with parallel tool calling. **Anthropic locked down 300 megawatts of new compute** through an exclusive SpaceX deal (220,000+ NVIDIA GPUs), **doubled Claude Code rate limits** for paid tiers, and made the Claude Platform on AWS generally available. At **Cannes 2026**, the industry launched **Human Provenance in Film** — the first open-license AI disclosure standard — while **Steven Soderbergh** premiered "John Lennon: The Last Interview" with ~10% AI-generated footage. **Krea shipped Krea 2**, a style-first foundation image model. **Flick raised $6M** for AI-native filmmaking. **Vertigo Films + Federation Studios spun out amersia + Woven** — the production stack that made "Critterz" is now a standalone tooling company.

---

## The Big Stories This Week

### OpenAI Ships Three Realtime Voice Models — and the Pricing Rewrites What's Possible for AV

OpenAI released three audio-class models to the Realtime API on May 11. None are flagship LLM releases. All three change what's *economically viable* in an AV workflow.

- **GPT-Realtime-2** — voice agent. GPT-5-class reasoning, 128K context, parallel tool calling. Audio: $32/M input, $64/M output. Text: $4/M input, $24/M output.
- **GPT-Realtime-Translate** — streaming speech-to-speech translation across **70+ input languages → 13 output languages**, priced by duration: **$0.034/min** ($2.04/hour).
- **GPT-Realtime-Whisper** — streaming low-latency speech-to-text transcription, also by duration: **$0.017/min** ($1.02/hour).

**Why the pricing matters more than the models do.** AV teams have been doing transcription, translation, and voice work with AI for years. The block has never been capability — it's been unit economics. Real-time transcription at $1/hour, real-time translation at $2/hour, and a voice agent that can call tools mid-conversation at audio-token rates around $1–$2 per minute of intensive use mean a producer can leave transcription running over an eight-hour shoot day for **$8**, dub a 25-minute scratch track to twelve languages for **less than a dollar per language**, and prototype an on-set translator app for an international shoot for the price of two takeaway lunches per day.

The less-obvious use case is the **voice agent as a workflow surface**: an editor can talk to an agent with tool access to Premiere, Frame.io, and project metadata, in actual conversation, with sub-2-second response latency. The prototype that's been "six months from shippable" is now an afternoon of integration work.

### The Compute Capacity Wars: Anthropic Locks Down 220K GPUs via SpaceX

Anthropic announced an exclusive compute deal with SpaceX on May 6 that flipped a real capacity switch for anyone whose workflow runs through Claude.

**The deal**: exclusive use of all compute from SpaceX's **Colossus 1** data center in Memphis — **300+ megawatts**, **220,000+ NVIDIA GPUs** (H100, H200, GB200), online within one month. SpaceX operates the facility; Anthropic gets exclusive output. Separately, both companies have expressed interest in developing "multiple gigawatts of orbital AI compute capacity" — still exploratory.

**Same-day user impact** (effective May 6):

- **Claude Code five-hour rate limits doubled** for Pro, Max, Team, and Enterprise seats
- **Peak-hours throttling removed** for Pro and Max accounts
- **Opus API rate limits substantially raised**

A May 11 follow-up made **Claude Platform on AWS generally available** — Managed Agents, code execution, skills, web search, and Files API natively on AWS with AWS authentication and billing. The two announcements stack: Anthropic now has meaningfully more direct compute *and* a distribution channel through every existing AWS enterprise account.

**The structural story.** Model providers are increasingly betting on **physical-infrastructure deals** (Anthropic ↔ SpaceX, OpenAI ↔ Stargate, Google's TPU verticalization) rather than commodity cloud GPU rentals. For AV teams whose workflows depend on a particular model being responsive on a deadline, the provider-to-power-grid line is now a relevant lens.

### Cannes Pulse: An Open-License AI Disclosure Standard, and Soderbergh's AI-Assisted Lennon Doc

Two threads from Cannes 2026 worth flagging together — they're answering the same question (*how does AI sit inside a mainstream production?*) from opposite ends of the stack.

**Human Provenance in Film** launched May 13 at the Marché du Film. The Mise En Scène Company released the standard as a **free, open-license disclosure framework** any producer, distributor, or platform can adopt without negotiation. Three designations:

- **No AI Used** — no generative AI in the production pipeline at all
- **Assistive AI** — AI used for non-creative tasks (transcription, captioning, color correction assist, metadata, search)
- **Generative AI** — generative AI used in creative output

The framework is the first industry-led, voluntary disclosure standard to ship with a license that lets any platform adopt it without negotiation. Expectation in the room at Cannes: a major streamer or distributor will require disclosure to this standard within 18 months.

**Steven Soderbergh premiered "John Lennon: The Last Interview"** at the festival with **approximately 10% AI-generated footage** of Lennon and Yoko Ono. Soderbergh's framing: sequences "that couldn't have been filmed in real life." The film uses AI to fill historical gaps where source material doesn't exist, rather than to extend or replace performances. It's the first documentary from a top-tier American director to ship with a disclosed generative-AI segment of meaningful size.

**The two together are the story.** Disclosure standard *and* marquee-director use case landing the same week at the same festival. The industry that spent 2023–2025 litigating whether AI belongs in production is, at Cannes 2026, building the conventions that will govern *how* it does.

### Krea 2 Ships a Style-First Foundation Image Model

Krea released **Krea 2** on May 12 — its first foundation image model built from scratch, with an explicit design bet on **style transfer and aesthetic control** rather than open-ended generation.

- **Style transfer system** — pass in reference images; the model decomposes aesthetic features and reapplies them
- **Moodboards** — multi-style mixing with slider-adjustable influence per reference
- **Style-strength control** — generate across a spectrum from "loose interpretation" to "near-mimicry"
- **~15-second generation**
- Ranked **#2** on Contra Labs' style-fidelity benchmark (0.14 pts behind GPT Image 2)

**For AV teams**: storyboarding to a director's reference deck, mood-board-driven previs, brand-style work where the client comes with existing visual language. Open-ended generation models produce a striking image; Krea 2's bet is that producing *the specific image you already see in your head* is the more valuable problem.

### Flick Raises $6M for AI-Native Filmmaking — With an Explicit "Cinematic Control" Pitch

**Flick** announced a $6M seed round on May 11, led by True Ventures, with **GV, Y Combinator, Lightspeed, Formosa Capital, Pioneer Fund, Olive Tree Capital, and N1**. Founded by **Zoey Zhang** (filmmaker) and **Ray Wang** (founding engineer on Instagram Stories).

The pitch: the gap in AI filmmaking isn't quality, it's *direction*. Most generative video produces striking 8-second clips but provides little affordance for the working filmmaker's actual job — making decisions about framing, pacing, performance, and continuity, and iterating on each one until the cut works. Flick is building the iteration surface.

**Filmmaker Residency**: **10+ short AI-native films** by emerging filmmakers, with showcase slots at **Cinequest, MIT, and Omni AI Film Festival**.

Flick is the third high-profile bet in six weeks (alongside Buzzy's "Photoshop for AI video" and amersia's Woven) on the thesis that **the next phase of AI video is direction and editing tooling, not better base models.**

### amersia + Woven Launch Out of "Critterz"

**Vertigo Films and Federation Studios** announced **amersia**, a new AI entertainment company, on May 14, alongside its first technology product: **Woven**.

Critterz was made with a proprietary production stack — image generation, GPT-5 for structural work, custom pipeline tooling, human-led creative direction. Vertigo and Federation have now spun the underlying technology into a standalone company. Woven is positioned to automate **repetitive production tasks** (asset passes, continuity checks, version control, technical handoffs) rather than replace artistic judgment. Director Nik Kleverov: "Woven is built around human-led creativity."

**The pattern**: marquee AI-assisted project ships → underlying tech gets spun out → spun-out product becomes the playbook for the next 4–6 projects. amersia is the first cleanly executed example at scale. Expect 4–6 more of these in the next two quarters.

### Quick Hits

- **Doug Liman's "Bitcoin: Killing Satoshi"** ($70M; Gal Gadot, Casey Affleck, Pete Davidson, Isla Fisher) selling at Cannes via Patrick Wachsberger's 193. AI-generated backgrounds/lighting; performances captured normally. 20-day soundstage + 30 weeks post with **55 AI artists**. Comparable traditional production: ~$300M.
- **Stephen Kay's "Answr"** — Iceland-shot AI thriller about human-AI relationships. Moises Arias + Rain Spencer, scored by Tyler Bates. Gersh + Radiant selling at Cannes.
- **Storyverse AI Studio** debuts at Cannes with a "Director-level AI System" that takes projects script-to-screen in as few as 5 days.
- **Baidu ERNIE 5.1** (May 8–9) — roughly one-third the parameters of ERNIE 5.0 at ~6% of comparable training cost, ranked #4 globally (#1 among Chinese models) on Arena Search.
- **Anthropic Claude Platform on AWS** GA May 11 — Managed Agents, code execution, skills, web search, Files API native on AWS.

---

## Tip of the Week

### Build Your First Reusable AI Skill This Weekend

Last week's tip was the personal context file — the foundation layer of the Agent OS framework. This week's tip is the natural next step: **turn one recurring task you do every week into a reusable "skill."**

**The problem it solves.** Even with a strong context file, every individual prompt still re-explains the task. *"Summarize this call into action items, decisions, and follow-up owners — under 200 words, bullet points, flag anything that needs my approval."* You write that every Friday. A skill is the same instruction, but written once and named — so next Friday you just say "use my call-summary skill."

**What goes in a skill** (one page per skill, three sections):

1. **When to use it** — the trigger condition
2. **The steps** — the actual instructions, the clearer the better
3. **The output format** — the literal template the output should match

**Five starter skills every AV professional should write first**:

- **Call summary** — meeting/client/vendor calls → structured action items
- **Status update draft** — your weekly week-in-review format
- **Email triage** — thread in, one-line summary + draft reply out
- **Shot list scaffold** — script or scene description in, structured shot list out
- **Asset metadata pass** — clip file or thumbnail in, suggested keywords/tags/description out

**Where to drop them**: ChatGPT Custom Instructions, a Claude Project, an `AGENTS.md`, or just a markdown file you paste from. Build one this weekend. Build the second next weekend. By the end of a quarter you have a dozen skills running and you've stopped re-explaining the same task forever.

This is Step 2 of the Agent OS framework. Last week was **Identity + Context**. This week is **Skills**. Next week we'll cover **Memory**.

---

## Why This Week Matters

A few patterns worth noting:

- **The pricing of voice just collapsed.** $1.02/hour transcription and $2.04/hour translation aren't a technical breakthrough — they're a unit-economics breakthrough. The capability has been ambient for 18+ months. What changed this week is that an AV team can leave transcription running across a shoot day for the cost of a coffee. When the price of a capability drops below the justification threshold, the capability stops being an experiment and becomes the default. That transition happened to voice this week.

- **Cannes 2026 is the first festival where AI is being normalized rather than litigated.** The conversation has moved from *should* AI be in films to *how* do we disclose it, credit it, contract for it, and let buyers and audiences differentiate. The Human Provenance standard, Soderbergh's documentary, the proliferation of AI-assisted features at the Marché, the doubled AI for Talent Summit, the spun-out tooling companies — these are all answers to the *how* question, not the *should* one.

- **The compute layer is consolidating.** Anthropic + SpaceX, OpenAI + Stargate, Google's vertical TPU strategy, Meta's in-house silicon — model providers are signing physical-infrastructure deals, not just chip orders. For AV teams whose workflows depend on a specific model's reliability at a particular moment, the provider-to-power-grid line is now a relevant operating concern.

- **The "Critterz precedent" becomes a stack.** amersia is the first cleanly executed example of a pattern about to repeat: a marquee project ships, the production tooling that made it ships, the tooling becomes the playbook for the next 4–6 projects. Bitcoin: Killing Satoshi, Answr, and the Storyverse slate are the watch-items for what spinouts come next.

- **"Cinematic control" emerges as a distinct product category.** Flick, Buzzy, Krea 2, and amersia/Woven are all pointing at the same product category — distinct from base-model generation. The base-model leaderboard race is approaching diminishing returns; the iteration-layer race is just starting. AV teams that move first on direction-focused workflows get a 12–18-month head start.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. This is the quick summary — the full edition has the complete technical breakdown and sources. Curated with AI assistance. Questions or suggestions? Reply to this message.*
