import pytest
from fastapi.testclient import TestClient
from app import app

# Create a TestClient using the FastAPI app
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == 200

def test_get_breaking_news():
    # Test without date and time
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    # Test with a specific date
    response = client.get("/breaking-news?date=31-07-2024")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "15:11" in response.json()

    # Test with a specific time
    response = client.get("/breaking-news?time=15:11")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    # Test with both date and time
    response = client.get("/breaking-news?date=31-07-2024&time=15:11")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json() == {"31-07-2024": {"15:11": "כשהיא על סף ניצחון קריטי: השיוט של שרון קנטור בוטל - בגלל היעדר רוח"}}

def test_date_not_found():
    response = client.get("/breaking-news?date=01-01-2000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Date not found"}

def test_time_not_found():
    response = client.get("/breaking-news?time=00:00")
    assert response.status_code == 404
    assert response.json() == {"detail": "Time not found across all dates"}

def test_invalid_date_format():
    response = client.get("/breaking-news?date=2024-07-32")
    assert response.status_code == 404
    assert response.json() == {"detail": "Date not found"}
