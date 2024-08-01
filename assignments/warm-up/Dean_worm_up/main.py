import logging
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from typing import Optional, List
from pydantic import BaseModel
from services.breaking_news import get_breaking_news
from services.db import init
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

init()

app = FastAPI(
    title="Breaking News API",
    description="An API to fetch breaking news based on date and time.",
    version="1.0.0"
)

class NewsItem(BaseModel):
    time: str
    headline: str

class NewsResponse(BaseModel):
    date: str
    news: List[NewsItem]

def parse_time(time_str: str):
    try:
        return datetime.strptime(time_str, '%H:%M').time()
    except ValueError as e:
        logger.error(f"Invalid time format: {time_str} - {e}")
        return None

@app.get("/health", summary="Health Check", description="Check the health status of the API")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}

@app.get("/breaking-news", response_model=List[NewsResponse])
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    logger.info(f"Breaking news endpoint called with date={date} and time={time}")
    try:
        breaking_news_data = get_breaking_news(date, time)

        if not breaking_news_data:
            raise HTTPException(status_code=404, detail="No news available for the provided date and time.")

        formatted_news = []

        for news_date, news_items in breaking_news_data.items():
            news_list = [NewsItem(time=item_time, headline=headline) for item_time, headline in news_items.items()]
            formatted_news.append(NewsResponse(date=news_date, news=news_list))

        if date and time:
            logger.info(f"Handling date and time: {date} and {time}")
            if date in breaking_news_data and time in breaking_news_data[date]:
                specific_news = [NewsItem(time=time, headline=breaking_news_data[date][time])]
                return [NewsResponse(date=date, news=specific_news)]
            else:
                raise HTTPException(status_code=404, detail="No news available for the provided date and time.")

        return formatted_news

    except Exception as e:
        logger.error(f"Error fetching breaking news: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

handler = Mangum(app)
