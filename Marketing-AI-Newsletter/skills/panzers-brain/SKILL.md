---
name: panzers-brain
version: 1.1.4
description: |
  Panzer's complete editorial intelligence — audit content quality AND fix it in one pass.
  Combines the Content Audit framework (5 quality dimensions, scoring, pattern identification)
  with the Humanizer framework (35 AI-ism patterns, rewriting, personality injection).
  Use when reviewing, editing, or rewriting any written content. Built from analysis of
  247 professional editorial comments, Wikipedia's "Signs of AI writing" guide, Pangram Labs
  research, and published LLM-vocabulary studies (Kobak et al., Liang et al., Reinhart et al.).
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# Panzer's Brain

The complete editorial skill. Audit content quality, identify every AI fingerprint, rewrite to fix, and inject real personality — all in one pass.

This skill merges two proven frameworks:
- **Content Audit** — 5 quality dimensions built from 247 professional editorial comments
- **Humanizer** — 35 AI-ism detection patterns from Wikipedia's "Signs of AI writing" guide, Pangram Labs research, and published LLM-vocabulary studies

## When to Use This Skill
- Reviewing AI-generated or AI-assisted content drafts
- Rewriting content to remove AI patterns and add personality
- Conducting quality assessments of articles, blog posts, or marketing copy
- Training content teams on editorial best practices
- Preparing editorial feedback with concrete fixes
- Any writing task where the output needs to sound human

---

## PHASE 1: AUDIT

Scan the content against all five quality dimensions. Score each one. Identify every issue before touching a word.

### Dimension 1: Specificity & Substance (25.8% of issues — Highest Priority)

**Check for:**
- Vague claims without supporting details
- Missing examples, statistics, or concrete illustrations
- Placeholder-style language that sounds correct but lacks depth
- Generic statements that could apply to any company or situation

**Red flags:** "various tools", "common errors", "many factors", "This is a prime opportunity to..." (without specifics)

**Fix:** Ask "Can this be illustrated with a product name, stat, use case, or scenario?" Require at least one concrete example per major claim.

### Dimension 2: Structure & Flow (12.9% of issues)

**Check for:**
- Paragraph uniformity (same length, same pattern)
- Missing transitions between ideas
- Abrupt topic jumps
- Lack of topic sentences and connective tissue

**Red flags:** "Why is this here?" moments, chunky paragraphs stacked without variation, missing setup for new ideas

**Fix:** Add transitional phrases and topic sentences, vary paragraph lengths, use signposting ("First," "However," "This means that..."), ensure each section builds on the previous one.

### Dimension 3: AI Fingerprints (6.0% of issues — Critical for Brand Trust)

This is the big one. 35 distinct patterns organized into six categories. Scan for all of them.

#### Content Patterns

**3a. Inflated Significance & Legacy**
Words to watch: stands/serves as, is a testament/reminder, vital/significant/crucial/pivotal/key role/moment, underscores/highlights importance, reflects broader, symbolizing ongoing/enduring/lasting, setting the stage for, marking/shaping the, represents a shift, key turning point, evolving landscape, indelible mark, deeply rooted

Before: "The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions."
After: "The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office."

**3b. Undue Emphasis on Notability**
Words to watch: independent coverage, local/regional/national media outlets, active social media presence

Before: "Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers."
After: "In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods."

**3c. Superficial -ing Analyses**
Words to watch: highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

Before: "The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land."
After: "The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast."

**3d. Promotional Language**
Words to watch: boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

Before: "Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty."
After: "Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church."

**3e. Vague Attributions & Weasel Words**
Words to watch: Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

Before: "Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem."
After: "The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences."

**3f. Formulaic "Challenges and Future Prospects"**
Words to watch: Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

Before: "Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges... Korattur continues to thrive as an integral part of Chennai's growth."
After: "Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods."

**3y. Manufactured Discourse**
Claims that a subject "sparked debate" or "prompted reflection" with no actual source — discourse invented to make the subject sound consequential. RAG-era chatbots now attach these to named sources regardless of what the source said, so verify any "X highlighted/noted" claim against the source.

Words to watch: has sparked, generated debate about, prompted broader reflection on, raising questions about, shaped emerging policy discussions

Before: "GriefBots have prompted broader reflection on mortality and memory in a digital age."
After: "A 2025 Pew survey found 23% of respondents had used an AI companion app after a bereavement."

**3z. Stock Openers & Narrative Clichés**
Each genre gets a canned opener: emails start "I hope this email finds you well," reviews start "I recently had the pleasure of," cover letters work in "keen." Pangram's n-gram data shows some phrases run 10,000–50,000x more common in AI text: "as a poignant" (49,000x), "reminder of the enduring" (31,000x), "into the complex interplay" (21,000x), "in the ever-evolving" (11,000x).

Words to watch: I hope this email finds you well, I recently had the pleasure of, stark reminder, newfound sense of purpose, faced numerous challenges, couldn't help but feel, a sense of unease/solace washed over, unwavering, unyielding, cautionary tale, the human spirit, turn of events, air thick with, heart pounding

Fix: Delete the opener and start with the actual point. Replace narrative clichés with the specific detail they're papering over.

**3aa. Proper-Noun Avoidance & Generic Specifics**
AI dodges proper nouns and concrete facts, smoothing rare specifics into transferable generalities — "inventor of the first train-coupling device" becomes "a revolutionary titan of industry." The subject ends up simultaneously less specific and more exaggerated. When forced to pick names, AI picks the most generic ones (Pangram: 60–70% of AI-generated character names are "Emily" or "Sarah").

The tell: a paragraph that could apply to any company, person, or product with the nouns swapped.

Fix: Reverse the regression. Restore product names, model numbers, dates, dollar figures, and people. (This is Dimension 1 — the two reinforce each other.)

**3bb. Didactic Disclaimers**
Advice-style caveats injected into informational prose, addressed to an imagined reader — residue of assistant training.

Words to watch: it's important/crucial to note/remember/consider, worth noting, may vary, always consult a professional, be sure to check

Before: "The tax credit can reach $7,500, though it's important to note that eligibility may vary, so always consult a tax professional."
After: "The tax credit can reach $7,500 for vehicles assembled in North America under the 2022 rules."

**3cc. Restating Conclusions**
Conclusions that are long, open with a summary marker, and repeat most of what was already written. Human conclusions are shorter and add something — a next step, a date, an open question.

Words to watch: In summary, In conclusion, Overall, To sum up, a "Conclusion" heading in a piece that shouldn't have one

Fix: Cut the restatement. End on the last piece of new information, or a concrete next step.

#### Language & Grammar Patterns

**3g. Overused AI Vocabulary**
High-frequency AI words: Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

Statistically validated additions (Kobak et al. analyzed 14M+ PubMed abstracts; Liang et al. analyzed peer reviews): meticulous/meticulously, commendable, notable/notably, versatile, realm, ever-evolving, seamless/seamlessly, multifaceted, comprehensive (reflexive), invaluable, noteworthy. The excess words are overwhelmingly style words — verbs and adjectives — not topic nouns.

These appear far more frequently in post-2023 text and often co-occur.

Before: "Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet."
After: "Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south."

**3h. Copula Avoidance**
Words to watch: serves as/stands as/marks/represents [a], boasts/features/offers [a]

LLMs substitute elaborate constructions for simple "is"/"are"/"has."

Before: "Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet."
After: "Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet."

**3i. Negative Parallelisms**
"Not only...but..." and "It's not just about..., it's..." are massively overused.

Before: "It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement."
After: "The heavy beat adds to the aggressive tone."

**3j. Rule of Three Overuse**
AI forces ideas into groups of three to appear comprehensive.

Before: "The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights."
After: "The event includes talks and panels. There's also time for informal networking between sessions."

**3k. Synonym Cycling (Elegant Variation)**
Repetition-penalty code causes excessive synonym substitution.

Before: "The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home."
After: "The protagonist faces many challenges but eventually triumphs and returns home."

**3l. False Ranges**
"From X to Y" constructions where X and Y aren't on a meaningful scale.

Before: "Our journey has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter."
After: "The book covers the Big Bang, star formation, and current theories about dark matter."

**3dd. Stiff Synonym Substitution**
Beyond copula avoidance, AI systematically picks the formal or euphemistic synonym over the plain verb: authored (wrote), relocated (moved), utilized (used), attempted (tried), perished (died), commenced (started), endeavored (tried), procured (got). Plain verbs are a sign of human writing — restore them.

Before: "She authored three reports and relocated to Austin, where she utilized her network to procure funding."
After: "She wrote three reports and moved to Austin, where she used her network to get funding."

**3ee. Suspiciously Clean Copy**
Mechanical perfection is itself a tell when it clusters: zero typos, no fragments or run-ons, never starts a sentence with "And" or "But," perfectly consistent Oxford commas, almost no contractions, and — notably — no semicolons or parentheses (everything funnels through em dashes). Also watch for English-variety mismatch (e.g., flawless American spelling from a UK author) and abrupt style shifts mid-document where pasted AI text begins.

Fix: Use contractions where the register allows. Let a sentence start with "But." Vary the punctuation diet.

#### Style Patterns

**3m. Em Dash Overuse**
AI uses em dashes (—) more than humans. Replace most with commas or periods. The companion tell (Pangram): underuse of semicolons and parentheses — AI funnels every aside through em dashes, so a text with many dashes and zero semicolons/parens is doubly suspect.

**3m-ii. Declarative Kicker (Panzer's specific hate)**
A short statement — attached via em dash OR standing alone as its own sentence — that just confirms or restates what was already said. Sounds punchy but adds nothing. The tell: if you remove it, the meaning is identical. (A second half that *isn't* deletable but exists only to land a twist is 3m-iv, not this — don't let the deletability test clear it.)

Words/constructions to watch: "This is the fix.", "It's moving.", "The trend is real.", "The gaps are real.", "The risk is real.", "The opportunity is real.", "The [X] is real." (and the coordinate form "…, and the gaps are real." tacked onto a prior clause), "That's the point.", "This matters.", "It's working.", "That's it.", "This is why.", "And it shows.", "That's the difference." — and any variant where the sentence could be deleted without losing information. The "[X] is real" family asserts significance instead of showing it; if the gaps are real, name a gap — don't announce its realness.

**The "trap / catch / rub" faux-insight labeler (Panzer's specific hate — added v1.1.1).** A subspecies of the kicker that frames the previous point as a hidden gotcha to manufacture insight. The tell: it announces that something is tricky/important instead of just stating the substance. Almost always deletable, or foldable into the prior sentence.
Words/constructions to watch: "and that's the trap.", "Here's the trap:", "the trap is...", "that's the catch.", "here's the catch.", "here's the rub.", "that's the mistake (most teams make).", "and that's where it gets tricky.", "the gotcha is...", "here's the thing:", "but here's the kicker."
Before: "A GSC impression at position 24 isn't a citation. Not on its own — and that's the trap."
After: "A GSC impression at position 24 isn't a citation; it just means you ranked deep and nobody scrolled."

**The statement–reinforcement (Panzer's specific hate — added v1.1.2).** A claim, then an em dash, then a restatement/escalation of the same claim for drama — often negating a weak quoted version first ("doesn't explain *some* — it explains all"). Both halves say one thing. Fix: make it one direct statement; don't stage it. (When the two halves genuinely conflict instead of restating — the second shrinking or re-reading the first — it's 3m-iv.)
Words/constructions to watch: "X doesn't do A — it does B.", "doesn't 'explain some of the gap' — it explains basically all of it.", "isn't just A — it's B.", "not A — A by a mile.", "X isn't the problem — Y is."
Before: "Position 24 doesn't 'explain some of the gap' — it explains basically all of it."
After: "Position 24 explains basically all of the gap."

**The dramatic colon setup (Panzer's specific hate — added v1.1.2).** A colon — often after "so let me be blunt" / "the reality" — used mid-sentence to tee up a punchy declaration and manufacture gravity. Delete the windup; state the thing.
Words/constructions to watch: "so let me be blunt:", "Here's the truth:", "The reality:", "The answer is simple:", "Let me be honest:", "Bottom line:", "Here's what's actually happening:" — any colon whose only job is a drumroll.
Before: "…so let me be blunt: I don't think this is an AEO win."
After: "I don't think this is an AEO win."

**The definitional colon-unpack (Panzer's specific hate — added v1.1.3).** An abstract noun or claim, then a colon, then a parallel list (usually a triple) that only re-states the abstract term in concrete-sounding fragments. The colon promises a definition; the list delivers throat-clearing — the items rename the concept instead of advancing it. Distinct from the dramatic colon above: that one manufactures gravity, this one manufactures rigor. The tell: the abstract-noun-plus-colon is deletable, and what follows is either the real content (lead with it) or empty parallelism (cut it). Frequently chained with the "[X] is real" reinforcer as the very next sentence — kill both. Watch too for a doubled citation around it ("Source X reports… , according to Source X") and a tidy aphorism closing it out ("the same mention lands differently depending on where it sits").
Words/constructions to watch: "[abstract term]: how A, where B, and whether C", "X, including whether it appears, how it's described, and whether it shapes…", "X replaces Y with Z: [parallel triple]", "assign roles to platforms: Reddit for…, LinkedIn for…" — any "[abstract term]: [parallel triple]" where the triple defines the term rather than listing genuinely new specifics.
Before: "AEO sits inside a larger discipline most teams call AI visibility: how your brand shows up across AI-generated answers, including whether it appears, how it's described, and whether it shapes the category narrative."
After: "AI visibility is the bigger picture AEO sits inside. It asks whether your brand appears in AI answers, how they describe it, and whether it shapes the category."
Before: "AEO measurement replaces keyword rankings with citation-based metrics: how often you're cited, where you sit in the answer, and your share of voice against competitors. The traditional analytics stack was not built for this, and the gaps are real."
After: "AEO measurement tracks how often you're cited, where you sit in the answer, and your share of voice. Your existing analytics stack captures none of it."

Before (em dash form):
> "TTD moved 64m → 42m this week on pipeline automation. 12-week avg is 1h 35m — the trend is real, not a one-week blip."
> "Been circling this for months — it's moving."

Before (standalone sentence form):
> "Artifact/pipeline mismatches have been dragging TTD for months. This is the fix."
> "Been circling this for months. It's moving."

After:
> "TTD moved 64m → 42m this week on pipeline automation. 12-week avg is 1h 35m. Not a one-week blip."
> "Been circling this for months."
> "Artifact/pipeline mismatches have been dragging TTD for months — Jenn's artifact updater tool shared with the full team this week."

Fix: Delete the kicker. If the sentence following adds genuinely new information (a name, a number, an action), keep it and rewrite it to lead with that information instead of restating the previous sentence.

**3m-iii. Declarative Setup (Panzer's other specific hate)**
A short sentence that labels or previews what's about to be said instead of just saying it. The mirror of the Declarative Kicker: one labels before, the other restates after. Both are AI throat-clearing. The tell: if you delete the opener, the sentence underneath carries the same meaning with less friction.

Comes in a few common flavors:
- **Topic labeler:** "The [X] was the headline." / "[X] is part of it." / "That's the core of it."
- **Reader validator:** "You read the situation right." / "You called it." / "You're not wrong."
- **Importance flag:** "The [X] is real." / "This matters." / "Here's the thing:" / "Here's what counts:"
- **Meta-preview:** "What sets it apart is..." / "The point is..." / "What's interesting here is..."

Before (topic labeler):
> "The sprint recovery was the headline. Yellow/red in week 5, sprint-to-retainer conversion and $120k upsell by week 9, because you and Sydney diagnosed the root cause, scheduled the calibration, and rebuilt the artifacts over a weekend."

After:
> "Yellow/red in week 5, sprint-to-retainer conversion and $120k upsell by week 9 — you and Sydney diagnosed the root cause, scheduled the calibration, and rebuilt the artifacts over a weekend."

Before (topic labeler):
> "The Ramp close is part of it. George's note on April 6 said it plainly: couldn't have done it without you."

After:
> "George's note on April 6 on the Ramp close: couldn't have done it without you."

Before (reader validator):
> "You read the situation right. You've been doing ME-level work for months — managing three accounts, handling manual publishing on Smith AI when automation didn't cover the workflow, and running pre-client QA that CMs don't usually touch."

After:
> "You've been doing ME-level work for months: managing three accounts, handling manual publishing on Smith AI when automation doesn't cover the workflow, and running pre-client QA that CMs don't usually touch."

Before (importance flag + meta-preview):
> "The volume is real, but what sets it apart is that none of it comes back with rework flags."

After:
> "320 pieces in Q1 and none of it comes back with rework flags."

Fix: Delete the preamble. Lead with the specific information — the number, name, action, or quote. If the preamble contained a real claim ("the volume is real"), fold the underlying fact into the next sentence as a concrete detail instead of a label. The pattern is a tell because LLMs generate these openers as a hedge — a verbal signpost that says "a point is coming" in place of actually making the point.

**3m-iv. Twist Endings — Reinterpretation and Reversal (BANNED — added v1.1.4)**
Both shapes hold back the sentence's real content so the ending can land as a surprise. **This is a ban, not a judgment call.** Neither shape ships — not in headlines, not in marketing copy, not in Slack, not in docs. There is no version of the construction that earns its place, so do not weigh whether a particular instance works.

- **Reinterpretation (the true paraprosdokian).** The ending forces you to re-read the opening as something other than what it appeared to mean. "I've had a perfectly wonderful evening — but this wasn't it." The first half is built to be misread on purpose.
- **Reversal / antithesis.** An expansive or quantified first clause, then a clause that shrinks, negates, or exempts it. "Four steps, and only one of them is yours."

Distinct from the Declarative Kicker (3m-ii) and the statement–reinforcement, which both fail on redundancy. Here the second half is the payload, not a restatement, which is exactly how it slips past a deletability check — a non-deletable second half is not a defense. Also don't let real underlying facts launder the shape: "Four steps, and only one of them is yours" never says which step, what the other three are, or who performs them, and even when it does, the staged contrast goes.

Words/constructions to watch: "N things, and only one of them is X", "A thousand X — you'll only ever Y", "Everything about X changed. Your Y didn't.", "All of it, except the part that matters.", "X, and none of it is Y.", "…but that wasn't it.", "Y of them. One that counts." — any second clause whose job is the reversal.

Two markers make it findable: an **absolute or round number** in the first clause (everything, all, a thousand, four steps) and a **terse deflating flip** in the second (only one, none, didn't, except). Either one alone is fine; together they're the banned shape — and the ban follows them across sentence and paragraph boundaries, so a period or a line break between the beats is not a fix.

Before: "Four steps, and only one of them is yours."
After: "You approve the brief. The pipeline handles research, drafting, and QA."

Before: "A thousand integrations, and you'll only ever click one."
After: "Connects to Slack, HubSpot, Salesforce, and 1,000+ other tools."

Before: "Everything about billing changed. Your invoice didn't."
After: "Billing moved to Stripe this month. Your invoice arrives on the 1st as usual, same format and totals."

Fix: state the new situation concretely and positively. Drop the absolute, drop the negation, and describe what is rather than what isn't.

**The negative half doesn't get stated at all.** There is no rewrite that keeps both beats — splitting them into two sentences, two paragraphs, or a bullet pair doesn't fix it, because the paired change/no-change and many/few beat isn't a construction natural writing reaches for. Where sameness genuinely matters to the reader, it comes through as description of the new state ("arrives on the 1st as usual, same format and totals"), never as a claim that something didn't change. If the only content on one side of the contrast is its contrast with the other side, that side is rhetoric — cut it and keep the concrete half.

**3n. Overuse of Boldface**
AI emphasizes phrases in boldface mechanically. Strip bold from inline terms unless genuinely needed.

**3o. Inline-Header Vertical Lists**
Lists where items start with bolded headers followed by colons. Convert to flowing prose when possible.

Before:
> - **User Experience:** The user experience has been significantly improved.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

After: "The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption."

**3p. Title Case in Headings**
AI capitalizes all main words. Use sentence case: "Strategic negotiations and global partnerships" not "Strategic Negotiations And Global Partnerships."

**3q. Emojis in Headers/Lists**
AI decorates headings or bullet points with emojis. Remove them.

**3r. Curly Quotation Marks**
Primarily a ChatGPT/DeepSeek tell — Gemini and Claude typically don't use them, and Word/macOS/CMS typography produces them innocently. The stronger signal is inconsistent mixing of curly and straight quotes in one text. Normalize to one style.

**3ff. Uniform Rhythm (Low Burstiness)**
Human writing is bursty — short punchy sentences clustered against long winding ones. AI regresses to a mean sentence length, and paragraphs come out eerily equal in size, often in a neat intro / 3-body / conclusion mold with a bullet list dropped mid-piece. GPTZero quantifies it: burstiness below ~0.30 signals AI; humans typically run 0.65–0.85.

Fix: Covered by Rewriting Rule 5 — but treat uniformity as a detection signal, not just a style preference.

#### Communication Artifacts

**3s. Chatbot Artifacts**
Strip: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**3t. Knowledge-Cutoff Disclaimers**
Strip: as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**3u. Sycophantic/Servile Tone**
Strip: Great question!, That's an excellent point, You're absolutely right

**The flattering-question opener (Panzer's specific hate — added v1.1.2).** Opening a reply by praising the question and inflating it into a grand tension before answering — "Good question — and it's exactly the [tension/thing] our whole [X] rides on, so let me be blunt…". It flatters, manufactures stakes, and throat-clears in one move. Cut the entire windup; answer in the first sentence.
Before: "Good question — and it's exactly the tension our whole editorial bet rides on, so let me be blunt: I don't think this is an AEO win."
After: "I don't think this is an AEO win; the page just ranks on page 3."

**3gg. Paste Artifacts & Placeholder Text**
Machine residue that survives copy-paste — near-definitive proof of unreviewed AI output:
- ChatGPT citation placeholders: citeturn0search0, turn0image0, :contentReference[oaicite:0]{index=0}, oai_citation, stray "+1" after source names
- Tracking parameters on cited URLs: utm_source=chatgpt.com, utm_source=openai, utm_source=copilot.com, referrer=grok.com
- Unfilled templates: [Your Name], [Entertainer's Name], INSERT_SOURCE_URL, PASTE_YOUTUBE_VIDEO_URL_HERE, access-date=2025-XX-XX
- Stray ↩ footnote-return characters

**3hh. Markdown Bleed & Gratuitous Tables**
Raw Markdown surviving in non-Markdown contexts (\*\*bold\*\*, ## headings, [text](url), fenced code blocks, `---` breaks before every heading), headings that skip a level, and small two-column tables ("Metric | Figure") presenting trivia better written as prose. Markdown alone is a weak tell; mixed with faulty native markup it's strong.

**3ii. Citation Red Flags**
Checkable forensics on AI-drafted citations: multiple broken links with no archive copies (they never existed), ISBNs that fail checksum, DOIs that don't resolve or resolve to real-but-unrelated papers, book citations with no page numbers (or unverifiable ones), access-dates predating the draft, and the same reference re-cited after every single sentence. Spot-check every citation in an AI-assisted draft before it ships.

#### Filler & Hedging

**3v. Filler Phrases**
- "In order to achieve this goal" -> "To achieve this"
- "Due to the fact that" -> "Because"
- "At this point in time" -> "Now"
- "In the event that you need help" -> "If you need help"
- "The system has the ability to" -> "The system can"
- "It is important to note that the data shows" -> "The data shows"

**3w. Excessive Hedging**
Before: "It could potentially possibly be argued that the policy might have some effect on outcomes."
After: "The policy may affect outcomes."

Important refinement (Reinhart et al., PNAS): ordinary epistemic hedges — "perhaps," "tends to," "I think," "very" — are actually MORE common in human writing; LLMs avoid them. The AI tell is stacked hedge-words in one clause and assistant-voice caveats (see 3bb), not hedging itself. Don't strip a writer's natural qualifiers.

**3x. Generic Positive Conclusions**
Before: "The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction."
After: "The company plans to open two more locations next year."

#### What NOT to Flag (Ineffective Indicators)

Per Wikipedia's AI Cleanup project and Originality.ai's 10M-term analysis, these are NOT valid AI tells on their own — don't flag them:
- Perfect grammar or formal register (plenty of humans write cleanly)
- Transition words in isolation ("however," "moreover")
- "Bland" or "robotic" feel without a specific pattern to point to
- Any single vocabulary word — the signal is co-occurrence and density, not one "delve"
- Curly quotes from a Word/CMS workflow

Tells are also model-specific and time-decaying: broader-context/legacy framing is characteristic of ChatGPT and Grok but much less of Gemini/Claude, and several classic tells (knowledge-cutoff disclaimers, "In conclusion" sections) are now mostly historical (2023–24). Weigh density and clustering of patterns, not any single hit.

#### Signs of Human Writing (Keep These)

The inverse list — when rewriting, these are features, not bugs:
- Plain verbs: wrote, moved, used, tried, died, got
- Simple constructions: "there is a," "it has a"
- Natural epistemic hedges: "perhaps," "I think," "tends to"
- Sentence fragments. Starting with "And" or "But."
- Semicolons and parentheses (asides not funneled through em dashes)
- Definitive claims and superlatives with a stake: "was the first," "the best tool we tested"
- First-person specifics tied to real experience

### Dimension 4: Voice & Tone

**Check for:**
- Emotional resonance and warmth
- Natural cadence and rhythm
- Personality appropriate to brand/audience
- Conversational cues and natural transitions

**Red flags:** Flat, emotionless prose; overly formal language inappropriate for context; lack of personality or brand voice; syntactically correct but bland

**Fix:** Read aloud for rhythm, use natural transitions ("So what does this mean?"), add conversational elements appropriate to context, match formality to audience.

### Dimension 5: Content Necessity & Focus (1.6% of issues)

**Check for:**
- Relevance of each paragraph to article promise
- Off-topic detours and unnecessary tangents
- Clear purpose for every section

**Red flags:** "Is this client-requested?" uncertainty, paragraphs that don't advance the main point

**Fix:** Apply "do we need this?" filter to every paragraph. Cut or reframe content that doesn't belong.

---

## PHASE 2: REWRITE

After auditing, fix what you found. Don't just remove bad patterns — inject actual personality.

### The Rewriting Rules

1. **Preserve meaning** — Keep the core message intact
2. **Match voice** — Match the intended tone (formal, casual, technical, etc.)
3. **Add soul** — Don't just clean up; inject personality
4. **Be specific** — Replace vague with concrete
5. **Vary rhythm** — Short punchy sentences. Then longer ones that take their time. Mix it up.
6. **Have opinions** — Don't just report facts, react to them
7. **Acknowledge complexity** — Real humans have mixed feelings
8. **Use "I" when it fits** — First person isn't unprofessional
9. **Let some mess in** — Perfect structure feels algorithmic
10. **Be specific about feelings** — Not "this is concerning" but "there's something unsettling about agents churning away at 3am while nobody's watching"

### Signs of Soulless Writing (Clean But Still AI)

Even with zero AI-ism patterns, writing can still read as AI if:
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

### Before (Clean but Soulless)
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (Has a Pulse)
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle — but I keep thinking about those agents working through the night.

---

## PHASE 3: ANTI-AI AUDIT PASS

After rewriting, run the final two-step check:

1. **Ask:** "What makes the below so obviously AI generated?"
   - Answer briefly with remaining tells (if any)
2. **Then:** "Now make it not obviously AI generated."
   - Revise accordingly

This catches patterns you missed in Phase 1 and soullessness you didn't fix in Phase 2.

---

## OUTPUT FORMAT

### Quick Audit + Fix (default)

```
Content Audit: [Title]
Overall Quality Score: X/10

Strengths:
- [Strength 1]
- [Strength 2]

Priority Issues Found:
1. [Issue with count/percentage and locations]
2. [Next issue]
3. [Third issue]

---

[Rewritten content]

---

Anti-AI Audit:
- Remaining tells: [brief bullets, or "None detected"]
- [Final revision if needed]

Changes Made:
- [Summary of what changed and why]
```

### Detailed Report Format

```
Comprehensive Content Audit + Rewrite

1. SPECIFICITY ANALYSIS
Total paragraphs: X
Paragraphs lacking specific examples: Y (Z%)
Most common vague claims: [list]

2. STRUCTURAL ANALYSIS
Transition quality: [Score/10]
Paragraph variety: [Score/10]
Logical flow: [Score/10]

3. AI FINGERPRINT ANALYSIS
Patterns detected: [list by category]
Robotic phrases: X instances
Top phrases to eliminate: [list]

4. VOICE & TONE ANALYSIS
[Assessment]

5. CONTENT FOCUS ANALYSIS
Off-topic paragraphs: X
Unclear purpose sections: Y

---

REWRITE:
[Full rewritten content]

---

ANTI-AI AUDIT:
Pass 1 — "What makes this obviously AI?" [bullets]
Pass 2 — Final revision applied: [yes/no, with notes]
```

---

## QUALITY BENCHMARKS

**Excellent (9-10/10)**
- <10% of paragraphs lack specific examples
- No AI fingerprints detectable across all 35 patterns
- Varied paragraph structure throughout
- Clear, engaging human voice with personality
- Every paragraph serves the article's purpose

**Good (7-8/10)**
- <20% of paragraphs lack specificity
- Minor AI fingerprints in 1-2 places
- Mostly varied structure with occasional uniformity
- Generally human voice with rare flat moments
- 1-2 paragraphs may need tightening

**Needs Revision (5-6/10)**
- 20-40% of paragraphs are vague
- Multiple AI fingerprints visible
- Noticeable structural stiffness
- Tone is serviceable but bland
- Some off-topic content

**Requires Significant Rework (<5/10)**
- >40% of paragraphs lack substance
- AI fingerprints throughout
- Rigid, uniform structure
- Robotic voice dominates
- Content focus unclear

---

## PRE-PUBLICATION CHECKLIST

Before content goes live, verify:
- [ ] Specificity: Every claim has supporting detail
- [ ] AI detox: All 35 patterns scanned, none remain
- [ ] Twist endings: zero reinterpretation or reversal constructions (3m-iv is a hard ban)
- [ ] Structure: Varied paragraphs, clear transitions
- [ ] Voice: Sounds human, has personality, passes read-aloud test
- [ ] Focus: Every paragraph earns its place
- [ ] Anti-AI pass: Two-step audit completed, no remaining tells
- [ ] Soul check: Has opinions, varied rhythm, acknowledges complexity

---

## REFERENCE

Content Audit framework built from analysis of 247 professional editorial comments across GrowthX client content.

AI fingerprint patterns based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Key insight: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

v1.1.0 additions (June 2026 research pass) sourced from:
- [Pangram Labs — comprehensive guide to spotting AI writing patterns](https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns) and [AI phrases n-gram data](https://www.pangram.com/blog/pangram-ai-phrases)
- Kobak et al., Science Advances 2025 — "excess vocabulary" in 14M+ PubMed abstracts ([word list](https://github.com/berenslab/llm-excess-vocab))
- Liang et al., ICML 2024 ([arXiv:2403.07183](https://arxiv.org/abs/2403.07183)) — LLM word frequency in peer reviews
- Reinhart et al., [PNAS 2025](https://pnas.org/doi/10.1073/pnas.2422455122) — LLM vs. human grammatical/rhetorical style (source of the hedging refinement)
- [GPTZero — perplexity and burstiness](https://gptzero.me/news/perplexity-and-burstiness-what-is-it/)
- [Originality.ai — human detection accuracy study](https://originality.ai/blog/can-humans-detect-chatgpt) (source of the ineffective-indicators caution)
