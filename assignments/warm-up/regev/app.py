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

app = FastAPI()

@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    logger.info(f"Breaking news endpoint called with date={date} and time={time}")
    try:
        breaking_news_data = get_breaking_news(date, time)

        return breaking_news_data
    except Exception as e:
        logger.error(f"Error in breaking news endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

handler = Mangum(app)
