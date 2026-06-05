#!/usr/bin/env python3
"""Build the June 5, 2026 edition HTML page from the markdown sources."""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(ROOT, "editions", "2026-06-05.md")
SIMPLIFIED_PATH = os.path.join(ROOT, "editions", "2026-06-05-simplified.md")
OUT_DIR = os.path.join(ROOT, "site", "editions", "2026-06-05")
OUT_PATH = os.path.join(OUT_DIR, "index.html")

with open(MD_PATH, "r", encoding="utf-8") as f:
    edition_md = f.read()

with open(SIMPLIFIED_PATH, "r", encoding="utf-8") as f:
    simplified_md = f.read()

edition_md_js = json.dumps(edition_md)
simplified_md_js = json.dumps(simplified_md)

OG_DESCRIPTION = (
    "Microsoft Build 2026 moves from Copilot to Autopilot with Scout, "
    "Work IQ APIs, Web IQ, Windows Agent Framework, Execution Containers, "
    "and Aion on-device models. DaVinci Resolve 21 officially ships with "
    "a new Photo page, IntelliSearch, CineFocus, and Final Cut Pro 12 XML. "
    "Grok Imagine 1.5 Preview adds an initial image-to-video API with "
    "native audio capabilities. PAI 2.0, VidMuse 2.0, OttoBox, and Adobe "
    "Firefly partner models show AI video tools becoming production "
    "workspaces rather than prompt boxes."
)
META_DESCRIPTION = OG_DESCRIPTION

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The AVS AI Dispatch &mdash; Week of June 5, 2026 | The AVS AI Dispatch</title>
  <meta name="description" content="{META_DESCRIPTION}">
  <meta property="og:title" content="The AVS AI Dispatch — Week of June 5, 2026">
  <meta property="og:description" content="{OG_DESCRIPTION}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://avaidispatch.com/editions/2026-06-05">
  <meta property="og:site_name" content="The AVS AI Dispatch">
  <meta property="og:image" content="https://avaidispatch.com/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://avaidispatch.com/og-image.png">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="canonical" href="https://avaidispatch.com/editions/2026-06-05">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/shared.css">
</head>
<body>

  <header class="site-header scrolled" id="siteHeader">
    <div class="header-inner">
      <a href="/" class="logo">
        <div class="logo-icon">AVS</div>
        <span class="logo-text">The AVS <em>AI</em> Dispatch</span>
      </a>
      <nav class="nav-links">
        <a href="/">Home</a>
        <a href="/#archive">Archive</a>
      </nav>
    </div>
  </header>

  <section class="section edition-page" id="edition" style="padding-top: 100px;">
    <div class="section-inner">
      <div class="latest-edition" id="editionContainer">
        <div class="edition-header">
          <div class="edition-meta">
            <span class="edition-badge">2026-06-05</span>
            <span class="edition-date">2026-06-05</span>
          </div>
          <a href="/" class="btn-back">&larr; All editions</a>
        </div>
        <div class="edition-body">
          <div id="videoMount"></div>
          <div id="podcastMount"></div>
          <div id="toggleMount"></div>
          <div class="edition-content" id="editionContent">Loading edition&hellip;</div>
        </div>
      </div>
    </div>
  </section>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-text">&copy; 2026 Audio/Video Services &mdash; The AVS AI Dispatch</div>
      <div class="footer-links">
        <a href="/">Home</a>
        <a href="/#archive">Archive</a>
        <a href="/brand-guidelines.html">Brand</a>
      </div>
    </div>
  </footer>

  <script src="/shared.js"></script>
  <script>
    const EDITION_MD = {edition_md_js};
    const HAS_AUDIO = true;
    const AUDIO_SRC = "/audio/2026-06-05.m4a";
    const AUDIO_TITLE = "AVS AI Dispatch \\u2014 Audio Summary";

    const VIDEO_SRC = "/video/2026-06-05.mp4";
    const VIDEO_TITLE = "From Copilot to Autopilot";
    const VIDEO_THUMB = "/video/thumbs/2026-06-05.png";
    const HAS_VIDEO = true;

    const videoMount = document.getElementById("videoMount");
    if (HAS_VIDEO) {{
      videoMount.innerHTML = `
        <div class="video-card">
          <div class="video-card-header">
            <div class="video-card-icon">
              <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
            </div>
            <div class="video-card-info">
              <div class="video-card-label">Video Edition</div>
              <div class="video-card-title">${{VIDEO_TITLE}}</div>
            </div>
          </div>
          <div class="video-card-body">
            <video controls playsinline preload="metadata" poster="${{VIDEO_THUMB}}">
              <source src="${{VIDEO_SRC}}" type="video/mp4">
            </video>
          </div>
        </div>`;
    }}

    const mount = document.getElementById("podcastMount");
    if (HAS_AUDIO) {{
      mount.innerHTML = buildPodcastPlayer(AUDIO_SRC, AUDIO_TITLE);
      initPodcastPlayer();
    }}

    const EDITION_SIMPLIFIED = {simplified_md_js};

    const toggleMount = document.getElementById("toggleMount");
    if (EDITION_SIMPLIFIED && EDITION_SIMPLIFIED !== "PLACEHOLDER_SIMPLIFIED") {{
      toggleMount.innerHTML = buildReadingToggle();
      document.getElementById("editionContent").innerHTML = markdownToHtml(EDITION_MD);
      initReadingToggle(EDITION_MD, EDITION_SIMPLIFIED);
    }} else {{
      document.getElementById("editionContent").innerHTML = markdownToHtml(EDITION_MD);
    }}
  </script>

  <script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
</body>
</html>
"""

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"Wrote {OUT_PATH} ({len(HTML):,} chars)")
print(f"  Full edition markdown:       {len(edition_md):,} chars")
print(f"  Simplified edition markdown: {len(simplified_md):,} chars")
