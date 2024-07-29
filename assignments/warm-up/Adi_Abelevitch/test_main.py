from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_get_all_breaking_news():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert "2024-07-29" in response.json()

def test_get_breaking_news_by_date():
    response = client.get("/breaking-news?date=2024-07-29")
    assert response.status_code == 200
    assert "09:00" in response.json()

def test_get_breaking_news_by_time():
    response = client.get("/breaking-news?time=09:00")
    assert response.status_code == 200
    assert "2024-07-29" in response.json()

def test_get_breaking_news_by_date_and_time():
    response = client.get("/breaking-news?date=2024-07-29&time=09:00")
    assert response.status_code == 200
    assert response.json() == {"news": "News at 9 AM"}

def test_get_breaking_news_not_found():
    response = client.get("/breaking-news?date=2024-07-30&time=09:00")
    assert response.status_code == 404
    assert response.json() == {"detail": "News not found for given date and time"}
