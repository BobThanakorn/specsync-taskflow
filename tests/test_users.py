def test_create_user(client):
    resp = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    assert resp.status_code == 201
    assert resp.json()["name"] == "Alice"


def test_create_user_duplicate_email(client):
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    resp = client.post("/users", json={"name": "Bob", "email": "alice@example.com"})
    assert resp.status_code == 409


# ---------------------------------------------------------------------------
# R-06: name length validation
# ---------------------------------------------------------------------------

def test_create_user_empty_name(client):
    resp = client.post("/users", json={"name": "", "email": "a@example.com"})
    assert resp.status_code == 422


def test_create_user_name_too_long(client):
    resp = client.post("/users", json={"name": "x" * 101, "email": "a@example.com"})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# R-07: list users
# ---------------------------------------------------------------------------

def test_list_users(client):
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    client.post("/users", json={"name": "Bob", "email": "bob@example.com"})
    resp = client.get("/users")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 2
    names = {u["name"] for u in data}
    assert names == {"Alice", "Bob"}


def test_list_users_empty(client):
    resp = client.get("/users")
    assert resp.status_code == 200
    assert resp.json() == []
