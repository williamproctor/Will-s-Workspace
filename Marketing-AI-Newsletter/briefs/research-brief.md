# Monday Signal research brief (for research agents)

The parent agent gives you: the edition slug (a Monday, YYYY-MM-DD), the coverage window (the Monday through Sunday before it), the production date, and the previous edition's slug. Everything else is here.

## What this is
Monday Signal (mondaysignal.com) is a weekly AI-and-tech briefing for marketers, produced for the GrowthX team (an AI-native growth and content agency). Each Monday edition covers the prior Monday–Sunday and is written from that Monday's vantage point.

Repo: `/workspace/Marketing-AI-Newsletter/`. Read these first:
- `AGENTS.md` (runbook: structure, sourcing rules, QA) and `SOURCES.md` (source lists, discovery vs citable sources).
- `research/<previous slug>/*.md`: the four research files from the last edition. **Copy their format exactly** (headings, "Receipts" bullets, "Comment window", timing notes, origins lines, dropped items). Line 5 of `research/<previous slug>/conversation-<previous slug>.md` is the carry-forward list for your edition: verify each item and use what checks out.
- Prior coverage, so you don't repeat it: `rg -n "^### " editions/<previous slug>.md` plus the two editions before it (`ls editions/` shows slugs). Follow-ups are fine when they carry new facts and are framed as follow-ups.

## Editorial policy (non-negotiable)
1. **Conversation-first.** The edition leads with "The Conversation": the three things marketing X and LinkedIn actually argued about that week (viral campaigns, AI ad backlashes, platform changes practitioners posted about, data posts that went around). Each needs primary receipts: X posts, LinkedIn posts, podcast quotes, conference-stage quotes, verbatim, with speaker, venue, date, and URL.
2. **Cite the origin, not the aggregator.** Roundups (Anicca, Search Engine Roundtable recaps, PPC Land weekly, Agency AEO "The Shift", woozeer, Silverback) are discovery indexes only. For every story, find who broke it or the primary document (company blog or help page, court PDF on CourtListener, regulator release, the original post, the outlet that reported it first) and cite that. No single outlet should dominate an edition.
3. **Verify the date of every candidate.** It must have happened, or been first reported, inside the window. Reposts of old stories get dropped. Stories that started just before the window and played out inside it are "straddles": note the start date plainly.
4. **Post-window facts** (after the window's Sunday, up to the production date) go only in a clearly labeled "Post-window (editor's note only)" line, with date and URL.
5. **Never guess a URL.** Only record URLs you saw in search results or fetched. If you can't find a primary post's URL, say so and attribute via the outlet that embedded it.
6. **Read primary documents for key numbers and names** (court filings, help pages, official posts, report releases). Secondary summaries flatten qualifiers. For timelines, check the product blog's "Updated" banner too: help-center pages can lag it (the Dynamic Search Ads auto-upgrade moved to February 2027 on Google's blog while a help page still said September).
7. **Verbatim means verbatim.** Copy quotes exactly; keep original casing and punctuation. Don't splice.
8. Conflicting numbers: record both, note who got the data first-hand, and prefer that.
9. GrowthX competes with AEO/GEO vendors (Profound, Peec, and others): report their news factually and neutrally.

## Discovery indexes (find stories here, then chase origins)
- Search Engine Roundtable daily recaps (`seroundtable.com/recap-MM-DD-YYYY-NNNNN.html`) and the Friday "Search News Buzz Video Recap" (`seroundtable.com/video-MM-DD-YYYY-NNNNN.html`); search "Search Engine Roundtable daily recap <date>".
- Anicca's Monday roundup: `anicca.co.uk/blog/YYYY-MM-DD-ai-in-marketing-management/`, which usually names sources per story. On the automated run (Monday 08:00 UTC), Anicca, Agency AEO, and woozeer usually haven't published that week's issue yet; lean on Search Engine Roundtable's five daily recaps plus its Friday video recap, and Lift Conversions' "The Lift Brief" (Friday to Friday).
- Agency AEO "The Shift" (`agencyaeo.com/insights/the-shift-...`), woozeer.com/ai-news, PPC Land, Silverback weekly roundups.
- Origin reporting and conversation: Digiday, Adweek, AdExchanger, Ad Age, Marketing Brew, Search Engine Land, Search Engine Journal, Social Media Today, The Verge, TechCrunch, CNBC, Axios, Business Insider, Press Gazette, MediaPost, Retail Brew, Modern Retail, Nieman Lab.
- Conversation-layer searches that work: "marketing LinkedIn debate <topic> <month year>", "viral ad backlash <month year>", "<brand> AI ad backlash X", "<person> LinkedIn post <phrase>". Coverage often embeds the original post (text and date); LinkedIn post URLs show up in search results. A LinkedIn activity ID shifted right by 22 bits is the post's timestamp in ms since the epoch.

## Tools
- WebSearch and WebFetch live in the dynamic `cursor` namespace: call `GetDynamicTools` (namespace "cursor") once, then `CallDynamicTool` with namespace "cursor" and toolName "WebSearch" or "WebFetch". Keep at most 3 web calls in parallel; retry transient errors once.
- Many sites (GeekWire, Search Engine Land, Axios, Forbes, Reuters, Bloomberg, openai.com, Nieman Lab) answer fetches with a Cloudflare 403. That's bot-blocking, not a dead link: confirm the exact URL through a search result instead.
- Large fetch results are written to a file path; read it with the Read tool or `sed -n`.

## What NOT to do
- Don't edit anything outside `research/<your slug>/`. Don't touch editions/, manifest.json, site/, TEAM-MEMORY.md, or git. Don't commit.

## Output
Write four files in `/workspace/Marketing-AI-Newsletter/research/<slug>/`, matching the previous edition's format:
1. `conversation-<slug>.md`: line 3 is the retro-production note ("Produced on <production date> from the Monday-<date> vantage point."), line 5 is "Carry-forward for the <next slug> edition (out of window, verified dates): ..." (scheduled events and developing stories for next week). Then three numbered conversation items, each with a timing note if needed, What happened, Receipts (verbatim quotes with speaker, venue, date, URL), and the Comment window with the take nobody has claimed yet. Then "Considered, not used".
2. `platforms-<slug>.md`: Google Ads, Google Search, YouTube, Meta, Amazon, OpenAI/ChatGPT, Microsoft/Bing, LinkedIn, TikTok, others. Each item gets its date, the facts, verbatim key lines, and an "Origins:" line of links.
3. `industry-<slug>.md`: agencies and holding companies, funding and M&A, measurement studies and data releases, courts, regulators and policy, publishers, commerce and payments. Same format. End with "Dropped on verification or relevance".
4. `analysis-<slug>.md`: retro-production note; "What leads" (proposed news lead, stories 2–6, the three conversation items); "Common-thread candidates" (4); "Angle candidates" (5, each with a Window); "Structure notes" (a Voices list of 8–10 verbatim quotes with URLs, watch-section items, diversity plan, duplication check against prior editions, claims to hold precisely).

Aim for 3 conversation items, about 6 news stories, 8–10 watch items, and 8–10 Voices, each with origin URLs and exact dates. Quality over quantity: an item that can't be verified at the origin gets dropped and listed under "Dropped".

## Return to the parent (under ~600 words)
- The four file paths written.
- Proposed lede in two sentences.
- The three conversation items (one line each, with the best receipt URL).
- The six proposed news stories (one line each, with date and primary URL).
- Post-window facts that deserve an editor's note (date and URL).
- Anything you couldn't verify that a reader might expect to see.
