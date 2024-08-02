from fastapi.testclient import TestClient
from app import app
import pytest
import datetime

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": 200}

def test_get_all_news():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) > 0

def test_get_news_by_date():
    test_date = "2024-07-30"
    response = client.get(f"/breaking-news?date={test_date}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert all(isinstance(key, str) and isinstance(value, str) for key, value in response.json().items())

def test_get_news_by_date_not_found():
    non_existing_date = "1990-01-01"
    response = client.get(f"/breaking-news?date={non_existing_date}")
    assert response.status_code == 404

def test_get_news_by_date_and_time():
    test_date = "2024-07-31"  
    test_time = "17:50"  
    response = client.get(f"/breaking-news?date={test_date}&time={test_time}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert test_time in response.json()

def test_get_news_by_date_and_time_not_found():
    non_existing_date = "1990-01-01"
    time = "14:11"
    response = client.get(f"/breaking-news?date={non_existing_date}&time={time}")
    assert response.status_code == 404

def test_get_news_by_time():
    test_time = "17:50" 
    response = client.get(f"/breaking-news?time={test_time}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_news_by_time_not_found():
    non_existing_time = "25:61"
    response = client.get(f"/breaking-news?time={non_existing_time}")
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main()
