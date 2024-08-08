# Breaking News API

## Description
This API provides breaking news updates based on date and time. It fetches news from a predefined URL and serves it using FastAPI.

## THERE IS TOW WAY TO START THE APPLICATION 

## [1] Installation
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Run
1. Run the application using Uvicorn:
    ```bash
    uvicorn main:app --reload
  ```

2. Access the API at `http://127.0.0.1:8000`.

## [2] Docker
1. Build Dockerfile 
    ``` bash
    sudo docker build -t my-fastapi-app.
    ```

2. run Docker 
    ``` bash
    sudo docker run -p 3000:3000 my-fastapi-app
    ```
## Endpoints
- `GET /health` - Check the health status of the API.
- `GET /breaking-news` - Fetch breaking news. Parameters:
  - `date` (optional): Date in `YYYY-MM-DD` format.
  - `time` (optional): Time in `HH:MM` format.

## Data Generation
The data is fetched from the configured URL and saved in the `db` folder. Ensure this folder exists or will be created on initialization.

