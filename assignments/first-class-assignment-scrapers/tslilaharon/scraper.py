import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

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
        dt = datetime.fromisoformat(dt_str)
        dt = dt + timedelta(hours=3)
        hour = dt.strftime('%H:%M')
        content = title_tag.text.strip()
        formatted_data[hour] = content

todays_date = datetime.now().strftime('%Y-%m-%d')
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)