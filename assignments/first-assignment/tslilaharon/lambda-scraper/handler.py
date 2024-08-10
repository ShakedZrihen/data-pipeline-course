from fastapi import FastAPI, Request
import boto3
import json

app = FastAPI()

sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://sqs:9324')
queue_url = "http://sqs:9324/queue/data-raw-q"

# Ensure the queue exists
def create_queue():
    try:
        sqs.create_queue(QueueName='data-raw-q')
    except sqs.exceptions.QueueNameExists as e:
        print("Queue already exists:", e)

create_queue()

@app.post("/scrape")
async def scrape_data(request: Request):
    data = await request.json()
    # Simulate scraping, here just echoing the input data
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(data))
    return {"status": "success", "message_id": response['MessageId']}
