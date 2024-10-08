from fastapi import FastAPI
import boto3
import json
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from mangum import Mangum
import requests

app = FastAPI()

sqs = boto3.client(
    'sqs',
    endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'us-west-1'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'local'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'local'))

@app.post("/scrape")
def scrape():
    try:
        res=requests.get('https://www.ynet.co.il/news/category/184')
        soup=BeautifulSoup(res.text,'html.parser')
        div=soup.find('div',class_='Accordion')
        section=div.find_all('div',class_='AccordionSection')
        formatted_data = {}
        for item in section:
            row=item.find('div',class_='titleRow')
            title=row.find('div',class_='title').text
            date=row.find('div',class_='date')
            time=date.find('time')
            datetime_value = time.get('datetime')
            dt = datetime.strptime(datetime_value, "%Y-%m-%dT%H:%M:%S.%fZ")
            new_dt = dt + timedelta(hours=3)
            new_time = new_dt.strftime("%H:%M")
            formatted_data[new_time] = title
        response = sqs.send_message(
            QueueUrl="http://sqs:9324/000000000000/data-raw-q",
            MessageBody=json.dumps(formatted_data, ensure_ascii=False)
        )
        print(f"Message sent. Message ID: {response['MessageId']}")
        return response['MessageId']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None   
   
handler = Mangum(app)
