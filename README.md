# TaskFlow API

A simple task management REST API for small teams.

> Note: this README is intentionally outdated as part of a demo scenario.

## Requirements

- Python 3.8+
- pip

## Setup

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Available endpoints

- `POST /tasks` — create a task
- `GET /tasks` — list tasks
- `GET /tasks/{id}` — get a single task

Search/filter and statistics endpoints are planned for a future release.
