import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

my_url = 'https://www.ynet.co.il/news/category/184'

response = requests.get(my_url)

soup = BeautifulSoup(response.text, 'html.parser')

accordion = soup.find('div', class_='Accordion')

news_divs = accordion.find_all('div', class_= 'AccordionSection')

#print(news_divs)

datetime_values = []
for news_div in news_divs:
    date_div = news_div.find('div', class_='date')
    #print(date_div)
    if date_div:
        time_element = date_div.find('time', class_='DateDisplay')
        #print(time_element)
        if time_element and 'datetime' in time_element.attrs:
            datetime_values.append(time_element['datetime'])

date_time_pairs =[]

for datetime_value in datetime_values:
    dt = datetime.fromisoformat(datetime_value.rstrip('Z'))
    date_time_pairs.append((dt.date(), dt.time()))

formatted_date_time_pairs = []
for date, time in date_time_pairs:
    formatted_time = time.strftime("%H:%M:%S")
    formatted_date_time_pairs.append((date, formatted_time))

news_titles =[]
for news_div in news_divs:
    title_div = news_div.find('div', class_='title')
    #print(title_div)
    if title_div:
        title_string = title_div.text.strip()
        news_titles.append(title_string)

news_items = list(zip(news_titles, formatted_date_time_pairs))

news_by_date = {}

for title, (date, time) in news_items:
    date_str = date.isoformat()
    if date_str not in news_by_date:
        news_by_date[date_str] = {}
    news_by_date[date_str][time] = title

for date_str, news in news_by_date.items():
    file_name = f"{date_str}.json"
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=4)
        
#for news_title, (date, time) in news_items:
    #print(f"Title: {news_title}, Date: {date}, Time: {time}")

