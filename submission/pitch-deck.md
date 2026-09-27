# SpecSync — Pitch Deck (10 slides)

> Convert to PDF (Canva / Google Slides / PowerPoint) and keep 2-3 sentences per slide.

## Slide 1 — Title
SpecSync: Spec-to-Code Traceability & DocSync Agent
Built with IBM Bob 2.0 · IBM Bob 2.0 Hackathon

## Slide 2 — Problem
- Specs, code, tests, and docs drift apart in every software team.
- Nobody knows which requirement has no implementation, which feature has no test, or which doc is outdated.
- Teams lose an estimated 10–15% of engineering time to documentation and traceability churn.

## Slide 3 — Solution
- One Agent-mode task in IBM Bob 2.0 reads the PRD (document understanding) and maps every requirement to code and tests.
- Parallel subagents build a traceability matrix + gap report (artifacts/*.json).
- Follow-up Agent tasks close the gaps (missing tests, missing feature) and sync the docs.

## Slide 4 — Demo
- Live dashboard: https://bobthanakorn.github.io/specsync-taskflow/
- Repo: https://github.com/BobThanakorn/specsync-taskflow
- Show: traceability matrix (green), gap report, before/after impact.

## Slide 5 — Impact (measured, TaskFlow sample)
| Metric | Before | After |
|---|---|---|
| Requirements implemented | 11/12 | 12/12 |
| Requirements covered by tests | 25% | 100% |
| Tests | 8 | 31 |
| Line coverage | n/a | 96% |
| Docs drift | 3 | 0 |
| Traceability effort | ~6 h | ~5 min |

## Slide 6 — Why IBM Bob 2.0
- Agent mode orchestrates multi-step analysis.
- Parallel tasks + subagents keep isolated contexts.
- Document understanding reads the PRD/ADRs.
- All sessions captured as evidence (bob_sessions/).

## Slide 7 — Business value
- ~5.9 hours saved per analysis run per team.
- 24 runs/year ≈ **~$10,600/team/year** (at $75/h loaded cost) — model stated, conservative.
- Scales to every repo, every sprint — fits the docs-drift problem IBM itself flags in modernization budgets (60–80% of dev spend).

## Slide 8 — Originality
- Traceability + doc-sync as an agentic pipeline — not another code-review or onboarding assistant.
- "Analyze → report → fix → sync" is re-runnable, artifact-driven, and grounded in Bob's document understanding.

## Slide 9 — Tech stack
- IBM Bob IDE (core) · FastAPI + SQLite · pytest (31 tests, 96% cov) · static dashboard (IBM Carbon-inspired dark theme)

## Slide 10 — Thank you
SpecSync — keep your docs honest.
Q&A · Team: [name]