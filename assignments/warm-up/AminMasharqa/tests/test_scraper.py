import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import as per your project structure

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_breaking_news():
    mock_data = {
        "2024-07-30 10:00:00": "Breaking news 1",
        "2024-07-30 11:00:00": "Breaking news 2",
    }
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert response.json() == {
        "date": [
            {"2024-07-30 10:00:00": "Breaking news 1"},
            {"2024-07-30 11:00:00": "Breaking news 2"},
        ]
    }

@pytest.mark.parametrize("date, expected_response", [
    ("2024-07-30", {"10:00:00": "Breaking news 1", "11:00:00": "Breaking news 2"}),
    ("2024-07-31", {}),
])
def test_breaking_news_by_date(date, expected_response):
    response = client.get(f"/breaking-news?date={date}")
    assert response.status_code == 200
    assert response.json() == expected_response

@pytest.mark.parametrize("time, expected_response", [
    ("10:00:00", {"2024-07-30": "Breaking news 1"}),
    ("12:00:00", {}),
])
def test_breaking_news_by_time(time, expected_response):
    response = client.get(f"/breaking-news?time={time}")
    assert response.status_code == 200
    assert response.json() == expected_response

@pytest.mark.parametrize("date, time, expected_response, expected_status", [
    ("2024-07-30", "10:00:00", "Breaking news 1", 200),
    ("2024-07-30", "12:00:00", "404 Not Found", 404),
])
def test_breaking_news_by_date_and_time(date, time, expected_response, expected_status):
    response = client.get(f"/breaking-news?date={date}&time={time}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == expected_response
    else:
        assert response.json() == {"detail": "News not found"}
