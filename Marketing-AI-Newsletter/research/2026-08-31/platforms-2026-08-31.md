# Platforms track — week of August 24–30, 2026

Origins first. PPC Land weekly synthesis ("The week AI agents got the ad account and Meta got a two-hour clock", https://ppc.land/the-week-ai-agents-got-the-ad-account-and-meta-got-a-two-hour-clock/) used as a discovery index.

## X / xAI
- **X Ads MCP launched Aug 24:** a remote Model Context Protocol server at ads-api.x.com/mcp exposing 23 X Ads tools to any MCP client (Grok, Claude Code, etc.): nine account/read, two analytics, two targeting search, **ten write functions**. Advertiser's own OAuth2 token, three scopes. Structural rule: every campaign and line item is created **paused**; nothing spends until explicitly activated. No beta label, no rollout schedule; docs live. Origin: X's announcement/docs (underlying); [PPC Land report](https://ppc.land/x-ads-mcp-gives-grok-and-claude-code-23-tools-to-run-ad-campaigns/).

## Google
- **AI Overviews dynamically expand** for "some queries" (confirmed Aug 28): full answer, open "Ask anything" box, organic results pushed down; expansion cancels if the user has started scrolling. Spotted by Chris Long Aug 27. Origins: [SEL](https://searchengineland.com/google-is-dynamically-expanding-ai-overviews-for-some-queries-486200) · [SER](https://www.seroundtable.com/google-ai-overviews-push-ai-mode-responses-41974.html) · [The Verge](https://www.theverge.com/tech/986364/google-search-ai-overviews-auto-expand).
- **/goto passthrough redirects on search clicks** (SER confirmed Aug 26; in testing since July): links route through an encoded google.com/goto redirect rather than directly to destinations. Derek Perkins (Nozzle) observed near-total coverage across residential IPs and called it anti-scraping engineering; rank trackers now need 500–1,000 requests per SERP to decode. Google declined comment. Marketing O'Clock EP 448 (Aug 31) led with it: https://marketingoclock.com/episodes/well-goto-a-world-with-google-searchs-goto-tracking-parameters/ · SER video recap: https://www.seroundtable.com/video-08-28-2026-41963.html
- **AI Mode books hotels** with Google Pay (Aug 27; US English, gradual rollout; partners Booking.com, Choice, Expedia, Hilton, IHG, Marriott, Priceline, Trip.com, Wyndham). Flight price tracking with target-price alerts in 180+ countries. (Via PPC Land weekly.)
- **Local Services Ads billing change Oct 1:** unanswered calls during business hours become billable if the caller holds 20+ seconds; follow-up calls billable even when the first contact didn't qualify. Notice emailed Aug 24; posted by Anthony Higman Aug 25; carried by SER. (Via PPC Land weekly; SER underlying.)
- **Ads product wave (SEL, Aug 25–28):** Gemini Omni video creation in Asset Studio (Aug 25); PMax channel-prioritization controls in test (Aug 25); LSA direct booking expanded to 500+ partners (Aug 25); AI-generated product titles report (Aug 26); Ads API Developer Assistant v4 (Aug 26); Demand Gen adds messaging ads, travel tools, AI video creation (Aug 27). Index: https://searchengineland.com/library/ppc
- **Site reputation abuse policy not enforced in the EEA from Aug 30** under an EC mandate; EEA searchers "will not benefit from Google's spam prevention" for those sites. [SER Aug 28 recap](https://www.seroundtable.com/recap-08-28-2026-41971.html)
- **Indexing/serving outage Aug 28** (~6:15–7:35am ET; WSJ/NYT/CNN fresh content missing). [SER](https://www.seroundtable.com/google-search-indexing-issues-41972.html)
- Also (SER recap): PDFs appearing less in results; favicon bug fixed; crawl-stats gap fixed; IRS/federal sites drop (government-side); AI Mode link carousels for developing topics; Stein soliciting AI Mode feature requests; alcohol ads policy update Sept 30; AI Mode sign-in prompt test.

## Meta
- **Ad placements control removed** (~Aug 25), replaced by value rules with a −90% floor; exclusion → suppression. Sequence detailed in conversation track. (Via PPC Land weekly.)
- **Teen settlement product terms** (Aug 26): daily two-hour limit on Instagram/Facebook for ages 13–17, nighttime blocks, parental tools — see industry track.

## Microsoft
- **AI Max rolled out to all Microsoft Advertising accounts** (~Aug 18–24). **Navah Hopkins (Microsoft) clarified on LinkedIn** under Marketing O'Clock's EP 447 post: AI Max is a campaign-level setting (ad-group settings survive); **Max CPC remains for eCPC, Target Impression Share, and Portfolio bidding** ("not every brand can hit the conversion thresholds needed for conversion-based bidding"). Primary: https://www.linkedin.com/posts/marketing-o-clock_digitalmarketingnews-digitalmarketingpodcast-activity-7497639027114872832-ppHQ · Episode: https://poddtoppen.se/podcast/1401725029/marketing-oclock-digital-marketing-news/microsofts-ai-max-is-going-all-around-the-globe
- **AI Max search-term landing page report** (12 default columns) shipped. **Bing testing renaming "Copilot Search" answers to "AI Overview"** (spotted by Sachin Patel). (Via PPC Land weekly.)

## The Trade Desk
- **Zuma released Aug 27** (Q3 update to Kokai): upgraded Koa optimization model claims 32% average CPA cut across 62 campaigns (versus the prior model, not a control); Applied Settings view; Audience Unlimited AI expansion. Closed beta: Koa AI assistant coordinating agents, dynamic frequency management. **Opens its AI layer to external tools including Claude.** Kokai adoption 100%. Goodway Group's Tom Swierczewski praised restored controls. Digiday reporting underlying. (Via PPC Land weekly.)

## Cloudflare
- **Bot Preference Sync** (published Aug 21, rolling to all plans week of Aug 24): auto-writes robots.txt from dashboard AI-bot policies, prepending generated directives. (Via PPC Land weekly.)

## LinkedIn
- Slop button reached mainstream coverage (Fortune Aug 25); rolling out more widely to comments (Search Engine Watch, Sept 1).
