import os
import datetime
from fastapi import FastAPI, HTTPException, Query, Depends
from typing import Optional, Dict
from mangum import Mangum
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from services.db import create_latest_news, get_latest_news, get_latest_news_by_date


class NewsResponse(BaseModel):
    news: Dict[str, str]


news_example = {
    "2024-07-30": {"08:00": "News at 8 AM", "12:00": "News at noon"},
    "2024-07-31": {"09:00": "News at 9 AM"},
}

app = FastAPI()


create_latest_news()


def get_news_data():
    return get_latest_news()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.get(
    "/breaking-news",
    response_model=NewsResponse,
    responses={
        200: {
            "content": {"application/json": {"example": news_example}},
            "description": "News found",
        },
        404: {"description": "News not found"},
    },
)
def get_breaking_news(
    date: Optional[datetime.date] = Query(None, example="2024-07-31"),
    start_time: Optional[datetime.time] = Query(None, example="09:00"),
    end_time: Optional[datetime.time] = Query(None, example="12:00"),
    news_data: Dict[str, Dict[str, str]] = Depends(get_news_data),
) -> NewsResponse:
    if date:
        date_str = f'{date.strftime("%Y-%m-%d")}.json'
        if date_str not in news_data:
            raise HTTPException(
                status_code=404, detail="News not found for the specified date"
            )
        filtered_news = {
            news_time: news_title
            for news_time, news_title in news_data[date_str].items()
            if (
                (
                    start_time is None
                    or datetime.datetime.strptime(news_time, "%H:%M").time()
                    >= start_time
                )
                and (
                    end_time is None
                    or datetime.datetime.strptime(news_time, "%H:%M").time() <= end_time
                )
            )
        }

        if not filtered_news:
            raise HTTPException(
                status_code=404, detail="News not found for the specified time range"
            )
    else:
        filtered_news = {
            f"{date_str} {news_time}": news_title
            for date_str, news_items in news_data.items()
            for news_time, news_title in news_items.items()
            if (
                (
                    start_time is None
                    or datetime.datetime.strptime(news_time, "%H:%M").time()
                    >= start_time
                )
                and (
                    end_time is None
                    or datetime.datetime.strptime(news_time, "%H:%M").time() <= end_time
                )
            )
        }

        if not filtered_news:
            filtered_news = {
                f"{date_str} {news_time}": news_title
                for date_str, news_items in news_data.items()
                for news_time, news_title in news_items.items()
            }

    return NewsResponse(news=filtered_news)


@app.get("/generate-news")
def generate_news():
    news_data = generate_random_news()
    save_news(news_data)
    return {"message": "Random news generated and saved successfully"}


handler = Mangum(app)
