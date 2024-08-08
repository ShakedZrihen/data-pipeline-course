from datetime import datetime
import requests


todays_date = datetime.now().strftime('%Y-%m-%d')  # yyyy-mm-dd
current_hour = datetime.now().hour

def test_health():
    response = requests.get("http://localhost:3000/health")
    assert response.status_code == 200


def test_breaking_news():
    response = requests.get("http://localhost:3000/breaking-news")
    assert response.status_code == 200
    assert response.json() != {"detail": "No News Found"}


def test_breaking_news_time():
    response = requests.get(f"http://localhost:3000/breaking-news?time={current_hour}")
    assert response.status_code == 200
    assert response.json() != {"detail": "No News Found"}


def test_breaking_news_date():
    response = requests.get(f"http://localhost:3000/breaking-news?date={todays_date}")
    assert response.status_code == 200
    assert response.json() != {"detail": "No News Found"}


def test_breaking_news_date_negative():
    response = requests.get("http://localhost:3000/breaking-news?date=1999-10-10")
    print(response.json())
    assert response.status_code == 404
    assert response.json() == {"detail": "No News Found"}


def test_breaking_news_time_negative():
    response = requests.get("http://localhost:3000/breaking-news?time=25")
    assert response.status_code == 404
    assert response.json() == {"detail": "No News Found"}


def test_breaking_news_time_date_negative():
    response = requests.get("http://localhost:3000/breaking-news?time=25&date=1999-10-10")
    assert response.status_code == 404
    assert response.json() == {"detail": "No News Found"}
