# TaskFlow API

A lightweight task-management REST API for small teams, built with FastAPI and SQLite.

## Requirements

- Python 3.9+
- pip

## Quick start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the development server
uvicorn app.main:app --reload

# 3. Open the interactive docs
# http://127.0.0.1:8000/docs

# 4. Run the test suite
python -m pytest tests/
```

## Available endpoints

### Tasks

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks` | List tasks (supports filtering) |
| `GET` | `/tasks/stats` | Task counts grouped by status |
| `GET` | `/tasks/{id}` | Get a single task |
| `PATCH` | `/tasks/{id}` | Update a task |
| `DELETE` | `/tasks/{id}` | Delete a task |
| `POST` | `/tasks/{id}/assign` | Assign a task to a user |

#### Filtering — `GET /tasks`

All parameters are optional and can be combined:

| Query param | Type | Description |
|-------------|------|-------------|
| `status` | string | Exact match: `todo`, `in_progress`, `done` |
| `priority` | string | Exact match: `low`, `medium`, `high` |
| `q` | string | Case-insensitive substring match on the task title |

```bash
# Tasks that are done and have "deploy" in the title
curl "http://localhost:8000/tasks?status=done&q=deploy"
```

### Users

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/users` | Create a user |
| `GET` | `/users` | List all users |

### Health

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Liveness check |

## Example curl commands

```bash
# Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Write tests", "priority": "high"}'

# List all tasks
curl http://localhost:8000/tasks

# Filter by status
curl "http://localhost:8000/tasks?status=todo"

# Filter by priority and keyword
curl "http://localhost:8000/tasks?priority=high&q=tests"

# Get task stats
curl http://localhost:8000/tasks/stats

# Update a task
curl -X PATCH http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'

# Delete a task
curl -X DELETE http://localhost:8000/tasks/1

# Create a user
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'

# Assign task 1 to user 1
curl -X POST "http://localhost:8000/tasks/1/assign?user_id=1"
```

## Storage

Tasks and users are stored in a local SQLite database (`taskflow.db`).
See [specs/ADR-001.md](specs/ADR-001.md) for the rationale.

## Full API reference

See [docs/api.md](docs/api.md) for a complete endpoint reference including
all parameters and error codes.
