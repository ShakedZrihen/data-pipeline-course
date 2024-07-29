import os
import json
from datetime import datetime
from typing import Dict, Any

def load_news_data(date: str) -> Dict[str, Any]:
    filename = os.path.join('.', f"{date}.json")
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

def save_news_data(date: str, data: Dict[str, Any]) -> None:
    filename = os.path.join('.', f"{date}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_all_news_data() -> Dict[str, Any]:
    news_data = {}
    for filename in os.listdir('.'):
        if filename.endswith('.json'):
            date = filename.split('.')[0]
            with open(filename, 'r', encoding='utf-8') as f:
                news_data[date] = json.load(f)
    return news_data
