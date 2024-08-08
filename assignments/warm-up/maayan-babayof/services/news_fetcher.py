import requests
from bs4 import BeautifulSoup
import datetime
from dateutil.parser import isoparse
from typing import Dict

def fetch_news() -> Dict[str, Dict[str, str]]:
    data = {}
    html = requests.get("https://www.ynet.co.il/news/category/184")
    soup = BeautifulSoup(html.text, "html.parser")
    soup = soup.find("div", {"class": "article-flashes-page"})
    for article in soup.find_all("div", {"class": "AccordionSection"}):
        if article.find("time"):
            date = isoparse(article.find("time").attrs["datetime"])
            date_str = f"{date:%Y-%m-%d}"
            time_str = f"{date:%H:%M}"
            value = article.find("div", {"class": "title"}).text
            if date_str not in data:
                data[date_str] = {}
            data[date_str][time_str] = value
    return data
