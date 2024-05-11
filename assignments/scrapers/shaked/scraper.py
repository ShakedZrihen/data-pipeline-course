import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# bs4 documentation: https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup
# bs4 cheat sheet: https://proxiesapi.com/articles/the-complete-beautifulsoup-cheatsheet-with-examples

# URL to scrape
url = 'https://news.walla.co.il/breaking'

# TODO: handle pagination for more than 1 page

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Validate soup is got the data
# print(soup.prettify())

# get all flashes
flashes = soup.find_all('h1', class_='breaking-item-title')

# format data to the desired format

formatted_data = {}

for flash in flashes:
    hour = flash.find('span', class_='red-time').text
    content = [text for text in flash.contents if isinstance(text, str)]
    formatted_data[hour] = content[-1]

# validate formatting
# print(formatted_data)

# save the formatted_data to file
todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
