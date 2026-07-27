/* Signal & Scale — shared JS (markdown renderer, reading toggle, podcast player) */

function buildPodcastPlayer(audioSrc, title) {
  return `
    <div class="podcast-player" id="podcastPlayer">
      <button class="podcast-play-btn" id="podcastPlayBtn" aria-label="Play audio briefing">
        <svg viewBox="0 0 24 24" id="podcastPlayIcon"><polygon points="6,3 20,12 6,21"/></svg>
      </button>
      <div class="podcast-info">
        <div class="podcast-label">Audio Briefing</div>
        <div class="podcast-title">${title}</div>
        <div class="podcast-progress-wrap">
          <span class="podcast-time" id="podcastCurrent">0:00</span>
          <div class="podcast-progress" id="podcastProgress">
            <div class="podcast-progress-bar" id="podcastBar"></div>
          </div>
          <span class="podcast-time" id="podcastDuration">--:--</span>
        </div>
      </div>
      <button class="podcast-speed-btn" id="podcastSpeedBtn">1x</button>
      <button class="podcast-volume-btn" id="podcastVolumeBtn" aria-label="Mute">
        <svg viewBox="0 0 24 24"><polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
      </button>
      <audio id="podcastAudio" preload="metadata" src="${audioSrc}"></audio>
    </div>`;
}

function initPodcastPlayer() {
  const audio = document.getElementById('podcastAudio');
  if (!audio) return;
  const playBtn = document.getElementById('podcastPlayBtn');
  const playIcon = document.getElementById('podcastPlayIcon');
  const bar = document.getElementById('podcastBar');
  const progress = document.getElementById('podcastProgress');
  const curTime = document.getElementById('podcastCurrent');
  const durTime = document.getElementById('podcastDuration');
  const speedBtn = document.getElementById('podcastSpeedBtn');
  const volBtn = document.getElementById('podcastVolumeBtn');
  const speeds = [1, 1.25, 1.5, 1.75, 2];
  let speedIdx = 0;

  function fmt(s) {
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60);
    return m + ':' + (sec < 10 ? '0' : '') + sec;
  }

  audio.addEventListener('loadedmetadata', () => { durTime.textContent = fmt(audio.duration); });
  audio.addEventListener('timeupdate', () => {
    if (!audio.duration) return;
    bar.style.width = (audio.currentTime / audio.duration * 100) + '%';
    curTime.textContent = fmt(audio.currentTime);
  });
  audio.addEventListener('ended', () => {
    playIcon.innerHTML = '<polygon points="6,3 20,12 6,21"/>';
  });

  playBtn.addEventListener('click', () => {
    if (audio.paused) {
      audio.play();
      playIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>';
    } else {
      audio.pause();
      playIcon.innerHTML = '<polygon points="6,3 20,12 6,21"/>';
    }
  });

  progress.addEventListener('click', (e) => {
    if (!audio.duration || isNaN(audio.duration)) return;
    const rect = progress.getBoundingClientRect();
    const ratio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
    audio.currentTime = ratio * audio.duration;
  });

  speedBtn.addEventListener('click', () => {
    speedIdx = (speedIdx + 1) % speeds.length;
    audio.playbackRate = speeds[speedIdx];
    speedBtn.textContent = speeds[speedIdx] + 'x';
  });

  let muted = false;
  volBtn.addEventListener('click', () => {
    muted = !muted;
    audio.muted = muted;
    volBtn.querySelector('svg').innerHTML = muted
      ? '<line x1="23" y1="1" x2="1" y2="23"/><polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/>'
      : '<polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>';
  });
}

function buildReadingToggle() {
  return `
    <div class="reading-toggle" id="readingToggle">
      <button class="reading-toggle-btn active" data-mode="standard" id="toggleStandard">
        <svg viewBox="0 0 24 24" width="14" height="14"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="14 2 14 8 20 8" fill="none" stroke="currentColor" stroke-width="2"/><line x1="16" y1="13" x2="8" y2="13" stroke="currentColor" stroke-width="2"/><line x1="16" y1="17" x2="8" y2="17" stroke="currentColor" stroke-width="2"/></svg>
        Full Briefing
      </button>
      <button class="reading-toggle-btn" data-mode="simplified" id="toggleSimplified">
        <svg viewBox="0 0 24 24" width="14" height="14"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
        Quick Summary
      </button>
    </div>`;
}

function initReadingToggle(standardMd, simplifiedMd) {
  const container = document.getElementById('editionContent');
  const btnStd = document.getElementById('toggleStandard');
  const btnSimp = document.getElementById('toggleSimplified');
  if (!btnStd || !btnSimp || !container) return;

  function setMode(mode) {
    const md = mode === 'standard' ? standardMd : simplifiedMd;
    renderEdition(container, md);
    btnStd.classList.toggle('active', mode === 'standard');
    btnSimp.classList.toggle('active', mode === 'simplified');
    container.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  btnStd.addEventListener('click', () => setMode('standard'));
  btnSimp.addEventListener('click', () => setMode('simplified'));
}

/* Render markdown into a container, then upgrade it into the scannable
   edition layout: every H3 block becomes an expandable story card
   (collapsed by default), the Sources section folds away, and an
   expand/collapse-all bar is added. */
function renderEdition(container, md) {
  container.innerHTML = markdownToHtml(md);
  enhanceEdition(container);
}

function enhanceEdition(container) {
  const STOPS = ['H2', 'H3', 'HR'];

  // 1) Wrap each H3 and its following block into <details class="story-card">
  const headings = Array.from(container.querySelectorAll(':scope > h3'));
  headings.forEach((h3) => {
    const details = document.createElement('details');
    details.className = 'story-card';
    const summary = document.createElement('summary');
    summary.className = 'story-summary';
    const body = document.createElement('div');
    body.className = 'story-body';

    container.insertBefore(details, h3);
    summary.appendChild(h3);
    details.appendChild(summary);

    let node = details.nextSibling;
    while (node) {
      if (node.nodeType === 1 && STOPS.includes(node.tagName)) break;
      const next = node.nextSibling;
      body.appendChild(node);
      node = next;
    }
    details.appendChild(body);
  });

  // 2) Fold the Sources section behind a single toggle
  const h2s = Array.from(container.querySelectorAll(':scope > h2'));
  const sourcesH2 = h2s.find((h) => h.textContent.trim().toLowerCase() === 'sources');
  if (sourcesH2) {
    const details = document.createElement('details');
    details.className = 'sources-fold';
    const summary = document.createElement('summary');
    const body = document.createElement('div');
    body.className = 'sources-body';

    let node = sourcesH2.nextSibling;
    const collected = [];
    while (node) {
      if (node.nodeType === 1 && (node.tagName === 'H2' || node.tagName === 'HR')) break;
      collected.push(node);
      node = node.nextSibling;
    }
    collected.forEach((n) => body.appendChild(n));
    const count = body.querySelectorAll('p, li').length;
    summary.textContent = count ? 'View all ' + count + ' sources' : 'View sources';
    details.appendChild(summary);
    details.appendChild(body);
    sourcesH2.parentNode.insertBefore(details, sourcesH2.nextSibling);
  }

  // 3) Expand/collapse-all bar, placed after the lede, before the first section
  const cards = container.querySelectorAll('details.story-card');
  if (cards.length) {
    const bar = document.createElement('div');
    bar.className = 'expand-bar';
    bar.innerHTML =
      '<span class="expand-hint">Click any headline to read the full item</span>' +
      '<span class="expand-actions">' +
      '<button type="button" data-action="expand">Expand all</button>' +
      '<button type="button" data-action="collapse">Collapse all</button>' +
      '</span>';
    bar.addEventListener('click', (e) => {
      const btn = e.target.closest('button');
      if (!btn) return;
      const open = btn.dataset.action === 'expand';
      cards.forEach((c) => { c.open = open; });
    });
    const firstH2 = container.querySelector(':scope > h2');
    container.insertBefore(bar, firstH2 || container.firstChild);
  }
}

function markdownToHtml(md) {
  const codeBlocks = [];
  md = md.replace(/```[^\n]*\n([\s\S]*?)```/g, (_, code) => {
    const idx = codeBlocks.length;
    codeBlocks.push(
      `<pre><code>${escapeHtml(code.replace(/\n$/, ''))}</code></pre>`
    );
    return `\n@@CODEBLOCK_${idx}@@\n`;
  });

  md = convertTables(md);
  md = convertLists(md);
  return md
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '')
    .replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<figure class="edition-figure"><img src="$2" alt="$1" loading="lazy"><figcaption>$1</figcaption></figure>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    .replace(/^---$/gm, '<hr>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/^(?!<)(.+)$/gm, '<p>$1</p>')
    .replace(/<p><\/p>/g, '')
    .replace(/<p>(<h[23]>)/g, '$1')
    .replace(/(<\/h[23]>)<\/p>/g, '$1')
    .replace(/<p>(<hr[^>]*>)<\/p>/g, '$1')
    .replace(/<p>(<blockquote>)/g, '$1')
    .replace(/(<\/blockquote>)<\/p>/g, '$1')
    .replace(/<p>(<table)/g, '$1')
    .replace(/(<\/table>)<\/p>/g, '$1')
    .replace(/<p>(<ul)/g, '$1')
    .replace(/(<\/ul>)<\/p>/g, '$1')
    .replace(/<p>(<figure)/g, '$1')
    .replace(/(<\/figure>)<\/p>/g, '$1')
    .replace(/<p>@@CODEBLOCK_(\d+)@@<\/p>/g, (_, idx) => codeBlocks[Number(idx)] || '')
    .replace(/@@CODEBLOCK_(\d+)@@/g, (_, idx) => codeBlocks[Number(idx)] || '');
}

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function convertTables(md) {
  const lines = md.split('\n');
  let out = [], inTable = false, isHeader = true;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith('|') && line.endsWith('|')) {
      const cells = line.split('|').slice(1, -1).map(c => c.trim());
      if (cells.every(c => /^[-:]+$/.test(c))) continue;
      if (!inTable) { out.push('<table>'); inTable = true; isHeader = true; }
      const tag = isHeader ? 'th' : 'td';
      out.push('<tr>' + cells.map(c => `<${tag}>${c}</${tag}>`).join('') + '</tr>');
      if (isHeader) isHeader = false;
    } else {
      if (inTable) { out.push('</table>'); inTable = false; }
      out.push(lines[i]);
    }
  }
  if (inTable) out.push('</table>');
  return out.join('\n');
}

function convertLists(md) {
  const lines = md.split('\n');
  let out = [], inList = false;
  for (let i = 0; i < lines.length; i++) {
    const match = lines[i].match(/^- (.+)$/);
    if (match) {
      if (!inList) { out.push('<ul>'); inList = true; }
      out.push(`<li>${match[1]}</li>`);
    } else {
      if (inList) { out.push('</ul>'); inList = false; }
      out.push(lines[i]);
    }
  }
  if (inList) out.push('</ul>');
  return out.join('\n');
}
