from fastapi import FastAPI, HTTPException, Query
from services.breaking_news import fetch_news_data
from datetime import datetime
from mangum import Mangum
app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "API is running"}

@app.get("/breaking-news")
def breaking_news(date: str = None, time: str = None):
    news_data = fetch_news_data()
    if date and time:
        news = news_data.get(date, {}).get(time)
        if not news:
            raise HTTPException(status_code=404, detail="News not found for the specified date and time")
        return {news}
    elif date:
        if date not in news_data:
            raise HTTPException(status_code=404, detail="No news found for the specified date")
        return news_data[date]
    elif time:
        news_items = {date: times.get(time) for date, times in news_data.items() if time in times}
        if not news_items:
            raise HTTPException(status_code=404, detail="No news found for the specified time")
        return news_items
    else:
        todays_date = datetime.now().strftime('%Y-%m-%d')
        news_today = news_data.get(todays_date, {})
        news_list = [{hour: news} for hour, news in news_today.items()]
        return {todays_date: news_list}



handler = Mangum(app)