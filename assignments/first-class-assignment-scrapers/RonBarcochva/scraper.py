import requests
import json
from bs4 import BeautifulSoup
import datetime

def main():
    data = {}
    html = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(html.text, 'html.parser')
    soup = soup.find('div', {'class': 'article-flashes-page'})
    for article in soup.find_all('div', {'class': 'AccordionSection'}):
        date = datetime.datetime.fromisoformat(article.find('time').attrs['datetime'])
        key1 = f'{date:%Y-%m-%d}'
        key2 = f'{date:%H:%M}'
        value = article.find('div', {'class': 'title'}).text
        if not (key1 in data.keys()):
            data[key1] = {}
        data[key1][key2] = value
    for key in data.keys():
        with open(f'{key}.json', 'w') as outfile:
            outfile.write(json.dumps(data[key], indent=4))


if __name__ == '__main__':
    main()
