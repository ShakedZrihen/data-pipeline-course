import requests
from bs4 import BeautifulSoup
import datetime
from pytz import timezone
import json
import os

def scrape_ynet():
    news = {}
    tz = timezone("Asia/Jerusalem")
    resp = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(resp.text, 'html.parser')
    div_array = soup.select('div.titleRow')
    for item in div_array:
        datetime_element = ''
        time = ''
        if item.find('time').has_attr('datetime'):
            datetime_element = item.find('time')['datetime']
            time = datetime.datetime.fromisoformat(datetime_element).astimezone(tz).strftime("%H:%M")

        title = item.contents[-2].text
        news[time] = title
        
    file_path = os.path.split(os.path.realpath(__file__))[0]
    file_name = file_path + '/news.json'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False)

        
    # news = {}
    # for item in h1:
    #     time = item.find('span').text 
    #     description = item.contents[-1] 
    #     news[time] = description
        
    # with open('news.json', 'w', encoding='utf-8') as f:
    #     json.dump(news, f, ensure_ascii=False)
    
scrape_ynet()
