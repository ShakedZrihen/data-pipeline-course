from fastapi import FastAPI
from mangum import Mangum
from typing import Optional
from functions.get_all_news import get_all_news
from functions.get_news_by_hour import news_by_hour

app = FastAPI()

@app.get("/health")
def health_code():
    return 200


@app.get("/breaking-news?time={time}")
def get_news_by_hour(time : str):
    hours = news_by_hour(time)
    return hours

def get_news():
    data = get_all_news()
    return data


handler = Mangum(app)