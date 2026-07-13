def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_item(client):
    response = client.post("/items", json={"name": "Widget", "description": "A test widget"})
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Widget"
    assert body["description"] == "A test widget"
    assert "id" in body


def test_create_item_without_description(client):
    response = client.post("/items", json={"name": "Widget"})
    assert response.status_code == 200
    assert response.json()["description"] is None


def test_list_items(client):
    client.post("/items", json={"name": "Widget"})
    client.post("/items", json={"name": "Gadget"})

    response = client.get("/items")
    assert response.status_code == 200
    names = {item["name"] for item in response.json()}
    assert names == {"Widget", "Gadget"}


def test_get_item(client):
    created = client.post("/items", json={"name": "Widget"}).json()

    response = client.get(f"/items/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_get_item_not_found(client):
    response = client.get("/items/999999")
    assert response.status_code == 404


def test_replace_item(client):
    created = client.post("/items", json={"name": "Widget", "description": "old"}).json()

    response = client.put(f"/items/{created['id']}", json={"name": "Gizmo", "description": "new"})
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Gizmo"
    assert body["description"] == "new"


def test_replace_item_drops_omitted_fields(client):
    created = client.post("/items", json={"name": "Widget", "description": "old"}).json()

    response = client.put(f"/items/{created['id']}", json={"name": "Gizmo"})
    assert response.status_code == 200
    assert response.json()["description"] is None


def test_replace_item_not_found(client):
    response = client.put("/items/999999", json={"name": "X"})
    assert response.status_code == 404


def test_update_item(client):
    created = client.post("/items", json={"name": "Widget", "description": "old"}).json()

    response = client.patch(f"/items/{created['id']}", json={"description": "new"})
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Widget"
    assert body["description"] == "new"


def test_update_item_not_found(client):
    response = client.patch("/items/999999", json={"name": "X"})
    assert response.status_code == 404


def test_delete_item(client):
    created = client.post("/items", json={"name": "Widget"}).json()

    response = client.delete(f"/items/{created['id']}")
    assert response.status_code == 204

    response = client.get(f"/items/{created['id']}")
    assert response.status_code == 404


def test_delete_item_not_found(client):
    response = client.delete("/items/999999")
    assert response.status_code == 404
