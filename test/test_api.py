from fastapi.testclient import TestClient
from endpoints.sports_inventory import app

client = TestClient(app)


def test_add_item():
    response = client.post("/item/", json={"name": "football", "quantity": 20})
    assert response.status_code == 200 or response.status_code == 404
    msg = response.json()
    assert msg == {"message": "Item added successfully"} or msg == {"message": "Item already exist"}


def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) >= 0


def test_update_item():
    response = client.put("/update/5/", json={"quantity": 20})
    assert response.status_code == 200 or response.status_code == 404
    msg = response.json()
    assert msg == {"message": "Item updated successfully"} or msg == {"message": "Specified item not exist"}
