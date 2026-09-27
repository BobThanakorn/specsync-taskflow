import sqlite3
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from app.db import get_db
from app.schemas import TaskCreate, TaskOut, TaskUpdate
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


def row_to_task(row):
    return TaskOut(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        due_date=row["due_date"],
        status=row["status"],
        priority=row["priority"],
        assignee_id=row["assignee_id"],
        created_at=row["created_at"],
    )


@router.post("", response_model=TaskOut, status_code=201)
def create_task(payload: TaskCreate, db: sqlite3.Connection = Depends(get_db)):
    task_service.validate_title(payload.title)
    task_service.validate_due_date(payload.due_date)
    task_service.validate_priority(payload.priority)
    cur = db.execute(
        "INSERT INTO tasks (title, description, priority, due_date, created_at)"
        " VALUES (?, ?, ?, ?, ?)",
        (
            payload.title,
            payload.description,
            payload.priority,
            payload.due_date.isoformat() if payload.due_date else None,
            datetime.utcnow().isoformat(),
        ),
    )
    db.commit()
    row = db.execute("SELECT * FROM tasks WHERE id = ?", (cur.lastrowid,)).fetchone()
    return row_to_task(row)


@router.get("", response_model=list[TaskOut])
def list_tasks(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    return [row_to_task(r) for r in rows]


@router.get("/stats", response_model=dict)
def get_stats(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute("SELECT status, COUNT(*) AS count FROM tasks GROUP BY status").fetchall()
    counts = {"todo": 0, "in_progress": 0, "done": 0, "total": 0}
    for row in rows:
        counts[row["status"]] = row["count"]
        counts["total"] += row["count"]
    return counts


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: sqlite3.Connection = Depends(get_db)):
    row = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return row_to_task(row)


@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: sqlite3.Connection = Depends(get_db)):
    if db.execute("SELECT 1 FROM tasks WHERE id = ?", (task_id,)).fetchone() is None:
        raise HTTPException(status_code=404, detail="Task not found")
    allowed = {"title", "description", "status", "priority", "due_date"}
    updates = {k: v for k, v in payload.model_dump(exclude_unset=True).items() if k in allowed}
    if "title" in updates:
        task_service.validate_title(updates["title"])
    if "due_date" in updates:
        task_service.validate_due_date(updates["due_date"])
    if "status" in updates:
        task_service.validate_status(updates["status"])
    if "priority" in updates:
        task_service.validate_priority(updates["priority"])
    if updates:
        sets = ", ".join(f"{key} = ?" for key in updates)
        values = [
            value.isoformat() if isinstance(value, datetime) else value
            for value in updates.values()
        ]
        values.append(task_id)
        db.execute(f"UPDATE tasks SET {sets} WHERE id = ?", values)
        db.commit()
    row = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    return row_to_task(row)


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: sqlite3.Connection = Depends(get_db)):
    if db.execute("SELECT 1 FROM tasks WHERE id = ?", (task_id,)).fetchone() is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()


@router.post("/{task_id}/assign", response_model=TaskOut)
def assign_task(task_id: int, user_id: int, db: sqlite3.Connection = Depends(get_db)):
    if db.execute("SELECT 1 FROM tasks WHERE id = ?", (task_id,)).fetchone() is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db.execute("SELECT 1 FROM users WHERE id = ?", (user_id,)).fetchone() is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.execute("UPDATE tasks SET assignee_id = ? WHERE id = ?", (user_id, task_id))
    db.commit()
    row = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    return row_to_task(row)
