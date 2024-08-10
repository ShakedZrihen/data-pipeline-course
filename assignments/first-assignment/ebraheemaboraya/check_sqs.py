import boto3
import json

# Initialize the SQS client
sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://localhost:9324')

# URL of the SQS queue
SQS_QUEUE_URL = "http://localhost:9324/000000000000/data-raw-q"

all_messages = []  # List to store all messages

while True:
    # Receive messages from the queue (up to 10 at a time)
    response = sqs.receive_message(
        QueueUrl=SQS_QUEUE_URL,
        MaxNumberOfMessages=10  # SQS max limit per request
    )

    messages = response.get('Messages', [])

    if not messages:
        print("No more messages in the queue.")
        break

    for message in messages:
        body = message['Body']
        try:
            # Attempt to decode the JSON message
            decoded_message = json.loads(body)
            all_messages.append(decoded_message)  # Store each message
            
            # Delete the message from the queue
            sqs.delete_message(
                QueueUrl=SQS_QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
            print(f"Deleted message ID: {message['MessageId']}")
        except json.JSONDecodeError as e:
            print(f"Failed to decode message ID {message['MessageId']}: {e}")
            print(f"Message content: {body}")

# Optionally, you can print all messages at once
print("\nAll messages received:")
for i, msg in enumerate(all_messages, 1):
    print(f"Message {i}: {msg}")
