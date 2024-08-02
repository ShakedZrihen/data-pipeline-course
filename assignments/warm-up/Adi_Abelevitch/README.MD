# Breaking News API

This project provides an API to fetch breaking news from Ynet in real-time. The API allows you to get the latest breaking news, filter by date and time, and perform health checks to ensure the server is running correctly.

# Adi Abelevitch Warm-up

1. install python requirements

```bash
pip install -r requirements.txt
```

2. install serverless (node) requirements

```bash
npm i
```

3. run it as serverless-offline application:

```bash
./node_modules/.bin/serverless offline start
```

or run it as a stand-alone server

```bash
uvicorn app:app --reload
```
API Endpoints
Health Check
GET /health - Returns 200 if the API is up.
Breaking News
GET /breaking-news - Returns all breaking news in the following format:
{
  "date": [{ "hour": "news" }]
}

GET /breaking-news?time=<time>`-Returns all breaking news for a specific time`
```bash
{
  "hour": "news"
}
```
```bash
For only time:
{
  "date": "news in specific time (if exists)"
}
```
```bash
For both date and time:
{
  "news in specific date and time (if exists), 404 if not exist"
}
```
#Deployment
Run Unit Tests
To run unit tests using pytest:
```bash
pytest test_main.py
```
#Examples
Here are some examples of how to use the API:
Health Check:
```bash
GET http://localhost:3000/health
```
Get all breaking news:
```bash
GET http://localhost:3000/breaking-news
```
Get breaking news by time:
```bash
GET http://localhost:3000/breaking-news?time=23:58
```
Get breaking news by date and time:
```bash
GET http://localhost:3000/breaking-news?date=2024-07-31&time=08:03
```


#Project Structure
.warm-up
├── app.py
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── serverless.yml
├── test_main.py
├── services
│   ├── breaking_news.py
│   └── content_genrator.py
|   |__ db.py

