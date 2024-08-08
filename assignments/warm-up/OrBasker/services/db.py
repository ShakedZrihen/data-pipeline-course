from services.news_generator import scrape_news_ynet, save_news, generate_random_news
import json
import datetime
import os

DB_FOLDER = "resources"


def create_latest_news():
    news_data = scrape_news_ynet()
    save_news(news_data)
    return news_data


def get_latest_news():
    news = {}
    for date in sorted(os.listdir(DB_FOLDER), reverse=True):
        with open(f"{DB_FOLDER}/{date}", "r", encoding="utf-8") as infile:
            news[date] = json.load(infile)
    return news


def get_latest_news_by_date(date: datetime):
    with open(f"{DB_FOLDER}/{date}.json", "r", encoding="utf-8") as infile:
        return json.load(infile)
