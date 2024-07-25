import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# URL to scrape
url = 'https://www.ynet.co.il/news/category/184'
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# get all breaking-news
breaking_news = soup.find_all('div', class_='AccordionSection')

formatted_data = {}

for news in breaking_news:
    hour = news.find('time', class_='DateDisplay').attrs['datetime'][11:19]

    content= news.findNext('div',class_='title').text
    formatted_data[hour] = content[:]


todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)

file_path = os.path.join(script_dir, f'{todays_date}.json')


