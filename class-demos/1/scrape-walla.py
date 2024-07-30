import requests
from bs4 import BeautifulSoup
import json

news = {
    # [time]: description
}


def scrape():
    resp = requests.get("https://news.walla.co.il/breaking")
    soup = BeautifulSoup(resp.text, "html.parser")
    h1 = soup.select("h1.breaking-item-title")
    for item in h1:
        time = item.find("span").text
        description = item.contents[-1]
        news[time] = description

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(news, f, ensure_ascii=False)


scrape()
