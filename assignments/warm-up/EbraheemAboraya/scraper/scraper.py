import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def get_ynet_breaking_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title_rows = soup.find_all('div', class_='titleRow')
    
    news_data = []
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    for row in title_rows:
        title_element = row.find('div', class_='title')
        dateclass = row.find('div', class_='date')
        time_element = dateclass.find('time', class_='DateDisplay') 
        
        if time_element and title_element:
            datetime_str = time_element['datetime']
            datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            item_date_str = datetime_obj.strftime('%Y-%m-%d')
            
            if item_date_str == date_str:
                hour = datetime_obj.strftime('%H:%M')
                content = title_element.get_text().strip()
                news_data.append({'hour': hour, 'title': content})
    
    return news_data

def save_news_to_json(news_data):
    date_str = datetime.now().strftime("%Y-%m-%d")
    folder_name = "../data/"
    filename = f"{folder_name}/{date_str}.json"
    
    # Ensure the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    url = "https://www.ynet.co.il/news/category/184"
    news_data = get_ynet_breaking_news(url)
    save_news_to_json(news_data)
