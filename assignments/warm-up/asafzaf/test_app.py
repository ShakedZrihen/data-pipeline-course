from fastapi.testclient import TestClient
from app import app
import json

filename = "2024-07-27"

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_breaking_news_success():
    response = client.get("/breaking-news")
    with open(f"./{filename}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        test_obj = { f"{filename}": data }
        assert response.status_code == 200
        assert response.json() == test_obj

def test_breaking_news_with_date():
    response = client.get(f"/breaking-news?date={filename}")
    assert response.status_code == 200
    assert "2024-07-27" in response.json()

def test_breaking_news_with_time():
    time = "18:45"
    response = client.get(f"/breaking-news?time={time}")
    assert response.status_code == 200
    assert time in response.json().get(f"{filename}") 
    
def test_breaking_news_not_found():
    response = client.get("/breaking-news?date=invalid_date")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}  