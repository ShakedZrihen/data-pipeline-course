import json

def handler(event, context):
    for record in event['Records']:
        data = json.loads(record['body'])
        print(data)
