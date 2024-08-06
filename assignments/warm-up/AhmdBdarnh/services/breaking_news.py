import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import os

def fetch_news():
    url = "https://www.ynet.co.il/news/category/184"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    news_data = {}
    for section in soup.find_all("div", class_="AccordionSection"):
        date_tag = section.find("time", class_="DateDisplay")
        title_tag = section.find("div", class_="title")
        
        if date_tag and title_tag:
            date_time = date_tag["datetime"]
            date = date_time.split("T")[0]
            time_text = date_tag.get_text(strip=True)
            
            if '|' in time_text:
                hour = time_text.split('|')[1].strip()
            else:
                original_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                adjusted_time = original_time + timedelta(hours=3)
                hour = adjusted_time.strftime("%H:%M")

            news = title_tag.get_text(strip=True)
            
            if date not in news_data:
                news_data[date] = []
            news_data[date].append({hour: news})
    
    return news_data

def save_news_to_file(date, news):
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, f"{date}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({date: news}, f, indent=4, ensure_ascii=False)

def get_saved_news():
    news_data = {}
    for filename in os.listdir("data"):
        if filename.endswith(".json"):
            date = filename.split(".json")[0]
            with open(f"data/{filename}", "r", encoding="utf-8") as f:
                news_data.update(json.load(f))
    return news_data
