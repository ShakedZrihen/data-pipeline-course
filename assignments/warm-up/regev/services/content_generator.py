import random
import json
from datetime import datetime, timedelta
import os
import requests
from bs4 import BeautifulSoup


def generate_random_content():
    response = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('div', class_='titleRow')

    formatted_data = {}

    for news in breaking_news:
        hour_tag = news.find('time', class_='DateDisplay')
        if hour_tag and 'datetime' in hour_tag.attrs:
            dates = datetime.strptime(hour_tag.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
            hour = f'{dates.hour + 3}:{dates.minute}'
            date = f'{dates.year}-{dates.month:02}-{dates.day}'
            content = news.get_text(strip=True)
            if not (date in formatted_data):
                formatted_data[date] = {}
            
            formatted_data[date][hour] = content
    
    return formatted_data

    

    
def save_content_to_file(content, path='.'):
    for date, item in content.items():
        
        filename = os.path.join(path, f"{date}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)
