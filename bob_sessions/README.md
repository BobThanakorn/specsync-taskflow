# bob_sessions — หลักฐานการใช้ IBM Bob IDE (required for judging)

เก็บ screenshots ของ **task session consumption summary** ทุก task ที่รันใน Bob IDE

## วิธี capture
1. หลัง task รันเสร็จ → คลิก task header ใน Bob IDE
2. จะเห็น "task session consumption summary" → screenshot เฉพาะส่วนนี้
3. บันทึกเป็น **PNG** ชื่อไฟล์ตามรูปแบบ:

```
bob_sessions/task-01-analyze-specs.png
bob_sessions/task-02-fix-gaps.png
bob_sessions/task-03-update-docs.png
```

## Checklist
- [ ] task-01: สกัด requirement + traceability matrix (Agent mode, parallel, subagents)
- [ ] task-02: เจน test + implement search/filter
- [ ] task-03: อัปเดต docs (README/ADR/API docs)
