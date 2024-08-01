import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# bs4 documentation: https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup
# bs4 cheat sheet: https://proxiesapi.com/articles/the-complete-beautifulsoup-cheatsheet-with-examples

# URL to scrape
url = 'https://www.ynet.co.il/news/category/184'

# TODO: handle pagination for more than 1 page

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Validate soup is got the data
# print(soup.prettify())

# get all breaking-news
breaking_news = soup.find_all('div', class_='titleRow')

# format data to the desired format

formatted_data = {}


for news in breaking_news:
    # hour = news.find_all('time', class_='DateDisplay')[0].attrs["datetime"]

    datetime_str = news.find('time', class_='DateDisplay').attrs["datetime"]
    datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
    hour = datetime_obj.strftime('%H:%M')

    title = news.find('div', class_='title').text
    formatted_data[hour] = title
    # formatted_data[title] = title

# validate formatting
# print(formatted_data)

# save the formatted_data to file
todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
