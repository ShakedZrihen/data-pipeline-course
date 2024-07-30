# test_main.py

import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio
async def test_breaking_news_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/breaking-news")
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.asyncio
async def test_breaking_news_no_date_no_time():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/breaking-news")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
