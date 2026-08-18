# Platform, Industry & Measurement Research — Week of August 10–16, 2026

Compiled 2026-08-18 (retroactive). Primary synthesis: PPC Land weekly (https://ppc.land/ad-tech-repriced-everything-this-week-except-the-thing-doing-the-counting/); PPC Land single stories; Anicca weekly.

## Google's three-change September (the control squeeze)

1. **Aug 17 bidding target change begins rolling out** (disclosed June 15). Mechanics per Ginny Marvin (Marketing O'Clock interview, Aug 12): reaches campaigns that simultaneously carry a Target CPA/ROAS, are budget-constrained, and deliver better than target. One-way correction: over-performers drift toward target; under-performers get nothing; unconstrained campaigns untouched. **Ad-group-level targets are in scope** (audit surface much larger in lead gen/older builds). Formats: Search, Shopping, PMax, Demand Gen, Travel with target strategies + Limited by budget. Google will not adjust targets/budgets on advertisers' behalf. Marvin: allow 1–2 full conversion cycles before reading results; rollout is gradual → first credible signal lands ~September, at Q4 commitment time. Measured (Aug 11) warning: a $5 actual CPA is not automatically a new target; placement mix can shift beneath a stable ROAS.
2. **Sept 1 AI Max conversion** — exits closed: legacy creation ended Aug 3; Google stopped accepting new campaign-level broad match configurations Aug 13; migrated campaigns keep search term matching on by default; ACA cohort inherits automated query expansion unless switched off at ad-group level. Older API versions live to ~Sept 2027; DSA migration Feb 2027.
3. **Campaign-level language targeting removed from Search AND Performance Max starting September** (Marvin, LinkedIn, Aug 14 — closing a removal first scheduled for end of 2025). Scope surprise: 2025 documentation said non-Search campaign types wouldn't change; PMax is now explicitly named. Prioritization logic switches active: for searches with a clear language, the system prioritizes the matching ad/landing page (reassigns auction slots in bilingual parallel-campaign setups). "User language" broadened to any language set, regularly interacted with, or searched in. Google does not translate creatives (on record — matters for regulated advertisers).
- Combined diagnosis (PPC Land): three platform changes inside four weeks, each removing a variable a media team could hold constant; September performance movement will have at least three plausible in-platform causes and no control condition.

## Lunio: AI Max invalid traffic (published Aug 12)

- Retail search campaigns with AI Max: **72% more invalid traffic** than search campaigns without it. Internal-to-Google comparison: AI Max campaigns rose 2.46% (Q4 2025) → 5.28% (Q2 2026) while standard search in the same accounts eased 3.72% → 3.07%. **Diverging lines, not one rising line.**
- AI Max accounted for **68% of all invalid clicks** detected across the Google search dataset. Dataset: 414M+ clicks, Oct 2025–Jun 2026, across Google, Bing, LinkedIn, Meta, native/social.
- Google Shopping: highest campaign-type average at 6.33%; steepest climb 4.16% → **7.51%** in Q2 (one in thirteen clicks); AI Max reached standard Shopping Apr 30, inside the window (Lunio doesn't attribute). Meta averaged 5.99%, TikTok 5.56%.
- Worked example: $10M/yr retailer at $3.70 CPC loses ~$500K to wasted spend at the 5% retail average (+ modeled ~$1.25M lost revenue opportunity; internal inconsistency vs 3:1 ratio noted in report).
- Context: Google's own AI Max uplift claim has moved three times (14% at May 2025 beta → 7% full-suite figure at April 2026 GA, retail excluded → 27% for exact/phrase-dominant adopters, May 2026). Independent record: Nov 2025 smec study ~35% lower ROAS; Aug 2025 test: 99% of AI Max impressions produced zero conversions across ~30K terms. Reporting cannot split expanded vs literal traffic inside a keyword row; none of the controls report on validity.
- Nick Morley (Lunio CEO): retailers "particularly vulnerable" given sales events compress spend into short windows.

## Ad tech repriced (equities + measurement)

- **The Trade Desk: -22%** after +3% revenue ($715.1M; Q3 guide implies YoY contraction). Jeff Green: growth "below our expectations and below the standard we hold ourselves to."
- **AppLovin: -19.7% after +53%** ($1.92B) — no new Axon model gains to point to.
- Criteo -24% (revenue -11%), Taboola -27.5%, Teads -24%; PubMatic +20.8%, Magnite +8.6%, Zeta +13% (+44% revenue).
- Madison & Wall (Luke Stillman): Amazon+Google+Meta ≈ **56% of US advertising last year → ~58% this year**; open internet projected **-1.4%** while digital grows 12.2%.
- **Comscore**: restructuring strips $20–25M annual costs; Q2 revenue $79.2M (-11.3%); **adjusted EBITDA -85%** to $1.3M; CEO salary -20%; CCO exits with transition brief covering "creator relationships and answer engine optimisation opportunities." Product bets include **AEO/GEO prompt data from its opt-in panel** — observed consumer prompts vs the synthetic prompts current AI-visibility platforms use; validation with leading firms claimed, negotiations begun.
- **Exit from public markets:** IAS → Novacap ($1.9B); LiveRamp → Publicis (shareholder vote Aug 17); Innovid private; DoubleVerify → Nielsen (~$2.15B; DV's Q2: revenue +3% below guidance, first activation decline as a public company); Criteo takeover interest. Digiday: "the public ad tech era is over."

## The AEO measurement stack (counts without connections)

- **Google Search Console generative AI performance report live for everyone** (Aug 11, no formal announcement): impressions, pages, countries, devices, dates (hourly–monthly). **No click data, no query data.** You can count machine reads; you can't optimize inputs or outcomes.
- **OpenAI demoted ChatGPT sources** (Aug 13): Sources button moved into the three-dot More actions menu. Attribution demoted, not removed.
- **Microsoft Clarity ratio card** (Aug 13): ranks which AI operators scrape most and refer least (sample: 6,000:1 crawl-to-referral against 41 referrals), linking to filtered session recordings. Free; requires CDN connection.
- Digiday (Aug 13): CMOs can't link AI visibility to sales despite tool spend. Stanley 1913 case (Aug 12): adapted marketing after finding human-performing work needed different approaches for AI pickup.
- Anicca roundup: **AI Visibility** launched a free tool measuring how often ChatGPT/Gemini recommend brands; **Jellyfish** added Share of Model feature adjusting ad spend based on AI mention frequency.
- Traffic datapoints: Mediavine created a publisher-advocacy role as Google page views fall 34% across 18,000 sites; Arena Group rebranded to **Paradium.AI** (revenue $22.2M vs $45M prior year; traffic -27% YoY); Press Gazette top-50 US news sites: only Substack grows.

## Machine-audience regulation & infrastructure

- **Stealth Bot Prohibition Act** introduced (reported Aug 10): requires AI stealth crawlers to disclose identity/purpose; **$53,000 per violation**; authored by News/Media Alliance; NY version already passed. Axel Springer's Amelia Binder: **25% of Politico's hosting costs now go to bot management.** Tampa Bay Times: bots degrade service for humans.
- Stanford study (Aug 11): **5% of IP addresses send 55% of all web requests**; <0.2% of domains hold a unique IPv4; 44% of client IPs carry 2+ user agents — frequency caps and household matching read a thinning signal.
- Europe: publishers face more AI scraping, fewer referrals, more ignored robots.txt than North America (Digiday, Aug 14). France: AI summaries complaint — traffic cut up to 38%, publishers invoke 2022 commitments binding Google to July 2027.
- Agent-stack split: **Fluency blocks AI from touching live ad spend** across $3B budgets (deterministic agents only) vs **Kochava StationOne** chat-run ad ops with write scope undisclosed. Yahoo DSP Agent Network: 23 tech partners.

## ChatGPT Ads (continued maturation)

- oCPC for product feed campaigns; expanded measurement partnerships (Triple Whale, Hightouch); smarter pixel diagnostics; carousel rollout continuing. **Automatic Advanced Matching becomes default on existing web pixels Aug 17** unless opted out. AdRoll gained ChatGPT ad access for select SMB/B2B customers (Aug 11 pilot).

## Also noted

- GA4 dropped the fixed 3-day engaged-view window (Aug 14): click-through windows now 1–90 days; retroactivity unstated — three days before the bidding change. Diagnostic hazard.
- Spotify drops AI persona artists from recommendations mid-September (self-disclosure open now).
- Google Search Profiles threshold lowered to 35,000 subscribers (YouTube/Instagram/X; TikTok stays 100K).
- DOJ backs revival of antitrust claims against ten advertisers over the alleged X boycott; X ad revenue context: $367M in Q2 2026 vs $1.076B in Twitter's last public quarter.
- Google Ads AI dashboards from text prompts; AI Overviews on the GA homepage; Ask Advisor peer benchmarking (Aug 10).
