import requests
from bs4 import BeautifulSoup
import datetime
from pytz import timezone
import json
import os

def scrape_ynet():
    file_path = os.path.split(os.path.realpath(__file__))[0]
    file_name = file_path + '/news.json'
    news = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        news = json.load(f)

    tz = timezone("Asia/Jerusalem")
    resp = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(resp.text, 'html.parser')
    div_array = soup.select('div.titleRow')
    for item in div_array:
        datetime_element = ''
        time = ''
        date = ''
        if item.find('time').has_attr('datetime'):
            datetime_element = item.find('time')['datetime']
            time = datetime.datetime.fromisoformat(datetime_element).astimezone(tz).strftime("%H:%M")
            date = datetime.datetime.fromisoformat(datetime_element).astimezone(tz).strftime("%d/%m/%Y")
            
        title = item.contents[-2].text
        time_json = {time : title}
        if date in news:
            news[date] += [time_json]
        else:
            news[date] = [time_json]
         
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False)
        
if __name__ == "__main__":
    print("scraper")