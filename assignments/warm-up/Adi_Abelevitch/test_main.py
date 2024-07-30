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

def test_get_news_by_date_and_time():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    time = "14:11"  
    response = client.get(f"/breaking-news?date={today}&time={time}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json(), dict)
        assert time in response.json()

def test_get_news_by_time():
    time = "14:11"  
    response = client.get(f"/breaking-news?time={time}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json(), dict)

if __name__ == "__main__":
    pytest.main()
