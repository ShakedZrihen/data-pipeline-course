import json
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('div', class_='titleRow')
    formatted_data = {}
    todays_date = datetime.now().strftime('%Y-%m-%d')
    for news in breaking_news:
        hour_tag = news.find('time', class_='DateDisplay')
        if hour_tag and 'datetime' in hour_tag.attrs:
            dates = datetime.strptime(hour_tag.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
            hour = dates.hour + 3
            minute = dates.minute
            # Ensure hours are within 24-hour format
            while hour >= 24:
                hour -= 24
            formatted_hour = f'{hour:02}:{minute:02}'
            content = news.get_text(strip=True)
            if todays_date not in formatted_data:
                formatted_data[todays_date] = {}
            formatted_data[todays_date][formatted_hour] = content

    return formatted_data

def save_content_to_file(content, path='.'):
    for date, item in content.items():
        filename = os.path.join(path, f"{date}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news_content = fetch_news()
    save_content_to_file(news_content)
