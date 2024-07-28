from db.db import Database
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
        filtered_data = []
        if date:
            filtered_data = filter_data(data, "date", date)
        
        if time:
            if not filtered_data:
                filtered_data = filter_data(data, "hour", time)
            else:
                filtered_data = filter_data(filtered_data, "hour", time)

        if not filtered_data:
            raise HTTPException(status_code=404, detail="Breaking news with those filters doesn't exist")
        
        return filtered_data
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)

