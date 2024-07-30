from fastapi import FastAPI, HTTPException
from .scraper import scrape_ynet

app = FastAPI()
# this is the same as the previous snippet

@app.get("/health")
def health_check():
    return {"status": "API is up and running"}

@app.get("/breaking-news")
def breaking_news():
    news = scrape_ynet()
    return news

@app.get("/breaking-news")
def breaking_news(date: str = None, time: str = None):
    news = scrape_ynet()
    if date and time:
        news_item = news.get(f"{date} {time}:00")
        if news_item:
            return {f"{date} {time}:00": news_item}
        else:
            raise HTTPException(status_code=404, detail="News not found for specified date and time")
    elif date:
        filtered_news = {key: value for key, value in news.items() if key.startswith(date)}
        if filtered_news:
            return filtered_news
        else:
            raise HTTPException(status_code=404, detail="News not found for specified date")
    elif time:
        filtered_news = {key: value for key, value in news.items() if key.endswith(f"{time}:00")}
        if filtered_news:
            return filtered_news
        else:
            raise HTTPException(status_code=404, detail="News not found for specified time")
    return news
