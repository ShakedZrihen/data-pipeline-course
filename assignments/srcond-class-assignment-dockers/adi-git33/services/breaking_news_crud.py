from scraper.scraper_db import Database
from fastapi import HTTPException
from services.utils import filter_data
db = Database()

def breaking_news_get_all():
    try:
        return db.get_data()
    except Exception as err:
        raise HTTPException(status_code=500, detail={err})
        

def breaking_news_get_filtered(date, time):
    try:
        data = db.get_data()
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)
    
    return filter_data(data, date, time)
 

