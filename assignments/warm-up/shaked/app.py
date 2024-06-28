from fastapi import FastAPI, HTTPException
from mangum import Mangum
from typing import Optional
import json

app = FastAPI()


@app.get("/health")
def health():
    return 200


@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    with open("2024-05-11.json", "r") as file:
        breaking_news_data = json.load(file)

    if time:
        news_in_time = breaking_news_data.get(time)
        return news_in_time or HTTPException(
            status_code=404, detail="News not found for specific time"
        )

    formatted_data = []
    for news in breaking_news_data:
        print(f"news: {news}, {breaking_news_data[news]}")
        formatted_data.append({news: breaking_news_data[news]})

    return {"2024-05-11": formatted_data}


handler = Mangum(app)
