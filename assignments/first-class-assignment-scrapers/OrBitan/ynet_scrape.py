import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

news_list = {}


def ynet_scrape():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news= soup.find_all('div', class_='titleRow')
    for new in news:
        date = new.find('div', class_='date')
        title = new.find('div', class_='title')
        time_ = date.find('time', class_='DateDisplay')
        realTime = time_.get('data-wcmdate')
        realTime = realTime[11:16]
        hour = int(realTime[0:2])
        minuts = int(realTime[3:5])
        hour += 3
        hour = hour % 24
        final_time = str(hour) + ":" + str(minuts)
        news_list[final_time] = title.text
    print(news_list)

ynet_scrape()
todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(news_list, f, ensure_ascii=False, indent=4)