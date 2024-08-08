# Local Development Environment for Data Pipeline

## Description

This project sets up a local development environment using Docker Compose for a data pipeline. The environment includes multiple services that interact with each other to scrape data from a website, process it, and store it in a PostgreSQL database.

## Components

1. **Lambda Scraper (Serverless Framework + FastAPI)**:
   - Exposes a POST route `/scrape` to trigger data scraping and send the scraped data to an SQS queue.

2. **SQS (Amazon Simple Queue Service)**:
   - Includes SQS infrastructure with a queue named `data-raw-q`.

3. **Lambda Processor (Serverless Framework)**:
   - Triggered by SQS events to process and print the data.

4. **PostgreSQL**:
   - A database container with a `users` table.

5. **Lambda CRUD (Serverless Framework + FastAPI)**:
   - Exposes a GET route `/health` which returns a 200 status.

## Project Structure

