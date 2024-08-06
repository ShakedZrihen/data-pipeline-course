from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == 200

def test_breaking_news_fetch():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert response.json() is not None
