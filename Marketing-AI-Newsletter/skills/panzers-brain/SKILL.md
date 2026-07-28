---
name: panzers-brain
version: 1.0.0
description: |
  Panzer's complete editorial intelligence — audit content quality AND fix it in one pass.
  Combines the Content Audit framework (5 quality dimensions, scoring, pattern identification)
  with the Humanizer framework (24 AI-ism patterns, rewriting, personality injection).
  Use when reviewing, editing, or rewriting any written content. Built from analysis of
  247 professional editorial comments and Wikipedia's "Signs of AI writing" guide.
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
- **Humanizer** — 24 AI-ism detection patterns from Wikipedia's "Signs of AI writing" guide

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

This is the big one. 24 distinct patterns organized into six categories. Scan for all of them.

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

#### Language & Grammar Patterns

**3g. Overused AI Vocabulary**
High-frequency AI words: Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

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

#### Style Patterns

**3m. Em Dash Overuse**
AI uses em dashes (—) more than humans. Replace most with commas or periods.

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
ChatGPT uses curly quotes. Normalize to straight quotes.

#### Communication Artifacts

**3s. Chatbot Artifacts**
Strip: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**3t. Knowledge-Cutoff Disclaimers**
Strip: as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**3u. Sycophantic/Servile Tone**
Strip: Great question!, That's an excellent point, You're absolutely right

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

**3x. Generic Positive Conclusions**
Before: "The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction."
After: "The company plans to open two more locations next year."

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
- No AI fingerprints detectable across all 24 patterns
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
- [ ] AI detox: All 24 patterns scanned, none remain
- [ ] Structure: Varied paragraphs, clear transitions
- [ ] Voice: Sounds human, has personality, passes read-aloud test
- [ ] Focus: Every paragraph earns its place
- [ ] Anti-AI pass: Two-step audit completed, no remaining tells
- [ ] Soul check: Has opinions, varied rhythm, acknowledges complexity

---

## REFERENCE

Content Audit framework built from analysis of 247 professional editorial comments across GrowthX client content.

AI fingerprint patterns based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Key insight: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
