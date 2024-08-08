#!/bin/sh
trap "exit 1" INT

echo "AWS Endpoint URL: ${AWS_ENDPOINT_URL}"
echo "AWS Region: ${AWS_DEFAULT_REGION}"

AWS_REGION=${AWS_DEFAULT_REGION:-us-west-1}
AWS_ENDPOINT_URL: "http://sqs:9324"

QUEUES="data-raw-q"
for QUEUE_NAME in $QUEUES
do 
    until aws sqs --endpoint-url ${AWS_ENDPOINT_URL} get-queue-url --queue-name ${QUEUE_NAME} --region ${AWS_REGION} > /dev/null 2> /dev/null
    do
        echo "Creating queue $QUEUE_NAME"
        aws sqs --endpoint-url ${AWS_ENDPOINT_URL} create-queue \
            --queue-name ${QUEUE_NAME} \
            --region ${AWS_REGION}
        echo "Queue creation response: $?"
        sleep 5
    done
done

trap - INT
