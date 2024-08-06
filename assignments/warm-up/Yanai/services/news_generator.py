import os
import requests
import json
import datetime
from bs4 import BeautifulSoup

def generate_content():
    data = {}
    html = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(html.text, 'html.parser')
    soup = soup.find('div', {'class': 'article-flashes-page'})
    for article in soup.find_all('div', {'class': 'AccordionSection'}):
        time_element = article.find('time')
        if time_element:
            iso_str = time_element.attrs['datetime']
            # handle the Z timezone issue by replacing Z with '+00:00'
            iso_str = iso_str.replace('Z', '+00:00')
            date = datetime.datetime.fromisoformat(iso_str)
            key1 = f'{date:%Y-%m-%d}'
            key2 = f'{date:%H:%M}'
            title_element = article.find('div', {'class': 'title'})
            if title_element:
                value = title_element.text
                if key1 not in data:
                    data[key1] = {}
                data[key1][key2] = value
    return data

def save_content(data):
    for key in data.keys():
        file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', f'{key}.json')
        with open(file_path, 'w', encoding='utf-8') as outfile:
            json.dump(data[key], outfile, indent=4, ensure_ascii=False)
