from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Dict, List, Optional

app = FastAPI()

# Dummy data for demonstration purposes
breaking_news = {
    "2023-07-01": {
        "08:00": "News at 8 AM",
        "12:00": "News at 12 PM"
    },
    "2023-07-02": {
        "09:00": "News at 9 AM",
        "15:00": "News at 3 PM"
    }
}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/breaking-news")
async def get_breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    if date and time:
        news = breaking_news.get(date, {}).get(time)
        if news:
            return {"news": news}
        else:
            raise HTTPException(status_code=404, detail="News not found")
    elif date:
        return breaking_news.get(date, {})
    elif time:
        results = {date: news.get(time) for date, news in breaking_news.items() if time in news}
        if results:
            return results
        else:
            raise HTTPException(status_code=404, detail="News not found")
    else:
        return breaking_news

