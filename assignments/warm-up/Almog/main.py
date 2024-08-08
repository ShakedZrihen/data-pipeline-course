from fastapi import FastAPI, HTTPException
import os
import json
from mangum import Mangum  # Import Mangum

app = FastAPI()

def load_data(date: str):
    file_name = f"{date}.json"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise HTTPException(status_code=404, detail="Data not found for the given date")

@app.get("/health")
def health_check():
    return {"status": "UP"}

@app.get("/breaking-news")
def get_breaking_news(date: str = None, time: str = None):
    if date:
        data = load_data(date)
        if time:
            if time in data:
                return {time: data[time]}
            else:
                raise HTTPException(status_code=404, detail="No news found for the given time on this date")
        return data
    else:
        all_news = {}
        for file_name in os.listdir():
            if file_name.endswith(".json"):
                date = file_name.split(".json")[0]
                all_news[date] = load_data(date)
        return all_news

# Wrap the FastAPI app with Mangum for AWS Lambda compatibility
handler = Mangum(app)
