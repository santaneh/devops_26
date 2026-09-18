from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Byggstenar — kopiera och kombinera (fler exempel finns i test_main.py):
#
#   client.post("/api/items", json={"text": "milk"})     # skapa en anteckning
#   created = client.post(...).json()                    # ...och få tillbaka objektet
#   client.delete(f"/api/items/{created['id']}")         # ta bort en anteckning
#   response = client.get("/api/items/stats")            # hämta summeringen
#   assert response.json() == {"count": ..., "total_characters": ...}
#
# Varje test är en funktion vars namn börjar med test_. Appen nollställs
# automatiskt mellan varje test (tests/conftest.py), så varje test börjar tomt.


# Skriv ert test här:

def test_charAmountAfterDeletion() -> None:
    first = client.post("/api/items", json={"text": "milk"}).json()
    client.post("/api/items", json={"text": "bread"})

    response = client.delete(f"/api/items/{first['id']}")
    assert response.status_code == 204

    response = client.get("/api/items/stats")
    assert response.status_code == 200
    assert response.json() == {"count": 1, "total_characters": 5}
