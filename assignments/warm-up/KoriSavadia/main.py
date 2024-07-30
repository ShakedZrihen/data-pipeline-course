from fastapi import FastAPI, Query, HTTPException, Request
from starlette.responses import JSONResponse
from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from mangum import Mangum
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "OK"}, status_code=200)


@app.get("/breaking-news")
async def breaking_news(date: Optional[str] = None, time: Optional[str] = None):
    url = 'https://www.ynet.co.il/news/category/184'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve news")

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        breaking_news = soup.find_all('div', class_='titleRow')
    except Exception as e:
        logger.error(f"Failed to parse HTML: {e}")
        raise HTTPException(status_code=500, detail="Failed to parse news content")

    formatted_data: Dict[str, List[Dict[str, str]]] = {}

    for news in breaking_news:
        try:
            datetime_str = news.find('time', class_='DateDisplay').attrs["datetime"]
            datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            date_str = datetime_obj.strftime('%Y-%m-%d')
            hour = datetime_obj.strftime('%H:%M')
            title = news.find('div', class_='title').text.strip()

            if date_str not in formatted_data:
                formatted_data[date_str] = []

            formatted_data[date_str].append({hour: title})
        except Exception as e:
            logger.error(f"Error processing news entry: {e}")

    if date and not time:
        if date in formatted_data:
            return JSONResponse(content=formatted_data[date], status_code=200)
        else:
            raise HTTPException(status_code=404, detail="Date not found")

    if time and not date:
        filtered_data: Dict[str, str] = {}
        for date_key, entries in formatted_data.items():
            for entry in entries:
                if time in entry:
                    filtered_data[date_key] = entry[time]
                    break

        if filtered_data:
            return JSONResponse(content=filtered_data, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="No news found for the specific time")

    if date and time:
        if date in formatted_data:
            for entry in formatted_data[date]:
                if time in entry:
                    return JSONResponse(content={time: entry[time]}, status_code=200)
            raise HTTPException(status_code=404, detail="Time not found for the specific date")
        else:
            raise HTTPException(status_code=404, detail="Date not found")

    return JSONResponse(content=formatted_data, status_code=200)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

handler = Mangum(app)
