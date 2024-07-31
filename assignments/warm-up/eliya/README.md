# Eliya: Warm-up

Simple web api using python and Fast-API that expose the collected data from ynet

## Features

- Retrieve a all breaking news
- Retrieve all breaking news from specific date
- Retrieve all breaking news from specific time
- Retrieve all breaking news from specific date and time

## Instructions

1. install python requirements

```bash
pip install -r requirements.txt
```

2. install serverless (node) requirements

```bash
nvm use # to config the specific node version
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

## Routes

1. ### **Retrieve all breaking news :**
   - Route: /breaking-news
2. ### **Retrieve all breaking news from specific date :**
   - Route: /breaking-news?date=<date>
3. ### **Retrieve all breaking news from specific time :**
   - Route: /breaking-news?time=<time>
4. ### **Retrieve all breaking news from specific date and time :**
   - Route: /breaking-news?date=<date>&time=<time>
5. ### **Retrieve "200" if the api is up :**
   - Route: /health

> **_NOTE:_** date format: YYYY-MM-DD, time format: HH:MM
