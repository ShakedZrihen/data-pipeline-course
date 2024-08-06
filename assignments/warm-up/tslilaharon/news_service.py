import json
import os
import logging
from news_scraper import fetch_and_save_data

def get_news(date: str = None, time: str = None):
    logging.info(f"Fetching news with date={date} and time={time}")
    
    file_path = 'news_data.json'
    
    if not os.path.exists(file_path):
        file_path, data = fetch_and_save_data()
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    if date and time:
        if date in data and time in data[date]:
            return {time: data[date][time]}, 200
        else:
            return {"error": "News not found for the given date and time."}, 404
    elif date:
        if date in data:
            return data[date], 200
        else:
            return {"error": "News not found for the given date."}, 404
    elif time:
        result = {}
        for d in data:
            if time in data[d]:
                result[d] = data[d][time]
        if result:
            return result, 200
        else:
            return {"error": "News not found for the given time."}, 404
    else:
        return data, 200
