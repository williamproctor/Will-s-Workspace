# The AVS AI Dispatch — Week of May 22, 2026

> Quick Summary: **Google I/O 2026 happened this week.** **Gemini Omni Flash** — a new multimodal video model with conversational editing — ships to the Gemini app, **Google Flow**, and free to **YouTube Shorts Remix** and **YouTube Create**. **Gemini 3.5 Flash** ships as a frontier model claiming **4× the speed and < ½ the cost** of comparable models — Google demoed it building a functional OS in 12 hours with 93 parallel agents under $1,000 in API cost. **Google Flow becomes a creative copilot** with project-spanning Flow Agent, vibe-coded Flow Tools, and mobile apps. **Lyria 3 + Lyria 3 Pro** ship for developers — up to three-minute songs with vocals, lyrics, and multimodal input. **Andrej Karpathy joined Anthropic** to build a team using Claude to accelerate Claude pre-training itself; Anthropic also shipped MCP tunnels and self-hosted sandboxes. **OpenAI's reasoning model disproved an 80-year-old Erdős math conjecture** — Fields Medalist Tim Gowers verified. **Cannes 2026** closes tomorrow; the press has converged on the framing that AI "came out of the closet" this year, with Demi Moore's *"AI is here, the fight against it is one we will lose"* as the defining quote.

---

## The Big Stories This Week

### Gemini Omni Flash — Google's New Multimodal Video Model Ships to Every Surface

Google's I/O 2026 introduced **Gemini Omni** — the first model in a new family Google says can "create anything from any input." The first available model is **Gemini Omni Flash**, targeting video first; image and audio outputs are on the roadmap.

**What's new versus Veo and Nano Banana**:

- **Multimodal input in one prompt** — combine text, images, video clips, audio references in a single request
- **Conversational editing** — swap backgrounds, characters, wardrobes, voices, add cinematic zooms via chat
- **Character consistency** — identity, voice, and lens look preserved across cuts automatically
- **Real-world physics + scene continuity** — Google's stated focus area on the new model

**Availability + pricing**:

- **Gemini app + Google Flow** — global, Google AI Plus ($7.99/mo), Pro ($19.99/mo), Ultra ($249.99/mo)
- **YouTube Shorts Remix + YouTube Create app** — free, 18+, with watermarking, source video links, and creator opt-outs
- **10-second clip cap** — a product decision, not a technical limitation; cap will rise
- **Developer/enterprise API** — Gemini API + Agent Platform API, "coming weeks following launch," with SynthID + C2PA on all outputs

The honest assessment: raw video quality still trails Seedance 2.0 and Kling, but the conversational editing surface is best-in-class, and Flow + Omni Flash + Lyria 3 inside the same platform is a different proposition than any previous Google video release.

### Gemini 3.5 Flash — Frontier-Class, 4× Speed, < ½ Cost

Google's headline I/O model launch. The first in a "Gemini 3.5" family positioned as "frontier intelligence with action." Gemini 3.5 Pro coming next month.

**Per Google's internal benchmarks**, 3.5 Flash beats **Claude Sonnet 4.6, Claude Opus 4.7, and GPT-5.5** on:

- **MCP Atlas + Toolathlon** — agentic tool-use
- **Finance agent v2** — multi-step analysis
- **MMMU Pro** — multimodal understanding
- **MRCR v2 (1M pointwise)** — long-context

**Marquee demo**: Antigravity (Google's agent dev platform) used 3.5 Flash to build **a fully functional OS in 12 hours, with 93 agents in parallel, under $1,000 in API cost**.

**Internal traction**: Gemini 3.5 Flash now driving **3 trillion-plus tokens/day** of internal Google usage, up from 500B/day in March.

**For AV teams**, the question is whether 3.5 Flash is now the best agentic model for AV workflows. Worth A/B testing against your current stack this week. Anthropic and OpenAI will ship counter-positioning in the next 4–6 weeks.

### Google Flow Becomes a Creative Copilot

The most AV-relevant I/O update. Flow shipped its V2 platform release with three additions:

- **Flow Agent** — project-spanning planning + execution. Brainstorming, storyboarding, scene generation, dialogue, multi-variation generation, **batch editing across an entire project**. Rolling out to all Flow users globally.
- **Flow Tools** — vibe-code your own utilities (image editors, video resizers, custom shaders, hand-drawn animation passes) in natural language; share them with other Flow users who can remix them. All users can use existing Tools; Google AI subscribers can create and remix.
- **Flow Music** — section-by-section song editing, full-track covers, music video creation. Pairs Lyria 3 Pro (audio) with Omni Flash (video) inside one project.
- **Mobile** — native iOS + Android apps shipped for Flow and Flow Music.

**The numbers**: 140+ countries, 1.5B+ images/videos created since 2025 launch, 50B+ images created with Nano Banana since summer 2025.

For AV teams Flow now reads as "credible production tool" rather than "interesting consumer demo" — especially for rapid prototyping, social-first content, pre-vis, mood-board work, and music-video work for branded content.

### Lyria 3 + Lyria 3 Pro Ship for Developers

Google's music gen play, in public preview through the Gemini API + Vertex AI.

- **Lyria 3 Clip** — 30-second clips, 44.1 kHz stereo, MP3, optimized for speed and high-volume requests
- **Lyria 3 Pro** — up to ~3-minute songs with full structural awareness (intros, verses, choruses, bridges), MP3 or WAV
- **Vocals + timed lyrics**, or pass your own lyrics
- **Multimodal input** — text prompt + up to 10 reference images
- **8 languages** (English, German, Spanish, French, Hindi, Japanese, Korean, Portuguese)
- **SynthID watermarking + C2PA**

**Lyria 2 reference pricing**: $0.06 per 30 seconds. Lyria 3 specific pricing not yet published.

**Workspace integration**: Lyria 3 is wired into **Google Vids** for custom branded soundtrack generation inside corporate-video workflows.

Lyria 3 + ElevenLabs Expressive (May 8) + OpenAI Realtime (May 15) = every audio surface an AV team touches now has a strong AI-native foundation option.

### Karpathy Joins Anthropic, Plus Anthropic's Other Big Week

**Andrej Karpathy joined Anthropic on May 19** — one of the most consequential individual AI hires of the year. He reports to pre-training lead Nick Joseph and is building a brand-new team focused on **using Claude to accelerate Claude pre-training research itself**. The bet: AI-assisted research velocity is how Anthropic stays competitive structurally, not just compute capacity.

Karpathy was an original OpenAI co-founder (one of the original 11), led AI at Tesla, then ran Eureka Labs before joining this week.

Anthropic also brought on **Chris Rohlf** (20-year cyber vet, Meta + Yahoo) to the frontier red team.

**Product-side updates**:

- **MCP tunnels in research preview** (May 19) — connect Managed Agents to MCP servers in private networks
- **Self-hosted sandboxes for Managed Agents** (May 19) — run tool execution outside Anthropic infrastructure
- **Compliance API integrations** (May 21) — security/compliance tools for platform governance
- Claude Code v2.1.143 → v2.1.146 shipped through the week

**For AV teams**, the MCP tunnels release is the one to track. Production AV networks often have private infrastructure (enterprise Frame.io, on-prem asset libraries, internal review platforms). MCP tunnels mean a Claude Managed Agent can now reach them without exposing them publicly.

Broader context: Anthropic is reportedly valued at ~$800B with an IPO target as early as late 2026.

### OpenAI's Reasoning Model Disproves an 80-Year-Old Math Conjecture

On May 20, OpenAI announced an internal general-purpose reasoning model disproved Erdős's 1946 **planar unit distance conjecture** — an 80-year-old open problem. The proof was verified by **Fields Medalist Tim Gowers** and mathematicians including Noga Alon, Melanie Wood, Thomas Bloom, and others.

For 80 years, mathematicians believed square-grid constructions were essentially optimal. OpenAI's model produced a fundamentally new family of constructions yielding **n^(1+0.014) unit distances** — the first polynomial improvement in 80 years. The construction draws on **algebraic number theory** (infinite class field towers) applied to discrete geometry — a cross-field connection no human mathematician had made.

OpenAI's framing: **"the first time AI has autonomously solved a prominent open problem central to a field of mathematics."**

**Why this matters for AV teams indirectly**: the same capability — *"hold together long, difficult chains of reasoning, connect ideas across fields"* — is the primitive behind the agentic workflow tools production AV teams are increasingly relying on. A model that can autonomously disprove an 80-year-old conjecture is the same model class that can autonomously hold together a 30-step production pipeline.

### Cannes 2026 Wrap: "AI Came Out of the Closet"

Cannes 2026 closes May 23. The press wrap has converged on a single framing: **AI "came out of the closet"** this year.

**The numbers**: 40,000 professionals, 16,000 Marché registrants, 140 countries, 250 events at the Marché (45+ AI-focused), "AI on the Lot" growing 600 → 1,200 → expected 2,000 in June, World AI Film Festival drawing 5,500 submissions from 80 countries.

**The defining quote**: **Demi Moore** at the jury press conference (May 12): *"AI is here. Against-ness breeds against-ness. To fight it is to fight a battle that we will lose. To find ways in which we can work with it is a more valuable path to take."* And the more important second half: *"Are we doing enough to protect ourselves? I don't know. My inclination would be to say probably not."*

**Stephen Follows** in his Marché wrap: *"AI is regarded as an analyst, not an author."* Using AI for project analysis, audience simulation, storyboarding, and marketing copy is openly discussed. AI as creative author remains contested, with Soderbergh's Lennon doc the most prominent test case.

**Hollywood stayed home** — Nolan and Spielberg declined invitations. The withdrawal created a gap that independent AI-assisted productions filled. The official competition continued its formal ban on AI-generated work; the Marché's openness was the visible counterpoint.

**The leading indicator**: **Gossip Goblin** (Zack London, Stockholm) — eight-person AI film outfit, off-the-shelf tools, **500M+ views** on satirical AI shorts. LA talent agents flying to Stockholm to meet him. Expect 10–20 more visible kitchen-table AI studios by year-end.

The framing has fully settled: the festival closed the door on the *should* question. The remaining questions are procedural — disclosure, credits, contracts, talent rights. SAG-AFTRA's next negotiating cycle is the watch-item.

### Quick Hits

- **Google Pics** — new AI image creation + editing tool (Nano Banana model), object-level segmentation, text editing + translation, Workspace integration. Trusted testers today; AI Pro/Ultra + Workspace business preview this summer.
- **Gemini Spark** — 24/7 personal AI agent powered by 3.5 Flash, cloud VMs, MCP support, confirmation gates before high-stakes actions. Trusted testers this week; beta for US AI Ultra next week.
- **Antigravity 2.0 + Managed Agents in Gemini API** — single API call provisions a Linux sandbox + agent harness; pay-as-you-go (100K–3M tokens typical); Antigravity SDK for self-hosting.
- **$100/month Google AI Ultra dev plan** — 5× higher limits than AI Pro, 20TB storage, YouTube Premium Lite included (also added free to AI Pro).
- **WebMCP proposed as open web standard** — Chrome 149 origin trial; browser-based agents call structured tools via JS functions and HTML forms.

---

## Tip of the Week

### Build Your Memory Layer This Weekend — Start a Decisions Log

Two weeks ago we built a one-page personal context file. Last week we built a reusable AI skill. This week's tip: **start a decisions log.**

**The problem it solves.** Without memory, the AI you work with re-litigates settled questions every session. You and the model worked through the right way to handle a tricky vendor handoff three weeks ago — you documented the choice nowhere — this week's prompt re-asks the same question and you re-argue your way back to the same answer.

**What goes in a decisions log** — one row per decision, five fields:

1. **Date** — when you decided
2. **Decision** — one sentence
3. **Context** — the situation (2–3 sentences)
4. **Reasoning** — why this option over alternatives
5. **Status** — *active* / *superseded* / *abandoned*

**Five categories every AV pro should be logging from week one**:

- **Tool choices** — "we use Frame.io because the SSO integration is cleaner"
- **Workflow norms** — "we cut at 24p for client review because feedback is more honest"
- **Client and stakeholder preferences** — Director X hates yellow casts; Producer Y wants captions burned in
- **Format and deliverable specs** — standard SDR master is BT.1886 + 16-235; HDR is HDR10 P3-D65
- **Vendor relationships** — Vendor X is reliable but slow; Vendor Y is fast but inconsistent above 4K

**Where to drop it**: a `DECISIONS.md` next to your `AGENTS.md`, a Claude Project file, a Notion database, or a Google Doc you can paste from. Reference it from prompts: *"check my decisions log before suggesting changes."*

**Why it compounds**: skills tell AI *how* to do recurring work. Memory tells AI *what's already been decided*. Six months in, the AI you work with starts agreeing with you about how your work is supposed to run — because it has the receipts.

This is Step 3 of the Agent OS framework. Week 1 = **Identity + Context**. Week 2 = **Skills**. Week 3 (this week) = **Memory**. Next week = **Connections**.

---

## Why This Week Matters

A few patterns worth noting:

- **The agentic frame is now the industry frame.** Three years ago the industry talked about AI assistants. This I/O codified the move to **agents** as the primary frame. Spark, Flow Agent, Antigravity, WebMCP, Anthropic's Karpathy hire (AI-accelerated research agents), OpenAI's Erdős announcement (autonomous reasoning agent disproving a conjecture). The "assistant" framing has retired; the agent framing has won.

- **The audio + video generation stack just collapsed into one surface.** Gemini Omni Flash + Lyria 3 Pro + Flow Music + Flow Agent + Flow Tools = one platform, one subscription, multi-modal production. The era of *"one specialty tool per modality"* is ending; the era of *"one integrated production surface across modalities"* has begun. Strategic implication: evaluate platforms holistically, not as a video tool versus a music tool versus a voice tool.

- **The compute-versus-research bet is splitting publicly.** Anthropic put Karpathy on Claude-accelerating-Claude-pre-training-research. Google's 3.5 Flash demo of building an OS in 12 hours with 93 parallel agents under $1,000 is the same argument from the other direction. The Erdős proof is OpenAI's contribution. Whoever wins the meta-research-acceleration race compounds faster on the long run.

- **Cannes 2026 retired the AI debate.** The festival closed the door on the *should* question. Soderbergh, Liman, the World AI Film Festival's 5,500 submissions, Gossip Goblin's 500M views from a Stockholm apartment, Demi Moore's quote, the Marché's 45+ AI panels, the Human Provenance disclosure standard. The remaining questions are procedural — credits, disclosure, contracts, talent rights, training-data licensing — and consequential, but not philosophical anymore.

- **Vibe-code-your-own-tool surfaces are coming to creative software.** Flow Tools is the first major creative app to let users build custom utilities in natural language and share them with other users. Adobe, Avid, Resolve, Premiere will all ship analogous surfaces within 4–6 quarters. AV teams that invest now in building and sharing custom Flow tools build community-leverage that compounds across 18 months.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. This is the quick summary — the full edition has the complete technical breakdown and sources. Curated with AI assistance. Questions or suggestions? Reply to this message.*
