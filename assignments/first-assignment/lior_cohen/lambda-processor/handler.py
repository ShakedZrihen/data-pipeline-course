from os import getenv
from time import sleep
import boto3


def handler(event, context):
    sqs = boto3.client(
        'sqs',
        endpoint_url=getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
        region_name=getenv('AWS_DEFAULT_REGION', 'us-west-1'),
        aws_access_key_id=getenv('AWS_ACCESS_KEY_ID', 'local'),
        aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY', 'local'),
    )
    queue_url = "http://sqs:9324/000000000000/data-raw-q"
    response = sqs.receive_message(QueueUrl=queue_url)
    print('Waiting for messages...')
    while not len(response['Messages']):
        sleep(5)
        response = sqs.receive_message(QueueUrl=queue_url)
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=response['Messages'][0]['ReceiptHandle'])
    print(response['Messages'][0]['Body'])
    return response
