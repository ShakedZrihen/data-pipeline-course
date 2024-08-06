import os
import time
import boto3
import json

def handler(event, context):
    sqs = boto3.client(
        'sqs',
        endpoint_url=os.getenv('SQS_ENDPOINT_URL', 'http://sqs:9324'),
        region_name=os.getenv('AWS_DEFAULT_REGION', 'elasticmq')
    )
    print('Waiting for messages') 
    try:
        response = sqs.receive_message(QueueUrl="http://sqs:9324/000000000000/data-raw-q")
        print('Waiting for messages')
        while not len(response['Messages']):
            time.sleep(5)
            response = sqs.receive_message(QueueUrl="http://sqs:9324/000000000000/data-raw-q")
        print(response['Messages'][0]['Body'])
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    
if __name__ == '__main__':
    handler(None, None)
