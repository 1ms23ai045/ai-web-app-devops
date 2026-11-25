
from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Course Registration Portal" in response.data
    assert b"Ramaiah Institute of Technology" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json


def test_health_status():
    client = app.test_client()
    response = client.get("/health")

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "Course Registration System"
