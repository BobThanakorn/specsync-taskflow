# Bob Task 3 — Fix documentation drift

Run after task 2 finishes.

```
@README.md @specs/ADR-001.md @specs/PRD.md @app

Use document understanding to compare the codebase under app/ with the current
README.md. Fix every documentation drift:

1. Update README.md:
   - correct the required Python version to match what the code actually uses
   - list ALL endpoints that exist: tasks CRUD, users create/list, task assign,
     task stats, health — and the search/filter query parameters added recently
   - add quick-start commands (pip install, uvicorn, pytest) and example curl
2. Create docs/api.md describing every endpoint, its parameters, and error codes.
3. Create specs/ADR-002.md documenting the design decision behind the
   search/filter implementation (query params vs full-text search).
4. Do NOT modify specs/PRD.md — it is the source of truth.

Save the files and print a bullet summary of what was updated and why.
```

When done: screenshot the task session consumption summary → `bob_sessions/task-03-update-docs.png`
