from fastapi import FastAPI,HTTPException
from mangum import Mangum
from typing import Optional
from services.breaking_news import get_breaking_news
from services.db import init


app = FastAPI()
init()

@app.get("/health")
def health():
    return 200

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    breaking_news_data = get_breaking_news()
    if not date and not time:
      return breaking_news_data
    filtered_data = {}

    if date:
        if date in breaking_news_data:
            if time:
                # If time is also provided, filter by both date and time
                if time in breaking_news_data[date]:
                    filtered_data[date] = {time: breaking_news_data[date][time]}
                else:
                    # Time not found for the specified date
                    raise HTTPException(status_code=404, detail="Time not found for the specified date")
            else:
                # Only date is provided, return all events for that date
                filtered_data = breaking_news_data[date]
        else:
            # Date not found
            raise HTTPException(status_code=404, detail="Date not found")
    elif time:
        # If only time is provided, search all dates for that time
        for date_key, events in breaking_news_data.items():
            if time in events:
                if date_key not in filtered_data:
                    filtered_data[date_key] = {}
                filtered_data[date_key][time] = events[time]
        
        if not filtered_data:
            # Time not found in any date
            raise HTTPException(status_code=404, detail="Time not found in any date")
    
    return filtered_data
       
    
handler = Mangum(app)
