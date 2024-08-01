import json
import os
import logging
from datetime import datetime, timedelta
from services.generator import generate_random_content, save_content_to_file
from config import DB_FOLDER

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def format_time(time_str):
    try:
        parts = time_str.split(':')
        hour = int(parts[0])
        minute = int(parts[1])

        hour %= 24

        time_obj = datetime.strptime(f"{hour:02d}:{minute:02d}", '%H:%M')
    except Exception as e:
        logger.error(f"Error parsing time: {time_str} - {e}")
        return None
    return time_obj.strftime('%H:%M')

def get():
    logger.info(f"Fetching data from DB_FOLDER: {DB_FOLDER}")
    data = {}
    for date in os.listdir(DB_FOLDER):
        if date.endswith('.json'):
            file_path = os.path.join(DB_FOLDER, date)
            logger.info(f"Loading data from file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                news = json.load(f)
                converted_news = {}
                for time, headline in news.items():
                    try:
                        formatted_time = format_time(time)
                        if not formatted_time:
                            continue
                        converted_news[formatted_time] = headline
                    except ValueError as e:
                        logger.error(f"Invalid time format in file {file_path}: {time} - {e}")
                data[date.replace('.json', '')] = converted_news
    
    logger.info(f"Fetched data: {data}")
    return data

def init(path='db'):
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        os.makedirs(path)
    
    today = datetime.now().date()
    
    all_data = {}
    for day_offset in range(8): 
        date = today - timedelta(days=day_offset)
        daily_data = generate_random_content(date)
        all_data.update(daily_data)
    
    save_content_to_file(all_data, path)
