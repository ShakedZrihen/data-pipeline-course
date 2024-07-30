import json
import os

data = {}


def init():
    directory = os.path.abspath("data")
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            f = os.path.join(directory, filename)
            with open(f, encoding='utf-8') as file:
                file_data = json.load(file)
                date = os.path.splitext(filename)[0]
                data[date] = file_data
    return data


def get_all():
    reports = {}
    for date in data:
        reports[date] = normalize_data(data[date])
    return reports


def get_by_date(date):
    if date in data:
        return data[date]
    return {}


def get_by_time(time):
    reports = {}
    for date in data:
        if time in data[date]:
            reports[date] = data[date][time]
    return reports


def get_by_time_and_date(date, time):
    if date in data and time in data[date]:
        return data[date][time]


def normalize_data(reports):
    normalized = []
    for key, value in reports.items():
        normalized.append({key: value})
    return normalized


init()
# print(get_all())
# print(get_by_date("2024-07-30"))
# print(get_by_time("17:04:55"))
# print(get_by_time_and_date("2024-07-30","17:04:55"))

