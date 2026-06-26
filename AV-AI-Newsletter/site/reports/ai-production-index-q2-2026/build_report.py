#!/usr/bin/env python3
"""Build the Q2 2026 AVS AI Production Index HTML report."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT_MD = (ROOT / "report.md").read_text(encoding="utf-8")
REPORT_MD_JS = json.dumps(REPORT_MD)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The AVS AI Production Index — Q2 2026 | The AVS AI Dispatch</title>
  <meta name="description" content="A quarterly assessment of what AI can and cannot do in audio/video production. Q2 2026 edition.">
  <meta property="og:title" content="The AVS AI Production Index — Q2 2026">
  <meta property="og:description" content="A quarterly assessment of what AI can and cannot do in audio/video production. No hype. Just what works, what is close, and what is still a demo.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://avaidispatch.com/reports/ai-production-index-q2-2026">
  <meta property="og:site_name" content="The AVS AI Dispatch">
  <meta property="og:image" content="https://avaidispatch.com/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://avaidispatch.com/og-image.png">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="canonical" href="https://avaidispatch.com/reports/ai-production-index-q2-2026">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/shared.css?v=20260626">
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
            <span class="edition-badge" style="background: var(--ink-soft);">Research Report</span>
            <span class="edition-date">Q2 2026</span>
          </div>
          <a href="/" class="btn-back">&larr; Home</a>
        </div>
        <h1 class="report-hero-title">The AVS AI Production Index <span class="report-hero-dash">&mdash;</span> Q2&thinsp;2026</h1>
        <nav class="report-switcher" aria-label="AVS AI Production Index editions">
          <a href="/reports/ai-av-production-capability-assessment">Q1 2026</a>
          <a href="/reports/ai-production-index-q2-2026" class="active" aria-current="page">Q2 2026</a>
        </nav>
        <div class="pdf-download-bar">
          <div class="pdf-download-inner">
            <div class="pdf-download-text">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10M7 12h6M7 16h8"/></svg>
              <span>This report is also available as a <strong>12-slide PDF deck</strong></span>
            </div>
            <a href="/reports/ai-production-index-q2-2026/AV_AI_Production_Index_Q2_2026.pdf" download class="pdf-download-btn">Download PDF</a>
          </div>
        </div>
        <div class="edition-body">
          <div id="editionContent"></div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-text">&copy; 2026 Audio/Video Services &mdash; The AVS AI Dispatch</div>
      <div class="footer-links">
        <a href="/">Home</a>
        <a href="/#archive">Archive</a>
        <a href="/brand-guidelines.html">Brand</a>
      </div>
    </div>
  </footer>

  <script src="/shared.js?v=20260626"></script>
  <script>
    const REPORT_MD = {REPORT_MD_JS};
    const html = markdownToHtml(REPORT_MD);
    document.getElementById('editionContent').innerHTML = html.replace(/^<h1[^>]*>.*?<\\/h1>\\s*/i, '');
  </script>

  <script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
</body>
</html>
"""

(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print(f"Wrote {ROOT / 'index.html'} ({len(HTML):,} chars)")
