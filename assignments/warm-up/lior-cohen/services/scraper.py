import requests
from bs4 import BeautifulSoup
from datetime import datetime


def fill_todays_data(data, breaking_news, news_time):
    for news in breaking_news:
        hour_raw = news.find('time', class_='DateDisplay').attrs['datetime']
        hour_before_timezone = hour_raw[11:16]
        hour_after_timezone = f"{(int(hour_before_timezone[:2]) + 3)%24}{hour_before_timezone[2:]}"
        content = news.text
        if not news_time or hour_after_timezone.split(":")[0] == news_time:
            data[hour_after_timezone] = content


def fill_data(data, sub_data, news_date):
    todays_date = datetime.now().strftime('%Y-%m-%d')  # yyyy-mm-dd
    if news_date and todays_date == news_date and sub_data:
        data[todays_date] = sub_data
    elif sub_data and not news_date:
        data[todays_date] = sub_data


def scrape(news_date, news_time):
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='titleRow')

    todays_data = {}
    formatted_data = {}

    fill_todays_data(todays_data, breaking_news, news_time)

    fill_data(formatted_data, todays_data, news_date)

    return formatted_data
