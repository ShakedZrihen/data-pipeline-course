import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pytz

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
            time = now.time()
            hm = time.strftime("%H:%M")
    formatted_data[hm] = content.text


todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)


