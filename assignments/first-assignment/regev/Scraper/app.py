from datetime import datetime
import json
import logging
import os
from bs4 import BeautifulSoup
from fastapi import FastAPI
import requests
from mangum import Mangum
import boto3


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Breaking News API",
    description="An API to fetch breaking news based on date and time.",
    version="1.0.0"
)

sqs = boto3.client(
    'sqs',
    endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'us-west-1'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'local'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'local'),
)


@app.post("/Scraper", summary="Health Check", description="Check the health status of the API")
def generate_random_content():
    queue_url = "http://sqs:9324/000000000000/data-raw-q"
    response = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(response.text, 'html.parser')

    breaking_news = soup.find_all('div', class_='titleRow')
    

    formatted_data = {}

    for news in breaking_news:
        hour_tag = news.find('time', class_='DateDisplay')
        if hour_tag and 'datetime' in hour_tag.attrs:
            dates = datetime.strptime(hour_tag.attrs['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
            hour = dates.hour + 3
            minute = dates.minute
            # Ensure hours are within 24-hour format
            while hour >= 24:
                hour -= 24
            formatted_hour = f'{hour:02}:{minute:02}'
            date = f'{dates.year}-{dates.month:02}-{dates.day:02}'
            content = news.get_text(strip=True)
            if date not in formatted_data:
                formatted_data[date] = {}
            formatted_data[date][formatted_hour] = content

        
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(formatted_data, ensure_ascii=False))       
    
    return json.dumps(formatted_data,ensure_ascii=False)


handler = Mangum(app)
