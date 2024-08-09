import json
import os
from datetime import datetime, timedelta
from services.content_generator import generate_news_content, save_content_to_file
from config import DB_FOLDER

def get():
    data = {} 
    for date_file in os.listdir(DB_FOLDER):
        if date_file.endswith('.json'):
            file_path = os.path.join(DB_FOLDER, date_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                news = json.load(f)    
    return news


def init():
    todays_date = datetime.now().strftime('%d-%m-%Y')
    generated_content = generate_news_content()
    save_content_to_file(generated_content, todays_date, DB_FOLDER)


