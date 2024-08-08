import os
import json
import datetime
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from mangum import Mangum
import boto3

app = FastAPI()
sqs = boto3.client(
    'sqs',
    endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'us-west-1'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'local'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'local'),
)


@app.get("/scrape", status_code=200)
def scrape():
    try:
        queue_url = "http://sqs:9324/000000000000/data-raw-q"
        data = dict()
        html = requests.get('https://www.ynet.co.il/news/category/184')
        soup = BeautifulSoup(html.text, 'html.parser')
        soup = soup.find('div', {'class': 'article-flashes-page'})
        for article in soup.find_all('div', {'class': 'AccordionSection'}):
            if article.find('time'):
                date = datetime.datetime.fromisoformat(article.find('time').attrs['datetime'])
                key1 = f'{date:%Y-%m-%d}'
                key2 = f'{date:%H:%M}'
                value = article.find('div', {'class': 'title'}).text
                if not (key1 in data.keys()):
                    data[key1] = {}
                data[key1][key2] = value
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(data, ensure_ascii=False)
        )
        print(f"Message sent. Message ID: {response['MessageId']}")
        return response['MessageId']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


handler = Mangum(app)
