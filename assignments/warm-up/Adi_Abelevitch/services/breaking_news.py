from fastapi import HTTPException
from .db import get_breaking_news as fetch_breaking_news

def fetch_news_data():
    return fetch_breaking_news()

def get_news_by_date(news_data, date):
    if date in news_data:
        return news_data[date]
    else:
        return None

def get_news_by_time(news_data, time):
    result = {date: news_data[date][time] for date in news_data if time in news_data[date]}
    if result:
        return result
    else:
        return None

def get_news_by_date_and_time(news_data, date, time):
    if date in news_data and time in news_data[date]:
        return {time: news_data[date][time]}
    else:
        return None

def format_all_news(news_data):
    formatted_data = {}
    for date in news_data:
        news_from_date = []
        for news_time in news_data[date]:
            news_from_date.append({news_time: news_data[date][news_time]})
        formatted_data[date] = news_from_date
    return formatted_data

def handle_date_and_time_request(news_data, date, time):
    result = get_news_by_date_and_time(news_data, date, time)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="News not found for the specified date and time")

def handle_date_request(news_data, date):
    result = get_news_by_date(news_data, date)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="News not found for the specified date")

def handle_time_request(news_data, time):
    result = get_news_by_time(news_data, time)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="News not found for the specified time")

def handle_all_news_request(news_data):
    return format_all_news(news_data)
