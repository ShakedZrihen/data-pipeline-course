import json
import os
import logging
from datetime import datetime, timedelta
from services.content_generator import generate_random_content, save_content_to_file
from config import DB_FOLDER

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get():
    logger.info(f"Fetching data from DB_FOLDER: {DB_FOLDER}")
    data = {}
    
    for date in os.listdir(DB_FOLDER):
        if date.endswith('.json'):
            file_path = os.path.join(DB_FOLDER, date)
            logger.info(f"Loading data from file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                news = json.load(f)
                data[date.replace('.json', '')] = news
    
    logger.info(f"Fetched data: {data}")
    return data

def init():
    generated_content = generate_random_content()
    save_content_to_file(generated_content, DB_FOLDER)
