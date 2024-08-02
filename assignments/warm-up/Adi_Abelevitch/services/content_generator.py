import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

def fetch_news():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('div', class_='titleRow')
    formatted_data = {}
    todays_date = datetime.now().strftime('%Y-%m-%d')
    previous_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    for news in breaking_news:
        hour_tag = news.find('time', class_='DateDisplay')
        if hour_tag and 'datetime' in hour_tag.attrs:
            date_time_str = hour_tag.attrs['datetime']
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            date_time_obj += timedelta(hours=3)  

            news_date = date_time_obj.strftime('%Y-%m-%d')
            news_time = date_time_obj.strftime('%H:%M')
            
            content = news.get_text(strip=True)

            if news_date not in formatted_data:
                formatted_data[news_date] = {}

            formatted_data[news_date][news_time] = content

    return formatted_data

def save_content_to_file(content, path='resources'):
    for date, items in content.items():
        filename = f"{path}/{date}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({date: items}, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news_content = fetch_news()
    save_content_to_file(news_content)
