# FastAPI AWS Lambda Example

## Description
This project is a simple FastAPI application that exposes breaking news data via HTTP endpoints.

## Requirements
- Python 3.8+
- `pip install -r requirements.txt`

## Running the Application
To run the FastAPI application locally:
1. install serverless (node) requirements

```nvm use # to config the specific node version
npm i```

2. run it as serverless-offline application:
```./node_modules/.bin/serverless offline start```

```bash
uvicorn main:app --reload```
