#!/bin/sh
aws --endpoint-url=http://sqs:9324 sqs create-queue --queue-name data-raw-q
