from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_get_breaking_news():
    response = client.get("/breaking-news?date=2024-07-30")
    assert response.status_code == 200
    assert response.json() == {"08:00": "News at 8 AM", "12:00": "News at noon"}

    response = client.get("/breaking-news?date=2024-07-30&time=08:00")
    assert response.status_code == 200
    assert response.json() == {"08:00": "News at 8 AM"}

    response = client.get("/breaking-news?date=2024-07-30&time=15:00")
    assert response.status_code == 404

    response = client.get("/breaking-news?time=09:00")
    assert response.status_code == 200
    assert response.json() == {"2024-07-31": "News at 9 AM"}
