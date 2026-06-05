# The AVS AI Dispatch — Week of June 5, 2026

> Quick Summary: **Microsoft Build 2026 moved the frame from Copilot to Autopilot.** Microsoft announced **Scout**, an experimental always-on agent for selected Frontier customers that can work across Teams, Outlook, OneDrive, SharePoint, Windows, and Microsoft 365 context with governance controls. **DaVinci Resolve 21 officially shipped** with a new Photo page, IntelliSearch, CineFocus, expanded AI tools, Final Cut Pro 12 XML support, and broad workflow updates. **xAI released Grok Imagine 1.5 Preview** as an initial image-to-video API: source image in, natural-language shot direction, up to 720p, native audio support, currently image-to-video only on the API. The broader AI video stack kept filling in with **PAI 2.0**, **VidMuse 2.0**, **OttoBox**, and **Adobe Firefly partner-model integrations** — all pointing toward AI video tools becoming production workspaces, not just prompt boxes.

---

## The Big Stories This Week

### Microsoft Build 2026: From Copilot to Autopilot

Microsoft Build ran June 2-3, and the main story was a category shift: **Chat -> Cowork -> Code -> Autopilots**.

The headline product is **Microsoft Scout**, the first agent in Microsoft's new Autopilot category. Scout is designed to work across:

- Teams
- Outlook
- OneDrive
- SharePoint
- calendars and email
- browser work
- local device actions
- Microsoft 365 context

The difference from a normal Copilot is persistence. Copilot waits for a prompt inside an app. Scout is positioned as an always-on work agent that tracks priorities, monitors open loops, and takes multi-step action inside organizational guardrails.

Scout is not broadly available yet. It is an experimental Frontier / private-preview release with Entra identity, Intune policy, opt-in attestation, audit trails, and admin controls. That governance layer matters: Microsoft is showing how always-on agents might be deployed in real organizations rather than treated as consumer chatbots with extra permissions.

Supporting Build announcements:

- **Work IQ APIs** — opens the Microsoft 365 context layer to agents; GA expected June 16.
- **Web IQ** — model-agnostic, MCP-native web grounding layer for agents.
- **Windows Agent Framework** — open-source runtime for agent registration, memory, and cross-agent communication.
- **Microsoft Execution Containers** — sandboxed runtime for running agents more safely on Windows.
- **Aion 1.0 Instruct / Aion 1.0 Plan** — on-device Windows AI models, including a 14B reasoning/tool-calling model.
- **Project Solara** — platform for agent-first desk and wearable device concepts.

For AVS, the Microsoft 365 surface is the point. Our work already lives in Teams, Outlook, SharePoint, OneDrive, calendars, and review documents. Microsoft is moving agents into that exact context.

### DaVinci Resolve 21 Officially Ships

DaVinci Resolve's developer officially released **DaVinci Resolve 21** on June 3 after the public beta cycle.

Major updates:

- New **Photo page** for still-image work inside Resolve
- **IntelliSearch** for faster clip and project search
- **CineFocus** for AI-assisted focal emphasis after capture
- Expanded AI-assisted tools across finishing workflows
- Final Cut Pro 12 XML import/export
- Dynamic project switching for multi-user projects
- Broad updates across edit, color, audio, VFX, collaboration, formats, and stability

The practical point: Resolve 21 is not a speculative AI-video platform. It is a production application shipping AI into the real edit/color/audio/VFX stack.

The pattern is also important. The most useful AI in professional tools often appears as workflow compression: search gets faster, focus adjustments get easier, still-image and video finishing live closer together, and handoffs improve.

Resolve 21 is available as a free download. Resolve Studio remains a $295 one-time purchase.

### Grok Imagine 1.5 Preview

xAI released **Grok Imagine 1.5 Preview** through the API on June 3 under the model name `grok-imagine-video-1.5-preview`.

Keep this one in the "early preview" category. The current API endpoint is **image-to-video**:

- Input: a still image
- Prompt: natural-language shot direction
- Output: animated video up to 720p
- Pricing: $0.080 per second
- Rate limit: 60 requests per minute
- Regions: `us-east-1`, `us-west-2`, `eu-west-1`

Important clarification: the API endpoint is not a general text-to-video endpoint. Some app and web surfaces may expose text-to-video experiences, but the documented developer endpoint is image in, video out.

The broader Grok Imagine 1.5 line also supports native audio generation. The cautious read: this is an initial image-to-video preview with native-audio capabilities, not yet a settled production standard.

For AVS, the pattern matters more than the brand. Like last week's Aleph 2.0 story, Grok Imagine reinforces that the source frame or keyframe is becoming the control surface for video generation. Text describes intent; the image anchors the visual result.

### The AI Video Platform Stack Keeps Filling In

Several smaller video-platform updates landed this week. None needs to be the lead by itself. Together, they show where AI video tools are going: away from single-prompt generation and toward production workspaces with timelines, memory, keyframes, local search, upscaling, voice, and agentic assistance.

**PAI 2.0**:
- Rapid variant generation
- 2x2 keyframes for each 15-second segment
- Native cinematic 4K generation
- Easy Mode for guided creation
- Pro Mode with a Canvas workspace for organizing, editing, and regenerating details

**VidMuse 2.0**:
- **Shot Refine by Quoting** — select a shot and ask the agent to revise only that shot
- Built-in Timeline Editor
- Asset Library with Memory for persistent images, video, audio, character references, and product references
- Rebuilt Agent framework

**OttoBox by OmAI**:
- Local media ingestion with OCR, ASR, shot segmentation, and vector tagging
- Natural-language video search
- Rough-cut generation, highlight extraction, scripts, and narration
- Local/on-device angle for sensitive footage

**Adobe Firefly partner-model ecosystem**:
- ElevenLabs Multilingual v2 for generated speech inside Firefly
- Topaz Astra for video upscaling inside Firefly Boards
- Firefly continuing to act as a hub where Adobe and partner models sit inside one creative workspace

The common thread: the useful question is no longer "can it make a clip?" It is "can it help manage the whole revision loop?"

### Quick Hits

- **Gemini 3.5 Pro is still pending** — Google committed to a June rollout, but there is still no public model card, pricing row, API model string, or general availability announcement.
- **GitHub Copilot AI-credit billing began June 1** — agentic work is increasingly priced as metered model usage, not just a seat license.
- **Adobe Firefly AI Assistant remains a watch item** — Adobe has previewed an agentic assistant for Firefly Video Editor that can orchestrate multi-step work across Creative Cloud apps.

---

## Tip of the Week

### Back to Basics, Week 2: Specificity Over Flattery

Last week, we started the **Back to Basics** series with a simple principle: **context is the lever, not the model**. This week is about the next common prompting mistake: opening with flattery instead of instruction.

Most weak prompts start like this:

```text
You are an expert video producer. Help me make this script better.
```

That sounds natural, but it gives the model almost nothing useful. "Expert" is vague. "Better" is vague. The output format is unspecified. The audience is missing. The constraints are missing.

Use this instead:

```text
Your task is to revise this 90-second internal training script for clarity.

Audience: non-technical staff.
Tone: calm, plainspoken, professional.
Constraints: keep it under 220 words, keep all safety instructions intact,
remove jargon, and preserve the three-step structure.
Output: return only the revised script, then a 3-bullet explanation of what changed.
```

The principle is **specificity over flattery**. Modern models do not need to be complimented into competence. They need a clear task, audience, constraints, examples, and success criteria.

For AV work, this matters because the work has real constraints:

- A script has a runtime.
- A caption set has a reading-speed limit.
- A stakeholder email has a tone.
- A training video has safety instructions that cannot be changed.
- Review notes need to be organized by timecode.

The weekend exercise: rewrite one prompt you actually use in five fields:

1. **Task** — what the model should do.
2. **Audience** — who the output is for.
3. **Constraints** — what must be preserved, avoided, shortened, or emphasized.
4. **Input** — the source material or context.
5. **Output format** — exactly what you want back.

This works in Claude, ChatGPT, Gemini, Copilot, Grok, and whatever ships next. The model changes. The principle does not.

Next week: **Show, Don't Tell** — why 2-3 examples of good output often outperform a page of abstract instructions.

---

## Why This Week Matters

- **Agents are moving into governed work context.** Scout is interesting because it is always-on, but it is deployable because it has Entra identity, admin controls, Intune setup, and audit trails. Context only becomes usable in organizations when permissions, logging, and policy are built in.

- **Video tools are becoming workspaces, not prompt boxes.** PAI 2.0, VidMuse 2.0, OttoBox, Adobe Firefly, Grok Imagine 1.5, and last week's Aleph 2.0 all point in the same direction: timelines, references, memory, keyframes, local search, upscaling, speech, audio, and shot-specific revision.

- **The frame is becoming the control surface.** Grok Imagine animates a source image. Aleph 2.0 propagates a keyframe edit. VidMuse revises quoted shots. PAI uses keyframes per segment. Text describes intent; the image or shot carries the visual contract.

- **Local media intelligence matters for sensitive footage.** OttoBox's local-ingestion approach is early, but the idea is important: transcription, OCR, shot segmentation, vector search, and rough-cut assistance without moving raw media off device.

---

*The AVS AI Dispatch is a weekly AI digest for the Audio/Video Services team. This is the quick summary — the full edition has the complete technical breakdown and sources. Curated with AI assistance. Questions or suggestions? Reply to this message.*
