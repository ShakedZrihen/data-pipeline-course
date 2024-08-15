from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from app import app
from services.db import data

client = TestClient(app)

mock_data = {
    "2024-07-31": {
        "09:49:35": "Report 1",
        "09:37:33": "Report 2",
        "09:34:14": "Report 3",
        "09:33:16": "Report 4"
    },
    "2024-07-30": {"09:49:35": "Report 5"}
}


@pytest.fixture
def mock_db():
    with patch.dict(data, mock_data, clear=True):
        yield data


def test_health_check(mock_db):
    res = client.get("/health")
    assert res.status_code is 200


def test_breaking_news_200(mock_db):
    res = client.get("/breaking-news")
    assert res.status_code is 200
    assert res.json() == {"2024-07-31": [{
        "09:49:35": "Report 1"},
        {"09:37:33": "Report 2"},
        {"09:34:14": "Report 3"},
        {"09:33:16": "Report 4"}],
        "2024-07-30": [{"09:49:35": "Report 5"}]}


def test_breaking_news_by_date_200(mock_db):
    res = client.get("/breaking-news?date=2024-07-30")
    assert res.status_code == 200
    assert res.json() == {'09:49:35': 'Report 5'}


def test_breaking_news_by_date_404(mock_db):
    res = client.get("/breaking-news?date=30-07-2024")
    assert res.status_code == 404
    assert res.json() == {'error': 'Invalid Date'}


def test_breaking_news_by_date_404_not_found(mock_db):
    res = client.get("/breaking-news?date=2023-07-30")
    assert res.status_code == 404
    assert res.json() == {'error': 'Not Found'}

