import json
import boto3
import time
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# SQS Client Setup
sqs_client = boto3.client('sqs', endpoint_url="http://sqs:9324")
queue_url = "http://sqs:9324/000000000000/data-raw-q"  # Local queue URL

app = FastAPI()

def process_messages():
    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,  # Number of messages to retrieve
        WaitTimeSeconds=2  # Long polling (adjust as needed)
    )

    messages = response.get('Messages', [])

    if not messages:
        return "No messages in the queue"

    results = []
    for message in messages:
        body = json.loads(message['Body'])
        
        # Prepare the message body as pretty-printed JSON
        formatted_message = json.dumps(body, indent=4)
        results.append(formatted_message)
        
        # Print the message body
        print("Received message:")
        print(formatted_message)

        # Delete the message from the queue after processing
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        print("Message processed and deleted")
    
    return "\n".join(results)

@app.get("/process")
async def process_endpoint():
    result = process_messages()
    return {"result": result}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

if __name__ == "__main__":
    main()
