import boto3
import json

sqs = boto3.client('sqs', endpoint_url='http://sqs:9324', region_name='elasticmq', aws_access_key_id='x', aws_secret_access_key='x')

def process_message():
    response = sqs.receive_message(QueueUrl='http://sqs:9324/queue/data-raw-q', MaxNumberOfMessages=1)

    if 'Messages' in response:
        for message in response['Messages']:
            body = json.loads(message['Body'])
            # Ensure Unicode is correctly handled when printing
            print(json.dumps(body, indent=4, ensure_ascii=False))
            sqs.delete_message(QueueUrl='http://sqs:9324/queue/data-raw-q', ReceiptHandle=message['ReceiptHandle'])

if __name__ == "__main__":
    process_message()
