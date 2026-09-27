def test_create_user(client):
    resp = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    assert resp.status_code == 201
    assert resp.json()["name"] == "Alice"


def test_create_user_duplicate_email(client):
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    resp = client.post("/users", json={"name": "Bob", "email": "alice@example.com"})
    assert resp.status_code == 409
