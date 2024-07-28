import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# URL to scrape
url = 'https://www.ynet.co.il/news/category/184'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# get all breaking-news
breaking_news = soup.find_all('div', class_='titleRow')

# format data to the desired format
formatted_data = {}

for news in breaking_news:
    hour_raw = news.find('time', class_='DateDisplay').attrs['datetime']
    hour_before_timezone = hour_raw[11:16]
    hour_after_timezone = f"{(int(hour_before_timezone[:2]) + 3)%24}{hour_before_timezone[2:]}"
    content = news.text
    formatted_data[hour_after_timezone] = content

# validate formatting
print(formatted_data)

# save the formatted_data to file
todays_date = datetime.now().strftime('%Y-%m-%d')  # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
