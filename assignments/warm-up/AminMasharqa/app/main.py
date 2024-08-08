from fastapi import FastAPI, HTTPException
import json
from datetime import datetime, timezone
import os

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "API is up and running"}

@app.get("/breaking-news")
async def get_breaking_news(date: str = None, time: str = None):
    try:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        filename = f"{date_str}.json"
        if os.path.exists(filename):
            with open(filename, "r") as json_file:
                data = json.load(json_file)
        else:
            raise HTTPException(status_code=404, detail="No news data found for today.")
        
        if date and time:
            for news_date in data:
                if news_date == date:
                    for news in data[news_date]:
                        if time in news:
                            return {news_date: news[time]}
            raise HTTPException(status_code=404, detail="No news found for the specified date and time.")
        
        if date:
            if date in data:
                return data[date]
            raise HTTPException(status_code=404, detail="No news found for the specified date.")
        
        if time:
            news_at_time = {}
            for news_date in data:
                for news in data[news_date]:
                    if time in news:
                        news_at_time[news_date] = news[time]
            if news_at_time:
                return news_at_time
            raise HTTPException(status_code=404, detail="No news found for the specified time.")
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
