import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

url = 'https://www.ynet.co.il/news/category/184'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

breaking_news = soup.find_all('div', class_='AccordionSection')

formatted_data = {}

for news in breaking_news:
    date_div = news.find('div', class_='date')
    if date_div:
        date = date_div.find('time', class_='DateDisplay')
        if date:  # Check if the date element exists
            real_time = date.get('datetime')
            title_div = news.find('div', class_='title')
            title = title_div.text.strip() if title_div else "No title"

            date_obj = datetime.strptime(real_time, '%Y-%m-%dT%H:%M:%S.%fZ')

            adjusted_time = date_obj + timedelta(hours=3)

            # Format the adjusted datetime object back to string
            adjusted_time_str = adjusted_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3] + 'Z'
            day_date = adjusted_time_str[:10]
            time_str = adjusted_time_str[11:16]

            reversed_date = datetime.strptime(day_date, '%Y-%m-%d').strftime('%d-%m-%Y')

            if reversed_date not in formatted_data:
                formatted_data[reversed_date] = {}

            formatted_data[reversed_date][time_str] = title
        else:
            print(f"Warning: No datetime found for a news item: {news}")
    else:
        print(f"Warning: No date div found for a news item: {news}")

# Save the formatted data to a file
todays_date = datetime.now().strftime('%Y-%m-%d')  # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
