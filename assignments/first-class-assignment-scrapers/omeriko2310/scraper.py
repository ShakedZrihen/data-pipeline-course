import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = 'https://www.ynet.co.il/news/category/184'  # Ensure this is the correct URL for Ynet's breaking news
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_sections = soup.find_all('div', class_='AccordionSection')

# Format data to the desired format
formatted_data = {}

for section in news_sections:
    title_element = section.find('div', class_='title')
    time_element = section.find('time', class_='DateDisplay')
    if title_element and time_element:
        title = title_element.text.strip()
        # Extract the time from the datetime attribute
        datetime_attr = time_element.get('datetime')
        if datetime_attr:
            hour = datetime_attr.split('T')[1][:5]  # This assumes the format is like '2024-07-25T10:22:00Z'
            formatted_data[hour] = title

todays_date = datetime.now().strftime('%Y-%m-%d')  # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)

if formatted_data:
    print("Formatted data saved successfully.")
else:
    print("No data was formatted and saved.")
