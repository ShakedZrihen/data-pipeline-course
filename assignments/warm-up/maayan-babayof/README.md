# Breaking News API

## Warm-Up Exercise

This project sets up a simple FastAPI application to expose collected breaking news data. It’s designed to run on AWS Lambda using the Serverless Framework.

## Prerequisites

Before starting, make sure to install the necessary packages and tools:

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. ## Install Node.js Dependencies:
```bash
npm install
```
## Install Serverless Framework:
```bash
npm install -g serverless
```
# Running the Server Locally
To run the FastAPI server locally, use Uvicorn:
```bash
uvicorn main:app --reload
```
# Running Serverless Offline
For local development using Serverless Framework, start the offline server:
```bash
serverless offline start
```
Note: You may need to log in Serverless Framework or configure AWS credentials for deployment.

# Running Unit Tests
To run the unit tests for the project, use:
```bash
pytest
```
# API Endpoints
## /health
Description: Check if the API is up and running.

Response:
```json
{
  "status": "OK"
}
```
## /breaking-news
Description: Retrieve all breaking news.

Response:
```json
{
  "2024-07-31": [
    {
      "09:49:35": "Report 1"
    },
    {
      "09:37:33": "Report 2"
    }
  ]
}
```
## /breaking-news?date=<date>
Description: Retrieve breaking news for a specific date.

Example Request:
```bash
/breaking-news?date=2024-07-31
```
Response:

```json
{
  "09:49:35": "Report 1",
  "09:37:33": "Report 2"
}
```
## /breaking-news?time=<time>
Description: Retrieve breaking news for a specific time.
Example Request:
```bash
/breaking-news?time=09:00
```
Response:

```json
{
  "2024-07-31": "Report"
}
```
## /breaking-news?date=<date>&time=<time>
Description: Retrieve breaking news for a specific date and time.
Example Request:

```bash
/breaking-news?date=2024-07-31&time=09:00
```
