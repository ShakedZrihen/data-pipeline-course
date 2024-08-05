from typing import Optional, Dict
import datetime  # Add this import
from .news_fetcher import fetch_news
from .data_storage import load_news_data

class NewsService:
    def __init__(self):
        self.news_data = load_news_data()

    def get_all_news(self) -> Dict[str, Dict[str, str]]:
        return self.news_data

    def get_news_for_date(self, date: Optional[datetime.date], start_time: Optional[datetime.time], end_time: Optional[datetime.time]) -> Dict[str, str]:
        date_str = date.strftime("%Y-%m-%d")
        if date_str not in self.news_data:
            return {}
        date_news = self.news_data[date_str]
        filtered_news = {time: news for time, news in date_news.items()
                          if (start_time is None or datetime.datetime.strptime(time, "%H:%M").time() >= start_time)
                          and (end_time is None or datetime.datetime.strptime(time, "%H:%M").time() <= end_time)}
        return filtered_news

    def get_news_for_time(self, start_time: Optional[datetime.time], end_time: Optional[datetime.time]) -> Dict[str, str]:
        filtered_news = {}
        for date_str, date_news in self.news_data.items():
            for time, news in date_news.items():
                if (start_time is None or datetime.datetime.strptime(time, "%H:%M").time() >= start_time) and \
                   (end_time is None or datetime.datetime.strptime(time, "%H:%M").time() <= end_time):
                    filtered_news[date_str] = filtered_news.get(date_str, {})
                    filtered_news[date_str][time] = news
        return filtered_news
