import sys
import os
from datetime import datetime
from services.db import get_breaking_news as fetch_breaking_news

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_breaking_news(date: str = None, time: str = None):
    data = fetch_breaking_news()
    if data is None:
        print("No data fetched from Ynet")
        return None
    print(f"Fetched data: {data}")

    if date and time:
        print(f"Searching for date: {date} and time: {time}")
        if date in data and time in data[date]:
            return {time: data[date][time]}
        print(f"Data not found for date: {date} and time: {time}")
        return None
    elif date:
        print(f"Searching for date: {date}")
        if date in data:
            return data[date]
        print(f"Data not found for date: {date}")
        return None
    elif time:
        print(f"Searching for time: {time}")
        result = {date: news for date, news in data.items() if time in news[date]}
        if result:
            return result
        print(f"Data not found for time: {time}")
        return None
    else:
        return data

if __name__ == "__main__":
    news = get_breaking_news()
    print(news)
