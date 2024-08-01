import requests

def test_health():
    response = requests.get("http://localhost:3000/health")
    assert response.status_code == 200

def test_breaking_news():
    response = requests.get("http://localhost:3000/breaking-news")
    assert response.status_code == 200
    assert response.json() != {"message": "No breaking news found"}

