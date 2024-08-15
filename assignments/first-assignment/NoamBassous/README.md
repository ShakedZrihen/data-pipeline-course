# Building a Local Environment using Docker Compose


This project sets up a local development environment for a data pipeline using Docker Compose. The environment includes multiple services that interact with each other to scrape data from a website, process it, and store it in a PostgreSQL database.

## Components

1. **Lambda Scraper**: Scrapes data from a website and sends it to SQS.
2. **SQS**: Acts as a queue for raw data.
3. **Lambda Processor**: Processes the data from SQS.
4. **PostgreSQL**: Database for storing processed data.
5. **Lambda CRUD**: Exposes a health check endpoint.

## Setup

### Technical Specifications

- Docker 20.x or later
- Docker Compose 1.27 or later
- Python 3.11 or later
- Serverless Framework 2.x or later

### Steps to Run

1. **Navigate to your directory**:
    ```sh
    cd project_directory
    ```

2. **Build and start the Docker containers in detached mode**:
    ```sh
    docker-compose up -d --build
    ```

3. **View logs from the Lambda Processor**:
    ```sh
    docker-compose logs -f lambda-processor
    ```

4. **Test the Lambda Scraper**:
    - Use any HTTP client like `curl` or Postman to make a POST request to `http://localhost:3000/scrape`.

5. **Check the health of Lambda CRUD**:
    - Visit `http://localhost:3001/health` in your browser or use an HTTP client to make a GET request.

## Endpoints

- **Lambda Scraper**:
  - **URL**: `http://localhost:3000/scrape`
  - **Method**: POST

- **Lambda CRUD**:
  - **URL**: `http://localhost:3001/health`
  - **Method**: GET