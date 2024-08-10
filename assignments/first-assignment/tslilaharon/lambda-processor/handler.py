import time
import boto3
from botocore.exceptions import ClientError

sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://sqs:9324')
queue_url = "http://sqs:9324/queue/data-raw-q"

def process_event():
    while True:
        try:
            print("Polling for messages...")
            response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
            messages = response.get('Messages', [])
            if not messages:
                print("No messages found.")
            for message in messages:
                print("Received message: ", message['Body'])
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
        except ClientError as e:
            print("Error: ", e)
            time.sleep(10)  # Wait before retrying
        time.sleep(5)  # Poll every 5 seconds

if __name__ == "__main__":
    process_event()
