# Bob Task 1 — Analyze specs & build traceability matrix

คัดลอกทั้ง block ลงใน Bob IDE (Agent mode), ก่อนรันเปลี่ยน directory ไปที่โฟลเดอร์โปรเจกต์นี้แล้ว

```
@specs/PRD.md @specs/ADR-001.md

You are SpecSync's analysis agent. Use document understanding to read the PRD
and extract every requirement (R-01..R-12) as a list.

Then analyze the codebase under app/ and tests/. For each requirement determine:
1. status: "implemented" or "missing" — point to the exact file and function
   (format "app/routers/tasks.py::create_task").
2. test_covered: true or false — point to the exact test ("tests/test_tasks.py::test_create_task").

IMPORTANT: run the code-structure analysis and the test-coverage analysis in
PARALLEL using subagents, then merge their findings. Do not modify any code.

Write three JSON artifacts that match the schemas in artifacts/schema/:
- artifacts/requirements.json  (per requirements.schema.json)
- artifacts/matrix.json        (per matrix.schema.json)
- artifacts/gaps.json          (per gaps.schema.json: every requirement where
  status=missing OR test_covered=false, with severity and a concrete fix
  suggestion; include the summary object with counts)

End your reply with a markdown summary table: requirement id, status,
test_covered, gap type.
```

เมื่อเสร็จ: screenshot task session consumption summary → `bob_sessions/task-01-analyze-specs.png`
