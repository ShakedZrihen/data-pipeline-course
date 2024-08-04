from fastapi import FastAPI, HTTPException
from mangum import Mangum
from typing import Optional
from services.breaking_news import fetch_news_data, handle_date_and_time_request, handle_date_request, handle_time_request, handle_all_news_request
from services.db import fetch_news_data
import os
import json
app = FastAPI()

news = fetch_news_data()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Breaking News API. Use /docs for API documentation."}

@app.get("/health")
def health():
    return {"status": 200}

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    news_data = fetch_news_data()
    if news_data is None:
        raise HTTPException(status_code=404, detail="No news data available")

    if date and time:
        return handle_date_and_time_request(news_data, date, time)
    elif date:
        return handle_date_request(news_data, date)
    elif time:
        return handle_time_request(news_data, time)
    else:
        return handle_all_news_request(news_data)

handler = Mangum(app)