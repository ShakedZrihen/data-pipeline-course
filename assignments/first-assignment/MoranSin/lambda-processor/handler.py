import json
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def process(event, context):
    logger.info("Processing complete")
    logger.info("Received event: %s", json.dumps(event))
    try:
        time.sleep(2)
        if event is None:
            raise ValueError("Event data is None")
        
        data = event
        print(data)
        
        logger.info("Processing complete")
        
    except (json.JSONDecodeError, ValueError) as e:
        logger.error("Error processing data: %s", e)

    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed successfully')
    }