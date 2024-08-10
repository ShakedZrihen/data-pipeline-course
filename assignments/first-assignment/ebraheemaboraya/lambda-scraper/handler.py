from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import boto3
from botocore.config import Config
import os

app = FastAPI()

# Setting up SQS client with endpoint URL from environment default
sqs_endpoint_url = os.getenv('SQS_ENDPOINT_URL', 'http://sqs:9324')
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',
    aws_access_key_id='dummy_access_key',
    aws_secret_access_key='dummy_secret_key',
    use_ssl=False,
    endpoint_url=sqs_endpoint_url,
    config=Config(retries={'max_attempts': 0}, connect_timeout=5, read_timeout=60)
)

#queue URL
SQS_QUEUE_URL = f"{sqs_endpoint_url}/000000000000/data-raw-q"

def get_ynet_breaking_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title_rows = soup.find_all('div', class_='titleRow')
    
    news_data = []
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    print(f"Scraping news for date: {date_str}")
    
    for index, row in enumerate(title_rows):
        try:
            title_element = row.find('div', class_='title')
            dateclass = row.find('div', class_='date')

            if not title_element or not dateclass:
                print(f"Skipping row {index+1}: missing title or date")
                continue  # skip date is not found

            time_element = dateclass.find('time', class_='DateDisplay')

            if not time_element:
                print(f"Skipping row {index+1}: missing time element")
                continue  # Skip if no time element is found

            datetime_str = time_element['datetime']
            datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            item_date_str = datetime_obj.strftime('%Y-%m-%d')

            if item_date_str == date_str:
                hour = datetime_obj.strftime('%H:%M')
                content = title_element.get_text().strip()
                news_data.append({'hour': hour, 'title': content})
                print(f"Adding news item: {hour} - {content}")
            else:
                print(f"Skipping row {index+1}: date mismatch")
        except Exception as e:
            print(f"Error processing row {index+1}: {e}")
    
    print(f"Total news items found for today: {len(news_data)}")
    return news_data

@app.post("/scrape")
async def scrape_and_send_to_sqs():
    try:
        url = "https://www.ynet.co.il/news/category/184"
        news_data = get_ynet_breaking_news(url)

        items_sent = 0

        # Send each news item to the SQS queue
        for item in news_data:
            response = sqs.send_message(
                QueueUrl=SQS_QUEUE_URL,
                MessageBody=json.dumps(item)
            )
            items_sent += 1
            print(f"Sent item to SQS: {item}")

        return {"message": f"{items_sent} items scraped and sent to SQS"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


