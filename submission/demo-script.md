# SpecSync — Demo Video Script (detailed, ~3:30)

> บรรยาย (narration) เป็นภาษาอังกฤษ เพื่อให้ judge เข้าใจ ส่วนคำแนะนำในวงเล็บเป็นภาษาไทยบอกว่าต้องโชว์/กดอะไร

## ก่อนอัด (เตรียมล่วงหน้า 5 นาที)
- [ ] เปิด Terminal ที่โฟลเดอร์ `taskflow` พร้อมคำสั่ง pytest (รันไว้ก่อน 1 รอบให้ warm)
- [ ] เปิด browser tab: `https://bobthanakorn.github.io/specsync-taskflow/` (dashboard)
- [ ] เปิด browser tab: `https://github.com/BobThanakorn/specsync-taskflow` (repo)
- [ ] เปิดไฟล์ `artifacts/gaps.json` (ใช้โชว์ gap ที่เจอ)
- [ ] ปิด notification ทั้งหมด, ตั้ง resolution 1080p

---

## 0:00–0:30 — Problem (screen: PRD vs code / old README)

**Say:** "Every software team has this problem: requirements, code, tests, and docs
drift apart. Nobody knows which requirement has no implementation, which feature
has no test, or which doc is outdated."

**Show:**
1. เปิด `specs/PRD.md` → ชี้ R-11 (Search & filter) ที่เป็น requirement
2. เปิด (git history หรือ screenshots) โค้ด `list_tasks` เวอร์ชันเดิมที่ไม่มี filter
   - ถ้าง่ายสุด: เลื่อนไป `artifacts/gaps.json` แล้วชี้ GAP-001 "missing_feature — R-11"
3. ชี้ baseline ตัวเลข: "11 of 12 implemented, only 3 of 12 tested, 3 doc drifts."

**Say:** "I built SpecSync — an agentic pipeline on IBM Bob 2.0 that finds these
gaps automatically, closes them, and keeps docs honest."

---

## 0:30–1:30 — How it works + Bob evidence (screen: pipeline + bob_sessions + artifacts)

**Say:** "Here's the pipeline. One Agent-mode task in IBM Bob 2.0 uses document
understanding to read the PRD, then parallel subagents map every requirement to
code and test coverage, and write a traceability matrix and gap report."

**Show:**
1. เปิด dashboard → scroll ไป section **"How it works"** (pipeline diagram + 4 feature badges)
2. เปิด `bob_sessions/specsync_session_summary_01.png` → ชี้ Bobcoins/consumption (หลักฐานใช้ Bob จริง)
3. เปิด `artifacts/matrix.json` + `artifacts/gaps.json` → ชี้ว่ามันถูก generate ขึ้นมา ไม่ใช่เขียนมือ
   - ชี้ GAP types: `missing_feature` (1), `missing_test` (10), `doc_drift`

**Say:** "The analysis found 11 gaps. A follow-up Agent task closed them — it
implemented the missing search/filter feature, wrote the missing tests, and a third
step rewrote the documentation to match reality."

---

## 1:30–2:30 — Live proof: tests + coverage (screen: Terminal)

**Say:** "Let me show the working result. This is the final code, fully tested."

**Show (รันจริงสด):**
1. Terminal: `.venv\Scripts\python.exe -m pytest -q`
   - ให้เห็น "31 passed"
2. Terminal: `.venv\Scripts\python.exe -m pytest -q --cov=app --cov-report=term`
   - ให้เห็น "TOTAL ... 96%"

**Say:** "8 tests before, 31 after. 96% line coverage. Every requirement now has a
test — including the new search/filter feature."

---

## 2:30–3:10 — Dashboard: matrix + impact (screen: dashboard)

**Say:** "Everything is visualized in the dashboard."

**Show:**
1. Scroll ไป **Traceability matrix** → ชี้ครบ 12/12 สีเขียว (status + tested)
2. Scroll ไป **Gap report** → ชี้ gap แต่ละตัวที่ถูกปิด
3. Scroll ไป **Measured impact** → ชี้กราฟ before/after:
   - Requirements implemented 11 → 12
   - Test coverage 25% → 100%
   - Tests 8 → 31
   - Docs drift 3 → 0

**Say:** "From 25% to 100% requirement coverage, and documentation drift went to
zero — in about five minutes instead of hours of manual work."

---

## 3:10–3:30 — Wrap-up (screen: repo + thank you)

**Say:** "The repo is public with the full Bob session evidence, the working API,
the tests, and the artifacts. SpecSync turns traceability and doc-sync into an
automated, re-runnable pipeline — powered by IBM Bob 2.0. Thank you."

**Show:** repo homepage (`github.com/BobThanakorn/specsync-taskflow`) → ชี้โฟลเดอร์ `bob_sessions/`, `artifacts/`, `app/`, `tests/`

---

## Tips
- อัดรอบเดียว ไม่ต้องตัดต่อ ถ้าพลาดตอนไหน อัดซ่อมเฉพาะตอนนั้นแล้วต่อ
- พูดชัด ไม่เร็วเกิน ตรวจเสียงก่อนอัดจริง 10 วิ
- อัป YouTube (unlisted ได้) → วางลิงก์ลง `submission/SUBMISSION.md`

## คำสั่งที่ต้องรันสด (copy ไว้ก่อน)
```
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m pytest -q --cov=app --cov-report=term
```
