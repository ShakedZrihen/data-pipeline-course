import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pytz

def generate_news_content():
    url = 'https://www.ynet.co.il/news/category/184'
    tz = pytz.timezone('Asia/Jerusalem')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='titleRow')

    formatted_data = {}
    for news in breaking_news:
        hour = news.find('div', class_='date')
        time = hour.find('time', class_='DateDisplay')
        content = news.find('div', class_='title')
        for i in hour.findAll('time'):
            if i.has_attr('datetime'):
                dt = datetime.fromisoformat(i['datetime'])
                now = dt.astimezone(tz) 
                date = now.strftime("%d-%m-%Y")
                time = now.time()
                hm = time.strftime("%H:%M")
                if date not in formatted_data:  
                    formatted_data[date] = {}
                formatted_data[date][hm] = content.text  
    return formatted_data

def save_content_to_file(content, date, path='.'):
    filename = os.path.join(path, f"{date}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
