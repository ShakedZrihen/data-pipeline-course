from fastapi import FastAPI, Response, status
from mangum import Mangum
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
import os
import json
import requests
import boto3
from pydantic import BaseModel

app = FastAPI()
sqs = boto3.client(
    'sqs',
    endpoint_url='http://sqs:9324',
    aws_access_key_id='local',
    aws_secret_access_key='local',
    region_name='us-west-1'
)
queue_url = 'http://sqs:9324/000000000000/data-raw-q'

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape")
def scrape():
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='AccordionSection')
    news_list = {}
    for news in breaking_news:
        title = news.find('div', class_='titleRow').text
        hour = news.find('time', class_='DateDisplay').get('datetime')
        hour_obj = parser.parse(hour)
        currentTime = hour_obj.strftime("%H:%M:%S")
        news_list[currentTime] = title

    date = datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'{date}.json')

    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(news_list, ensure_ascii=False)
    )

    print("Scraping completed and data sent to SQS")

handler = Mangum(app)
