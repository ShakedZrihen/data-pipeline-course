from fastapi import APIRouter, HTTPException
from typing import Optional
from functions.get_all_news import get_all_news
from functions.validator import validate_input

date_format = "%d/%m/%Y"
time_format ="%H:%M"

router = APIRouter()

@router.get("/")
def root():
    return "warm-up by MoranSin"

@router.get("/health")
def health_code():
    return 200


@router.get("/breaking-news")
async def get_news(date: Optional[str] = None, time: Optional[str] = None):
    if not validate_input(date, date_format) or not validate_input(time, time_format):
        raise HTTPException(status_code=400, detail="Invalid input")
    
    data = get_all_news()
    formatted_data = {}
    if date:
        day_data = data[date]
        if time:
            for news in day_data:
                if time in news:
                    formatted_data.update(news)
        formatted_data = day_data
    if time and not date:
        for news_date in data:
            for news in data[news_date]:
                if time in news:
                    formatted_data.update(news)
    if not date and not time:
        formatted_data = data                
    if formatted_data:
        return formatted_data
    else:
        return HTTPException(status_code=404, detail="No matches were found")