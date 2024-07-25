
from services.db import get as get_from_db


def get_breaking_news(date: str = None):
    data = get_from_db()
    response = data
    if date and date in data:
        response = data[date]
    # check time
    return response