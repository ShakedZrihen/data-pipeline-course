from fastapi import FastAPI, Query
from mangum import Mangum
import json
from typing import Optional

app = FastAPI()

data_path = "data.json"

@app.get("/")
def hello_world():
    return 200

@app.get("/breaking-news")
def extract_breaking_news(data_path):

    with open(data_path, 'r', encoding='utf-8') as file:
        news_data = json.load(file)

    breaking_news = {"date": []}
    for time, news in news_data.items():
        breaking_news["date"].append({time: news})

    return breaking_news

@app.get("/breaking-news")
def extract_breaking_news(
    date: Optional[str] = Query(None, description="Date in YYYY-MM-DD format"),
    time: Optional[str] = Query(None, description="Time in HH:MM format")
):
    with open(data_path, 'r', encoding='utf-8') as file:
        news_data = json.load(file)

    if date and time:
        news_item = news_data.get(time)
        if news_item and date in time:
            return {time: news_item}
        else:
            return 404

    if date and not time:
        filtered_news = {time: news for time, news in news_data.items() if date in time}
        return filtered_news

    if time and not date:
        news_item = news_data.get(time)
        if news_item:
            return {time: news_item}
        else:
            return {"error": "No news found for the specified time"}

    return news_data

handler = Mangum(app)
