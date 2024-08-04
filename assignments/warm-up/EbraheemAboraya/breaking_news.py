import os
import json
from fastapi import HTTPException
from datetime import datetime

def load_news_data(filename):
    with open(os.path.join('data', filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def get_breaking_news(date: str = None, time: str = None):
    if date and time:
        # Fetch news for a specific date and time
        filename = f"{date}.json"
        if not os.path.exists(os.path.join('data', filename)):
            raise HTTPException(status_code=404, detail="No news file found for this date.")
        news_data = load_news_data(filename)
        time_news = {item['hour']: item['title'] for item in news_data if item['hour'] == time}
        if not time_news:
            raise HTTPException(status_code=404, detail="No news at this time.")
        return time_news

    elif date:
        # Fetch news for a specific date
        filename = f"{date}.json"
        if not os.path.exists(os.path.join('data', filename)):
            raise HTTPException(status_code=404, detail="No news file found for this date.")
        news_data = load_news_data(filename)
        return {item['hour']: item['title'] for item in news_data}

    elif time:
        # Fetch news across all dates for a specific time
        all_files = [f for f in os.listdir('data') if f.endswith('.json')]
        time_news = {}
        for file in all_files:
            news_data = load_news_data(file)
            for item in news_data:
                if item['hour'] == time:
                    date = file.split('.')[0]
                    time_news[date] = item['title']
        if not time_news:
            raise HTTPException(status_code=404, detail="No news at this time.")
        return time_news

    else:
        # Fetch all news
        all_files = [f for f in os.listdir('data') if f.endswith('.json')]
        all_news = {}
        for file in all_files:
            date = file.split('.')[0]
            news_data = load_news_data(file)
            all_news[date] = {item['hour']: item['title'] for item in news_data}
        return all_news
