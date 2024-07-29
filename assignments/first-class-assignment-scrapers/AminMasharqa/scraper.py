import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_content_from_remote(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def parse_one_item(item):
    date_str = ""
    title = ""

    for child in item.children:
        if child.name == "div" and "date" in child.get("class", []):
            time_element = child.find("time")
            if time_element and time_element.has_attr("datetime"):
                date_str = time_element["datetime"]
        elif child.name == "div" and "title" in child.get("class", []):
            title = child.text.strip()

    if date_str and title:
        news_time = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        news_time_str = news_time.strftime("%H:%M")
        return news_time_str, title
    return None

def save_to_file(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

def scrape_ynet():
    url = "https://www.ynetnews.com/category/3089"
    soup = get_content_from_remote(url)

    news_items = soup.find_all("div", class_="titleRow")
    news_dict = {}

    for item in news_items:
        parsed_item = parse_one_item(item)
        if parsed_item:
            news_time_str, title = parsed_item
            news_dict[news_time_str] = title

    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}.json"
    save_to_file({"content": news_dict}, filename)

if __name__ == "__main__":
    scrape_ynet()
