import os
import requests
import json
import datetime
from bs4 import BeautifulSoup
import random


def scrape_news_ynet():
    data = {}
    html = requests.get("https://www.ynet.co.il/news/category/184")
    soup = BeautifulSoup(html.text, "html.parser")
    soup = soup.find("div", {"class": "article-flashes-page"})
    for article in soup.find_all("div", {"class": "AccordionSection"}):
        if article.find("time"):
            string_date = article.find("time").attrs["datetime"]
            if string_date.endswith("Z"):
                string_date = string_date[:-1]

            date = datetime.datetime.fromisoformat(string_date)
            key1 = f"{date:%Y-%m-%d}"
            key2 = f"{date:%H:%M}"
            value = article.find("div", {"class": "title"}).text
            if not (key1 in data.keys()):
                data[key1] = {}
            data[key1][key2] = value
    return data


def generate_random_news():
    data = {}
    base_date = datetime.datetime.now()

    for i in range(7):
        date = base_date + datetime.timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        data[date_str] = {}
        for j in range(random.randint(1, 5)):  # Random number of news items per day
            time = datetime.time(random.randint(0, 23), random.randint(0, 59)).strftime(
                "%H:%M"
            )
            data[date_str][time] = f"Random news item {j+1} for {date_str}"

    return data


def save_news(data):
    for key in data.keys():
        with open(
            f"{os.path.dirname(__file__)}/../resources/{key}.json",
            "w",
            encoding="utf-8",
        ) as outfile:
            outfile.write(json.dumps(data[key], indent=4, ensure_ascii=False))
