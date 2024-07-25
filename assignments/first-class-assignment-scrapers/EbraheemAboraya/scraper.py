import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_ynet_breaking_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title_rows = soup.find_all('div', class_='titleRow')
    
    news_data = []
    
    for row in title_rows:
        title_element = row.find('div', class_='title')
        dateclass = row.find('div', class_='date')
        time_element = dateclass.find('time', class_='DateDisplay') if dateclass else None
        
        if time_element and title_element:
            datetime_str = time_element['datetime']
            datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            hour = datetime_obj.strftime('%H:%M')
            content = title_element.get_text().strip()
            
            news_data.append({'hour': hour, 'title': content})
    
    return news_data

def save_news_to_json(news_data):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    url = "https://www.ynet.co.il/news/category/184"
    news_data = get_ynet_breaking_news(url)
    save_news_to_json(news_data)
