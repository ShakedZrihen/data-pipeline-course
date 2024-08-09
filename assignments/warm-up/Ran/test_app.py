import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_breaking_news_with_date():
    response = client.get("/breaking-news?date=01-08-2024")
    assert response.status_code in [200]

def test_breaking_news_with_time():
    response = client.get("/breaking-news?time=23:59")
    assert response.status_code in [200]

def test_breaking_news_with_date_and_time():
    response = client.get("/breaking-news?date=01-08-2024&time=01:43")
    assert response.status_code in [200]

def test_breaking_news_with_invalid_date():
    response = client.get("/breaking-news?date=invalid-date")
    assert response.status_code in [404]

def test_breaking_news_with_invalid_time():
    response = client.get("/breaking-news?time=invalid-time")
    assert response.status_code in [404]
