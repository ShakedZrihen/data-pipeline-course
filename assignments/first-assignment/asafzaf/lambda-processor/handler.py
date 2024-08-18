import boto3
import time
import json
import logging

sqs_endpoint_url = 'http://sqs:9324'
sqs_access_key = 'fake_access_key'
sqs_secret = 'fake_secret_key'
sqs_region = 'us-east-1'
queue_name = 'data-raw-q'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

sqs = boto3.client(
            'sqs',
            endpoint_url='http://sqs:9324',
            aws_access_key_id='fake_access_key',
            aws_secret_access_key='fake_secret_key',
            region_name='us-east-1'
        )

def print_message(message):
    json_message = json.loads(message['Body'])
    print("Message recieved: ", json_message)
    
def lambda_processor():
    
    print(sqs._endpoint)
    
    print("SQS client created")
        
    response = sqs.get_queue_url(QueueName='data-raw-q')
    queue_url = response.get('QueueUrl')  # Ensure this is not None
        
    print("listening to queue: ", queue_name)
    
    while True:
        try:
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20  # Long polling
            )
            messages = response.get('Messages', [])
            for message in messages:
                print_message(message)
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
        except Exception as e:
            print("Error receiving message:", str(e))
        time.sleep(5)  # Delay before next poll
        
if __name__ == "__main__":
    time.sleep(5)
    print("Starting lambda processor")
    lambda_processor()