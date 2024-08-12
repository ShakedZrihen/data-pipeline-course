from fastapi import FastAPI, Request
import boto3
import json

app = FastAPI()

# Correctly configure the SQS client
sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://localhost:9324')

# Specify the correct queue URL (make sure the queue URL is correctly formatted)
queue_url = 'http://localhost:9324/queue/data-raw-q'

@app.post("/scrape")
async def scrape(request: Request):
    data = await request.json()
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(data)
    )
    return {"status": "success", "response": response}
