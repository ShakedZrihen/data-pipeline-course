import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_breaking_news():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch the breaking news")

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
            while hour >= 24:
                hour -= 24
            formatted_hour = f'{hour:02}:{minute:02}'
            date = f'{dates.year}-{dates.month:02}-{dates.day:02}'
            content = news.get_text(strip=True)
            if date not in formatted_data:
                formatted_data[date] = {}
            formatted_data[date][formatted_hour] = content

    return formatted_data
