# The AVS AI Dispatch — Week of May 8, 2026

> Quick Summary: **Cannes 2026 opens Tuesday with the AI question split clean down the middle** — AGC boards "Critterz," the first $30M mainstream commercial AI-assisted animated feature, while the festival itself bans AI from Palme d'Or competition. **OpenAI ships GPT-5.5 Instant** as the new default for every ChatGPT user, with a 52.5% reduction in hallucinated claims. **xAI's Grok 4.3** lands with strong agentic benchmarks at roughly half the price of GPT-5.5, plus #1 leads on legal and corporate-finance evaluations. **Topaz Labs follows last week's Next-Gen rebuild with Hyperion 2** (a new SDR-to-HDR upscaler) and a UXP panel that drops Topaz cloud processing into the Premiere editing interface. The **AI-actor likeness economy** moves from concept to capital — Twinnin opens a $3M seed round backed by Google and NVIDIA while UK union Equity refuses to endorse the platform, and **YouTube's deepfake-detection tool quietly rolls out to the entire entertainment industry**, free to any actor or athlete who can pass an ID-plus-selfie verification.

---

## The Big Stories This Week

### Cannes 2026: AGC Boards "Critterz" While the Festival Bans AI From Competition

Cannes opens Tuesday, May 12 with the AI question split between the festival and its market. **AGC Studios boarded "Critterz" for worldwide sales** on May 5 — the first mainstream commercial film to use generative AI throughout its production pipeline. **Budget: ~$30M** (vs. ~$80–100M for a comparable traditional animated feature). **Production timeline: ~9 months** (vs. ~3 years). Direction by **Nik Kleverov** (Native Foreign), produced by **Chad Nelson** (OpenAI creative strategist), with screenplay by **James Lamont and Jon Foster** (*Paddington in Peru*). The voice cast is **entirely human**; AI is used in the production pipeline rather than for performance.

**Cannes itself banned AI from Palme d'Or competition** — the festival's stated position: "AI imitates very well, but it will never feel deep emotions." The **Marché du Film expanded its AI for Talent Summit** to two mornings (May 15–16), up from a single day in 2025.

**Why the split is the story.** Cannes is positioning itself as both gatekeeper and growth platform — protecting the artistic legitimacy of the Palme d'Or while letting the market embrace whatever buyers will pay for. Cannes 2026 is the first major festival to draw the "AI as production infrastructure" vs. "AI as creative authorship" line publicly. The next data point is buyer reception. If "Critterz" sells well at the Marché, the $30M ÷ 9-month production model becomes the precedent every AI-assisted feature for the next 24 months gets benchmarked against.

### OpenAI Ships GPT-5.5 Instant — The Default Quality Bar Moves

OpenAI released **GPT-5.5 Instant** on May 5, replacing GPT-5.3 Instant as the default model for every ChatGPT user — including the free tier. This is not a minor refresh.

The headline numbers:

- **52.5% reduction in hallucinated claims** on high-stakes prompts in medicine, law, and finance
- **37.3% reduction in inaccurate claims** on user-flagged factual errors
- **AIME 2025: 81.2** (vs. 65.4 for GPT-5.3 Instant)
- **1M token context window**, 128K max output tokens
- Better web-search use, better image analysis, better personalization

**API pricing**: $5.00 per million input tokens, $30.00 per million output, $0.50 cached input. Prompts above 272K input tokens are charged at 2× input and 1.5× output. GPT-5.3 Instant remains available to paid API users for three months.

**For AV teams**, the floor moved. Anyone using ChatGPT for shot-list scaffolding, rough script polish, transcription cleanup, metadata pass review, or release-note drafting is now getting the upgraded model whether they paid for it or not. The hallucination reduction matters most where AV intersects technical claims — codecs, color spaces, audio formats, platform specs.

### Grok 4.3: Agentic Benchmarks at Roughly Half the Price of GPT-5.5

xAI publicly announced **Grok 4.3** on May 5–6 after a quiet API rollout April 30. Grok 4.3 sits behind GPT-5.5, Claude Opus 4.7, and Gemini 3.1 Pro on broad capability — but its positioning is the story.

The benchmark profile:

- **#1 on Vals Case Law (v2): 79.3%** — the model now leads the legal benchmark
- **#1 on Vals Corporate Finance (v2): 68.5%**
- **Tied #1 on τ²-Bench Telecom: 98%** — agentic customer-support evaluation
- **+321 Elo points** on GDPval-AA real-world agentic tasks (1,179 → 1,500)

**API pricing**: $1.25 per million input tokens, $2.50 per million output — roughly 37.5% lower input and 58.3% lower output costs vs. Grok 4.20, and approximately one-quarter to one-half the comparable GPT-5.5 / Claude Opus 4.7 token cost. Cached input ~$0.31 per million.

**The positioning is the story.** Grok 4.3 is being marketed not as the smartest model but as the one to use when you need agentic tool calling at scale and have to manage cost. For AV teams whose AI use is dominated by background batch tasks (metadata generation, transcription cleanup, rough draft work) rather than frontier creative work, the price-per-token math gets attention.

### Topaz Ships Hyperion 2 + a Native Adobe Premiere Panel

Topaz Labs followed last week's Next-Gen rebuild with two pieces that matter more for working AV teams than the original launch did. **Hyperion 2** is a new SDR-to-HDR upscaler that uses inverse tone mapping to convert standard dynamic range footage to HDR, expanding the dynamic range from 6–10 stops to 12–17.6 stops, BT.1886/Rec. 709 SDR sources to BT.2100/PQ HDR output. The pitch: archival SDR libraries get a one-pass route to HDR delivery.

**Topaz Labs for Premiere** is the bigger workflow change. The new UXP panel (`topazlabs.com/premiere-panel`) lets editors send media directly from a Premiere project timeline to Topaz cloud processing and pull the result back into the same project bin without an export-import roundtrip. Same Topaz subscription tiers; cloud-processing minutes count against the standard credit pool.

CEO Eric Yang framed Next-Gen + Hyperion 2 + Premiere panel as Topaz's first model architecture overhaul since 2018. The short-term context is that the Premiere integration moves Topaz from "the tool you switch to when you need a rescue pass" into "a tab inside your existing edit session."

### The Likeness Economy Moves: Twinnin Raises $3M, YouTube Detection Goes Live for Hollywood

Two stories that, taken together, define the AI-actor likeness economy in 2026 — one selling licensed digital likenesses to studios, the other helping take down unlicensed deepfakes.

**Twinnin opened a $3M seed round** at a $25M post-money valuation. The platform lets actors post a digital likeness that studios and brands can license. **Pricing**: $14.99/year for actors; $499–$1,200/month for studios/brands. Backers include **Google and NVIDIA**. The platform reports **2,000 signed actors with weekly subscriber doubling**. **UK actors' union Equity does not endorse the platform**, citing consent enforcement concerns. SAG-AFTRA's position is under review.

**YouTube expanded its AI-powered likeness detection tool** to the entire entertainment industry, built in partnership with **CAA, UTA, WME, and Untitled Management**. Works similarly to Content ID — scans YouTube for AI-generated deepfakes of enrolled participants and lets them request takedowns. Free; verification requires an ID and selfie video. Rollout sequence: creators (Fall 2025) → politicians and journalists (March 2026) → entertainment industry (April–May 2026).

**Why these stories travel together.** Twinnin is supply-side: a marketplace where actors can opt their faces into a system that monetizes synthetic use. YouTube's detection is the enforcement layer for what they did *not* opt into. Both are operating ahead of the union framework. Equity's non-endorsement and SAG-AFTRA's pending position make the gap explicit.

### ElevenLabs Ships Expressive Mode + Eleven v3 Conversational

ElevenLabs released **Expressive Mode for ElevenAgents** the week of May 4, anchored on a new TTS model — **Eleven v3 Conversational** — that maintains conversational context and produces speech reflecting intent, emotion, and emphasis. New turn-taking system reduces the awkward overlap-or-step-on-each-other failure mode of voice agents. 70+ language support with native expressive control across all of them.

Adjacent SDK updates: conversation tags, enhanced filters, expanded LLM model options (Claude Opus 4.7, GPT-5.4, GPT-5.5, Qwen3 added as agent backends), and increased MCP response timeouts.

**For AV teams**, the obvious uses are voice cloning for ADR pickup, multilingual dubbing, and voiceover drafts. The more interesting downstream is the agent integration: Eleven v3 Conversational + ElevenAgents + Claude Opus 4.7 with MCP tool access is the cleanest "talk to your post-production assistant" prototype currently shippable.

### Revopoint POP 4 Brings Native Gaussian Splatting to a Consumer 3D Scanner

Revopoint launched a **Kickstarter for the POP 4** the first week of May — a handheld 3D scanner with **native Gaussian Splatting export built in**. The pairing matters because it closes the loop on last week's lead story (Insta360 + Splatica's Project Eternal). One device captures a 360 walk-through. The other captures a fixed-volume object or space at sub-millimeter precision and exports the splat directly from the device.

POP 4 specs worth flagging:

- **0.03mm single-frame accuracy** — highest accuracy class for any consumer 3D scanner currently shipping
- **Multi-mode capture** with up to **105 fps in multi-line laser mode**
- **Direct `.PLY` and `.SPLAT` export** — drops directly into Unreal, Unity, Blender
- Color RGB capture integrated into the splat output

**The category context is the story.** Within a single week (Insta360) and the next (Revopoint), consumer hardware has moved from "Gaussian splatting is a research demo" to "you can buy two different devices that produce splats out of the box." For AVS teams running virtual production, previs, or location-scouting workflows, the implication is concrete: scene capture is no longer a specialty rig question. It's a procurement question.

---

## Tip of the Week

### Build a Personal Context File This Weekend

The single highest-leverage move any AV professional can make right now to adopt AI tools is to **write a one-page personal context file once, and reuse it everywhere**.

**Why it works.** Every time you start a new ChatGPT session, open a new Claude project, or fire up a new agent, you re-explain who you are, what your team does, what your current projects are. That re-explanation is the friction. It's also the reason most people's AI output reads generic — they're starting from zero on every prompt.

**Five short sections, one page total**:

1. **Identity** — name, role, team, communication style, 3–5 hard rules the AI should never break
2. **Context** — AVS team structure, current major projects, key stakeholders, recurring deliverables
3. **Tools you use** — Premiere, Resolve, Pro Tools, Frame.io, color/sound stack
4. **Voice samples** — two or three short examples of how you write or speak
5. **What you typically ask AI to help with** — drafting, summarizing, troubleshooting, ideation

**Where to drop it**: ChatGPT Custom Instructions, Claude Project Custom Instructions, `AGENTS.md` for agentic coding tools, or just a markdown file you paste from. Write once, benefit for a year. This is the user-side first move on the "Agent OS" framework we covered last week — the foundation layer the rest of the agent infrastructure builds on.

---

## Why This Week Matters

A few patterns worth noting:

- **The Cannes split is a template.** Cannes 2026 is the first major festival to draw a clean public line between AI as production infrastructure (allowed) and AI as creative authorship (banned from competition). Whether other festivals — Venice, Toronto, Sundance — adopt or reject the same boundary in their fall and winter announcements is now the next industry-watching question. The argument the festival is making is also the argument every individual AV professional is being asked to make on their own work.

- **Foundation models are competing on pricing-and-specialty, not headline capability.** GPT-5.5 Instant ships as a quality upgrade to the default. Grok 4.3 ships as cheaper and agentic-first with a deliberate domain bet. DeepSeek V4 ships as 86% cheaper than GPT-5.5. HappyHorse 1.0 ships as the #1 video model open-source. Nobody is winning the headline-capability race outright, and increasingly nobody is trying to. The right model for any given workflow is increasingly *not* the model at the top of the leaderboard.

- **Capture is migrating to consumer hardware faster than anyone predicted.** Two consecutive weeks of consumer Gaussian-splatting capture launches confirm the volumetric-capture migration. The standardization layer (`KHR_gaussian_splatting` glTF extension, NVIDIA's vkSplatting) is shipping at the same time as the consumer-capture layer. Scene capture is becoming a commodity input format the way 4K video capture became one between 2014 and 2018.

- **The likeness economy is being built in public — ahead of the union framework.** Twinnin's $3M seed (supply side) and YouTube's likeness-detection rollout (enforcement side) are answering the same question three weeks apart. Both are operating ahead of the union framework. Equity's non-endorsement and SAG-AFTRA's pending position are the early warning that the contract language hasn't caught up to the platform design yet.

- **NLE integration is the next AI moat.** Topaz shipping a Premiere UXP panel three weeks after a complete model architecture overhaul is the short version of where this is going. Adobe's Firefly Video Editor integrates Kling, Veo, Sora, and Topaz Astra. ElevenAgents integrates Claude, GPT-5.5, and Qwen3 as backends. The unit of competition is no longer the model — it's the surface where the model meets the editor's existing timeline.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. This is the quick summary — the full edition has the complete technical breakdown and sources. Curated with AI assistance. Questions or suggestions? Reply to this message.*
