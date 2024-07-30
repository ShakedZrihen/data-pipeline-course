import json
import os

import requests
from bs4 import BeautifulSoup
from dateutil import parser
from datetime import datetime

news_object = {}


def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='AccordionSection')
    for news in breaking_news:
        content = news.find('div', class_='title').text
        time_str = news.find('time').get('datetime')
        time = parser.parse(time_str).strftime('%H:%M:%S')
        news_object[time] = content


if __name__ == '__main__':
    scrape('https://www.ynet.co.il/news/category/184')
    file_name = datetime.today().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'{file_name}.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(news_object, f, ensure_ascii=False, indent=4)
