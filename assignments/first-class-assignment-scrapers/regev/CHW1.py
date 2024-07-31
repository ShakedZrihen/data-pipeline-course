import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

response = requests.get('https://www.ynet.co.il/news/category/184')

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

breaking_news = soup.find_all('div', class_='titleRow')


resultt= soup.find('time', class_='DateDisplay').attrs['datetime']

formatted_data = {}

for news in breaking_news:
    hour = news.find('time', class_='DateDisplay')
    hour = datetime.strptime(hour.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
    hour = f'{hour.hour + 3}:{hour.minute}'
    content = news.text
    formatted_data[hour] = content

todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)