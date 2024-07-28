from fastapi import APIRouter, HTTPException
from services.breaking_news_crud import breaking_news_get_all, breaking_news_get_filtered
from services.utils import validate_date, validate_time

router = APIRouter()


@router.get("/health")
async def root():
    return {"message": "App is running"}


@router.get("/breaking-news")
async def get_breaking_news(date: str = "", time: str = ""):
    if not validate_date(date) or not validate_time(time):
        raise HTTPException(status_code=400, detail="Invalid input")
    if date or time:
        breaking_news_get_filtered(date, time)
    else:
        return breaking_news_get_all()