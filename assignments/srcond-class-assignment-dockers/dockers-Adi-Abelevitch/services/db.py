import json
import os

def fetch_news_data(path='resources'):
    news_data = {}
    if not os.path.exists(path):
        os.makedirs(path)

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
    return news_data.get(date)

def get_news_by_time(news_data, time):
    result = {}
    for date in news_data:
        if time in news_data[date]:
            result[date] = news_data[date][time]
    return result if result else None
