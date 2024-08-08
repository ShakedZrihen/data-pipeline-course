from fastapi import FastAPI, HTTPException
from news_scraper import fetch_and_save_data
import os
import json
import logging

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "200"}

@app.get("/breaking-news")
def get_breaking_news(date: str = None, time: str = None):
    logging.info(f"Received request with date={date} and time={time}")
    
    file_path = 'news_data.json'
    
    if not os.path.exists(file_path):
        file_path, data = fetch_and_save_data()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if date and time:
        if date in data and time in data[date]:
            return {time: data[date][time]}
        else:
            raise HTTPException(status_code=404, detail="News not found for the given date and time.")
    elif date:
        if date in data:
            return data[date]
        else:
            raise HTTPException(status_code=404, detail="News not found for the given date.")
    elif time:
        result = {}
        for d in data:
            if time in data[d]:
                result[d] = data[d][time]
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="News not found for the given time.")
    else:
        return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
