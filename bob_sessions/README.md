# bob_sessions — IBM Bob IDE usage evidence (required for judging)

Store screenshots of the **task session consumption summary** for every task you
run in Bob IDE.

## How to capture
1. In the Bob IDE chat interface, select **Tasks** to open the task list.
2. Select the task related to this submission (the whole pipeline was run in one
   Agent-mode session: analyze → fix gaps → update docs).
3. Click the **task header** — the "task session consumption summary" is displayed.
4. Screenshot that panel. If it is longer than one screen, take several screenshots.
5. Save as **PNG** with clear names, e.g.:

```
bob_sessions/specsync_session_summary_01.png
bob_sessions/specsync_session_summary_02.png
```

## Checklist
- [ ] session summary screenshot(s) captured (single session covering all three phases)
- [ ] the artifacts JSON (`artifacts/*.json`) match the session output
- [ ] bob_sessions/ is committed in the final repository
