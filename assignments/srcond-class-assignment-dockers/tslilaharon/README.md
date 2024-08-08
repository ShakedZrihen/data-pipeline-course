# FastAPI Ynet News API

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the FastAPI app locally:
    ```sh
    uvicorn main:app --reload
    ```

3. Build the Docker image:
    ```sh
    docker build -t fastapi-server .
    ```

4. Run the Docker container:
    ```sh
    docker run -p 8000:8000 fastapi-server
    ```

## Endpoints

- `/health`: Check if the API is running.
- `/breaking-news`: Get all breaking news.
- `/breaking-news?date=<date>`: Get news for a specific date.
- `/breaking-news?time=<time>`: Get news for a specific time.
- `/breaking-news?date=<date>&time=<time>`: Get news for a specific date and time.
