from fastapi import FastAPI, HTTPException
import boto3
import json
from services.breaking_news import fetch_news_data
from mangum import Mangum

app = FastAPI()

sqs = boto3.client('sqs', endpoint_url='http://sqs:9324', region_name='us-west-1',
                   aws_access_key_id='local', aws_secret_access_key='local')
queue_url = 'http://sqs:9324/queue/data-raw-q'

@app.post("/scrape")
def scrape_data():
    try:
        news_data = fetch_news_data()
        if not news_data:
            raise HTTPException(status_code=500, detail="Failed to fetch news data")

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(news_data, json_file, ensure_ascii=False, indent=4)

        sqs_response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(news_data, ensure_ascii=False)
        )
        if sqs_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Data sent to SQS successfully")
            return {"message": "Data sent to SQS successfully", "data": news_data}
        else:
            print("Failed to send data to SQS")
            raise HTTPException(status_code=500, detail="Failed to send data to SQS")

    except Exception as e:
        print(f"Exception: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

handler = Mangum(app)
