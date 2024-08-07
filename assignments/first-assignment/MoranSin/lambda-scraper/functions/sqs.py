import boto3

# Configure the Boto3 client to use LocalStack
sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://localhost:4566')

# Create a queue
response = sqs.create_queue(
    QueueName='MyTestQueue',
    Attributes={
        'DelaySeconds': '5',
        'MessageRetentionPeriod': '86400'
    }
)

print(f'Queue URL: {response["QueueUrl"]}')
