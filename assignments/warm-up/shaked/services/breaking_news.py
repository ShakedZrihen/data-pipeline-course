
from services.db import get as get_from_db

def get_breaking_news(date: str = None, time: str = None):
    data = get_from_db()
    response = data
    if date in data:
        response = data[date]
    return response

