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
        time_element = news.find('time', class_='DateDisplay')
        if time_element and 'datetime' in time_element.attrs:
            time = time_element.attrs['datetime'][11:16]
        else:
            time = 'N/A'

        title_element = news.findNext('div', class_='title')
        content = title_element.text.strip() if title_element else 'No title'

        date_element = news.find('time', class_='DateDisplay')
        if date_element and 'datetime' in date_element.attrs:
            date = date_element.attrs['datetime'][:10]
        else:
            date = 'N/A'

        if date not in news_data:
            news_data[date] = {}
        news_data[date][time] = content
    return news_data
