def test_create_task(client):
    resp = client.post("/tasks", json={"title": "Write README"})
    assert resp.status_code == 201
    assert resp.json()["title"] == "Write README"
    assert resp.json()["status"] == "todo"
    assert resp.json()["priority"] == "medium"


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Task A"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.json()) == 1


def test_get_task(client):
    created = client.post("/tasks", json={"title": "Task A"}).json()
    resp = client.get(f"/tasks/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["id"] == created["id"]


def test_get_task_not_found(client):
    resp = client.get("/tasks/9999")
    assert resp.status_code == 404


def test_update_task(client):
    created = client.post("/tasks", json={"title": "Task A"}).json()
    resp = client.patch(f"/tasks/{created['id']}", json={"status": "done"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "done"


def test_delete_task(client):
    created = client.post("/tasks", json={"title": "Task A"}).json()
    resp = client.delete(f"/tasks/{created['id']}")
    assert resp.status_code == 204
    assert client.get("/tasks").json() == []


# ---------------------------------------------------------------------------
# R-02: list returns correct field values
# ---------------------------------------------------------------------------

def test_list_tasks_fields(client):
    client.post("/tasks", json={"title": "Task A"})
    resp = client.get("/tasks")
    assert resp.status_code == 200
    task = resp.json()[0]
    assert task["title"] == "Task A"
    assert task["status"] == "todo"
    assert task["priority"] == "medium"
    assert "id" in task


# ---------------------------------------------------------------------------
# R-04: PATCH validation & 404
# ---------------------------------------------------------------------------

def test_update_task_invalid_status(client):
    created = client.post("/tasks", json={"title": "Task A"}).json()
    resp = client.patch(f"/tasks/{created['id']}", json={"status": "flying"})
    assert resp.status_code == 422


def test_update_task_invalid_priority(client):
    created = client.post("/tasks", json={"title": "Task A"}).json()
    resp = client.patch(f"/tasks/{created['id']}", json={"priority": "extreme"})
    assert resp.status_code == 422


def test_update_task_not_found(client):
    resp = client.patch("/tasks/9999", json={"status": "done"})
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# R-05: DELETE 404
# ---------------------------------------------------------------------------

def test_delete_task_not_found(client):
    resp = client.delete("/tasks/9999")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# R-08: assign task to user
# ---------------------------------------------------------------------------

def test_assign_task(client):
    task = client.post("/tasks", json={"title": "Task A"}).json()
    user = client.post("/users", json={"name": "Alice", "email": "alice@example.com"}).json()
    resp = client.post(f"/tasks/{task['id']}/assign?user_id={user['id']}")
    assert resp.status_code == 200
    assert resp.json()["assignee_id"] == user["id"]


def test_assign_task_task_not_found(client):
    user = client.post("/users", json={"name": "Alice", "email": "alice@example.com"}).json()
    resp = client.post(f"/tasks/9999/assign?user_id={user['id']}")
    assert resp.status_code == 404


def test_assign_task_user_not_found(client):
    task = client.post("/tasks", json={"title": "Task A"}).json()
    resp = client.post(f"/tasks/{task['id']}/assign?user_id=9999")
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# R-09: title validation
# ---------------------------------------------------------------------------

def test_create_task_empty_title(client):
    resp = client.post("/tasks", json={"title": ""})
    assert resp.status_code == 422


def test_create_task_whitespace_title(client):
    resp = client.post("/tasks", json={"title": "   "})
    assert resp.status_code == 422


def test_create_task_title_too_long(client):
    resp = client.post("/tasks", json={"title": "x" * 101})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# R-10: due_date must be in the future
# ---------------------------------------------------------------------------

def test_create_task_past_due_date(client):
    resp = client.post("/tasks", json={"title": "Task A", "due_date": "2020-01-01T00:00:00"})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# R-11: filtering by status, priority, q (case-insensitive)
# ---------------------------------------------------------------------------

def test_filter_by_status(client):
    client.post("/tasks", json={"title": "Alpha"})
    client.post("/tasks", json={"title": "Beta"})
    # mark first as done
    first_id = client.get("/tasks").json()[0]["id"]
    client.patch(f"/tasks/{first_id}", json={"status": "done"})

    resp = client.get("/tasks?status=done")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["status"] == "done"


def test_filter_by_priority(client):
    client.post("/tasks", json={"title": "Low prio", "priority": "low"})
    client.post("/tasks", json={"title": "High prio", "priority": "high"})

    resp = client.get("/tasks?priority=low")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["priority"] == "low"


def test_filter_by_q(client):
    client.post("/tasks", json={"title": "Write README"})
    client.post("/tasks", json={"title": "Fix bug"})

    resp = client.get("/tasks?q=readme")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert "README" in data[0]["title"]


def test_filter_by_q_case_insensitive(client):
    client.post("/tasks", json={"title": "Write README"})
    client.post("/tasks", json={"title": "Fix bug"})

    resp = client.get("/tasks?q=README")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

    resp2 = client.get("/tasks?q=readme")
    assert len(resp2.json()) == 1


def test_combined_filters(client):
    client.post("/tasks", json={"title": "Deploy API", "priority": "high"})
    client.post("/tasks", json={"title": "Deploy DB", "priority": "low"})
    client.post("/tasks", json={"title": "Write docs", "priority": "high"})

    resp = client.get("/tasks?q=deploy&priority=high")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["title"] == "Deploy API"


def test_filter_no_match(client):
    client.post("/tasks", json={"title": "Task A"})
    resp = client.get("/tasks?status=done")
    assert resp.status_code == 200
    assert resp.json() == []


# ---------------------------------------------------------------------------
# R-12: /stats endpoint
# ---------------------------------------------------------------------------

def test_get_stats(client):
    client.post("/tasks", json={"title": "T1"})
    client.post("/tasks", json={"title": "T2"})
    t3 = client.post("/tasks", json={"title": "T3"}).json()
    client.patch(f"/tasks/{t3['id']}", json={"status": "done"})

    resp = client.get("/tasks/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert data["todo"] == 2
    assert data["done"] == 1
    assert data["in_progress"] == 0
    assert data["total"] == 3
