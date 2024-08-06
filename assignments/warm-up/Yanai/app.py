from typing import Optional
from fastapi import FastAPI, Response, status
from mangum import Mangum
from services.news import get_breaking_news
from services.db import init

app = FastAPI()
init()


@app.get("/health", status_code=200)
def health():
    return {"status code: 200"}


@app.get("/breaking-news", status_code=200)
def breaking_news(response: Response, date: Optional[str] = None, time: Optional[str] = None):
    breaking_news_data = get_breaking_news()
    if not date and not time:
        return breaking_news_data
    if date:
        if not (date in breaking_news_data):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No breaking news found"}
        breaking_news_data = breaking_news_data[date]
        if time:
            breaking_news_data = {key: value for key, value in breaking_news_data.items() if time in key}
    elif time:
        for date_news in [item for item in breaking_news_data]:
            breaking_news_data[date_news] = {key: value for key, value in breaking_news_data[date_news].items() if
                                             time in key}
            if not breaking_news_data[date_news]:
                del breaking_news_data[date_news]
    if not breaking_news_data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "No breaking news found"}
    return breaking_news_data


handler = Mangum(app)
