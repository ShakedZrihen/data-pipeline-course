import json
import os
from fastapi import HTTPException

def fetch_news_data():
    news_data = {}
    path = 'resources'
    for file_name in os.listdir(path):
        if file_name.endswith(".json"):
            new_path = f'{path}/{file_name}'
            with open(new_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    if isinstance(data, dict):
                        for key, value in data.items():
                            if isinstance(value, dict):
                                news_data[key] = value
                            else:
                                print(f"Warning: Skipping key '{key}' with value type {type(value).__name__}. Expected dictionary.")
                except json.JSONDecodeError:
                    print(f"Warning: Failed to decode JSON in file '{file_name}'")
                    continue
    return news_data

def get_news_by_date(news_data, date):
    if date in news_data:
        return news_data[date]
    else:
        return None

def get_news_by_time(news_data, time):
    result = {}
    for date in news_data:
        if time in news_data[date]:
            result[date] = news_data[date][time]
    return result if result else None

def get_news_by_date_and_time(news_data, date, time):
    if date in news_data and time in news_data[date]:
        return {time: news_data[date][time]}
    else:
        return None

def format_all_news(news_data):
    return news_data

def handle_date_and_time_request(news_data, date, time):
    result = get_news_by_date_and_time(news_data, date, time)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="News not found for the specified date and time")

def handle_date_request(news_data, date):
    result = get_news_by_date(news_data, date)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="News not found for the specified date")

def handle_time_request(news_data, time):
    result = get_news_by_time(news_data, time)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="News not found for the specified time")

def handle_all_news_request(news_data):
    return format_all_news(news_data)
