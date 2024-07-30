from fastapi import FastAPI, HTTPException
from mangum import Mangum
from typing import Optional
from services.breaking_news import get_breaking_news

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Breaking News API. Use /docs for API documentation."}

@app.get("/health")
def health():
    return {"status": 200}

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    print(f"Received request for date: {date}, time: {time}")
    news_data = get_breaking_news()
    if news_data is None:
        print("No news data available")
        raise HTTPException(status_code=404, detail="No news data available")

    print(f"Fetched data: {news_data}")

    if date and time:
        print(f"Searching for date: {date} and time: {time}")
        if date in news_data and time in news_data[date]:
            return {time: news_data[date][time]}
        else:
            print(f"Date {date} or time {time} not found in data")
            raise HTTPException(status_code=404, detail="News not found for the specified date and time")
    elif date:
        print(f"Searching for date: {date}")
        if date in news_data:
            return news_data[date]
        print(f"Data not found for date: {date}")
        raise HTTPException(status_code=404, detail="News not found for the specified date")
    elif time:
        print(f"Searching for time: {time}")
        result = {date: news_data[date][time] for date in news_data if time in news_data[date]}
        if result:
            return result
        print(f"Data not found for time: {time}")
        raise HTTPException(status_code=404, detail="News not found for the specified time")
    else:
        formatted_data = {}
        for date in news_data:
            news_from_date = []
            for news_time in news_data[date]:
                news_from_date.append({news_time: news_data[date][news_time]})
            formatted_data[date] = news_from_date
        return formatted_data

handler = Mangum(app)
