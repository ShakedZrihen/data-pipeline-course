# Data Pipeline Project

## Introduction

This project sets up a data pipeline using Docker Compose. It includes services for scraping data from a website, processing the data, and storing it in a PostgreSQL database.

## Requirements

- Docker: Version 20.x or later
- Docker Compose: Version 1.27 or later
- Python: Version 3.11 or later
- Serverless Framework: Version 2.x or later

## Setup

1. Clone the repository:
   ```sh
   git clone <repository-url>

Navigate to the project directory:
   ```bash
cd assignments/first-assignment/AdiAbelevitch/
   ```
Build and start the services:
   ```bash
docker-compose up -d --build
   ```

## Endpoints

- **Lambda Scraper**:
  - **URL**: `http://localhost:8000/docs`for API documentation.
  - **Method**: POST

- **Lambda CRUD**:
  - **URL**: `http://localhost:8001/health`
  - **Method**: GET

- **Lambda Processor**:
  - Processes messages automatically when they are placed in the SQS queue.

## API Documentation

The API documentation can be accessed via Postman:
[View API Documentation](https://documenter.getpostman.com/view/32470335/2sA3s3HBNo)
