from fastapi import FastAPI, HTTPException
from news_service import get_news
import logging

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "200"}

@app.get("/breaking-news")
def get_breaking_news(date: str = None, time: str = None):
    logging.info(f"Received request with date={date} and time={time}")
    news, status_code = get_news(date, time)
    if status_code == 404:
        raise HTTPException(status_code=404, detail=news["error"])
    return news

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
