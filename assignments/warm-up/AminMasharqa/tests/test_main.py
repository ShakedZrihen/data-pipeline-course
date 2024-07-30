from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API is up and running"}

def test_breaking_news():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
