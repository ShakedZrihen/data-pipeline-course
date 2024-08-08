import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_breaking_news():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    data = response.json()