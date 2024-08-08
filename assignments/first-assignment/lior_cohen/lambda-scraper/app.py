from os import getenv
from json import dumps
import boto3
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from services.scraper import scrape


app = FastAPI()
sqs = boto3.client(
    'sqs',
    endpoint_url=getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
    region_name=getenv('AWS_DEFAULT_REGION', 'us-west-1'),
    aws_access_key_id=getenv('AWS_ACCESS_KEY_ID', 'local'),
    aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY', 'local'),
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return 200


@app.get("/breaking-news")
async def breaking_news(date=None, time=None):
    queue_url = "http://sqs:9324/000000000000/data-raw-q"
    if not (result := scrape(date, time)):
        raise HTTPException(status_code=404, detail="No News Found")
    return sqs.send_message(QueueUrl=queue_url, MessageBody=dumps(result, ensure_ascii=False))

handler = Mangum(app)
