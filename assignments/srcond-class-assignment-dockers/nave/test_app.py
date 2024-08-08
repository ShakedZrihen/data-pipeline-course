import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_breaking_news():
    response = client.get("/breaking-news")
    assert response.status_code == 200

def test_get_breaking_news_date():
    response = client.get("/breaking-news?date=2023-07-01")
    assert response.status_code == 200

def test_get_breaking_news_time():
    response = client.get("/breaking-news?time=08:00")
    assert response.status_code == 200

def test_get_breaking_news_date_time():
    response = client.get("/breaking-news?date=2023-07-01&time=08:00")
    assert response.status_code == 200
    assert response.json() == {"news": "News at 8 AM"}

def test_get_breaking_news_not_found():
    response = client.get("/breaking-news?date=2023-07-03")
    assert response.status_code == 200