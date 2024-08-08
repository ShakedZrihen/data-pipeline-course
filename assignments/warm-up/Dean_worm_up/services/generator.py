import os
import json
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

def generate_random_content(date):
    print(f"Fetching content for {date}")  
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('div', class_='titleRow')

    formatted_data = {}

    for news in breaking_news:
        hour_tag = news.find('time', class_='DateDisplay')
        if hour_tag and 'datetime' in hour_tag.attrs:
            news_date = datetime.strptime(hour_tag.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
            if news_date == date:
                hour = (datetime.strptime(hour_tag.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').hour + 3) % 24
                minute = datetime.strptime(hour_tag.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').minute
                formatted_hour = f'{hour:02}:{minute:02}'
                date_str = f'{news_date.year}-{news_date.month:02}-{news_date.day:02}'
                content = news.get_text(strip=True)
                if date_str not in formatted_data:
                    formatted_data[date_str] = {}
                formatted_data[date_str][formatted_hour] = content

    print(f"Content for {date}: {formatted_data}")  
    return formatted_data

def save_content_to_file(content, path='db'):
    if not os.path.exists(path):
        os.makedirs(path)  
    if not content:
        print("No content to save") 
    else:
        print(f"Saving content to {path}")  
        for date, item in content.items():
            filename = os.path.join(path, f"{date}.json")
            print(f"Saving file: {filename}") 
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(item, f, ensure_ascii=False, indent=4)

def init(path='.'):
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        os.makedirs(path)
    
    today = datetime.now().date()
    
    all_data = {}
    for day_offset in range(8): 
        date = today - timedelta(days=day_offset)
        print(f"Fetching data for {date}")
        daily_data = generate_random_content(date)
        all_data.update(daily_data)
    
    save_content_to_file(all_data, path)
