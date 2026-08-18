# Source-diversity audit and re-sourcing — 2026-08-18

Will's review of the August 17 edition: nearly every story cited ppc.land, which "looks like I am just scraping and repurposing their content." This pass re-sourced the affected editions to the origins of each story and added an automated ceiling (`scripts/check_source_diversity.py`).

## Citation counts for the dominant domain (before → after)

| Edition | ppc.land before | ppc.land after | Top-domain share after |
|---|---|---|---|
| 2026-08-17 (full) | 26 | 13 | 22% (warn tier; remainder is PPC Land's own reporting + one credited roundup line) |
| 2026-08-17 (simplified) | 12 | 4 | 21% |
| 2026-08-03 (full) | 18 | 11 | 28% |
| 2026-08-03 (simplified) | 13 | 5 | 29% |
| 2026-07-27 (full) | 25 | 22 | 31% (mostly PPC Land originals: bakery, opt-out toggle, Meta feed, Amazon STV, earnings analysis) |
| 2026-07-27 (simplified) | 12 | 8 | 35% |

## Origins located and swapped in (all verified via search on 2026-08-18)

### August 17 edition
- Lunio invalid-traffic study → [Lunio's own report](https://www.lunio.ai/blog/invalid-traffic-retail-report). Bonus detail: 88 retail accounts; AI Max IVT +114% vs standard −17%; "cleanest to dirtiest" framing.
- The Trade Desk Q2 → [company release](https://www.thetradedesk.com/press-room/the-trade-desk-reports-second-quarter-2026-financial-results) (reported August 6) + [AdExchanger](https://www.adexchanger.com/programmatic/the-trade-desks-revenue-growth-stalls-as-big-brands-tighten-their-belts/) + [Digiday's by-the-numbers repricing analysis](https://digiday.com/marketing/by-the-numbers-wall-streets-tough-assessment-of-ad-tech/) (the piece the weekly synthesis was itself summarizing).
- Comscore restructuring → [press release](https://www.comscore.com/Insights/Press-Releases/2026/8/Comscore-Announces-ROI-Strategy-to-Transform-the-Business) ("ROI Strategy," August 11; SEC 8-K confirms board authorization August 6).
- Perplexity blocks Time's agent ads → [Digiday broke it](https://digiday.com/media/perplexity-blocks-times-ads-served-to-ai-agents-calling-them-deceptive/) (Dwyer statement was given to Digiday).
- GSC generative AI report → [Search Engine Roundtable](https://www.seroundtable.com/google-search-console-ai-report-live-41850.html). **Accuracy fix:** not fully live — John Mueller: "not yet every domain." Edition softened from "live for everyone."
- ChatGPT Sources demotion → [Search Engine Roundtable](https://www.seroundtable.com/openai-chatgpt-sources-less-visible-41864.html). **Accuracy fix:** a test spotted by Glenn Gabe (his X quote added to Voices), not a completed rollout.
- Clarity crawl-to-referral card → [Microsoft's announcement](https://clarity.microsoft.com/blog/scrape-to-referral-insights/).
- Stealth Bot Prohibition Act → [AdExchanger](https://www.adexchanger.com/ai/a-new-bill-targets-bad-bots-that-scrape-websites-without-permission/) + [News/Media Alliance release](https://www.newsmediaalliance.org/stealth-bot-prohibition-act-introduction/). **Precision fix:** H.R. 9915, introduced July 23; FTC + state AGs enforce.
- Search Profiles threshold → [SER's August 13 recap](https://www.seroundtable.com/recap-08-13-2026-41868.html).

### August 3 edition
- TAG/ANA/Fiducia slop study → [the announcement](https://www.prnewswire.com/news-releases/tagana-fiducia-analysis-quantifies-level-of-ai-slop-in-digital-advertising-supply-chain-for-first-time-302836519.html) + [eMarketer's analysis](https://www.emarketer.com/content/ai-slop-exposes-blind-spot-programmatic-advertising-ad-quality-metrics).
- Time serving ads to AI agents → [Digiday's July 30 original](https://digiday.com/media/time-has-started-serving-ads-to-ai-agents/) (adds Mobian format, Ally Bank/PMI as first buyers, Howard's more-bots-than-humans detail).
- Musk link-demotion claim (simplified) → thread coverage already used in the full edition.

### Not locatable; weekly synthesis retained (credited once per watch section)
Marvin's language-targeting announcement, KPMG agent survey, Fluency/Kochava, Spotify AI-persona policy, France age-check ruling, GA4 window change, IAB Australia guidance, EC Article 50 page, WARC study page, HubSpot Agent Hub, PMax exclusions (Digiday, URL not located), EC €890M fine origin.

## Structural change
Platform & Tool Watch bullets no longer repeat the same roundup URL per bullet; unattributed small items are covered by one italic credit line per section ("Unless linked otherwise, small items in this section were surfaced via …").
