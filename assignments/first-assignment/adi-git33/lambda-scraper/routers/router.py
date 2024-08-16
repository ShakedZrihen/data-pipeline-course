from fastapi import APIRouter, HTTPException
from services.scrapper import scrape_ynet
import boto3
import os
import json


sqs = boto3.client(
    'sqs', 
    region_name="us-east-1",
    endpoint_url='http://sqs:9324'
)

queue_url = 'http://sqs:9324/queue/data-raw-q'

router = APIRouter()

@router.post("/scrape")
async def scrape():
    try:
        scraped_data = scrape_ynet()
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(scraped_data, ensure_ascii=False)
        )
        return {"message": "Data has been scraped and sent to SQS", "sqs_response": response}
        # return scraped_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))