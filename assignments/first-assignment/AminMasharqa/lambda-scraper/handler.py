import json
import boto3
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from fastapi import FastAPI

# SQS Client Setup
sqs_client = boto3.client('sqs', endpoint_url="http://sqs:9324")
queue_url = "http://sqs:9324/000000000000/data-raw-q"  # Local queue URL

app = FastAPI()

def get_content_from_remote(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def parse_one_item(item):
    date_str = ""
    title = ""

    for child in item.children:
        if child.name == "div" and "date" in child.get("class", []):
            time_element = child.find("time")
            if time_element and time_element.has_attr("datetime"):
                date_str = time_element["datetime"]
        elif child.name == "div" and "title" in child.get("class", []):
            title = child.text.strip()

    if date_str and title:
        news_time = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        news_time += timedelta(hours=3)  # Adjust for timezone difference
        news_time_str = news_time.strftime("%H:%M")
        news_date_str = news_time.strftime("%Y-%m-%d")
        return news_date_str, news_time_str, title
    return None

def scrape_data():
    url = "https://www.ynetnews.com/category/3089"
    soup = get_content_from_remote(url)

    news_items = soup.find_all("div", class_="titleRow")
    news_dict = {}

    for item in news_items:
        parsed_item = parse_one_item(item)
        if parsed_item:
            news_date_str, news_time_str, title = parsed_item
            if news_date_str not in news_dict:
                news_dict[news_date_str] = []
            news_dict[news_date_str].append({news_time_str: title})

    return news_dict

@app.post("/scrape")
async def scrape():
    try:
        data = scrape_data()
        message_body = json.dumps(data)

        # Send data to local SQS
        sqs_client.send_message(QueueUrl=queue_url, MessageBody=message_body)
        return {"message": "Data sent to local SQS"}
    except Exception as e:
        return {"error": str(e)}
