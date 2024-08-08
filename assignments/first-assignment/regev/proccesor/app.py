import os
import time
import boto3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_sqs_client():
    """Create and return an SQS client."""
    return boto3.client(
        'sqs',
        endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://sqs:9324'),
        region_name=os.getenv('AWS_DEFAULT_REGION', 'us-west-1'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'local'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'local'),
    )

def handler(event, context):
    """Lambda handler to process SQS messages."""
    sqs = get_sqs_client()
    queue_url = 'http://sqs:9324/000000000000/data-raw-q'

    try:
        while True:
            # Poll the queue for messages
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )
            
            messages = response.get('Messages', [])
            if not messages:
                print("No messages received, continuing to poll.")
                time.sleep(7)
                continue
            
            
            for message in messages:
                print(f"Received message: {message['Body']}")
                
                
               
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print("Message processed and deleted from queue.")
                
            return {
                    'statusCode': 200,
                    'body': 'Messages processed successfully.'
                   }    
                
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise


