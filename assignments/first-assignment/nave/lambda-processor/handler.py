import json
import boto3
import time

sqs = boto3.client('sqs', 
                   endpoint_url = 'http://sqs:9324',
                   region_name='us-west-1', 
                   aws_access_key_id='local', aws_secret_access_key='local') 

def handler(event, context):
    res = sqs.receive_message(QueueUrl='http://sqs:9324/000000000000/data-raw-q')
    while not len(res['Messages']):
        time.sleep(5)
        res = sqs.receive_message(QueueUrl='http://sqs:9324/000000000000/data-raw-q')
    sqs.delete_message(QueueUrl='http://sqs:9324/000000000000/data-raw-q', ReceiptHandle=res['Messages'][0]['ReceiptHandle'])
    print(res['Messages'][0]['Body'])
    for record in event['Records']:
        print(json.loads(record['body']))
    return {"message": "Processed"}
