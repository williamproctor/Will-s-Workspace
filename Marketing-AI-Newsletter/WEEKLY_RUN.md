# Weekly automated run

Every Monday at 08:00 UTC (00:00 Pacific standard time, 01:00 during daylight time), a timer on the Monday Signal cloud agent starts this run. It researches the week that just ended, drafts the edition, checks it, and publishes it to mondaysignal.com. Will authorized automatic weekly publishing on 2026-10-21, so merging the edition PR is part of the job. Everything else (structure, sourcing, style) follows `AGENTS.md`.

Nothing unverified ships. If the run can't produce an edition that passes the gates below, it opens the PR without merging and reports what's missing.

## The timer
- Name: `monday-signal-weekly` (cursor-subscriptions `subscribe_timer`). Cron `0 8 * * 1,4`, in UTC: Mondays for the edition, Thursdays for a health check that also catches up any edition a failed Monday run missed. The UTC hour stays fixed year-round on purpose (see renewal below).
- Timers expire 7 days after they're created, so **every firing renews the timer first**: `list_subscriptions`, `unsubscribe` the existing `monday-signal-weekly`, then `subscribe_timer` with the same name, cron, and the exact prompt below. A firing always happens before its renewal, so the new expiry always lands after the next firing, and two firings a week mean one failed renewal can't break the chain.
- Prompt (re-create it exactly):

> Monday Signal timer (fires Mondays and Thursdays at 08:00 UTC). Follow Marketing-AI-Newsletter/WEEKLY_RUN.md: renew this timer first. If today is Monday in US Pacific time, produce, check, and publish the edition due today plus any missed weeks; on Thursday, run the health check and publish any missing edition. Will authorized automatic weekly publishing on 2026-10-21, so merging the edition PR is part of this job. End with a short report.

- To pause it, Will can remove it from the Listening pill above the chat composer, or ask the agent to unsubscribe it. To run an edition early or by hand, say "run this week's Monday Signal now" in the chat.

## Thursday health check
1. Renew the timer (above).
2. `python3 scripts/edition_dates.py`. If any edition is missing, run the steps below for it now.
3. Otherwise confirm the site: `https://www.mondaysignal.com/?nc=<ts>` and the latest edition URL return 200, then `node scripts/dom_test.js https://www.mondaysignal.com <latest slug>`. Reply in one or two lines.

## Steps

### 0. Renew the timer and orient
Renew the timer as described above before doing anything else.
```
cd /workspace && git checkout main && git pull origin main
cd Marketing-AI-Newsletter && python3 scripts/edition_dates.py
```
- Read the newest entries in `/workspace/TEAM-MEMORY.md` (top of the dated list) and skim `AGENTS.md`.
- If the due edition is already published and nothing is missing, report "already published" and stop.
- If several editions are missing (a missed week), produce each one, oldest first. Run research and drafting for them in parallel and give each drafting agent explicit cross-edition rules (which story belongs to which week; post-window facts become editor's notes only where they change how an item reads).
- Avoid duplicate runs: `git ls-remote --heads origin "cursor/weekly-edition-<slug>*"`. If a branch exists from the last few hours and its PR is open, finish that PR instead of starting over.

### 1. Branch
```
cd /workspace && git checkout -b cursor/weekly-edition-<slug>-6f9d
mkdir -p Marketing-AI-Newsletter/research/<slug>
```

### 2. Research (one subagent per edition)
Task tool, `generalPurpose`, foreground:
> Read /workspace/Marketing-AI-Newsletter/briefs/research-brief.md and follow it exactly. Edition slug <slug>; window <window>; production date <today>; previous edition slug <previous_slug>. Write your four files to /workspace/Marketing-AI-Newsletter/research/<slug>/.

### 3. Draft (one subagent per edition)
Task tool, `generalPurpose`, foreground:
> Read /workspace/Marketing-AI-Newsletter/briefs/drafting-brief.md and follow it exactly. Edition slug <slug>; title "# Monday Signal — Week of <Month D, YYYY>"; window <window>; production date <today>; previous edition slug <previous_slug>. Write editions/<slug>.md and editions/<slug>-simplified.md.

### 4. Review (the parent agent, not a subagent)
```
python3 scripts/qa_edition.py <slug> --fix --urls
```
- Zero errors required. Warnings: confirm each blocked URL appears in a search result, and get the word counts under budget (full ≤ 5,800, simplified ≤ 1,500).
- Read the full draft. Fix what the script can't see: kickers, setup sentences, twist endings, headlines that don't carry the news, claims stated more strongly than the research supports.
- Re-verify the two or three riskiest claims yourself at the origin: the lead story's numbers and quotes, anything legal or regulatory, and anything that corrects an earlier edition. If an earlier edition turns out wrong, fix it in place with a dated `*Correction, <Month D>: ...*` note and mention it in the new edition's watch section.
- Gates for publishing: at least two conversation items and four news stories with origin sources, QA clean, and the build check passing. If any gate fails, open the PR without merging, and report.

### 5. Build and test
```
python3 - <<'EOF'
import json, pathlib
p = pathlib.Path("editions/manifest.json"); raw = p.read_text(); data = json.loads(raw)
data["editions"].insert(0, {"slug": "<slug>", "title": "Week of <Month D, YYYY>",
  "hook": "<two sentences: the lead and the conversation>", "description": "<semicolon list of the stories>",
  "hasSimplified": True, "hasAudio": False, "hasVideo": False, "videoTitle": ""})
p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + ("\n" if raw.endswith("\n") else ""))
EOF
python3 scripts/generate_notebooklm_briefs.py <slug> --video-title "<short title, no trailing period>"
python3 scripts/generate_notebooklm_briefs.py <slug> --check
python3 scripts/build_site.py && python3 scripts/build_site.py --check
```
Then preview and DOM-test:
```
tmux -f /exec-daemon/tmux.portal.conf new-session -d -s signal-preview -c "$PWD" "python3 serve.py"
(cd /tmp && npm install jsdom --silent)
node scripts/dom_test.js http://localhost:8092 <slug> "<a phrase from the lede>"
```

### 6. Ship
- Commit the research and the edition separately: `Add research pass for the <slug> edition (week of <window>)`, then `Add <slug> edition: <three-story summary>`.
- `git push -u origin cursor/weekly-edition-<slug>-6f9d`, then call SetActiveBranch.
- Open the PR with ManagePullRequest (`create_pr`, base `main`, `draft: false`), describing the edition and the QA results.
- Merge: `gh pr merge <N> --merge`.
- Wait for Vercel (usually 3–5 minutes), polling without a trailing slash:
```
for i in $(seq 1 30); do ts=$(date +%s); c=$(curl -s -o /dev/null -L -w "%{http_code}" "https://www.mondaysignal.com/editions/<slug>?nc=$ts"); h=$(curl -s -L "https://www.mondaysignal.com/?nc=$ts" | grep -c "Week of <Month D, YYYY>"); echo "$c $h"; [ "$c" = 200 ] && [ "$h" -gt 0 ] && break; sleep 20; done
node scripts/dom_test.js https://www.mondaysignal.com <slug>
```

### 7. Wrap up
- Confirm with `list_subscriptions` that `monday-signal-weekly` exists with cron `0 8 * * 1,4` and an expiry later than next Thursday 08:00 UTC; renew it again if not.
- Add a TEAM-MEMORY entry only for something new (a failure, a fix, a sourcing pattern). Routine runs don't need one.
- Report to Will in a few sentences: the live link, the lede, the headlines, any correction made, and anything held back or unverified.
