# Breaking News API

1. **Install Python Requirements**

    ```bash
    pip install -r requirements.txt
    ```

2. **Install Serverless Framework and Plugins**

    ```bash
    npm install -g serverless@3.39.0
    serverless plugin install -n serverless-python-requirements
    ```

3. **Run it as a Stand-Alone Server**

    ```bash
    uvicorn main:app --reload
    ```

## Commands Available

1. **Check Health:**

    ```bash
    curl "http://127.0.0.1:8000/health"
    ```

2. **Get All Breaking News:**

    ```bash
    curl "http://127.0.0.1:8000/breaking-news"
    ```

3. **Get Breaking News by Date:**

    ```bash
    curl "http://127.0.0.1:8000/breaking-news?date=2024-08-06"
    ```

4. **Get Breaking News by Time:**

    ```bash
    curl "http://127.0.0.1:8000/breaking-news?time=21:33"
    ```

5. **Get Breaking News by Date and Time:**

    ```bash
    curl "http://127.0.0.1:8000/breaking-news?date=2024-08-06&time=21:33"
    ```


## Lambda Commands Available

1. **Check Health:**

    ```bash
    curl "https://xymy12d3xi.execute-api.us-east-1.amazonaws.com/health"
    ```

2. **Get All Breaking News:**

    ```bash
    curl "https://xymy12d3xi.execute-api.us-east-1.amazonaws.com/breaking-news"
    ```

3. **Get Breaking News by Date:**

    ```bash
    curl "https://xymy12d3xi.execute-api.us-east-1.amazonaws.com/breaking-news?date=2024-08-06"
    ```

4. **Get Breaking News by Time:**

    ```bash
    curl "https://xymy12d3xi.execute-api.us-east-1.amazonaws.com/breaking-news?time=21:33"
    ```

5. **Get Breaking News by Date and Time:**

    ```bash
    curl "https://xymy12d3xi.execute-api.us-east-1.amazonaws.com/breaking-news?date=2024-08-06&time=21:33"
    ```




## Testing

1. **Run Unit Tests**

    ```bash
    python -m pytest tests/test_main.py
    ```
