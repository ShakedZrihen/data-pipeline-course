
from services.db import get as get_from_db


def get_breaking_news(date: str = None):
    data = get_from_db()
    response = data
    if date:
        if date in data:
            response = data[date]
        else:
            response = {}
    # check time
    return response
