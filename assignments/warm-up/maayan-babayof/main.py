import datetime
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Dict, Union
from mangum import Mangum
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from services.news_service import NewsService

app = FastAPI()

# Initialize the news service
news_service = NewsService()

class NewsResponse(BaseModel):
    articles: Dict[str, Union[Dict[str, str], str]]  # Adjusted model to handle different cases

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get(
    "/breaking-news",
    response_model=NewsResponse,
    responses={
        200: {"description": "News found"},
        404: {"description": "No news found"},
    },
)
def fetch_breaking_news(
    date: Optional[datetime.date] = Query(None, examples="2024-08-05"),
    start_time: Optional[datetime.time] = Query(None, examples="09:00"),
    end_time: Optional[datetime.time] = Query(None, examples="12:00")
) -> NewsResponse:
    try:
        if date:
            # Get news for a specific date and time range
            news = news_service.get_news_for_date(date, start_time, end_time)
            if not news:
                raise HTTPException(status_code=404, detail="No news found for the specified date")
            return NewsResponse(articles={date.strftime("%Y-%m-%d"): news})
        elif start_time or end_time:
            # Get news for specific time range
            news = news_service.get_news_for_time(start_time, end_time)
            if not news:
                raise HTTPException(status_code=404, detail="No news found for the specified time")
            return NewsResponse(articles=news)
        else:
            # Get all news
            news = news_service.get_all_news()
            if not news:
                raise HTTPException(status_code=404, detail="No news found")
            return NewsResponse(articles=news)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

handler = Mangum(app)
