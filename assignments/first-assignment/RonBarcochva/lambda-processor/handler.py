import os
import time
import boto3


def handler(event, context):
    sqs = boto3.client(
        'sqs',
        endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
        region_name=os.getenv('AWS_DEFAULT_REGION', 'us-west-1'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'local'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'local'),
    )
    try:
        queue_url = "http://sqs:9324/000000000000/data-raw-q"
        response = sqs.receive_message(QueueUrl=queue_url)
        print('Waiting for messages...')
        while not len(response['Messages']):
            time.sleep(5)
            response = sqs.receive_message(QueueUrl=queue_url)
        print(response['Messages'][0]['Body'])
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    handler(None, None)
