from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint to ensure it returns the correct UP status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": 200}

def test_get_all_breaking_news():
    """Test retrieving all breaking news without date and time filters to ensure it returns a dictionary."""
    response = client.get("/breaking-news")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  

def test_get_breaking_news_by_date():
    """Test retrieving breaking news for a specific date to verify correct data formatting."""
    response = client.get("/breaking-news?date=2024-07-31")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  

def test_get_breaking_news_by_date_and_time():
    """Test retrieving breaking news for a specific date and time to ensure correct news retrieval."""
    response = client.get("/breaking-news?date=2024-07-31&time=14:50")
    assert response.status_code == 200
    assert isinstance(response.json(), dict) 
    assert "14:50" in response.json(), "News at the specified time should be present in the response"