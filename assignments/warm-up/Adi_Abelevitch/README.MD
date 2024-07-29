# Ynet Breaking News API

## How to run the code

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the server locally:
    ```
    uvicorn app:app --reload
    ```

3. To deploy the server using Serverless Framework, run:
    ```
    serverless deploy
    ```

4. Access the API documentation at:
    ```
    <server-endpoint>/docs
    ```

## API Endpoints

- `GET /health`: Check if the API is up.
- `GET /breaking-news`: Get all breaking news.
- `GET /breaking-news?date=<date>&time=<time>`: Get breaking news for a specific date and/or time.
