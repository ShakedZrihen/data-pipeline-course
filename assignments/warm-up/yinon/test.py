import requests

def test_health():
    response = requests.get("http://localhost:3000/health")
    assert response.status_code == 200

def test_breaking_news():
    response= requests.get("http://localhost:3000/breaking-news")
    assert response.status_code == 200

def test_breaking_news_date():
    response= requests.get("http://localhost:3000/breaking-news?date=2024-07-26")
    assert response.status_code == 404
    assert response.json() == {"detail":"Date not found"}
    
def test_breaking_news_time():
    response= requests.get("http://localhost:3000/breaking-news?time=00:00")
    assert response.status_code == 404
    assert response.json() == {"detail": "Time not found in any date"}