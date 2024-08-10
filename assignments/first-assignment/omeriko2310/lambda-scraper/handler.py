from fastapi import FastAPI, HTTPException
import boto3
import json
from datetime import datetime
from services.news_generator import scrape_news_ynet
import os

app = FastAPI()

sqs_endpoint_url = os.getenv("SQS_ENDPOINT_URL", "http://elasticmq:9324")
sqs = boto3.client("sqs", region_name="us-east-1", endpoint_url=sqs_endpoint_url)
queue_name = "data-raw-q"
queue_url = None


@app.on_event("startup")
def startup_event():
    global queue_url
    try:
        response = sqs.create_queue(QueueName=queue_name)
        queue_url = response["QueueUrl"]
        print(f"Queue URL: {queue_url}")
    except Exception as e:
        print(f"Error creating queue: {e}")
        raise HTTPException(status_code=500, detail=f"Error creating queue: {str(e)}")


@app.post("/scrape")
def scrape():
    global queue_url
    if not queue_url:
        raise HTTPException(
            status_code=500, detail="Queue URL not set. Initialization failed."
        )
    data = scrape_news_ynet()
    try:
        response = sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(data))
        return {"status": "success", "message_id": response["MessageId"], "data": data}
    except sqs.exceptions.QueueDoesNotExist as e:
        print(f"Queue does not exist: {e}")
        raise HTTPException(
            status_code=404, detail="The specified queue does not exist."
        )
    except Exception as e:
        print(f"Error sending message: {e}")
        raise HTTPException(status_code=500, detail=str(e))
