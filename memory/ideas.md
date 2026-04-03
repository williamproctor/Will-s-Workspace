# Background Ideas

Low-priority ideas captured during sessions. Agents should append here whenever they notice an opportunity, optimization, or creative connection that isn't part of the current task.

## How to Use

- Append ideas as they come up during work — don't interrupt the main task to pursue them.
- Include enough context that someone can evaluate the idea later without needing the original session.
- Review this file periodically to promote good ideas into actual tasks.

## Format

```
### yyyy-mm-dd — Idea title
Context: what you were doing when the idea came up
Idea: the actual suggestion
Value: why it matters (time saved, quality improved, new capability)
```

---

### 2026-04-01 — AEO-Audit as GrowthX sales lead magnet
Context: Researching AEO tools and found AINYC/aeo-audit, which scores websites across 13 AI citation ranking factors.
Idea: Run AEO-Audit on a prospect's domain before the first sales call and include the results in outreach. "We ran an AI visibility audit on your site — here's what ChatGPT, Gemini, and Perplexity actually say about you." Complements CheckThat's ongoing monitoring with a one-shot audit hook.
Value: Differentiates GrowthX outreach from generic cold emails. Gives the prospect something immediately useful. Low effort per prospect since it's automated.

### 2026-04-01 — Cheaper newsletter scoring with DeepSeek V3
Context: Researching newsletter automation pipelines. Multiple successful implementations use a two-model approach: cheap model scores/filters sources, expensive model writes the final output.
Idea: Add a scoring step to the AV-AI Newsletter skill between research and writing. Use DeepSeek V3 (~$0.02/batch) to rank sources by relevance, novelty, and department impact before Claude writes the newsletter. Currently Claude processes everything, including low-quality sources.
Value: Cuts token costs ~75% on the research phase. Improves newsletter quality by filtering noise before the writing model sees it.

### 2026-04-03 — A/B test the landing page form length
Context: Slimmed the GrowthX System form from 6 to 5 fields based on research (<=5 fields = 120% better conversion). But "biggest challenge" dropdown was providing useful lead qualification data.
Idea: Once there's real traffic, A/B test a 2-step form: Step 1 captures the 4 essential fields (name, email, company, role), Step 2 optionally asks company size + challenge with a progress bar. Multi-step forms with progress bars reduce abandonment per 2026 research. This preserves qualification data while minimizing initial friction.
Value: Gets the best of both worlds — low-friction capture AND useful qualification data. Could also inform which modules to recommend first based on challenge selection.

