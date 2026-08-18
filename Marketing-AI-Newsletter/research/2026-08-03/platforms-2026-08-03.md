# Platform & Vendor Research — Week of July 27–August 2, 2026

Compiled 2026-08-18 (retroactive). Primary synthesis: PPC Land weekly (https://ppc.land/bots-overtake-humans/); Meta IR; Paid Media Collective Issue 224 (https://www.linkedin.com/pulse/paid-media-news-week-31-yoann-ferrand-zujec); Search Engine Land.

## Earnings (four reports in 48 hours; all figures company-reported)

### Meta (Wed July 29)
- Ad revenue $59.36B (+27%); impressions +14%, price per ad +12%. Total revenue $60.8B (+28%).
- US/Canada: prices +20% on impressions +9%. Asia-Pacific: impressions +17%, prices +1%. Mature markets monetize via price, growth markets via volume.
- **Advantage+ passed $75B annual run-rate** (from $60B three quarters earlier; not a reported line item).
- **Meta Generative Recommender**: Susan Li called it "a paradigm shift in how our ads system works" — LLMs reason about ad content and user preferences together instead of scoring candidates individually. GEM ranking + sequence learning: +8.3% ad clicks, +15.7% conversions on Facebook; LLM preference pilots +1% app-event conversions on Instagram. 9M+ SMBs use at least one Meta AI creative tool.
- 1M+ businesses use Business Agent weekly. Movida (Brazilian car rental): +44% daily WhatsApp bookings, 85% of conversations resolved by the agent (company case).
- The cost side: capex $31.08B (vs $17.01B a year ago); FCF $784M (from $8.55B); total expenses +55% to $42.03B; operating margin 31%; net income $15.8B (-8%; $2.4B legal charge + $1.18B severance); EPS $6.18 (-13%, missed). $24.91B long-term debt issued; BlackRock JV for 1GW El Paso data center (Jul 28). Q3 guide $61–64B with EU personalization headwinds flagged. FoA other revenue crossed $1B for the first time (+73%, WhatsApp paid messaging + Meta One).
- Family daily active people 3.60B (+3%); Instagram passed 2B DAU; Threads crossed 500M MAU.

### Amazon (Thu July 30)
- Ads $19.8B (+26%), fastest in the six quarters disclosed; TTM $76.1B. Capex forecast raised $20B to ~$220B.
- **Alexa+ / Alexa for Shopping sponsored prompts: clickers convert 48% more often, spend 21% more** (seller-reported; CPC billing since Mar 25). 350M+ customers used the shopping assistant TTM; assistant users spend 40%+ more per order.
- Ads Agent expanded to 11 new countries; company-reported 8% lower CPI, 6% lower CPA.
- Prime Video sports: TNF/NBA/WNBA/NASCAR inventory "all sold out" (Jassy); 12-year exclusive Canadian NHL Wednesday deal (Fri).
- Prime Day calendar shifted into Q2 this year; CommerceIQ: US Prime Day ad spend fell 8.8% while conversion rates rose 17.1%.

### Microsoft (Wed July 29)
- Search ads ex-TAC +10% (9% cc), decelerating from 12%; guided mid-single digits. FY search $15.176B.
- Azure crossed $100B annual revenue; **Agent 365 registered ~40M agents within two months**; 650K+ MCP actions exposed via Dynamics 365; Copilot 30M paid seats; GitHub Copilot revenue +60% QoQ after usage-based billing.

### Reddit (Thu July 30)
- Ads +64% to $762M; conversion volume doubled; advertiser count +70%; Reddit Max revenue +150% sequential (Lenovo: +40% purchase value). Attain/Circana: 1.5x social-average ROAS for CPG; TransUnion: most efficient paid social for EMEA retail (~7x average).
- Stock fell 12.49% after hours: US daily uniques +6% to 53.2M vs a stated 100M target; Huffman called search referrals "choppy and volatile"; "AI Overviews has yet to make a similar level of positive impact"; direct users "worth multiples more."
- Disclosure change: Reddit stops reporting logged-in/logged-out split next quarter.

### Pattern
Every reported dollar of ad growth traveled through an automated buying product: Advantage+ (Meta), Ads Agent/sponsored prompts (Amazon), AI Max (Microsoft and Google), Reddit Max.

## OpenAI / ChatGPT Ads
- **New "Agent" campaign type spotted (Jul 31, Search Engine Roundtable):** clicking the ad starts a conversation with the advertiser's Business Agent instead of opening a website. Meta disclosed the same week that 1M businesses run its Business Agent weekly — click-to-agent now exists at two companies.
- **ChatGPT appeared in Google Ads auction insights** (practitioner find, Jyll Saskin Gales, Jul 28): present since May on exact-match keywords in niche financial software. First receipts of overlapping auctions.
- **GPT-5.6 API prices cut up to 80%** (Luna -80%, Terra -20%; Jul 29). Frontier-class-a-year-ago intelligence now ~6 cents on the dollar per task at ~9x speed; Sol gains a Fast mode (2.5x speed, 2x price). Agent economics reprice again.
- Head of Scaled Ads Solutions job posting names resellers/BPO as next advertiser tiers; no listed role covers merchant feed data quality.

## Google
- **AI Max migration timeline set (SEL):** Aug 3 — no new campaign-level Broad Match or legacy ACA; Sept 1–30 — auto-migration to AI Max; DSA reminders Jan 15, 2027; DSA auto-migration Feb 2027.
- PMax: limited alpha to switch off search partners + Display Network; household income exclusions surfaced Jul 27.
- Banned undisclosed incentivized reviews (Jul 28) with manual actions.
- Search Console platform properties GA (Jul 30): track Instagram/TikTok/X/YouTube profile performance in Google Search without a website.
- LSAs appearing inside AI Mode (Jul 30); D-U-N-S verification required in some US verticals.
- Dropped the 2007 rule requiring sites to block internal search results pages (Mueller/Splitt).
- AI content labels operational across Ads, Merchant Center, Ads Editor; AI label column in Asset Studio. DV360 attestation field live Jul 25.

## Meta platform plumbing
- Graph API v26.0 (Jul 30): 47 commerce endpoints blocked with no replacement; Poll ads, Explore Feed, Messenger Stories placements removed.
- Facebook Feed demoted to second tab in full-screen video test; free selfie-verification badge shipped Jul 27 (Pages excluded).

## Amazon retail plumbing
- 984M AI title rewrites logged since June; brand owners get a 14-day review window before AI-rewritten titles go live; mobile display parity Aug 10.

## Agent infrastructure
- **MCP specification rewrite finalized Jul 28**: sessions removed from the protocol (stateless transport); Extensions track; MCP Apps; OAuth hardening; 12-month deprecation floor. Ad platforms running MCP servers: Google Ads API, Amazon Ads, Meta connectors (write access), Snap, Pinterest, DoubleVerify, FreeWheel.
- **IAB Tech Lab AAMP v2.3 (Jul 30):** pricing provenance to stop AI agents fabricating bid prices; vendor approval gate.
- TikTok shipped 8 product sets Jul 28 including **Agentic Hub** (MCP door into Ads Manager), TopView regional exclusions, GMV Max Pro.
- Nielsen Ad Intel became conversational (5.5M brands, 23 media types, 90+ countries).
- Vanderbilt Policy Accelerator (Jul 30): Amazon and Walmart shopping agents dodge country-of-origin questions.
- Gemini Spark expanded to 160 more countries, still excluding EEA/UK.
