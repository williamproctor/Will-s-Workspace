# Platform & Vendor Research — Week of July 20–26, 2026

Primary-source sweep: ad platforms, search/answer engines, AI vendors. Compiled 2026-07-27.

## Google / Alphabet

### Q2 2026 earnings (July 22) — AI search monetization is now a disclosed revenue driver
- Revenue $119.8B (+24%); Google advertising $81.6B (+14%); **Search & Other $63.3B (+17%)**; YouTube ads $11.1B (+13%); Google Network **down 1% to $7.3B** (fifth consecutive quarterly decline streak softening from -4% in Q1). Quarter ended June 30; reported July 22, 2026.
- **AI Max out of beta, 500,000+ advertisers.** Google-reported: advertisers using AI Max or PMax see avg **15% more conversions or value at similar ROAS**. Caveat: independent tests (Nov 2025) found AI Max produced *higher* cost per conversion than broad/phrase/exact match in identical campaigns; unresolved publicly. Dynamic Search Ads retire September 2026 with auto-upgrade into AI Max.
- **AI Mode passed 1B monthly active users** (global expansion Oct 2025). Ad formats layering in: contextual sitelinks from the conversation; **Direct Offers** (Jan 2026 pilot with Chewy, Gap, L'Oréal; IHG Hotels & Resorts next, surfacing offers during trip planning); **Highlighted Answers** — "clearly marked sponsored links inside list responses" (Schindler) — debuted Google Marketing Live May 20, showing "early user traction."
- Pichai: Google now "sending billions of clicks to websites every week through AI features in Search." Set against independent CTR data pointing the other way (Ahrefs, Feb 4, 2026: AI Overviews correlate with **58% CTR reduction** for top-ranking pages).
- Gemini app 950M MAU; ~22B tokens/min processed (up from 16B a quarter earlier). Shopping ads relevance +20% (Google-reported). 83% of Google's own sales team uses Gemini tools weekly (company-reported).
- **Agentic commerce:** Universal Commerce Protocol — Target and Steve Madden now live (first named production deployments since Originality.ai's May 21 scan of 3M+ sites found just 26 public implementations). Universal Cart = cross-retailer checkout on Google surfaces.
- CapEx guidance raised to $195–205B for 2026.
- Sources: PPC Land earnings analysis (https://ppc.land/google-search-ads-gain-17-to-63-3-billion-while-network-drops-1/); Search Engine Land (https://searchengineland.com/google-ai-max-billions-new-monetizable-searches-483347); Alphabet IR (https://abc.xyz/investor/events/event-details/2026/2026-Q2-Earnings-Call-2026-GgTAq7Is0z/default.aspx).

### Search Console "Search generative AI control" (documented ~July 20)
- Domain-level toggle: include/exclude site content from **AI Overviews, AI Mode, and generative AI features in Discover**. Takes effect in 1–2 days. Not a ranking signal for regular Search. Does **not** stop model training (Google-Extended governs that). Gemini app excluded.
- Origin: UK CMA conduct requirement; testing began June 3, 2026 with UK properties; now rolling out to more regions. **Page-level controls scheduled March 3, 2027.**
- Sources: Google Search Console Help (https://support.google.com/webmasters/answer/16908024); PPC Land (https://ppc.land/google-gives-site-owners-a-toggle-to-exit-ai-overviews-and-ai-mode/).

### Other Google items in the window
- **July 21:** Gemini 3.6 Flash and 3.5 Flash-Lite announced; Flash uses 17% fewer output tokens, Flash-Lite at $0.30/M input tokens — agent workload economics improve without product changes (https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/).
- **July 22:** AI Overviews blackout ended in France (context: AIO associated with position-one clicks falling 27% → 11%).
- **July 23:** European Commission fined Google **€890M under the DMA**; decision records Google submitted proposals on applying self-preferencing principles to AI Overviews/AI Mode — dialogue continuing, no timeline.
- **July 23:** Image generation added to AI Overviews (Nano Banana model; 5B+ images since Aug 2025 debut).
- **July 23:** Display & Video 360 API July update adds `syntheticContentAttestationStatus` field on Creative and AdAsset resources (AI-content attestation), 10 days before EU AI Act Article 50 binds. Google Ads API v24.2 added SyntheticContentInfo/Attestation structures June 24.
- Digiday (week of July 20): Google testing **Performance Max opt-out of search partners + GDN inventory** — practitioners call it the biggest control concession since launch.

## OpenAI / ChatGPT Ads

### ChatGPT Ads matures into a performance channel (rolled out over the week; budget change effective July 27)
- **Conversion-optimized (oCPC) campaigns:** new Conversions objective; optimizes delivery toward clicks likely to convert; billing stays CPC.
- Daily budgets become **7-day rolling averages** with automatic intraday pacing (effective July 27 per Search Engine Roundtable).
- **Geo exclusions; AppsFlyer + Adjust MMP integrations; Automatic Advanced Matching** (hashed customer data for conversion attribution); **bulk async Ads API**; product feed cards with pricing and star ratings.
- Context: pilot began Feb 9, 2026 (US); self-serve Ads Manager with no minimums since May 5, 2026 (was $200K commitments / $60 CPM in beta). eMarketer frames this as OpenAI chasing $100B+ ad revenue by 2030 (OpenAI target, as reported).
- Sources: Search Engine Roundtable (https://www.seroundtable.com/chatgpt-ads-budget-api-ad-formats-more-41756.html); eMarketer (https://www.emarketer.com/content/chatgpt-ads-shift-clicks-conversions).

### ChatGPT ad marketplace data (Adthena, covered during the week)
- **7,378 advertisers** tracked in ChatGPT; tracked placements grew **97x in a quarter** (small base). Booking.com leads all three tracked markets; US = 60.1% of observed advertisers. Adthena reports ChatGPT ad frequency ~4x Google AI Mode's.
- **Auction is dark:** native Ads Manager reports only the advertiser's own CPC/impressions/CTR — no competitive view. UK advertisers saw costs swing **39%–278%** with no visible explanation. Adthena + dentsu launched a "Decision Intelligence" product to reconstruct auction visibility externally (three dentsu clients among top nine UK ChatGPT advertisers — disclosure).
- Source: PPC Land weekly (https://ppc.land/marketers-brief-ai-with-the-demographic-data-they-say-no-longer-works/).

## Meta
- **July 24: Seller app announced** — AI listing creation ("write the description, suggest a price and tag the item in about 30 seconds" — Meta claim, no accuracy rate published), unified inbox, inventory management, performance insights. Marketplace: 430M items, 44M vehicles listed monthly. US iOS 18+ first.
- **Facebook video-first test:** app opening directly into full-screen video, Classic Feed demoted to a second tab, later this year in video-heavy markets. Sits against EC's July 10 preliminary DSA finding on addictive design (autoplay/infinite scroll; potential 6% global turnover cap).
- **Facebook Verified** free selfie-based badge rolls out July 27 (people only; excludes brand Pages).
- **Q2 2026 earnings: Wednesday July 29**, 1:30pm PT (what to watch next week).
- Sources: PPC Land weekly + https://ppc.land/meta-demotes-facebook-feed-as-free-selfie-badge-rolls-out-today/ ; Meta IR (https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Second-Quarter-2026-Results/default.aspx).

## Amazon
- **July 22:** ~10 AI features land in Brand+ and Performance+; single-deal STV buying removed; audio in 16 locales; default-on model settings (PPC Land: https://ppc.land/amazon-kills-single-deal-stv-buying-in-brand-as-10-ai-features-land/).
- Amazon DSP: Adsquare location segments (6 markets, from July 23); talkSPORT/Times Radio podcast inventory via Octave (from July 24) — fourth audio deal in a month.

## Agent launches (marketing stack)
- **HubSpot Agent Hub public beta** — low-code canvas to assemble agents from prompts, knowledge sources, CRM data. Reference case: Ignite Reading cut a 15–20 min manual task to seconds (~350 hours/yr projected). Consumes HubSpot Credits; pricing beyond that unstated. HubSpot itself flagged the agent-isolation failure mode (sales agent prospecting an account while a service agent handles its open complaint).
- **Disney Campaign Manager AI video ad tool** — turns logos/past creative into CTV spots for SMBs; closed beta, no GA date.
- **GumGum Mindset Agent** — uploaded RFP → custom open-web targeting via The Trade Desk; Heineken, e.l.f., BBC testing.
- **Crunchbase MCP integration** — funding predictions inside Claude/ChatGPT-class assistants; company claims models anticipated 84% of funding events (vendor claim, no independent test).
- Pattern flag: every launch shipped a precise time-saving figure and no accuracy figure.
- Source: PPC Land weekly (link above).
