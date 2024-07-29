from fastapi import FastAPI
from mangum import Mangum
from typing import Optional
from functions.get_all_news import get_all_news

app = FastAPI()

@app.get("/health")
def health_code():
    return 200


@app.get("/breaking-news")
async def get_news(date: Optional[str] = None, time: Optional[str] = None):
    data = get_all_news()
    if date:
        return data[date]
    if time:
        entries_at_timestamp = [item[time] for item in data["28/07/2024"] if time in item]
        if entries_at_timestamp:
            for entry in entries_at_timestamp:
                return f"Event at {time}: {entry}"
            else:
                return f"No entries found for {time}"
    if date and time:
        specific_event = data[date][time]
        if specific_event:
            return specific_event
        else:
            return 404
        
    return data


handler = Mangum(app)