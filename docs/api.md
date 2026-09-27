# TaskFlow API Reference

All requests and responses use JSON. The base URL for a local development
server is `http://localhost:8000`.

An interactive version of this reference is available at `/docs` when the
server is running.

---

## Tasks

### `POST /tasks` — Create a task

**Request body**

| Field | Type | Required | Default | Constraints |
|-------|------|----------|---------|-------------|
| `title` | string | Yes | — | 1–100 chars, trimmed of whitespace |
| `description` | string | No | `null` | — |
| `priority` | string | No | `"medium"` | `low`, `medium`, `high` |
| `due_date` | datetime (ISO 8601) | No | `null` | Must be in the future |

**Response — `201 Created`**

Returns the created task object (see [Task object](#task-object)).

**Error codes**

| Code | Reason |
|------|--------|
| `422` | Title is empty, whitespace-only, or exceeds 100 characters |
| `422` | `priority` is not one of `low`, `medium`, `high` |
| `422` | `due_date` is in the past |

**Example**

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Deploy to staging", "priority": "high", "due_date": "2027-01-01T09:00:00"}'
```

---

### `GET /tasks` — List tasks

Returns an ordered list of all tasks. All query parameters are optional and
combinable.

**Query parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `status` | string | Exact match: `todo`, `in_progress`, `done` |
| `priority` | string | Exact match: `low`, `medium`, `high` |
| `q` | string | Case-insensitive substring match on the task title |

**Response — `200 OK`**

Array of task objects (see [Task object](#task-object)).

**Examples**

```bash
# All tasks
curl http://localhost:8000/tasks

# In-progress tasks only
curl "http://localhost:8000/tasks?status=in_progress"

# High-priority tasks with "deploy" in the title
curl "http://localhost:8000/tasks?priority=high&q=deploy"
```

---

### `GET /tasks/stats` — Task statistics

**Response — `200 OK`**

```json
{
  "todo": 3,
  "in_progress": 1,
  "done": 5,
  "total": 9
}
```

**Example**

```bash
curl http://localhost:8000/tasks/stats
```

---

### `GET /tasks/{id}` — Get a single task

**Path parameter:** `id` — integer task ID.

**Response — `200 OK`**

Single task object (see [Task object](#task-object)).

**Error codes**

| Code | Reason |
|------|--------|
| `404` | No task with the given `id` |

**Example**

```bash
curl http://localhost:8000/tasks/1
```

---

### `PATCH /tasks/{id}` — Update a task

**Path parameter:** `id` — integer task ID.

**Request body** (all fields optional; unknown fields are ignored)

| Field | Type | Constraints |
|-------|------|-------------|
| `title` | string | 1–100 chars, trimmed of whitespace |
| `description` | string | — |
| `status` | string | `todo`, `in_progress`, `done` |
| `priority` | string | `low`, `medium`, `high` |
| `due_date` | datetime (ISO 8601) | Must be in the future |

**Response — `200 OK`**

The updated task object (see [Task object](#task-object)).

**Error codes**

| Code | Reason |
|------|--------|
| `404` | No task with the given `id` |
| `422` | `status` or `priority` is not a valid value |
| `422` | `title` fails length/whitespace validation |
| `422` | `due_date` is in the past |

**Example**

```bash
curl -X PATCH http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'
```

---

### `DELETE /tasks/{id}` — Delete a task

**Path parameter:** `id` — integer task ID.

**Response — `204 No Content`**

Empty body.

**Error codes**

| Code | Reason |
|------|--------|
| `404` | No task with the given `id` |

**Example**

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

---

### `POST /tasks/{id}/assign` — Assign a task to a user

**Path parameter:** `id` — integer task ID.

**Query parameter:** `user_id` (required) — integer user ID.

**Response — `200 OK`**

The updated task object with `assignee_id` set (see [Task object](#task-object)).

**Error codes**

| Code | Reason |
|------|--------|
| `404` | No task with the given `id` |
| `404` | No user with the given `user_id` |

**Example**

```bash
curl -X POST "http://localhost:8000/tasks/1/assign?user_id=2"
```

---

## Users

### `POST /users` — Create a user

**Request body**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `name` | string | Yes | 1–100 characters |
| `email` | string | Yes | Must be unique; 3–255 characters |

**Response — `201 Created`**

Returns the created user object (see [User object](#user-object)).

**Error codes**

| Code | Reason |
|------|--------|
| `409` | A user with the same email already exists |
| `422` | `name` is empty or exceeds 100 characters |

**Example**

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'
```

---

### `GET /users` — List users

**Response — `200 OK`**

Array of user objects (see [User object](#user-object)).

**Example**

```bash
curl http://localhost:8000/users
```

---

## Health

### `GET /health` — Liveness check

**Response — `200 OK`**

```json
{"status": "ok"}
```

---

## Data shapes

### Task object

```json
{
  "id": 1,
  "title": "Deploy to staging",
  "description": "Run smoke tests after deploy",
  "status": "todo",
  "priority": "high",
  "due_date": "2027-01-01T09:00:00",
  "assignee_id": null,
  "created_at": "2026-09-25T10:00:00"
}
```

| Field | Type | Notes |
|-------|------|-------|
| `id` | integer | Auto-assigned |
| `title` | string | — |
| `description` | string \| null | — |
| `status` | string | `todo` \| `in_progress` \| `done` |
| `priority` | string | `low` \| `medium` \| `high` |
| `due_date` | datetime \| null | ISO 8601 |
| `assignee_id` | integer \| null | ID of the assigned user |
| `created_at` | datetime | ISO 8601, set on creation |

### User object

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

| Field | Type | Notes |
|-------|------|-------|
| `id` | integer | Auto-assigned |
| `name` | string | 1–100 chars |
| `email` | string | Unique |
