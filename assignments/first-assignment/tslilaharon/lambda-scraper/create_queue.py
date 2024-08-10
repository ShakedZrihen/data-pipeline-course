import boto3

sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://sqs:9324')

def create_queue():
    sqs.create_queue(QueueName='data-raw-q')

if __name__ == "__main__":
    create_queue()
