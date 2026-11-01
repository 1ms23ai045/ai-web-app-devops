from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    assert b"Welcome to AI Web Application!" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    
    assert response.status_code == 200


def test_health_status():
    client = app.test_client()
    response = client.get("/health")
    
    data = response.get_json()
    
    assert data["status"] == "healthy"
    assert data["application"] == "AI Web Application"
