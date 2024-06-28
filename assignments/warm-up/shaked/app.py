from fastapi import FastAPI
from mangum import Mangum
from typing import Optional
from services.breaking_news import get_breaking_news

app = FastAPI()


@app.get("/health")
def health():
    return 200


@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    breaking_news_data = get_breaking_news()
    formatted_data = {}
    for date in breaking_news_data:
        news_from_date = []
        for news in breaking_news_data[date]:
            news_from_date.append({news: breaking_news_data[date][news]})
        formatted_data[date] = news_from_date
    return formatted_data


handler = Mangum(app)
