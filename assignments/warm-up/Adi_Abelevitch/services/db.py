import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_breaking_news():
    url = 'https://news.walla.co.il/breaking'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch the breaking news")

    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('h1', class_='breaking-item-title')

    formatted_data = {}
    todays_date = datetime.now().strftime('%Y-%m-%d')  # התאריך הנוכחי

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
