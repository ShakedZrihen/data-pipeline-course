from fastapi import FastAPI
import boto3
import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

app = FastAPI()

sqs = boto3.client('sqs', endpoint_url='http://sqs:9324', region_name='elasticmq', aws_access_key_id='x', aws_secret_access_key='x')

@app.post("/scrape")
def fetch_news():
    url = "https://www.ynet.co.il/news/category/184"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_data = {}
    for section in soup.find_all("div", class_="AccordionSection"):
        date_tag = section.find("time", class_="DateDisplay")
        title_tag = section.find("div", class_="title")

        if date_tag and title_tag:
            date_time = date_tag["datetime"]
            date = date_time.split("T")[0]
            time_text = date_tag.get_text(strip=True)

            if '|' in time_text:
                hour = time_text.split('|')[1].strip()
            else:
                original_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                adjusted_time = original_time + timedelta(hours=3)
                hour = adjusted_time.strftime("%H:%M")

            news = title_tag.get_text(strip=True)

            if date not in news_data:
                news_data[date] = []
            news_data[date].append({hour: news})

    message_body = json.dumps(news_data)
    sqs.send_message(QueueUrl='http://sqs:9324/queue/data-raw-q', MessageBody=message_body)

    return {"status": "success", "data": news_data}
