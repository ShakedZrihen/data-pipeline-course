import datetime
from services.db import get_all, get_by_time, get_by_date, get_by_time_and_date
from fastapi import HTTPException


def vali_date(date_time, text_type):
    try:
        if text_type == "date":
            return datetime.datetime.strptime(date_time, '%Y-%m-%d')
        if text_type == "time":
            return datetime.datetime.strptime(date_time, '%H:%M:%S')

    except ValueError:
        raise HTTPException(status_code=404, detail="Invalid Date")


def get_breaking_news():
    return get_all()


def get_news_by_time(time):
    vali_dated = vali_date(time, "time")
    reports = get_by_time(vali_dated.strftime('%H:%M:%S'))
    if reports: return reports
    raise HTTPException(status_code=404, detail="Not Found")


def get_news_by_date(date):
    vali_dated = vali_date(date, "date")
    reports = get_by_date(vali_dated.strftime('%Y-%m-%d'))
    if reports: return reports
    raise HTTPException(status_code=404, detail="Not Found")


def get_news_by_date_and_time(date, time):
    vali_dated = vali_date(date, "date").strftime('%Y-%m-%d')
    vali_timed = vali_date(time, "time").strftime('%H:%M:%S')
    report = get_by_time_and_date(vali_dated, vali_timed)
    if report: return report
    raise HTTPException(status_code=404, detail="Not Found")


# print(get_breaking_news())
# print(get_news_by_date("2024-07-30"))
# print(get_news_by_time("17:04:55"))
# print(get_news_by_date_and_time("2024-07-30", "17:04:55"))
