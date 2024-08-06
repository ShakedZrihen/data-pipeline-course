from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from services.breaking_news import fetch_news, save_news_to_file, get_saved_news
import json
import os

app = FastAPI()

@app.get("/health")
def read_health():
    return 200

@app.get("/breaking-news")
def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    try:
        if 'AWS_EXECUTION_ENV' in os.environ:
            news = fetch_news()
        else:
            news = fetch_news()
            for date_key, items in news.items():
                save_news_to_file(date_key, items)
            news = get_saved_news()
        
        if date:
            file_path = f"data/{date}.json"
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    news = json.load(f)
                
                if time:
                    for entry in news[date]:
                        if time in entry:
                            pretty_news = json.dumps({time: entry[time]}, indent=4, ensure_ascii=False)
                            return JSONResponse(content=json.loads(pretty_news))
                    raise HTTPException(status_code=404, detail="News not found for the specified date and time")
                
                pretty_news = json.dumps(news, indent=4, ensure_ascii=False)
                return JSONResponse(content=json.loads(pretty_news))
            raise HTTPException(status_code=404, detail="News not found for the specified date")
        
        if time:
            result = {}
            for date_key, items in news.items():
                for item in items:
                    if time in item:
                        if date_key not in result:
                            result[date_key] = []
                        result[date_key].append({time: item[time]})
            if result:
                pretty_news = json.dumps(result, indent=4, ensure_ascii=False)
                return JSONResponse(content=json.loads(pretty_news))
            raise HTTPException(status_code=404, detail="News not found for the specified time")

        pretty_news = json.dumps(news, indent=4, ensure_ascii=False)
        return JSONResponse(content=json.loads(pretty_news))
    except HTTPException as e:
        raise e

from mangum import Mangum
handler = Mangum(app)
