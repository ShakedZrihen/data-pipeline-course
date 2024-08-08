import logging
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from typing import Optional
from services.breaking_news import get_breaking_news
from services.db import init

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the data
init()

app = FastAPI(
    title="Breaking News API",
    description="An API to fetch breaking news based on date and time.",
    version="1.0.0"
)

@app.get("/health", summary="Health Check", description="Check the health status of the API")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    logger.info(f"Breaking news endpoint called with date={date} and time={time}")
    try:
        breaking_news_data = get_breaking_news(date, time)

        if date and time:
            logger.info(f"Handling date and time: {date} and {time}")
            return breaking_news_data

        if date:
            logger.info(f"Handling date: {date}")
            return breaking_news_data

        if time:
            logger.info(f"Handling time: {time}")
            return breaking_news_data

        # Return all breaking news formatted by date and time
        formatted_response = {
            date: [{hour: news} for hour, news in hours.items()]
            for date, hours in breaking_news_data.items()
        }
        logger.info(f"Fetched breaking news data: {formatted_response}")
        return formatted_response
    except Exception as e:
        logger.error(f"Error in breaking news endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

handler = Mangum(app)
