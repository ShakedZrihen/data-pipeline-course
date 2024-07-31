import os
import datetime
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Dict
from mangum import Mangum
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from services.news_generator import scrape_news_ynet, save_news, generate_random_news


class NewsResponse(BaseModel):
    news: Dict[str, Dict[str, str]]


# Example news data for documentation
news_example = {
    "2024-07-30": {"08:00": "News at 8 AM", "12:00": "News at noon"},
    "2024-07-31": {"09:00": "News at 9 AM"},
}

news_data = scrape_news_ynet()
save_news(news_data)

app = FastAPI()


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
) -> NewsResponse:
    date_str = (
        date.strftime("%Y-%m-%d")
        if date
        else datetime.datetime.now().strftime("%Y-%m-%d")
    )

    if date_str in news_data:
        filtered_news = {}
        for news_time, news_title in news_data[date_str].items():
            news_time_obj = datetime.datetime.strptime(news_time, "%H:%M").time()
            if (start_time is None or news_time_obj >= start_time) and (
                end_time is None or news_time_obj <= end_time
            ):
                filtered_news[news_time] = news_title

        if filtered_news:
            return NewsResponse(news={date_str: filtered_news})
        else:
            raise HTTPException(
                status_code=404, detail="News not found for the specified time range"
            )
    raise HTTPException(status_code=404, detail="News not found for the specified date")


@app.get("/generate-news")
def generate_news():
    news_data = generate_random_news()
    save_news(news_data)
    return {"message": "Random news generated and saved successfully"}


handler = Mangum(app)
