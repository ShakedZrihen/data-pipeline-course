from fastapi import FastAPI, Query, HTTPException
from starlette.responses import JSONResponse
from fastapi.responses import JSONResponse
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "OK"}, status_code=200)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "OK"}, status_code=200)


@app.get("/breaking-news")
async def breaking_news(date: Optional[str] = Query(None), time: Optional[str] = Query(None)):
    url = 'https://www.ynet.co.il/news/category/184'

    # Send a GET request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return JSONResponse(content={"error": "Failed to fetch news data"}, status_code=500)

    soup = BeautifulSoup(response.content, 'html.parser')

    news_items = soup.select('div.titleRow')

    formatted_data: Dict[str, List[Dict[str, str]]] = {}

    for news in news_items:
        datetime_tag = news.find('time', class_='DateDisplay')
        if datetime_tag and 'datetime' in datetime_tag.attrs:
            datetime_str = datetime_tag['datetime']
            datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            date_str = datetime_obj.strftime('%Y-%m-%d')
            hour = datetime_obj.strftime('%H:%M')

            title_tag = news.find('div', class_='title')
            title = title_tag.text.strip() if title_tag else 'No title'

            if date_str not in formatted_data:
                formatted_data[date_str] = []
            formatted_data[date_str].append({hour: title})
        else:
            continue

    if date and time:
        if date in formatted_data:
            news_at_date_time = next((item[time] for item in formatted_data[date] if time in item), None)
            if news_at_date_time:
                return JSONResponse(content={"date": date, "time": time, "news": news_at_date_time}, status_code=200)
            else:
                return JSONResponse(content={"error": "No news found for the specified date and time"}, status_code=404)
        else:
            return JSONResponse(content={"error": "No news found for the specified date"}, status_code=404)
    elif date:
        if date in formatted_data and formatted_data[date]:
            news_at_date = {item_time: item[item_time] for item in formatted_data[date] for item_time in item}
            return JSONResponse(content=news_at_date, status_code=200)
        else:
            return JSONResponse(content={"error": "No news found for the specified date"}, status_code=404)
    elif time:
        news_at_time = {date_key: item[time] for date_key in formatted_data for item in formatted_data[date_key] if
                        time in item}
        if news_at_time:
            return JSONResponse(content=news_at_time, status_code=200)
        else:
            return JSONResponse(content={"error": "No news found for the specified time"}, status_code=404)
    else:
        return JSONResponse(content=formatted_data, status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


handler = Mangum(app)