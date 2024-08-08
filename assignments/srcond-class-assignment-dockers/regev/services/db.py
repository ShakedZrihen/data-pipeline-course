import json
import os
import logging
from datetime import datetime
from services.content_generator import generate_random_content, save_content_to_file
from config import DB_FOLDER

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def format_time(time_str):
    """Ensure time is in HH:MM format and adjust times greater than 24 hours"""
    try:
        # Split the time into hours and minutes
        parts = time_str.split(':')
        hour = int(parts[0])
        minute = int(parts[1])

        # Adjust hours greater than 24
        while hour >= 24:
            hour -= 24

        # Format the time properly
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
                        # Ensure time is in correct format
                        formatted_time = format_time(time)
                        if not formatted_time:
                            continue
                        converted_news[formatted_time] = headline
                    except ValueError as e:
                        # Log and skip invalid time formats
                        logger.error(f"Invalid time format in file {file_path}: {time} - {e}")
                data[date.replace('.json', '')] = converted_news
    
    logger.info(f"Fetched data: {data}")
    return data

def init():
    generated_content = generate_random_content()
    save_content_to_file(generated_content, DB_FOLDER)
