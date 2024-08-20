from mangum import Mangum
from fastapi import FastAPI, Response, HTTPException
from services.controller import get_breaking_news, get_news_by_time, get_news_by_date_and_time, get_news_by_date

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health", status_code=200)
async def health():
    return {"message": "Hi I am healthy"}


@app.get("/breaking-news", status_code=200)
async def breaking_news(res: Response, date: str | None = None, time: str | None = None):
    try:
        if not date and not time:
            return get_breaking_news()
        if date and not time:
            return get_news_by_date(date)
        if not date and time:
            return get_news_by_time(time)
        return get_news_by_date_and_time(date, time)

    except HTTPException as e:
        res.status_code = e.status_code
        res.body = e.detail
        return {"error": e.detail}


handler = Mangum(app)
