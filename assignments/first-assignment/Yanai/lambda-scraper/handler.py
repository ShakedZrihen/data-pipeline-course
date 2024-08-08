import subprocess
import os
from fastapi import FastAPI
import boto3
import json
from fastapi import FastAPI, Response, status
from services.news import get_breaking_news
from services.news_generator import generate_content
from services.db import init
from typing import Optional
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

init()
sqs = boto3.client('sqs', endpoint_url=AWS_ENDPOINT_URL, region_name=AWS_DEFAULT_REGION)
queue_name = "data-raw-q"
queue_url = None

def create_queue():
    global queue_url
    try:
        response = sqs.get_queue_url(QueueName=queue_name)
        queue_url = response['QueueUrl']
        print(f"Queue URL: {queue_url}")
    except sqs.exceptions.QueueDoesNotExist:
        response = sqs.create_queue(
            QueueName=queue_name,
            Attributes={
                'DelaySeconds': '0',
                'MessageRetentionPeriod': '86400'  # 1 day
            }
        )
        queue_url = response['QueueUrl']
        print(f"Created queue URL: {queue_url}")
    except Exception as e:
        print(f"Error creating queue: {e}")


app = FastAPI()

@app.post("/scrape")
async def scrape():
    if not queue_url:
        create_queue()
    if queue_url and sqs:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(get_breaking_news(), ensure_ascii=False)
        )
        return response
