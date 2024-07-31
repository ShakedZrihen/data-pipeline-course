import json
import os

def read_json_by_date(date_str):
    data=[]
    directory_path = os.path.abspath("data")
    file_name = f"{date_str}.json"
    file_path = os.path.join(directory_path, file_name)
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        return f"No data found for date: {date_str}"

def read_json_by_date_and_time(date,time):
    directory_path = os.path.abspath("data")
    file_name = f"{date}.json"
    file_path = os.path.join(directory_path, file_name)
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
        if time in data:
            return {time:data[time]}
        else:
            return f"No  data found for time: {time}"
    else:
        status_code = 404
        return status_code


def read_all_json():
    directory_path = os.path.abspath("data")
    all_data = {}

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, encoding='utf-8') as file:
                data = json.load(file)
                all_data[file_name] = data
    if all_data:
        return all_data
    else:
        return "No data found"

def read_json_by_time(time):
    directory_path = os.path.abspath("data")
    all_data_in_time = {}

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, encoding='utf-8') as file:
                data = json.load(file)
                if time in data:
                    data_time=data[time]
                    print(data_time)
                    all_data_in_time[file_name] = data_time

    if all_data_in_time:
        return all_data_in_time
    else:
        return f"No data found for date: {time}"

