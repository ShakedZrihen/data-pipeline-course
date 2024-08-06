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
        if date in breaking_news_data and time in breaking_news_data[date]:
            return {time: breaking_news_data[date][time]}
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified date and time")
    
    if date:
        if date in breaking_news_data:
            return breaking_news_data[date]
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified date")

    if time:
        news_by_time = {}
        for news_date in breaking_news_data:
            if time in breaking_news_data[news_date]:
                news_by_time[news_date] = breaking_news_data[news_date][time]
        if news_by_time:
            return news_by_time
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified time")

    return breaking_news_data


handler = Mangum(app)