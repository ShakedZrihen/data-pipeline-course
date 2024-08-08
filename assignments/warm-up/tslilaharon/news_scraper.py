import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import os

def fetch_and_save_data():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('div', class_='AccordionSection')
    formatted_data = {}

    for news in breaking_news:
        time_tag = news.find('time', class_='DateDisplay')
        title_tag = news.find('div', class_='title')

        if time_tag and title_tag:
            dt_str = time_tag['datetime']
            dt = datetime.fromisoformat(dt_str.rstrip('Z')) 
            dt = dt + timedelta(hours=3)  
            date = dt.strftime('%Y-%m-%d')
            hour = dt.strftime('%H:%M')
            content = title_tag.text.strip()
            if date not in formatted_data:
                formatted_data[date] = {}
            formatted_data[date][hour] = content

    with open('news_data.json', 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=4)

    return 'news_data.json', formatted_data
