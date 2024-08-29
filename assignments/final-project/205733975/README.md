# Final Project - Amit Ronen - 205733975

## Overview
This projects contain a full flow- Collection of the data from Spotify and save it to the DB, to its presentation by the UI.
## Project Structure

``` plaintext
205733975/
├── create-queues.sh
├── docker-compose.yml
├── elasticmq.conf
├── lambda-crud
│ ├── Dockerfile
│ ├── handler.py
│ ├── requirements.txt
│ ├── availDates.json
│ └── serverless.yml
├── lambda-processor
│ ├── Dockerfile
│ ├── handler.py
│ ├── requirements.txt
│ └── serverless.yml
├── lambda-scraper
│ ├── Dockerfile
│ ├── handler.py
│ ├── requirements.txt
│ └── serverless.yml
├── package-lock.json
├── package.json
├── requirements.txt
├── serverless.yml

```

## Endpoints

- **/charts?date=**: GET - Get all the chart's data for a date(yyyy-mm-dd).
- **/available-dates**: GET - Retrieve all the available dates of the chart's data.


## Docker Compose Setup & Run

### Build and Start the Services using Docker Compose:

```sh
docker-compose up --build
```

## API Commands

### Get chart data

```sh
http://localhost:3003/charts?date=
````

### Get available dates

```sh
http://localhost:3003/charts/available-dates
````