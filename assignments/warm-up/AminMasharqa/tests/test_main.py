import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import os
import logging
from app.main import app

client = TestClient(app)

def setup_function(function):
    # Clean up before running the test
    try:
        os.remove("news_data.json")
    except FileNotFoundError:
        pass

def teardown_function(function):
    # Clean up after running the test
    try:
        os.remove("news_data.json")
    except FileNotFoundError:
        pass

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API is up and running"}

@patch('app.main.get_news_data')
def test_breaking_news(mock_get_news_data):
    mock_data = {
        "2024-07-30 10:00:00": "Breaking news 1",
        "2024-07-30 11:00:00": "Breaking news 2",
    }
    logging.debug(f"Setting mock data: {mock_data}")
    mock_get_news_data.return_value = mock_data

    response = client.get("/breaking-news")
    logging.debug(f"Response status code: {response.status_code}")
    logging.debug(f"Response JSON: {response.json()}")

    assert response.status_code == 200
    assert response.json() == mock_data

@patch('app.main.scrape_ynet')
def test_trigger_scrape(mock_scrape_ynet):
    mock_scrape_ynet.return_value = {
        "2024-07-30 10:00:00": "Breaking news 1",
        "2024-07-30 11:00:00": "Breaking news 2",
    }
    logging.debug(f"Setting mock return value for scrape_ynet: {mock_scrape_ynet.return_value}")

    response = client.post("/scrape-news")
    logging.debug(f"Response status code: {response.status_code}")
    logging.debug(f"Response JSON: {response.json()}")
    
    assert response.status_code == 200
    assert response.json() == {"status": "Scraping completed", "news_count": 2}
