import json
import os
from typing import Dict

DB_FOLDER = "resources"

def load_news_data() -> Dict[str, Dict[str, str]]:
    news_data = {}
    for filename in os.listdir(DB_FOLDER):
        if filename.endswith(".json"):
            with open(os.path.join(DB_FOLDER, filename), "r", encoding="utf-8") as infile:
                date_str = filename.replace(".json", "")
                news_data[date_str] = json.load(infile)
    return news_data
