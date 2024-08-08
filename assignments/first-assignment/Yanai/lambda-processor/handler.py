import boto3
import json
import os
import time

sqs = boto3.client('sqs', endpoint_url=os.getenv("AWS_ENDPOINT_URL"), region_name=os.getenv("AWS_DEFAULT_REGION"))
global queue_url 
queue_url = "http://sqs:9324/000000000000/data-raw-q"


def is_queue_ready(queue_url):
    try:
        response = sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=['All']
        )
        return response['Attributes'] is not None
    except Exception as e:
        print(f"Error checking queue: {e}")
        return False

while True:
    if queue_url and is_queue_ready(queue_url):
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10  # Enable long polling
        )
        messages = response.get('Messages', [])
        if messages:
            for message in messages:
                print("Received message:")
                message_body = json.loads(message['Body'])
                print(json.dumps(message_body, indent=4, ensure_ascii=False))
                # Delete the message after processing
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
        else:
            print("No messages in queue.")
    else:
        print("Queue URL not available or queue not ready.")
        time.sleep(1)  # Wait for a while if the queue URL is not available