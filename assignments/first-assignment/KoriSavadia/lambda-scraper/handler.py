import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from fastapi import FastAPI
import boto3
from botocore.exceptions import NoCredentialsError
from mangum import Mangum

app = FastAPI()


@app.post("/scrape")
def scrape():
    print('scrape')
    url = 'https://www.ynet.co.il/news/category/184'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    breaking_news = soup.find_all('div', class_='titleRow')
    formatted_data = {}

    for news in breaking_news:
        # Attempt to find the 'time' element and its 'datetime' attribute
        time_element = news.find('time', class_='DateDisplay')
        if time_element and 'datetime' in time_element.attrs:
            datetime_str = time_element.attrs["datetime"]
            # Convert to datetime object
            datetime_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            hour = datetime_obj.strftime('%H:%M')
        else:
            # Handle the case where 'time' element is not found or 'datetime' attribute is missing
            print(
                "Skipping news item: 'time' element with class 'DateDisplay' not found or missing 'datetime' attribute")
            continue

        # Extract and format the title
        title_element = news.find('div', class_='title')
        if title_element:
            title = title_element.text.strip()
        else:
            # Handle the case where 'title' element is not found
            print("Skipping news item: 'title' element not found")
            continue

        # Add the formatted data
        formatted_data[hour] = title

    # Send formatted data to SQS
    sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://sqs:9324')
    queue_url = 'http://sqs:9324/queue/data-raw-q'

    try:
        sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(formatted_data))
    except NoCredentialsError:
        return {"error": "AWS credentials not found"}

    return formatted_data


handler = Mangum(app)
