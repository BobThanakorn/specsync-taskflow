# Bob Task 2 — Close the gaps: tests + missing feature

รันหลังจาก task 1 เสร็จและมี artifacts/gaps.json แล้ว

```
@artifacts/gaps.json @specs/PRD.md

Read the gap report and close every gap in it:

1. For every requirement with type "missing_test": write pytest tests under
   tests/ that verify the behavior described in the PRD (validation rules,
   user listing, task assignment, stats). Use the same TestClient + fixture
   style as the existing tests.
2. For the "missing_feature" gap (R-11 search/filter): implement it in
   app/routers/tasks.py. GET /tasks must accept optional query parameters
   status, priority, and q (case-insensitive substring match on title), and
   they must be combinable. Then add pytest tests for the new feature.
3. Run `.venv\Scripts\python.exe -m pytest` (this Windows venv has the
   dependencies installed) and fix anything that fails until the whole suite
   passes. Print the final pytest summary in your reply.

Use Agent mode. Keep changes minimal and idiomatic. Do not change existing
business logic unless a test proves it wrong.
```

เมื่อเสร็จ: screenshot consumption summary → `bob_sessions/task-02-fix-gaps.png`
