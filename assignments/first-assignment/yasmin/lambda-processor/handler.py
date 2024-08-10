import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def process(event, context):
    logger.info("Processing complete")
    try:
        
        if event is None:
            raise ValueError("Event data is None")
        
        data = event
        print(data)
        
        logger.info("Processing complete")
        
    except (json.JSONDecodeError, ValueError) as e:
        logger.error("Error processing data: %s", e)
