from datetime import datetime

from app.models import TaskPriority, TaskStatus


def validate_title(title: str):
    if not title or not title.strip():
        raise ValueError("title is required")
    if len(title) > 100:
        raise ValueError("title must be 100 characters or fewer")


def validate_due_date(due_date):
    if due_date is not None and due_date < datetime.utcnow():
        raise ValueError("due_date must be in the future")


def validate_status(status: str):
    allowed = [s.value for s in TaskStatus]
    if status not in allowed:
        raise ValueError(f"status must be one of: {', '.join(allowed)}")


def validate_priority(priority: str):
    allowed = [p.value for p in TaskPriority]
    if priority not in allowed:
        raise ValueError(f"priority must be one of: {', '.join(allowed)}")


def task_stats(tasks):
    counts = {"todo": 0, "in_progress": 0, "done": 0, "total": 0}
    for task in tasks:
        counts[task.status] = counts.get(task.status, 0) + 1
        counts["total"] += 1
    return counts
