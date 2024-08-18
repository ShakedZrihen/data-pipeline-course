
import os
import requests
from fastapi import FastAPI, HTTPException
from mangum import Mangum
import logging
from bs4 import BeautifulSoup
import json
from datetime import datetime
import boto3

app = FastAPI()

logging.basicConfig(level=logging.INFO)

sqs = boto3.client(
            'sqs',
            endpoint_url='http://sqs:9324',
            aws_access_key_id='fake_access_key',
            aws_secret_access_key='fake_secret_key',
            region_name='us-east-1'
        )


@app.post("/scrape")
def scrape():
    url = 'https://www.ynet.co.il/news/category/184'
    print(f"Scraping data from {url}...")
    scraped_data = {}

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_rows = soup.find_all('div', class_='titleRow')

        for row in news_rows:
            str_time = row.find('time', class_='DateDisplay')['datetime']
            obj_time = datetime.strptime(str_time, '%Y-%m-%dT%H:%M:%S.%fZ')
            formatted_time = obj_time.strftime('%H:%M')
            title = row.find('div', class_='title').text.strip()
            scraped_data[formatted_time] = title

        date = datetime.now().strftime('%Y-%m-%d')
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(curr_dir, f'{date}.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {file_path}")
        
        print ("SQS client created")
        response = sqs.get_queue_url(QueueName='data-raw-q')
        queue_url = response.get('QueueUrl')  # Ensure this is not None
        
        message = json.dumps(scraped_data)

        print ("Message created")

        if message is None:
            print("No message to send")
            return HTTPException(status_code=500, detail="No message to send")
        
        print ("Sending message to SQS")
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message
        )

        print(response)
        
        return 200
    except Exception as e:
        print("An error occurred")
        print("Error sending message to SQS:", str(e))
        return HTTPException(status_code=500, detail="An error occurred")


handler = Mangum(app)