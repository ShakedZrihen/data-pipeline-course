from fastapi import FastAPI
from mangum import Mangum
from functions.get_all_news import get_all_news

app = FastAPI()

@app.get("/health")
def health_code():
    return 200


@app.get("/breaking-news")
def get_news():
    data = get_all_news()
    return data

handler = Mangum(app)