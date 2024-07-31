import requests
from bs4 import BeautifulSoup  
from datetime import datetime, timedelta
import json 
import os
res=requests.get('https://www.ynet.co.il/news/category/184')
soup=BeautifulSoup(res.text,'html.parser')
div=soup.find('div',class_='Accordion')

section=div.find_all('div',class_='AccordionSection')
formatted_data = {}
for item in section:
     row=item.find('div',class_='titleRow')
     title=row.find('div',class_='title').text
     date=row.find('div',class_='date')
     time=date.find('time')
     datetime_value = time.get('datetime')
     dt = datetime.strptime(datetime_value, "%Y-%m-%dT%H:%M:%S.%fZ")
     new_dt = dt + timedelta(hours=3)
     new_time = new_dt.strftime("%H:%M")
     formatted_data[new_time] = title
     
todays_date = datetime.now().strftime('%Y-%m-%d') 
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
   json.dump(formatted_data, f, ensure_ascii=False, indent=4)