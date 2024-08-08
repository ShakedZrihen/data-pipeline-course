import logging
import boto3
import json
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.INFO)

sqs = boto3.client('sqs', 
                   endpoint_url = 'http://sqs:9324',
                   region_name='us-west-1', 
                   aws_access_key_id='local', aws_secret_access_key='local') 

# Initialize FastAPI app
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/scrape")
async def scrape_data(request: Request):
    try:
        url = 'https://www.ynet.co.il/news/category/184'

        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # get all breaking-news
        breaking_news = soup.find_all('div', class_='titleRow')

        # format data to the desired format
        formatted_data = {}   
        for row in breaking_news:
            dateTime = row.find('time').attrs['datetime']
            title = row.find('div', class_='title').text
            formatted_data[dateTime] = title
        logging.info(f"Sending message to SQS with data: {formatted_data}")
        response = sqs.send_message(QueueUrl='http://sqs:9324/000000000000/data-raw-q', MessageBody=json.dumps(formatted_data, ensure_ascii=False))
        logging.info(f"SQS Response: {response}")          
        return "Data sent to SQS"
    
    except Exception as e:
        # Log the error and re-raise the exception
        logging.error(f"Error sending message to SQS: {e}")
        raise
