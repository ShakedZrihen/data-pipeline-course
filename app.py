from fastapi import FastAPI, Response, status
from mangum import Mangum
from typing import Optional
from services.db import read_json_by_date, read_json_by_date_and_time, read_all_json, read_json_by_time

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/health")
async def health():
    return 200


@app.get("/breaking-news", status_code=200)
async def breaking_news(response: Response, date: Optional[str] = None, time: Optional[str] = None):
    if date and time:
        data = read_json_by_date_and_time(date, time)
        if data == 404:
            response.status_code = status.HTTP_404_NOT_FOUND
        return data
    if date:
        return read_json_by_date(date)
    if time:
        return read_json_by_time(time)
    if not date and not time:
        return read_all_json()


handler = Mangum(app)
