import json
import os
from services.news_scraper import generate,save_content
from config import DB_FOLDER

def get():
    data = {}
    for filename in os.listdir(DB_FOLDER):
        if filename.endswith('.json'):
            date = filename.split(".")[0]
            file_path = os.path.join(DB_FOLDER, date)
            with open(file_path+'.json', 'r', encoding='utf-8') as f:
                news = json.load(f)
                data[date] = news 
    return data

def init():
    save_content(generate())
