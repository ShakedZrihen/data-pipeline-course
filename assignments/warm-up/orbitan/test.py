from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": 200}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "massage": "200"}


def test_breaking_news():
    response = client.get("/breaking-news")
    assert response.status_code == 200

    response = client.get("/breaking-news?date=2024-07-30&time=13:29")
    assert response.status_code == 200

    response = client.get("/breaking-news?date=2024-07-30")
    assert response.status_code == 200

    response = client.get("/breaking-news?time=13:29")
    assert response.status_code == 200

    response = client.get("/breaking-news?date=2000-07-30&time=00:00")
    assert response.status_code == 404

    response = client.get("/breaking-news?date=2000-07-30")
    assert response.status_code == 404

    response = client.get("/breaking-news?time=00:00")
    assert response.status_code == 404


def test_catch_all():
    response = client.get("/nonexistentpath")
    assert response.status_code == 404
    assert response.json() == {"detail": "nonexistentpath Not Found"}
