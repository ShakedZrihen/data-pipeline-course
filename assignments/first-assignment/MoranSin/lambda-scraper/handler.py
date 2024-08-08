from fastapi import FastAPI, HTTPException
from mangum import Mangum
import boto3
import json
from functions.scraper import scraper

app = FastAPI()

sqs = boto3.client('sqs',
                 endpoint_url='http://sqs:9324', region_name='elasticmq', aws_access_key_id='local', aws_secret_access_key='local')
queue_url = 'http://sqs:9324/queue/data-raw-q'

@app.post("/scrape")
async def get_news():
    try:
        generated_content = scraper()

        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(generated_content, ensure_ascii=False)
        )
        print(f"Data scraped and sent to SQS: {response}")
        return {"message": "Data scraped and sent to SQS", "SQSResponse": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
   
    
handler = Mangum(app)