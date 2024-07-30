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

def test_get_news_by_date():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    response = client.get(f"/breaking-news?date={today}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_news_by_date_not_found():
    non_existing_date = "1990-01-01"
    response = client.get(f"/breaking-news?date={non_existing_date}")
    assert response.status_code == 404

def test_get_news_by_date_and_time():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    time = "14:11"  
    response = client.get(f"/breaking-news?date={today}&time={time}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json(), dict)
        assert time in response.json()

def test_get_news_by_date_and_time_not_found():
    non_existing_date = "1990-01-01"
    time = "14:11"  
    response = client.get(f"/breaking-news?date={non_existing_date}&time={time}")
    assert response.status_code == 404

def test_get_news_by_time():
    time = "14:11"  
    response = client.get(f"/breaking-news?time={time}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json(), dict)

def test_get_news_by_time_not_found():
    non_existing_time = "25:61"  
    response = client.get(f"/breaking-news?time={non_existing_time}")
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main()
