# Data Pipelines - First assignment

## Description

This project is about creating a local development using Docker Compose for Data Pipline.

The environment includes multiple services that interact with each other to scrape data from a website, process it, and store it in PostgreSQL database.

## Requirements
1. Docker: Version 20.x or later documentation
2. Docker Compose: Version 1.27 or later
3. Python: Version 3.11 or later
4. Serverless Framework: Version 2.x or later documentation
5. PostgreSQL: Latest Docker image

## Installation

To install this project, follow these steps:

1. Navigate to project folder:
```bash
cd developer-name
```

2. Run Docker-compose file:
```bash
docker-compose down
docker-compose up --build
```

3. Wait until docker containers up.

4. Open a new terminal and run:
```bash
Docker ps
```

5. You should see 5 instances, with image names:
- `asafzaf-lambda-scraper`
- `softwaremill/elasticmq:latest`
- `asafzaf-lambda-processor`
- `asafzaf-lambda-crud`
- `postgres:latest`

## Usage

To use this project, follow these instructions:

1. For check docker is fine - send GET request to `http://0.0.0.0:6000/health` (should return 200 for success).

2. For run scraper - send POST request to `http://0.0.0.0:4000/scrape` (Process container shoud print data log).
