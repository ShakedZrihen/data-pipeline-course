from fastapi import FastAPI, APIRouter, HTTPException
from typing import Optional

app = FastAPI()

# Router for health check
health_router = APIRouter()


@health_router.get("/health")
async def health():
    return {"status": "ok"}

# Router for breaking news
breaking_news_router = APIRouter()

breaking_news_data = {
    "2024-08-01": {
        "10:00": "News 1",
        "12:00": "News 2",
    },
    "2024-08-02": {
        "14:00": "News 3",
        "16:00": "News 4",
    },
}

@breaking_news_router.get("/breaking-news")
async def get_breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    if date and time:
        news = breaking_news_data.get(date, {}).get(time)
        if news:
            return {f"{date} {time}": news}
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified date and time")
    elif date:
        news = breaking_news_data.get(date)
        if news:
            return news
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified date")
    elif time:
        news = {d: news.get(time) for d, news in breaking_news_data.items() if time in news}
        if news:
            return news
        else:
            raise HTTPException(status_code=404, detail="News not found for the specified time")
    else:
        return breaking_news_data

# Include routers in the app
app.include_router(health_router)
app.include_router(breaking_news_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the YNet Breaking News API"}
