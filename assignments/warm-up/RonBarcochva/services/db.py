
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
from services.news_generator import generate_content, save_content


dotenv_path = join(dirname(__file__), '.env')
load_dotenv()


DB_FOLDER = os.environ.get('DB_FOLDER')


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
    save_content(generate_content())
