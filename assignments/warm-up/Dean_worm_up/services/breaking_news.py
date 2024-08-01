from fastapi import HTTPException
from services.db import get as get_from_db

def get_breaking_news(date: str = None, time: str = None):
    data = get_from_db()
    
    if date and time:
        if date in data and time in data[date]:
            return {date: {time: data[date][time]}}
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified date and time.")
    
    if date:
        if date in data:
            return {date: data[date]}
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified date.")
    
    if time:
        filtered_news = {d: {time: news[time]} for d, news in data.items() if time in news}
        if filtered_news:
            return filtered_news
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified time.")
    
    return data
