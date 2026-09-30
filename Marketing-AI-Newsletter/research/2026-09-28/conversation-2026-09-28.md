# Conversation track — week of September 21–27, 2026

Edition date: 2026-09-28. Produced retroactively on 2026-09-30 from the Monday-September-28 vantage point.

Carry-forward for the 2026-10-05 edition (out of window, verified dates): NBC News tests of Muse at big retailers (Sept 29; headline names Walmart); CNN on Muse's partner list and the "keys" problem (Sept 28); Digiday on agencies no longer hiring graduates, from the Sept 24 town hall (reported Sept 28); Profound's Aim demo (Sept 30); AI Max auto-upgrade for DSA/ACA/broad match (September window closes Sept 30); ad-tech joint proposed Final Judgment (~Oct 2); Google's September 2026 spam update completion (two-week rollout from Sept 24); CMA choice-screen consultation closes Oct 9; Ray-Ban Meta Audio ships Oct 13.

## 1. Kalshi's ad copied a creator's video and swapped his face

**What happened:** Wednesday Sept 23, YouTuber Elliot Choy posted side-by-side stills on X: his September 2025 video about moving into a New York apartment and a Kalshi ad that copies it nearly shot for shot (setting, computer, books in the background) with a white man in his place. Futurism says he found it because YouTube served it to him. NPR's Bobby Allyn confirmed it on X the same day. Kalshi's statement to Business Insider (Sept 24): about four months old, made by an agency that supplied the video; Kalshi no longer uses AI-generated content that depicts people and is reviewing the agency relationship; it declined to name the agency.

**Receipts (in window):**
- Elliot Choy (X, Sept 23): "i guess kalshi saw this and thought they should steal my video, turn me into a white dude, and run it as an ad" — embedded verbatim in [Business Insider](https://www.businessinsider.com/kalshi-in-hot-water-over-race-swapping-ai-ads-2026-9). Status URL not surfaced; cite via BI.
- Bobby Allyn, NPR (X, Sept 23): "A Kalshi rep says the ad is old and that they no longer use AI-generated ads." Also: Kalshi is "reviewing our relationship with" the agency. [The Verge, Sept 24](https://www.theverge.com/ai-artificial-intelligence/1000309/youtuber-elliot-choy-says-an-ai-kalshi-ad-stole-one-of-his-videos-and-changed-his-race) · [Futurism, Sept 24](https://futurism.com/artificial-intelligence/kalshi-admits-random-guy-video-ai-race-swap-ad)
- Pushpek Sidhu (Toronto creator; posted in June about a Kalshi ad replicating his World Cup video, script and gestures, with a white man in his place), to BI: "They could easily pay me a little bit."
- Mick Feldman, The Now (influencer agency), to BI: swapping a creator's face without consent is "completely unethical"; licensing an existing video typically costs about a quarter of making a new one with the creator.
- Zohaib Ahmed, Resemble AI, to BI: about 9% of ads in Meta's ad library in recent months contain generative AI.
- Dated context (prior window): Keaton Inglis, Kalshi head of growth, LinkedIn, Sept 9 (activity ID decodes to 2026-09-09 21:26 UTC): "We were the first brand to run a 100% AI-generated ad on broadcast. Then, while every other brand spent the next quarter figuring out how to make AI ads, we pivoted in the opposite direction: all-in on unmistakably human creativity." [Post](https://www.linkedin.com/posts/keatoninglis_why-kalshi-dropped-generative-ai-in-favor-activity-7503564502940925952-BmHz). Futurism also quotes his Ad Age line ("as human… as possible going forward").
- Industry echo, same week: Digiday's AI Marketing Strategies town hall (Sept 24, Chatham House): "It's like there's a growing acceptance of 'good enough — go.' I've seen lots of creative executions from our agencies, and our logo isn't right." [Digiday, Sept 25](https://digiday.com/marketing/marketers-bemoan-the-culture-of-good-enough-go-as-standards-fall-amid-the-ai-bubble/)

**Same-day platform context:** YouTube's Made on YouTube (Sept 23) took likeness detection to mobile and said voice detection is coming "later this year." Framing note: likeness detection matches a creator's face; the Kalshi ad kept everything except the face. Don't claim YouTube's tool would or wouldn't have caught it.

**Continuity:** last week's lead conversation was Novig's Sweeney ad (prediction-market marketing); Sept 21 watch section covered Microsoft's rule that a label doesn't save an unauthorized likeness.

**Comment window:** open. The take: "the agency made it" doesn't move the blame; Choy's post named Kalshi. Contract language for generated people is now a brand-safety item, and licensing is cheap by comparison.

## 2. Google switched on AI Mode checkout for Shopify stores by default

**What happened:** Tuesday Sept 22, Merchant Center emails told merchants: "Your Shopify store was matched to your Merchant Center, enabling native checkout on Google AI Mode and Gemini." And: "To be eligible, your products must be published on your Shopify storefront and available in Merchant Center. Eligible products are automatically included. There's nothing for you to set up." UCP checkout had been live for limited merchants since February; the wider rollout began Friday Sept 18. Opt-out: Shopify admin > Sales channels > Agentic (products stay discoverable; buyers are sent to the merchant's own checkout).

**Receipts:**
- Menachem Ani (JXT founder) posted the email on X; Mike Ryan (Smarter Ecommerce) asked whether it needed enabling; Ani: "No action on our end." [Search Engine Land](https://searchengineland.com/google-opens-native-ai-checkout-to-eligible-shopify-merchants-490407) · [Search Engine Roundtable, Sept 22](https://www.seroundtable.com/google-native-checkout-emails-42140.html)
- Nic McDonough posted the checkout live that morning (per SER). Sachin Patel's write-up: [Search Engine Watch, Sept 23](https://searchenginewatch.com/google-native-checkout-now-available-to-more-users/)
- **Primary document:** Shopify Help Center, "Selling on Google AI Mode and Gemini": "Purchasing in direct checkouts is activated by default for eligible stores"; "Google Analytics and custom pixels won't fire in Google AI Mode and Gemini's direct checkout. The checkout fires only server-to-server pixels (started, completed), so none of the standard or custom client side pixels fire." [Help page](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/google) (403 to bots; text confirmed via search index). Agentic storefronts overview: "active by default for eligible stores," covering ChatGPT, Google AI Mode and Gemini, Microsoft Copilot, and Meta surfaces such as Muse; AI-channel orders show in Shopify admin "with channel or referrer attribution." [Overview](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts)
- elsop's "GA4 doesn't fire" claim is now verified at the origin (Shopify's help page); cite Shopify, not elsop.
- PPC Land framed it as "without asking" and dated the March help page's early-access queue. [PPC Land](https://ppc.land/google-switched-on-ai-mode-checkout-for-shopify-stores-without-asking/) — use at most once.

**Comment window:** open through holiday code freeze. The take: default-on is how the AI checkout war is being fought; audit Sales channels > Agentic and reconcile AI-channel revenue in Shopify, since GA4 and browser pixels miss it.

## 3. AI Overviews got more links. Some of them lead to AI Mode.

**What happened:** Monday Sept 21, two posts. Malte Landwehr (Peec AI) on X: "Google massively increased the number of external links within AI Overview answers." Peec's chart ("External links in AI Overviews rise to 26%"): share of AIOs with an external link inside the answer text, daily average Aug 25–Sept 20, near zero until a step at "11 Sep," 26.2% on Sept 20. Earlier the same day, Gagan Ghotra posted an 18-second recording of bold, underlined AIO text that opened AI Mode instead of a site: "🆕 in AI Overviews answers Google is now testing showing anchor links which instead of taking to a webpage takes to AI Mode. Another day – Another Tactic! from Google to push users from usual search results to AI Mode #SEO".

**Receipts:**
- Both posts quoted verbatim (embedded tweets) in [Search Engine Journal, Sept 25](https://www.searchenginejournal.com/google-ai-overviews-have-more-links-but-not-all-reach-the-web/590762/) (Matt Southern). SEJ: Landwehr said in replies that if prompts changed "it was a small percentage"; his speculation that "over time more and more links will become links redirecting users to AI Mode."
- Barry Schwartz: "This doesn't 'feel' right to me but I think I should share this data point" — plus disclosure of a small investment in Peec. [SER, Sept 23](https://www.seroundtable.com/google-ai-overviews-more-external-links-42135.html)
- Search Console rules (via SEJ): a click on an external link in an AIO counts as a click; "If a link is a query refinement link, clicks and impressions are not counted for that link." The help pages don't say whether Ghotra's element is a refinement. The generative AI performance report (rolled out to all sites Aug 31) shows impressions only, no clicks or CTR.

**Comment window:** open while the chart circulates. The take: a link count is inventory, not traffic; check where the links go.

## Considered, not used as conversation items
- **Converse pulls Karina ad over KKK/lynching imagery** (apology Friday Sept 18; pulled, per ABC via Reuters, Sept 21; CEO Aaron Cain memo via Bloomberg). Not AI or tech; prior-window apology. Dropped. [Reuters](https://www.reuters.com/business/media-telecom/converse-pulls-ad-apologizes-after-backlash-over-alleged-kkk-imagery-abc-news-2026-09-22/)
- **Muse vs Amazon** had the biggest X moment of the week (Tobi Lütke's Sept 21 post) but carries the news lead instead.
- **Novig follow-ups** (CAD Management mention data via Yahoo) — covered last week; not repeated.
