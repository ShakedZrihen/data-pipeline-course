from fastapi import FastAPI, HTTPException
import boto3
import json
from botocore.config import Config
import os
app = FastAPI()

# Initialize the SQS client
sqs_endpoint_url = os.getenv('SQS_ENDPOINT_URL', 'http://sqs:9324')
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',
    aws_access_key_id='dummy_access_key',
    aws_secret_access_key='dummy_secret_key',
    use_ssl=False,
    endpoint_url=sqs_endpoint_url,
    config=Config(retries={'max_attempts': 0}, connect_timeout=5, read_timeout=60)
)


# URL of the SQS queue
SQS_QUEUE_URL = "http://localhost:9324/000000000000/data-raw-q"

@app.get("/check_sqs")
async def check_sqs_messages():
    try:
        # Receive messages from the SQS queue
        response = sqs.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            MaxNumberOfMessages=10,  # Adjust the number of messages to receive
            WaitTimeSeconds=2  # Wait time for long polling
        )

        messages = response.get('Messages', [])
        if not messages:
            return {"message": "No messages in the queue."}

        all_messages = []

        # Process each message
        for message in messages:
            try:
                # Decode the JSON message
                decoded_message = json.loads(message['Body'])
                all_messages.append(decoded_message)

                # Optionally, delete the message from the queue
                sqs.delete_message(
                    QueueUrl=SQS_QUEUE_URL,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Deleted message ID: {message['MessageId']}")
            except json.JSONDecodeError as e:
                print(f"Failed to decode message ID {message['MessageId']}: {e}")
                print(f"Message content: {message['Body']}")

        # Return all messages received
        return {"messages": all_messages}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
