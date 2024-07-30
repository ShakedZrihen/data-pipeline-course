import requests
from bs4 import BeautifulSoup


def fetch_news_data():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return parse_news(soup)


def parse_news(soup):
    news_data = {}
    breaking_news = soup.find_all('div', class_='AccordionSection')
    for news in breaking_news:
        time = news.find('time', class_='DateDisplay').attrs['datetime'][11:16]
        content = news.findNext('div', class_='title').text.strip()
        date = news.find('time', class_='DateDisplay').attrs['datetime'][:10]
        if date not in news_data:
            news_data[date] = {}
        news_data[date][time] = content
    return news_data
