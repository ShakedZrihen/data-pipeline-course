import sys
import os
from unittest.mock import patch
from fastapi import Depends

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from fastapi.testclient import TestClient
from main import app, get_news_data

client = TestClient(app)

# Static news data to be used for mocking
mocked_news_data = {
    "2024-07-30": {"08:00": "News at 8 AM", "12:00": "News at noon"},
    "2024-07-31": {"09:00": "News at 9 AM"},
}


def override_get_news_data():
    return mocked_news_data


app.dependency_overrides[get_news_data] = override_get_news_data


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


if __name__ == "__main__":
    test_health_check()
