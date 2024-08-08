from fastapi import FastAPI, HTTPException
from mangum import Mangum
from services.scraper import scrape

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return 200


@app.get("/breaking-news")
async def breaking_news(date=None, time=None):
    if not (result := scrape(date, time)):
        raise HTTPException(status_code=404, detail="No News Found")
    return result


handler = Mangum(app)
