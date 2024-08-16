import json
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def process(event, context):
    logger.info("Received event: %s", json.dumps(event))
    try:
        if event is None:
            raise ValueError("Event data is None")
        
        for record in event.get('Records', []):
            body = record.get('body', None)
            if body:
                print(body)
            else:
                print("No body found in this record")
              
    except (json.JSONDecodeError, ValueError) as e:
        logger.error("Error processing data: %s", e)

    return {
        'statusCode': 200,
        'body': json.dumps('Processing is done')
    }