import json
import os
from mangum import Mangum
from fastapi import FastAPI, Response, HTTPException
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from datetime import datetime
import boto3

app = FastAPI()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_default_region = os.getenv('AWS_DEFAULT_REGION', 'us-west-1')
aws_endpoint_url = os.getenv('AWS_ENDPOINT_URL', 'http://localhost:9324') 

sqs = boto3.client(
    'sqs',
    region_name=aws_default_region,
    endpoint_url=aws_endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
queue_url = sqs.list_queues().get('QueueUrls', [])[0]


@app.get("/")
def health():
    return {"message":"all good"}

@app.post("/scrape")
def scrape():
    print("\n\nscraping ynet\n\n")
    news_object = {}
    res = requests.get('https://www.ynet.co.il/news/category/184')
    soup = BeautifulSoup(res.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='AccordionSection')
    for news in breaking_news:
        content = news.find('div', class_='title').text
        time_str = news.find('time').get('datetime')
        time = parser.parse(time_str).strftime('%H:%M:%S')
        news_object[time] = content
    data_date = datetime.today().strftime('%Y-%m-%d')
    data = {data_date: news_object}
    try:
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(data)
        )
        print("message sent to qu