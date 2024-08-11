# Breaking News API - Amit Ronen

## Overview
This FastAPI project scrapes breaking news from Ynet and provides an API to access the latest news.

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
├── services
│ └── breaking_news.py
```

## Endpoints

- **/health**: GET - Check API status.
- **/breaking-news**: GET - Retrieve breaking news. Optional query parameters: date (YYYY-MM-DD), time.
- **/scrape**: POST - Scrape the latest breaking news and store in DB.


## Docker Compose Setup & Run

### Build and Start the Services using Docker Compose:

```sh
docker-compose up --build
```

## API Commands

### Health Check

```sh
http://0.0.0.0:3000/health 
````
### Retrieve Breaking News:
```sh
http://0.0.0.0:3000/breaking-news 
```
### Retrieve Breaking News by Date:
```sh
http://0.0.0.0:3000/breaking-news?date= 
```
### Retrieve Breaking News by Time:
```sh
http://0.0.0.0:3000/breaking-news?time= 
```
### Retrieve Breaking News by Date and Time:
```sh
http://0.0.0.0:3000/breaking-news?date=&time= 
```

### Trigger Scrape with Postman:
```sh
http://0.0.0.0:3000/scrape
```