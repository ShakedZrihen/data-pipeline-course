# Data Pipeline Project - First Assignment

## Description
This project is a local development environment set up using Docker Compose for a Data Pipeline. The environment includes multiple services that interact with each other to scrape data from a website, process it, and store it in a PostgreSQL database.

## Components
- **Lambda Scraper:** Scrapes data from a specified website and sends it to the SQS queue (`data-raw-q`).
- **SQS:** Queue for storing scraped data temporarily.
- **Lambda Processor:** Processes the data from the SQS queue and prints it as JSON.
- **PostgreSQL:** Stores user data in a table named `users`.
- **Lambda CRUD:** Provides a health check endpoint (`GET /health`) to ensure the service is running.

## Setup Instructions
**Build and start all services:**
docker-compose up --build -d

**Trigger the scraper to fetch data:**

Execute the following command:

curl -X POST "http://localhost:8000/scrape" -H "Content-Type: application/json" -d '{"key": "value"}'

Check the Lambda Processor logs:

View the logs with this command:

docker-compose logs lambda-processor

Verify the data in PostgreSQL:

Access the PostgreSQL container and check the users table:

docker exec -it tslilaharon-postgres-1 psql -U tslilaharon -d db_tslilaharon

SELECT * FROM users;

Perform a health check on the CRUD service:

Use the following command to perform a health check:

curl -X GET "http://localhost:8001/health"