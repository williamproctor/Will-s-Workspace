# GrowthX Content Library — Authoring Guide

How to produce new content pieces for the GrowthX Content Library. Every piece should feel premium, authoritative, and unmistakably GrowthX.

## Brand Identity Reference

Everything in this site is built from the **official GrowthX design system** at [growthx.ai/brand](https://growthx.ai/brand).

### Core Palette

| Token | Hex | Usage |
|---|---|---|
| `--background` | `#F1EEE9` | Page background ("Burrito Beige") |
| `--foreground` | `#080A0D` | Primary text, dark sections ("Metal Black") |
| `--secondary` | `#E6E3DE` | Subtle backgrounds, code blocks ("Karl the Fog") |
| `--pink` | `#FFC3D6` | Accent highlights ("Ocean Beach Sunset") |
| `--yellow` | `#FFE57B` | Accent highlights ("Mission Afternoon") |
| `--card` | `#FFFFFF` | Card surfaces ("iPod White") |
| `--muted` | `#959595` | Secondary text, timestamps |
| `--border` | `#B3B3B3` | Dividers, card borders |

### Typography

- **Primary:** Inter (web fallback for Messina Sans)
- **Monospace:** Geist Mono / JetBrains Mono
- **Body weight:** 480 | **Heading weight:** 580–680
- **Letter-spacing:** Tight. Headlines at `-0.07em`, body at `-0.03em`

### Logos

Official GrowthX logos are in `site/assets/`:
- `growthx-logo-dark.svg` / `.png` — for light backgrounds
- `growthx-logo-light.svg` / `.png` — for dark backgrounds

**Always use the SVG** for digital. PNG only as fallback.

---

## Content Types

### 1. Video + Article (Primary Format)

The flagship format. A video walkthrough (from Loom or produced) paired with a written deep dive. The article should stand alone without the video, but embed key clips inline.

**Structure:**
```
article-header
  → tag ("Video + Article")
  → title (compelling, specific)
  → subtitle (one-sentence summary)
  → meta (author, duration, date)

video-player (full walkthrough)
  → header with title
  → video element
  → progress bar + controls
  → chapter list with timestamps

article-body
  → h2 sections (3–5 per piece)
  → inline clips at key moments
  → blockquotes for pull-quotes
  → data/evidence where available
```

### 2. Article Only

Written deep dives without a primary video. Still embed inline clips where relevant.

### 3. Playbook

Operational, step-by-step content. More structured, more tactical. Uses the same template but with a "Playbook" tag.

---

## Producing a New Piece

### Step 1: Record the Loom

Record the walkthrough in Loom. Keep it under 20 minutes. Structure it with clear chapters — the chapter list in the video player is populated from timestamps in the HTML.

### Step 2: Download with the Vault Tools

```bash
cd GrowthX-System
python3 tools/loom_downloader.py https://www.loom.com/share/YOUR_VIDEO_ID
python3 tools/vault_manager.py index
```

The video lands in `content_vault/videos/loom/` and metadata in `content_vault/metadata/`.

### Step 3: Extract Clips

Identify 2–4 key moments from the full video. Cut them into standalone clips (30–120 seconds each). Place clips in `site/assets/clips/`.

**Naming convention:** `{topic}-{descriptor}.mp4`
- `marcel-infrastructure-gap.mp4`
- `atlas-pipeline-demo.mp4`
- `flywheel-data.mp4`

### Step 4: Create the Article Page

Copy `content/sample-article.html` as your starting point. Update:

1. **Page metadata** — title, description, OG tags
2. **Article header** — tag, title, subtitle, author, duration, date
3. **Video player** — video source path, chapter list with timestamps
4. **Article body** — written content with inline clips embedded
5. **Chapter data** in the `CHAPTERS` array (JS at bottom)

### Step 5: Embed Inline Clips

Use the `.inline-clip` component to embed video clips inside the article body. Place them after the paragraph they illustrate:

```html
<div class="inline-clip">
  <div class="inline-clip-header">
    <span class="inline-clip-badge">Clip</span>
    <span class="inline-clip-title">Marcel on the infrastructure gap</span>
  </div>
  <video controls preload="metadata">
    <source src="../assets/clips/your-clip.mp4" type="video/mp4">
  </video>
  <div class="inline-clip-caption">From the full walkthrough — 2:14 to 3:45</div>
</div>
```

### Step 6: Add to the Hub

Update the `CONTENT` or `PLAYBOOKS` array in `site/index.html`:

```javascript
{
  title: "Your Article Title",
  desc: "One-sentence description that hooks the reader.",
  tags: ["Video + Article", "18 min"],
  href: "content/your-article.html"
}
```

### Step 7: Tag in the Vault

```bash
python3 tools/vault_manager.py tag VIDEO_ID atlas infrastructure published
```

---

## Writing Guidelines

### Voice

GrowthX writes like it speaks: **direct, specific, and confident without being loud**. The brand voice from growthx.ai/company:

- **Clarity** — Make the complex simple
- **Speed** — Fast where it counts
- **Ownership** — Take initiative and deliver

Apply this to content: skip the throat-clearing, get to the insight, and back it with evidence.

### Structure

Every article follows a three-act pattern (borrowed from the sales enablement video structure):

1. **The Problem** — What the reader already suspects but hasn't articulated. Start past the obvious.
2. **The System** — How it actually works. Be specific. Show, don't describe.
3. **The Implication** — What this means for the reader's business. Make it actionable.

### Inline Clips Strategy

Clips serve three purposes:

1. **Authority** — Show Marcel or Matthew saying the key point. A face + voice carries more weight than text.
2. **Evidence** — Screen recordings of Atlas in action. Show the product working.
3. **Pacing** — Break up long text sections. A 60-second clip every 3–4 paragraphs keeps engagement high.

**Rules for clips:**
- Max 2 minutes each. 30–90 seconds is ideal.
- Every clip needs a caption with the timestamp range from the full video.
- Use the `.inline-clip-badge` to label them ("Clip", "Demo", "Data").
- Place clips after the paragraph that sets them up, not before.

### Visual Rules (from growthx.ai/brand)

- Video backgrounds: dark (#080A0D) for maximum contrast
- All media containers get `border-radius: 8px`
- Warm, natural lighting — no harsh flash or oversaturated color
- Keep UI screenshots to the GrowthX palette: cream background, near-black text, clean type
- Section dividers: 1px `border-top` in `#B3B3B3`
- Shadows: use sparingly. `shadow-sm` preferred over `shadow`

---

## File Structure

```
GrowthX-System/site/
├── index.html              ← Content hub / library page
├── shared.css              ← Design system (GrowthX tokens)
├── AUTHORING.md            ← This guide
├── assets/
│   ├── growthx-logo-dark.svg
│   ├── growthx-logo-dark.png
│   ├── growthx-logo-light.svg
│   ├── growthx-logo-light.png
│   └── clips/              ← Extracted video clips (git-ignored if large)
└── content/
    ├── sample-article.html ← Template article (copy to create new pieces)
    └── ...                 ← Future articles
```
