# Building a Local Environment using Docker Compose

## Description

as an engineer, you need to create a local development environment using Docker Compose for our Data Pipeline. The environment should include multiple services that interact with each other to scrape data from a website, process it, and store it in a PostgreSQL database.

### Components

1. **Lambda Scraper (Serverless Framework + FastAPI)**
   the lambda should:
   - expose one route: POST `/data`
   - put the data from `request.body` in sqs called `data-raw-q`

2. **SQS (Amazon Simple Queue Service)**

   - SQS infra
   - script that will create 1 queue: `data-raw-q`

3. **Lambda Processor (Serverless Framework)**

   - lambda that triggered by SQS event (can be configured using serverless framework)
   - print the data as JSON

4. **PostgreSQL**

   - DB container
   - 1 table: `users`

5. **Lambda CRUD (Serverless Framework + FastAPI)**

   the lambda should:

   - expose one route: GET `/health` which will return 200

   all lambdas can also be configured in the same `serverless.yml` file


## Technical Specifications

- **Docker**: Version 20.x or later [documentation](https://www.docker.com/)
- **Docker Compose**: Version 1.27 or later 
- **Python**: Version 3.11 or later
- **Serverless Framework**: Version 2.x or later [documentation](https://www.serverless.com/framework/docs/getting-started)
- **PostgreSQL**: Latest Docker image

> **_NOTE:_**  For this task, you can use chatGPT for help, but please understand what he suggest

## DoD

in your personal folder should be at least the following files:

1. `docker-compose.yml` - with all the component described above
2. `lambda.py` - code of lambda handlers
3. `serverless.yml`  - with all the lambdas
4. `requirements.txt` - All packages needed to run the code.
5. `README.md` - Instructions on how to run the code.

### suggested project structure

```
developer-name/
│
├── docker-compose.yml
├── lambda-scraper/
│ ├── handler.py
│ ├── serverless.yml
│ └── requirements.txt
├── lambda-processor/
│ ├── handler.py
│ ├── serverless.yml
│ └── requirements.txt
├── lambda-crud/
│ ├── handler.py
│ ├── serverless.yml
│ └── requirements.txt
```
