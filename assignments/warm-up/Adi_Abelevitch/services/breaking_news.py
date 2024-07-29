from typing import Optional, Dict, Any
from fastapi import HTTPException
from .db import load_news_data, get_all_news_data

def get_all_breaking_news() -> Dict[str, Any]:
    return get_all_news_data()

def get_breaking_news_by_date(date: str) -> Dict[str, Any]:
    news_for_date = load_news_data(date)
    if news_for_date:
        return news_for_date
    else:
        raise HTTPException(status_code=404, detail="News not found for given date")

def get_breaking_news_by_time(time: str) -> Dict[str, Any]:
    news_for_time = {}
    all_news_data = get_all_news_data()
    for date, news_data in all_news_data.items():
        if time in news_data:
            news_for_time[date] = news_data[time]
    if news_for_time:
        return news_for_time
    else:
        raise HTTPException(status_code=404, detail="News not found for given time")

def get_breaking_news_by_date_and_time(date: str, time: str) -> Dict[str, Any]:
    news_data = load_news_data(date)
    if time in news_data:
        return {"news": news_data[time]}
    else:
        raise HTTPException(status_code=404, detail="News not found for given date and time")
