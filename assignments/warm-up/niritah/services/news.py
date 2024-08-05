from services.db import get as get_from_db
def get_breaking_news():
    return get_from_db()
