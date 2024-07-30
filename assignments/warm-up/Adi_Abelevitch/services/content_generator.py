import json
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = 'https://news.walla.co.il/breaking'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('h1', class_='breaking-item-title')
    formatted_data = {}
    todays_date = datetime.now().strftime('%Y-%m-%d') 
    for news in breaking_news:
        hour_span = news.find('span', class_='red-time')
        if hour_span:
            hour = hour_span.text.strip()
            content = [text for text in news.contents if isinstance(text, str)]
            if content:
                if todays_date not in formatted_data:
                    formatted_data[todays_date] = {}
                formatted_data[todays_date][hour] = content[-1].strip()
    
    return formatted_data

def save_content_to_file(content, path='.'):
    for date, item in content.items():
        filename = os.path.join(path, f"{date}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news_content = fetch_news()
    save_content_to_file(news_content)
