from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base, engine, SessionLocal, Item
import boto3
import os
import json

app = FastAPI()

sqs_endpoint_url = os.getenv("SQS_ENDPOINT_URL", "http://elasticmq:9324")

sqs = boto3.client("sqs", region_name="us-east-1", endpoint_url=sqs_endpoint_url)

queue_name = "data-raw-q"
queue_url = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup_event():
    global queue_url
    try:
        response = sqs.get_queue_url(QueueName=queue_name)
        queue_url = response["QueueUrl"]
        print(f"Queue URL fetched: {queue_url}")
    except sqs.exceptions.QueueDoesNotExist:
        print(f"Queue {queue_name} does not exist. Creating queue.")
        try:
            response = sqs.create_queue(QueueName=queue_name)
            queue_url = response["QueueUrl"]
            print(f"Queue created. Queue URL: {queue_url}")
        except Exception as e:
            print(f"Error creating queue: {e}")
            raise HTTPException(
                status_code=500, detail=f"Error creating queue: {str(e)}"
            )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/getAll")
def get_all(db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()
        parsed_items = []
        for item in items:
            data = json.loads(item.data)
            parsed_items.append({"id": item.id, "data": data})
        return {"status": "ok", "data": parsed_items}
    except Exception as e:
        print(f"Error retrieving data from PostgreSQL: {e}")
        raise HTTPException(
            status_code=500, detail="Error retrieving data from PostgreSQL"
        )


@app.post("/processMessages")
def process_messages(db: Session = Depends(get_db)):
    global queue_url
    if not queue_url:
        response = sqs.get_queue_url(QueueName=queue_name)
        queue_url = response["QueueUrl"]

    try:
        response = sqs.receive_message(
            QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=20
        )

        messages = response.get("Messages", [])
        for message in messages:
            body = json.loads(message["Body"])
            print(f"Processing message: {body}")
            db_item = Item(data=json.dumps(body))
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            sqs.delete_message(
                QueueUrl=queue_url, ReceiptHandle=message["ReceiptHandle"]
            )

        return {"status": "success", "processed_messages": len(messages)}
    except Exception as e:
        print(f"Error processing messages: {e}")
        raise HTTPException(status_code=500, detail="Error processing messages")
