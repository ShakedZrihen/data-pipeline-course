from fastapi import FastAPI, HTTPException
import json
from typing import Optional
from mangum import Mangum


def load_json_data(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

app = FastAPI()

@app.get("/health")
def health():
    return 200

@app.get("/breaking-news")
def get_date_hours_news(date: Optional[str] = None, time: Optional[str] = None):
    file_path = "2024-07-31.json"
    
    try:
        data = load_json_data(file_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error decoding JSON")


    formatted_data = {}

    if date and time:
        if date in data:
            if time in data[date]:
                formatted_data = {date: {time: data[date][time]}}
            else:
                raise HTTPException(status_code=404, detail="Time not found for the given date")
        else:
            raise HTTPException(status_code=404, detail="Date not found")

    elif date:
        if date in data:
            formatted_data = data[date]
        else:
            raise HTTPException(status_code=404, detail="Date not found")

    elif time:
        for new_date, new_items in data.items():
            if time in new_items:
                if new_date not in formatted_data:
                    formatted_data[new_date] = {}
                formatted_data[new_date][time] = new_items[time]
        if not formatted_data:
            raise HTTPException(status_code=404, detail="Time not found across all dates")
    else:
        formatted_data = data

    return formatted_data

handler = Mangum(app)
