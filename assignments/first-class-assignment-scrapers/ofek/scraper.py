# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
import os
import json


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def scrape():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='AccordionSection')
    news_list = {}
    for news in breaking_news:
        title = news.find('div', class_='titleRow').text
        hour = news.find('time', class_='DateDisplay').get('datetime')
        hour_obj = parser.parse(hour)
        currentTime = hour_obj.strftime("%H-%M-%S")
        news_list[currentTime] = title

    date = datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'{date}.json')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(news_list, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    scrape()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
