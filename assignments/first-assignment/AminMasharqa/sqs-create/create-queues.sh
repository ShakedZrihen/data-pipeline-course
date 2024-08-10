#!/bin/bash

# Base URL of the SQS service
BASE_URL="http://localhost:9324"  # Change to the correct service URL if needed

# Function to create a queue and check for success
create_queue() {
  local queue_name=$1
  response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE_URL/000000000000/$queue_name")
  if [ "$response" -eq 200 ]; then
    echo "Queue '$queue_name' created successfully."
  else
    echo "Failed to create queue '$queue_name'. HTTP status code: $response"
  fi
}

# Create queues
create_queue "ynet-articles-q"
create_queue "ynet-comments-q"
create_queue "ynet-notifications-q"
create_queue "ynet-articles-q-dead"
create_queue "ynet-comments-q-dead"
create_queue "ynet-notifications-q-dead"

# Example of creating a queue with specific attributes (optional)
create_custom_queue_response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE_URL/000000000000/ynet-custom-q" -d '{
  "Attributes": {
    "DelaySeconds": "30",
    "MaximumMessageSize": "1024",
    "MessageRetentionPeriod": "86400",
    "ReceiveMessageWaitTimeSeconds": "20",
    "VisibilityTimeout": "30"
  }
}')

if [ "$create_custom_queue_response" -eq 200 ]; then
  echo "Custom queue 'ynet-custom-q' created successfully."
else
  echo "Failed to create custom queue 'ynet-custom-q'. HTTP status code: $create_custom_queue_response"
fi
