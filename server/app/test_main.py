from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_main():
    response = client.get("/docs")
    assert response.status_code == 200


def test_bill_v1():
    response = client.get("/api/v1/bills")
    assert response.status_code == 200
    data = response.json()[0]
    assert data["id"] == 2900994
    assert data["bill"] == "H.R. 3684: Infrastructure Investment and Jobs Act"
    assert data["supporters"] == 13
    assert data["opposers"] == 6


def test_legislators_v1():
    response = client.get("/api/v1/legislators")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for d in data:
        if "Rep. Don Bacon (R-NE-2)" in d["name"]:
            assert True
            break


def test_legislators_v2():
    response = client.get("/api/v2/legislators")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for d in data:
        if "Rep. David McKinley (R-WV-1)" in d["legislator"]:
            assert True
            break
