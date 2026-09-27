# TaskFlow API — Product Requirements Document (PRD)

- Version: 1.0
- Date: 2026-09-25
- Status: Approved

## Overview

TaskFlow is a lightweight task-management REST API. It lets client applications
create and manage tasks, assign tasks to users, and report task statistics.
TaskFlow is designed for small teams that need a simple, self-hosted backend.

## Actors

- **End user** — uses a client application backed by TaskFlow.
- **System admin** — deploys and maintains the API.

## Requirements

### Task CRUD

| ID | Requirement | Priority |
|----|-------------|----------|
| R-01 | `POST /tasks` creates a task with a title, optional description, optional due date and priority. Defaults: `status=todo`, `priority=medium`. Returns the created task with an `id`. | Must |
| R-02 | `GET /tasks` returns the full list of tasks. | Must |
| R-03 | `GET /tasks/{id}` returns a single task, or `404` if it does not exist. | Must |
| R-04 | `PATCH /tasks/{id}` updates any of title, description, status, priority, due date. `status` must be one of `todo`, `in_progress`, `done`; `priority` must be one of `low`, `medium`, `high`. Unknown fields are ignored. Returns `404` if the task does not exist. | Must |
| R-05 | `DELETE /tasks/{id}` removes a task and returns `204`. Deleting a non-existent task returns `404`. | Must |

### Users & assignment

| ID | Requirement | Priority |
|----|-------------|----------|
| R-06 | `POST /users` creates a user with a name (1–100 characters) and a unique email address. A duplicate email returns `409`. | Must |
| R-07 | `GET /users` lists all users. | Must |
| R-08 | `POST /tasks/{id}/assign?user_id={uid}` assigns a task to an existing user. Returns `404` if either the task or the user does not exist. | Must |

### Validation

| ID | Requirement | Priority |
|----|-------------|----------|
| R-09 | The task title is required, trimmed of whitespace, and limited to 100 characters. Invalid titles are rejected. | Must |
| R-10 | When a `due_date` is provided, it must be in the future. Past dates are rejected. | Must |

### Search & reporting

| ID | Requirement | Priority |
|----|-------------|----------|
| R-11 | `GET /tasks` supports optional query parameters: `status` (exact match), `priority` (exact match), and `q` (case-insensitive substring match on the title). Filters can be combined. | Should |
| R-12 | `GET /tasks/stats` returns task counts grouped by status (`todo`, `in_progress`, `done`) plus a `total`. | Should |

## Non-functional notes

- API responses are JSON.
- Storage is a local SQLite database (see ADR-001).
- Endpoint and error documentation must stay up to date with the code (see ADR-001).

## Out of scope

- Authentication and authorization.
- Push notifications and email.
