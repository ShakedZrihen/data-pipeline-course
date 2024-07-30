from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_breaking_news_no_params():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_breaking_news_by_date():
    response = client.get("/breaking-news?date=2024-07-30")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)

def test_breaking_news_by_time():
    response = client.get("/breaking-news?time=08:00")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)

def test_breaking_news_by_date_and_time():
    response = client.get("/breaking-news?date=2024-07-30&time=08:00")
    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        data = response.json()
        assert "date" in data
        assert "time" in data
        assert "news" in data


def test_breaking_news_invalid_time():
    response = client.get("/breaking-news?time=25:00")
    assert response.status_code == 404
