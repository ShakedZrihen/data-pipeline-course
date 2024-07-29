
import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = 'https://www.ynet.co.il/news/category/184'

scraped_data = {}

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_rows = soup.find_all('div', class_='titleRow')

    for row in news_rows:
        str_time = row.find('time', class_='DateDisplay')['datetime']
        obj_time = datetime.strptime(str_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_time = obj_time.strftime('%H:%M')
        title = row.find('div', class_='title').text.strip()
        scraped_data[formatted_time] = title

    date = datetime.now().strftime('%Y-%m-%d')
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(curr_dir, f'{date}.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)

except:
    print("An error occurred")


