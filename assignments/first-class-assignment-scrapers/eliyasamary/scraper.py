import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = 'https://www.ynet.co.il/news/category/184'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

all_news = soup.find_all('div', class_='titleRow')

data = {}

for news in all_news:
    time = news.find('div', class_='date').text
    title = news.find('div', class_='title').text
    data[time] = title
    
    print(data)



