import json

def handler(event, context):
    print("Received event!\n")

    for record in event['Records']:
        message_body = record['body']
        try:
            message = json.loads(message_body)
            print(f"Message received: {message}")
        except json.JSONDecodeError:
            print("Failed to decode JSON message.")

    return {
        'statusCode': 200,
        'body': message.get('Message', 'No message found')
    }
