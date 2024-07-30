import json
import os
from datetime import datetime, timedelta
from services.content_generator import generate_random_content, save_content_to_file
from config import DB_FOLDER

def get():
    data = {}
    
    for date in os.listdir(DB_FOLDER):
        if date.endswith('.json'):
            file_path = os.path.join(DB_FOLDER, date)
            with open(file_path, 'r', encoding='utf-8') as f:
                news = json.load(f)
                data[date.replace('.json', '')] = news
    
    return data


def init():
    for day in range(12, 31):
        specified_date = datetime.strptime(f'2024-05-{day}', '%Y-%m-%d')
        generated_content = generate_random_content()
        save_content_to_file(generated_content, specified_date, DB_FOLDER)


