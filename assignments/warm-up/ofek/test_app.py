import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200, "Hello"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200, "200"


def test_breaking_news_by_date_and_time():
    response = client.get("/breaking-news", params={"date": "2024-07-30", "time": "09:32:16"})
    assert response.status_code == 200
    assert response.json() == " ג'ודו: גילי שריר הפסידה לאלופה האולימפית - והודחה מפריז אחרי קרב אחד"


def test_breaking_news_by_date_and_time_erorr():
    response = client.get("/breaking-news", params={"date": "2025 07-31", "time": "09:32:16"})
    assert response.status_code == 404
    assert response.json() == 404


def test_breaking_news_by_time():
    response = client.get("/breaking-news", params={"time": "09:32:16"})
    assert response.status_code == 200
    assert response.json() == {
        "2024-07-30.json": " ג'ודו: גילי שריר הפסידה לאלופה האולימפית - והודחה מפריז אחרי קרב אחד"}
