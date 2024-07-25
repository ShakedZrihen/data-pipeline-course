import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import dateutil.parser as parser 

def convert_time(x):
    conv_time = parser.parse(x)
    format = "%H:%M"
    updated_time = conv_time + timedelta(hours=3)
    print(updated_time.strftime(format))
    

def scraper():
    response = requests.get("https://www.ynet.co.il/news/category/184", 'html.parser')
    html = BeautifulSoup(response.text, 'html.parser')
    headlines = html.find_all(attrs={'class':'title'})
    dates = html.find_all(attrs={'class':'DateDisplay'})
    for headline in headlines:
        print("headlines", headline.text)
    for time in dates:
        if time.has_attr('datetime'):
            convert_time(time['datetime'])

    
scraper()