import json

def handler(event, context):
    for record in event['Records']:
        print(json.loads(record['body']))
