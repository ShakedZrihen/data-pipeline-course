import requests
from bs4 import BeautifulSoup
from datetime import timedelta
import dateutil.parser as parser 
# import json
# import os

formatted_data = {}

def convert_time(x):
    conv_time = parser.parse(x)
    format = "%H:%M"
    updated_time = conv_time + timedelta(hours=3)
    return updated_time.strftime(format)
    

def scraper():
    response = requests.get("https://www.ynet.co.il/news/category/184", 'html.parser')
    html = BeautifulSoup(response.text, 'html.parser')
    titleRows = html.find_all(attrs={'class':'titleRow'})
        
    for headline in titleRows:
        if headline.find('time').has_attr('datetime'):
            datetimes = headline.find('time')['datetime'] 
            date = parser.parse(datetimes).strftime('%d/%m/%Y')
            hour = convert_time(datetimes)
        
        content = headline.contents[-2].text
        inner_json = {hour : content}
        if date in formatted_data:
            formatted_data[date] += [inner_json]
        else:
            formatted_data[date] = [inner_json]
    return formatted_data