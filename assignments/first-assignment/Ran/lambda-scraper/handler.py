from fastapi import FastAPI, HTTPException
import boto3
import json
from datetime import datetime
from services.content_generator import generate_news_content, save_content_to_file
from mangum import Mangum
import os

app = FastAPI()

sqs = boto3.client('sqs', endpoint_url='http://sqs:9324',region_name='us-east-1',aws_access_key_id='x', aws_secret_access_key='x')
queue_url = 'http://sqs:9324/queue/data-raw-q'

@app.post("/scrape")
def scrape():
    try:
        todays_date = datetime.now().strftime('%d-%m-%Y')
        generated_content = generate_news_content()
        
        output_dir = "data"
        os.makedirs(output_dir, exist_ok=True)
        save_content_to_file(generated_content, todays_date, output_dir)
        
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(generated_content, ensure_ascii=False)
        )
        return {"message": "Data scraped and sent to SQS", "SQSResponse": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

handler = Mangum(app)
