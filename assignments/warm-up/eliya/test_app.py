import io
import json
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

mock_data = {
    "2024-07-31 10:45": "Example news at 10:45 AM",
    "2024-07-31 10:35": "Example news at 10:35 AM",
    "2024-07-31 09:53": "Example news at 09:53 AM"
}

def mock_open(file_path, *args, **kwargs):
    if file_path == './news.json':
        return io.StringIO(json.dumps(mock_data))
    raise FileNotFoundError

def test_breaking_news_only_time(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)
    response = client.get("/breaking-news?time=10:45")
    assert response.status_code == 200
    assert response.json() == {"2024-07-31 10:45": "Example news at 10:45 AM"}

def test_breaking_news_only_date(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)
    response = client.get("/breaking-news?date=2024-07-31")
    assert response.status_code == 200
    assert response.json() == {"2024-07-31 10:45": "Example news at 10:45 AM", "2024-07-31 10:35": "Example news at 10:35 AM", "2024-07-31 09:53": "Example news at 09:53 AM"}

def test_breaking_news_date_and_time(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)
    response = client.get("/breaking-news?date=2024-07-31&time=10:35")
    assert response.status_code == 200
    assert response.json() == {"2024-07-31 10:35": "Example news at 10:35 AM"}

def test_breaking_news_no_parameters(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert response.json() == mock_data

def test_breaking_news_not_found(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)
    response = client.get("/breaking-news?date=2024-07-31&time=11:00")
    assert response.status_code == 200
    assert response.json() == 404

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == 200
