import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_ynet():
    url = "https://www.ynetnews.com/category/3089"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    news_items = soup.find_all("div", class_="titleRow")
    news_dict = {}

    for item in news_items:
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
            news_full_datetime = news_time.strftime("%Y-%m-%d %H:%M:%S")
            news_dict[news_full_datetime] = title

    sorted_news_dict = dict(sorted(news_dict.items(), key=lambda item: item[0], reverse=True))
    return sorted_news_dict
