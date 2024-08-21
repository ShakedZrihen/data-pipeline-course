import requests
import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def fetch_news():
    url = 'https://www.ynet.co.il/news/category/184'
    timezone = pytz.timezone('Asia/Jerusalem')
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.select('div.titleRow')

    news_data = {}
    for item in news_items:
        date_info = item.select_one('div.date')
        time_tag = date_info.select_one('time.DateDisplay')
        title = item.select_one('div.title')
        
        for time_element in date_info.find_all('time'):
            if 'datetime' in time_element.attrs:
                timestamp = datetime.fromisoformat(time_element['datetime'])
                local_time = timestamp.astimezone(timezone)
                
                date_str = local_time.strftime("%d-%m-%Y")
                time_str = local_time.strftime("%H:%M")
                
                if date_str not in news_data:
                    news_data[date_str] = {}
                
                news_data[date_str][time_str] = title.get_text(strip=True)
    return news_data

def store_news_data(content, date, directory='.'):
    file_path = os.path.join(directory, f"{date}.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)
