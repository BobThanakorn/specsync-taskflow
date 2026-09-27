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
