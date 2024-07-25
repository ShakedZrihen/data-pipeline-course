from fastapi import FastAPI
from mangum import Mangum
from typing import Optional
from services.news import get_breaking_news
from services.db import init
import uvicorn
app = FastAPI()
init()


@app.get("/health")
def health():
    return 200


@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    breaking_news_data = get_breaking_news(date)
    if not date and time:
        for date_news in breaking_news_data:
            breaking_news_data[date_news] = {key: value for key, value in breaking_news_data[date_news].items() if
                                             time in key}
    elif time:
        breaking_news_data = {key: value for key, value in breaking_news_data.items() if time in key}
    return breaking_news_data


handler = Mangum(app)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
