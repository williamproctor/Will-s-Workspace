#!/usr/bin/env node
// Render an edition page the way a browser does and walk every section in both reading modes.
//
// Setup (once per machine): cd /tmp && npm install jsdom
// Usage:
//   node scripts/dom_test.js http://localhost:8092 2026-10-26 "phrase that must appear" ...
//   node scripts/dom_test.js https://www.mondaysignal.com 2026-10-26
// Exits 1 if a mode renders no sections, raw markdown shows up, or a required phrase is missing from the full briefing.

let jsdom;
try {
  jsdom = require('jsdom');
} catch {
  jsdom = require('/tmp/node_modules/jsdom');
}
const { JSDOM, VirtualConsole } = jsdom;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const [base, slug, ...musts] = process.argv.slice(2);
if (!base || !slug) {
  console.error('usage: node scripts/dom_test.js <base-url> <slug> [required phrases...]');
  process.exit(2);
}
const local = base.includes('localhost') || base.includes('127.0.0.1');
const bust = () => (local ? '' : `?nc=${Date.now()}`);

async function load(url) {
  const dom = await JSDOM.fromURL(url, {
    runScripts: 'dangerously',
    resources: 'usable',
    pretendToBeVisual: true,
    virtualConsole: new VirtualConsole(),
  });
  await new Promise((r) => dom.window.addEventListener('load', r));
  await sleep(400);
  return dom;
}

async function walk(dom) {
  const doc = dom.window.document;
  const nav = [...doc.querySelectorAll('.nav-item')];
  let text = '';
  const raw = [];
  for (const item of nav) {
    item.dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
    await sleep(40);
    const body = doc.querySelector('.article-body');
    const t = body ? body.textContent : '';
    if (/\*\*[^*]+\*\*|\]\(http/.test(t)) raw.push(item.textContent.trim().slice(0, 60));
    text += `${item.textContent || ''} ${t}\n`;
  }
  return { count: nav.length, text, raw };
}

(async () => {
  let failed = false;
  const dom = await load(`${base}/editions/${slug}${local ? '/' : bust()}`);
  const doc = dom.window.document;
  console.log('title:', doc.title);

  const full = await walk(dom);
  console.log(`full briefing: ${full.count} sections; raw markdown: ${full.raw.length ? full.raw.join(' | ') : 'none'}`);
  if (!full.count || full.raw.length) failed = true;

  const quickButton = doc.querySelector('.mode-toggle button[data-mode="quick"]');
  if (quickButton) {
    quickButton.dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
    await sleep(150);
    const quick = await walk(dom);
    console.log(`quick summary: ${quick.count} sections; raw markdown: ${quick.raw.length ? quick.raw.join(' | ') : 'none'}`);
    if (!quick.count || quick.raw.length) failed = true;
  } else {
    console.log('quick summary: no toggle found');
    failed = true;
  }

  for (const phrase of musts) {
    const ok = full.text.includes(phrase);
    console.log(`  ${ok ? 'ok     ' : 'MISSING'} ${JSON.stringify(phrase)}`);
    if (!ok) failed = true;
  }

  const home = await load(`${base}/${bust()}`);
  const featured = home.window.document.querySelector('[class*=featured]');
  const featuredText = featured ? featured.textContent.replace(/\s+/g, ' ') : '';
  const featuresSlug = featuredText.includes(slug);
  console.log(`homepage features ${slug}: ${featuresSlug}`);
  if (!featuresSlug) failed = true;

  console.log(failed ? 'DOM TEST FAILED' : 'DOM TEST PASSED');
  process.exit(failed ? 1 : 0);
})().catch((e) => {
  console.error('ERROR', e);
  process.exit(1);
});
