from fastapi import FastAPI
from services.breaking_news import (
    get_all_breaking_news,
    get_breaking_news_by_date,
    get_breaking_news_by_time,
    get_breaking_news_by_date_and_time,
)
from typing import Optional, Dict, Any

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    if date and time:
        return get_breaking_news_by_date_and_time(date, time)
    elif date:
        return get_breaking_news_by_date(date)
    elif time:
        return get_breaking_news_by_time(time)
    else:
        return get_all_breaking_news()
