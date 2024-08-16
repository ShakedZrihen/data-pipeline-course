# Adi's First Assignment

## Description

In this assignment, we created a local development environment using Docker Compose for a Data Pipeline that includes a PostgreSQL database.

## Components

1. **lambda-crud**  
    A FastAPI server with a `GET /health` route to verify the server is running.  
    - **Port:** 3000  
    - **Health Check Route:** `http://localhost:3000/health`

2. **lambda-processor**  
    A Lambda function triggered by an SQS event that processes and prints JSON scraped data.  
    - **Port:** 9324

3. **lambda-scraper**  
    A FastAPI server with a `POST /scrape` route that scrapes data from a news website, writes it to a `data-raw-q.json` file, and sends the data to an SQS queue.  
    - **Port:** 8000  
    - **Scrape Route:** `http://localhost:8000/scrape`

4. **postgres**  
    A PostgreSQL database service that creates a `users` table.  
    - **Port:** 5432

## Setup

### Requirements

- Docker 20.x or later
- Docker Compose 1.27 or later
- Python 3.11 or later
- Serverless Framework 2.x or later

### Steps

1. Create a `.env` file with the following content:
    ```env
    POSTGRES_USER=username
    POSTGRES_PASSWORD=password
    POSTGRES_DB=dbname
    ```

2. Build and start the Docker containers in detached mode:
    ```bash
    docker-compose up -d
    ```

3. View logs from the `lambda-processor` service:
    ```bash
    docker-compose logs -f lambda-processor
    ```

4. Stop and remove the Docker containers:
    ```bash
    docker-compose down
    ```

