import json
import os
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from datetime import datetime

def fetch_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='AccordionSection')
    news_data = {}
    for article in articles:
        title = article.find('div', class_='title').text.strip()
        timestamp = article.find('time')['datetime']
        formatted_time = parser.parse(timestamp).strftime('%H_%M_%S')
        news_data[formatted_time] = title
    return news_data

def save_news(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    url = 'https://www.ynet.co.il/news/category/184'
    news_data = fetch_news(url)
    date_str = datetime.today().strftime('%Y_%m_%d')
    script_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_directory, f'{date_str}.json')
    save_news(news_data, full_path)
