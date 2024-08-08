import json

def process_message(event, context):
    for record in event['Records']:
        message_body = record['body']
        print(json.dumps(message_body,ensure_ascii=False))

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully')
    }
