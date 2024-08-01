# Ynet API

## Description
This is a simple web API built with FastAPI that exposes breaking news data from Ynet. The API is deployed as an AWS Lambda function using the Serverless Framework.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd ynet_api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1. Start the FastAPI server locally:
    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`

## Testing

1. Install pytest:
    ```bash
    pip install pytest
    ```

2. Run the tests:
    ```bash
    pytest
    ```

## Deployment

1. Install Serverless Framework:
    ```bash
    npm install -g serverless
    ```

2. Deploy the application:
    ```bash
    serverless deploy
    ```

3. The API will be available at the endpoint provided by Serverless.

## API Documentation

Swagger documentation is available at `<server-endpoint>/docs`.
