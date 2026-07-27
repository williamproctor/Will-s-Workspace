/* Signal & Scale — shared JS (markdown renderer, edition reader app, podcast player) */

/* ---------- Markdown renderer ---------- */

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

/* ---------- Edition model ---------- */

/* Parse rendered markdown into { overview, sections[{title, intro[], items[{title, plain, nodes[]}]}] } */
function parseEditionModel(md) {
  const host = document.createElement('div');
  host.innerHTML = markdownToHtml(md);
  const model = { overview: [], sections: [] };
  let section = null;
  let item = null;
  Array.from(host.children).forEach((node) => {
    const tag = node.tagName;
    if (tag === 'HR') return;
    if (tag === 'H2') {
      section = { title: node.textContent.trim(), intro: [], items: [] };
      model.sections.push(section);
      item = null;
      return;
    }
    if (tag === 'H3' && section) {
      item = { title: node.innerHTML, plain: node.textContent.trim(), nodes: [] };
      section.items.push(item);
      return;
    }
    if (!section) { model.overview.push(node); return; }
    (item ? item.nodes : section.intro).push(node);
  });
  return model;
}

/* Flatten the model into a linear list of readable entries */
function buildEntries(model, editionTitle) {
  const entries = [{
    kind: 'overview',
    group: null,
    kicker: 'This week',
    title: editionTitle,
    plain: 'Overview',
    nodes: model.overview,
  }];
  model.sections.forEach((section) => {
    if (section.items.length) {
      section.items.forEach((it, i) => {
        entries.push({
          kind: 'item',
          group: section.title,
          kicker: section.title,
          title: it.title,
          plain: it.plain,
          nodes: i === 0 && section.intro.length ? section.intro.concat(it.nodes) : it.nodes,
        });
      });
    } else if (section.intro.length) {
      entries.push({
        kind: 'section',
        group: null,
        kicker: 'Section',
        title: section.title,
        plain: section.title,
        nodes: section.intro,
      });
    }
  });
  return entries;
}

/* ---------- Edition reader app ---------- */

function initEditionApp(root, opts) {
  const state = { mode: 'full', entries: [], index: 0 };

  root.innerHTML = `
    <aside class="app-sidebar">
      <div class="sidebar-head">
        <div class="sidebar-meta">
          <span class="edition-badge">${escapeHtml(opts.slug)}</span>
          <a class="btn-back" href="/">&larr; All editions</a>
        </div>
        ${opts.simplifiedMd ? `
        <div class="mode-toggle" role="tablist" aria-label="Reading mode">
          <button type="button" role="tab" class="active" data-mode="full">Full briefing</button>
          <button type="button" role="tab" data-mode="quick">Quick summary</button>
        </div>` : ''}
      </div>
      <nav class="app-nav" aria-label="Edition contents">
        <span class="nav-indicator" aria-hidden="true"></span>
        <div class="nav-items"></div>
      </nav>
    </aside>
    <div class="app-article">
      <button type="button" class="article-back">&larr; Headlines</button>
      <div class="article-scroll">
        <div class="article-inner"></div>
      </div>
    </div>`;

  const nav = root.querySelector('.app-nav');
  const navItems = root.querySelector('.nav-items');
  const indicator = root.querySelector('.nav-indicator');
  const articleScroll = root.querySelector('.article-scroll');
  const articleInner = root.querySelector('.article-inner');
  const backBtn = root.querySelector('.article-back');

  /* Media block is built once so audio playback survives navigation */
  let mediaBlock = null;
  if (opts.hasVideo || opts.hasAudio) {
    mediaBlock = document.createElement('div');
    mediaBlock.className = 'article-media';
    if (opts.hasVideo) {
      mediaBlock.innerHTML += `
        <div class="video-card">
          <div class="video-card-header">
            <div class="video-card-icon"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
            <div class="video-card-info">
              <div class="video-card-label">Video Briefing</div>
              <div class="video-card-title">${escapeHtml(opts.videoTitle || '')}</div>
            </div>
          </div>
          <div class="video-card-body">
            <video controls playsinline preload="metadata" poster="${opts.videoThumb}">
              <source src="${opts.videoSrc}" type="video/mp4">
            </video>
          </div>
        </div>`;
    }
    if (opts.hasAudio) {
      mediaBlock.innerHTML += buildPodcastPlayer(opts.audioSrc, opts.audioTitle || 'Audio Briefing');
    }
  }

  function setMode(mode) {
    state.mode = mode;
    const md = mode === 'quick' && opts.simplifiedMd ? opts.simplifiedMd : opts.editionMd;
    state.entries = buildEntries(parseEditionModel(md), opts.editionTitle);
    buildNav();
    root.querySelectorAll('.mode-toggle button').forEach((b) => {
      b.classList.toggle('active', b.dataset.mode === mode);
    });
    select(0, { animate: true, fromHash: false });
  }

  function buildNav() {
    navItems.innerHTML = '';
    let lastGroup = null;
    state.entries.forEach((entry, i) => {
      if (entry.group && entry.group !== lastGroup) {
        const label = document.createElement('div');
        label.className = 'nav-group';
        label.textContent = entry.group;
        navItems.appendChild(label);
      }
      lastGroup = entry.group;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'nav-item' + (entry.kind !== 'item' ? ' nav-overview' : '');
      btn.dataset.index = i;
      btn.innerHTML = `<span class="nav-item-text">${entry.kind === 'item' ? entry.title : escapeHtml(entry.plain)}</span>`;
      btn.addEventListener('click', () => select(i, { animate: true, openMobile: true }));
      navItems.appendChild(btn);
    });
  }

  function moveIndicator(btn) {
    if (!btn || !indicator) return;
    const h = btn.offsetHeight || 0;
    indicator.style.height = h ? h - 14 + 'px' : '0px';
    indicator.style.transform = 'translateY(' + (btn.offsetTop + 7) + 'px)';
  }

  function renderEntry(entry) {
    articleInner.innerHTML = '';

    const head = document.createElement('header');
    head.className = 'article-head';
    const titleHtml = entry.kind === 'item' ? entry.title : escapeHtml(entry.title);
    head.innerHTML = `<div class="article-kicker">${escapeHtml(entry.kicker)}</div><h1 class="article-title">${titleHtml}</h1>`;
    articleInner.appendChild(head);

    if (entry.kind === 'overview' && mediaBlock) articleInner.appendChild(mediaBlock);

    const body = document.createElement('div');
    body.className = 'edition-content article-body';
    entry.nodes.forEach((n) => body.appendChild(n));
    articleInner.appendChild(body);

    const pager = document.createElement('div');
    pager.className = 'article-pager';
    const prev = state.entries[state.index - 1];
    const next = state.entries[state.index + 1];
    if (prev) {
      pager.innerHTML += `<button type="button" class="pager-btn pager-prev">
        <span class="pager-dir">&larr; Previous</span><span class="pager-title">${escapeHtml(prev.plain)}</span></button>`;
    } else {
      pager.innerHTML += '<span class="pager-spacer"></span>';
    }
    if (next) {
      pager.innerHTML += `<button type="button" class="pager-btn pager-next">
        <span class="pager-dir">Next &rarr;</span><span class="pager-title">${escapeHtml(next.plain)}</span></button>`;
    }
    pager.querySelector('.pager-prev') && pager.querySelector('.pager-prev').addEventListener('click', () => select(state.index - 1, { animate: true }));
    pager.querySelector('.pager-next') && pager.querySelector('.pager-next').addEventListener('click', () => select(state.index + 1, { animate: true }));
    articleInner.appendChild(pager);
  }

  function select(i, o) {
    const options = o || {};
    if (i < 0 || i >= state.entries.length) return;
    state.index = i;
    const entry = state.entries[i];

    navItems.querySelectorAll('.nav-item').forEach((b) => {
      const active = Number(b.dataset.index) === i;
      b.classList.toggle('active', active);
      if (active) {
        b.setAttribute('aria-current', 'true');
        moveIndicator(b);
        if (b.scrollIntoView) b.scrollIntoView({ block: 'nearest' });
      } else {
        b.removeAttribute('aria-current');
      }
    });

    renderEntry(entry);
    articleScroll.scrollTop = 0;

    if (options.animate !== false) {
      articleInner.classList.remove('article-enter');
      void articleInner.offsetWidth;
      articleInner.classList.add('article-enter');
    }
    if (options.openMobile) root.classList.add('article-open');
    if (window.history && history.replaceState) history.replaceState(null, '', '#r' + i);
  }

  root.querySelectorAll('.mode-toggle button').forEach((b) => {
    b.addEventListener('click', () => { if (!b.classList.contains('active')) setMode(b.dataset.mode); });
  });

  backBtn.addEventListener('click', () => root.classList.remove('article-open'));

  document.addEventListener('keydown', (e) => {
    if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
    if (e.key === 'ArrowDown' || e.key === 'j') { e.preventDefault(); select(state.index + 1, { animate: true }); }
    else if (e.key === 'ArrowUp' || e.key === 'k') { e.preventDefault(); select(state.index - 1, { animate: true }); }
    else if (e.key === 'Escape') { root.classList.remove('article-open'); }
  });

  /* Initial state: honor a #rN deep link when present */
  state.entries = buildEntries(parseEditionModel(opts.editionMd), opts.editionTitle);
  buildNav();
  if (opts.hasAudio) initPodcastPlayer(mediaBlock);
  const hashMatch = (window.location.hash || '').match(/^#r(\d+)$/);
  const start = hashMatch ? Math.min(Number(hashMatch[1]), state.entries.length - 1) : 0;
  select(start, { animate: true, openMobile: start > 0 });
  window.addEventListener('resize', () => {
    const active = navItems.querySelector('.nav-item.active');
    if (active) moveIndicator(active);
  });
}

/* ---------- Podcast player ---------- */

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

function initPodcastPlayer(scope) {
  const rootEl = scope || document;
  const audio = rootEl.querySelector('#podcastAudio');
  if (!audio) return;
  const playBtn = rootEl.querySelector('#podcastPlayBtn');
  const playIcon = rootEl.querySelector('#podcastPlayIcon');
  const bar = rootEl.querySelector('#podcastBar');
  const progress = rootEl.querySelector('#podcastProgress');
  const curTime = rootEl.querySelector('#podcastCurrent');
  const durTime = rootEl.querySelector('#podcastDuration');
  const speedBtn = rootEl.querySelector('#podcastSpeedBtn');
  const volBtn = rootEl.querySelector('#podcastVolumeBtn');
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
