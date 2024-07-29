from fastapi import APIRouter, HTTPException
from services.breaking_news_crud import breaking_news_get_all, breaking_news_get_filtered
from services.utils import validate_input

date_format = "%d/%m/%Y"
time_format ="%H:%M"

router = APIRouter()


@router.get("/health")
async def root():
    return {"message": "App is running"}


@router.get("/breaking-news")
async def get_breaking_news(date: str = "", time: str = ""):
    if not validate_input(date, date_format) or not validate_input(time, time_format):
        raise HTTPException(status_code=400, detail="Invalid input")
    if date or time:
        filtered_res = breaking_news_get_filtered(date, time)
        if not filtered_res:
            raise HTTPException(status_code=404, detail="Breaking news with those filters doesn't exist")
        return filtered_res
    else:
        return breaking_news_get_all()