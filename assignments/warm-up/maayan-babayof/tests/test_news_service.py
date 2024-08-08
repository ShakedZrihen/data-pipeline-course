import datetime
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_fetch_breaking_news_no_params():
    response = client.get("/breaking-news")
    assert response.status_code == 200
    # Add more assertions based on the expected output structure

def test_fetch_breaking_news_by_date():
    # Replace with actual date you expect to have news for
    date = "2024-08-05"
    response = client.get(f"/breaking-news?date={date}")
    assert response.status_code == 200
    # Add more assertions based on the expected output structure

def test_fetch_breaking_news_by_time():
    # Replace with actual time range you expect to have news for
    start_time = "09:00"
    end_time = "12:00"
    response = client.get(f"/breaking-news?start_time={start_time}&end_time={end_time}")
    assert response.status_code == 200
    # Add more assertions based on the expected output structure

def test_fetch_breaking_news_by_date_and_time():
    # Replace with actual date and time range you expect to have news for
    date = "2024-08-05"
    start_time = "09:00"
    end_time = "12:00"
    response = client.get(f"/breaking-news?date={date}&start_time={start_time}&end_time={end_time}")
    assert response.status_code == 200
    # Add more assertions based on the expected output structure

def test_fetch_breaking_news_not_found():
    # Use a date/time that will definitely not have news
    date = "9999-12-31"
    response = client.get(f"/breaking-news?date={date}")
    assert response.status_code == 404
    assert response.json() == {"detail": "No news found for the specified date"}

