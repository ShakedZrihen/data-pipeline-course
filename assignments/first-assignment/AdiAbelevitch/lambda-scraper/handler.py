from fastapi import FastAPI, HTTPException
import boto3
import json
from datetime import datetime
from services.content_generator import fetch_news, store_news_data
from mangum import Mangum
import os

app = FastAPI()

sqs_client = boto3.client(
    'sqs', 
    endpoint_url='http://sqs:9324', 
    region_name='us-east-1', 
    aws_access_key_id='x', 
    aws_secret_access_key='x'
)

queue_endpoint = 'http://sqs:9324/queue/data-raw-q'

@app.post("/scrape")
def scrape_news():
    try:
        current_date = datetime.now().strftime('%d-%m-%Y')
        news_content = fetch_news()

        output_directory = "data"
        os.makedirs(output_directory, exist_ok=True)
        store_news_data(news_content, current_date, output_directory)

        sqs_response = sqs_client.send_message(
            QueueUrl=queue_endpoint,
            MessageBody=json.dumps(news_content, ensure_ascii=False)
        )
        return {
            "message": "Data Sent To SQS",
            "SQSResponse": sqs_response,
            "news_data": news_content
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

handler = Mangum(app)
