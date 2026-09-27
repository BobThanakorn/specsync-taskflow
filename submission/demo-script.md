# Demo Video Script — SpecSync (target 2:30)

## 0:00–0:35 — Problem (screen: PRD + old README / gap list)
- "Specs, code, tests, and docs drift apart. Nobody knows what's covered and what's not."
- Show `specs/PRD.md` R-11 (search/filter required) + old `README.md` claiming it's "planned".
- Show baseline numbers: 11/12 implemented, 3/12 tested, 11 gaps.

## 0:35–1:25 — Bob in action (screen: bob_sessions screenshots + artifacts)
- "SpecSync runs on IBM Bob 2.0 — one Agent-mode task, parallel subagents, document understanding."
- Show task-01 screenshot: requirement extraction → traceability matrix.
- Show `artifacts/gaps.json`: gap list with severity + fix suggestions.
- Show task-02 screenshot: Bob implementing search/filter + tests.

## 1:25–2:00 — Dashboard (screen: dashboard/index.html via http server)
- Traceability matrix: green = covered, red = gap.
- Gap report cards.
- Filter feature now live (show `GET /tasks?status=done&q=...`).

## 2:00–2:30 — Impact & wrap
- After: 12/12 implemented, ~12/12 tested, 0 doc drift.
- "6 hours of manual traceability → 5 minutes. Built with IBM Bob 2.0."
- CTA: repo link + bob_sessions evidence.

## Tips
- Record with OBS / Windows Game Bar.
- Keep each segment tight; total ≤ 3 min.
- Upload to YouTube (unlisted is fine) → paste link in SUBMISSION.md.