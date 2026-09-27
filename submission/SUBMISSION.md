# SpecSync — Submission Draft (lablab.ai)

> Copy this into the lablab submission form. Adjust the wording as needed.
> The "After" numbers will be updated once Bob finishes the tasks.

## Project title
**SpecSync — Spec-to-Code Traceability & DocSync Agent**

## One-liner
An IBM Bob 2.0 agentic pipeline that reads your PRD, maps every requirement to
code and tests, finds the gaps, closes them, and keeps your documentation honest.

## Problem
Teams lose ~10-15% of engineering time keeping specs, code, tests, and docs in
sync. Nobody knows which requirement has no implementation, which feature has no
test, or which doc is lying — until it bites in production.

## Solution
SpecSync uses IBM Bob 2.0 as the core: one Agent-mode task uses **document
understanding** to read the PRD, runs **parallel subagents** to map requirements
to code and test coverage, and writes a traceability matrix + gap report to
artifacts/. A follow-up Agent task closes the gaps (missing tests, missing
feature) and a third task fixes documentation drift. A dashboard visualizes the
whole pipeline.

## Impact (measured on the TaskFlow sample project)
| Metric | Before | After |
|---|---|---|
| Requirements implemented | 11 / 12 | 12 / 12 |
| Requirements covered by tests | 3 / 12 (25%) | 12 / 12 (100%) |
| Test suite size | 8 tests | 31 tests |
| Line coverage (`pytest --cov`) | n/a | 96% |
| Gaps detected & closed | — | 11 (missing_feature + missing_test + doc_drift) |
| Documentation drift points | 3 | 0 |
| Manual traceability effort | ~6 hours | ~5 minutes |

## Tech stack
- **IBM Bob IDE** (Agent mode, parallel tasks, subagents, document understanding, context mentions) — core
- FastAPI + SQLite (stdlib) + pytest
- HTML/CSS/JS dashboard (IBM Carbon-inspired dark theme)

## Repo
https://github.com/BobThanakorn/specsync-taskflow

## Demo video
(Paste the YouTube link after recording.)

## Evidence of Bob usage
`bob_sessions/` contains task session consumption summary screenshots for each task.