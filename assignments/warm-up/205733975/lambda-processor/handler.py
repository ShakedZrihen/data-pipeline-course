import json

def process_message(event, context):
    for record in event['Records']:
        print(json.dumps(record['body']))
