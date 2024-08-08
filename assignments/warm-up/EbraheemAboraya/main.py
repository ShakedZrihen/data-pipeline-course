from fastapi import FastAPI, HTTPException
app = FastAPI()

from breaking_news import get_breaking_news

@app.get("/health")
def health_check():
    return {"status": 200}

@app.get("/breaking-news")
def breaking_news(date: str = None, time: str = None):
    try:
        news = get_breaking_news(date, time)
        return news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
