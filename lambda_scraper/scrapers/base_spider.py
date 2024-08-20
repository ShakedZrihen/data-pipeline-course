import scrapy
import json
import boto3
from abc import ABC, abstractmethod
from settings import settings


class BaseSpider(scrapy.Spider, ABC):
    def __init__(self, urls, queue_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = urls
        self.sqs = boto3.client(
            "sqs",
            region_name=settings.aws.region_name,
            aws_access_key_id=settings.aws.access_key_id,
            aws_secret_access_key=settings.aws.secret_access_key,
            endpoint_url=settings.queue_url,  # This points to ElasticMQ
        )
        self.queue_url = queue_url

    def send_to_sqs(self, data):
        message_body = json.dumps(data)
        response = self.sqs.send_message(
            QueueUrl=self.queue_url, MessageBody=message_body
        )
        self.log(f"Message sent to SQS: {response['MessageId']}")

    @abstractmethod
    def parse(self, response):
        pass
