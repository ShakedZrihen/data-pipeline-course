import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = 'https://news.walla.co.il/breaking'

# TODO: handle pagination for more than 1 page

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

breaking_news = soup.find_all('h1', class_='breaking-item-title')

formatted_data = {}

for news in breaking_news:
    hour = news.find('span', class_='red-time').text
    content = [text for text in news.contents if isinstance(text, str)]
    formatted_data[hour] = content[-1] 
    todays_date = datetime.now().strftime('%Y-%m-%d') 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)