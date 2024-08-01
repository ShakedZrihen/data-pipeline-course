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

# Get all breaking-news
breaking_news = soup.find_all('div', class_='titleRow')

# Format data to the desired format
formatted_data = {}

for news in breaking_news:
    # hour = news.find_all('time', class_='DateDisplay')[0].attrs["datetime"]

    datetime_str = news.find('time', class_='DateDisplay').attrs["datetime"]
    datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
    hour = datetime_obj.strftime('%H:%M')

    title = news.find('div', class_='title').text.strip()

    formatted_data[hour] = title

# Print the formatted data in the desired format
for hour, title in formatted_data.items():
    print(f"{hour}: {title}")

# Save the formatted_data to file
todays_date = datetime.now().strftime('%Y-%m-%d')  # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
