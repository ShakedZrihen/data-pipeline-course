import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

# bs4 documentation: https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup
# bs4 cheat sheet: https://proxiesapi.com/articles/the-complete-beautifulsoup-cheatsheet-with-examples

# URL to scrape
url = 'https://www.ynet.co.il/news/category/184'

# TODO: handle pagination for more than 1 page

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

breaking_news = soup.find_all('div', class_='titleRow')

# format data to the desired format

formatted_data = {}

for news in breaking_news:
    date = news.find('time', class_='DateDisplay')
    real_time = date.get('data-wcmdate')
    title = news.find('div', class_='title').text

    # Parse the date string into a datetime object
    date_obj = datetime.strptime(real_time, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Adjust the time using timedelta
    adjusted_time = date_obj + timedelta(hours=3)

    # Format the adjusted datetime object back to string if necessary
    adjusted_time_str = adjusted_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3] + 'Z'
    # print(adjusted_time.hour,":",adjusted_time.minute)
    
    formatted_data[adjusted_time_str[11:16]] = title
    

# save the formatted_data to file
todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')



with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
    