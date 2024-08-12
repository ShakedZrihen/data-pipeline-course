# Local Development Environment for Data Pipeline - Esty Brandes

## Overview

This project sets up a local development environment using Docker Compose for a data pipeline. The pipeline includes multiple services that interact with each other to scrape data from a website, process it, and store it in a PostgreSQL database.

## Components

- **Lambda Scraper**: Exposes a POST /scrape route to scrape data and put it in an SQS queue.
- **SQS**: Amazon Simple Queue Service (simulated locally using ElasticMQ).
- **Lambda Processor**: Processes messages from the SQS queue.
- **PostgreSQL**: Database service with a single table `users`.
- **Lambda CRUD**: Exposes a GET /health route to check service health.

## Requirements

- Docker: Version 20.x or later
- Docker Compose: Version 1.27 or later
- Python: Version 3.11 or later
- Serverless Framework: Version 2.x or later

## Setup

1. Clone the repository:

```sh
git clone <repository-url>
cd developer-name
