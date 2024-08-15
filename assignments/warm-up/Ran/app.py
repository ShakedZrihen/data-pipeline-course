from fastapi import FastAPI, HTTPException
from mangum import Mangum
from typing import Optional
from services.breaking_news import get_breaking_news
from services.db import init

app = FastAPI()
init()

@app.get("/")
def health():
    return 200

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    breaking_news_data = get_breaking_news()

    if date and time:
        news_at_time = breaking_news_data.get(date, {}).get(time)
        if news_at_time:
            return {time: news_at_time}
        raise HTTPException(status_code=404, detail="News not found for the date and time")
    
    if date:
        news_on_date = breaking_news_data.get(date)
        if news_on_date:
            return news_on_date
        raise HTTPException(status_code=404, detail="News not found for the date")

    if time:
        news_by_time = {news_date: times[time] for news_date, times in breaking_news_data.items() if time in times}
        if news_by_time:
            return news_by_time
        raise HTTPException(status_code=404, detail="News not found for the time")

    return breaking_news_data

handler = Mangum(app)
