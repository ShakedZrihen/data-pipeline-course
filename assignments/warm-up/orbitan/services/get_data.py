import os
import json
from fastapi import HTTPException
from .config import data_directory


def Get_Data():
    db = {}
    for json_file in os.listdir(data_directory):
        if json_file.endswith(".json"):
            file_path = os.path.join(data_directory, json_file)
            with open(file_path, "r", encoding="utf-8") as file:
                temp_data = json.load(file)
                key_date = os.path.splitext(json_file)[0]
                db[key_date] = temp_data
    return db


def query_all(db):
    temp_data = {}
    for key, value in db.items():
        temp_data[key] = [value]
    return temp_data


def query_date(db, date):
    if date in db:
        return db[date]
    raise HTTPException(status_code=404, detail="404, Not Found")


def query_time(db, time):
    temp_data = {}
    for temp_date in db:
        # return temp_date
        if time in db[temp_date]:
            temp_data[time] = db[temp_date][time]
    if len(temp_data) == 0:
        raise HTTPException(status_code=404, detail="404, Not Found")
    return temp_data


def query_date_time(db, date, time):
    if date in db and time in db[date]:
        return db[date][time]
    raise HTTPException(status_code=404, detail="404, Not Found")
