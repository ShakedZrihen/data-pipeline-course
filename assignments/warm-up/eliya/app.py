from fastapi import FastAPI
from mangum import Mangum
from typing import Optional
import json

app = FastAPI()

data_path = "./news.json"

@app.get("/health")
def health():
    return 200


@app.get("/breaking-news")
def extract_breaking_news(
    date: Optional[str] = None,
    time: Optional[str] = None
):
    with open(data_path, 'r', encoding='utf-8') as file:
        news_data = json.load(file)

    if date and time:
        for timestamp, news_item in news_data.items():
            if timestamp.startswith(f"{date} {time}"):
                return {timestamp: news_item}
        return 404

    if date and not time:
        filtered_news = {time: news for time, news in news_data.items() if date in time}
        if filtered_news:
            return filtered_news
        else:
            return {"error": "No news found for the specified date"}

    if time and not date:
        filtered_news = {timestamp: news for timestamp, news in news_data.items() if timestamp.endswith(time)}
        if filtered_news:
            return filtered_news
        else:
            return {"error": "No news found for the specified time"}
        # news_item = news_data.get(time)
        # if news_item:
        #     return {time: news_item}
        # else:
        #     return {"error": "No news found for the specified time"}

    return news_data


handler = Mangum(app)
