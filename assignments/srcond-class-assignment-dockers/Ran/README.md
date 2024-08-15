# Ran Warm-up

1. Install Python Requirements

   ```bash
   pip install -r requirements.txt
   ```

2. Install Serverless (Node) Requirements

   ```bash
   npm i
   ```

3. Run as Serverless-Offline Application

   ```bash
   ./node_modules/.bin/serverless offline start
   ```

   Or Run as a Stand-Alone Server

   ```bash
   uvicorn app:app --reload
   ```

4. open your browser and enter the following URLs


   - Health Check Endpoint:

     ```http
     http://localhost:8000/
     ```


   - Breaking News with Date Filter:

     ```http
     http://localhost:8000/breaking-news?date=<date>
     ```

     Replace `<date>` with the desired date.

   - Breaking News Endpoint with Time Filter:

     ```http
     http://localhost:8000/breaking-news?time=<time>
     ```

     Replace `<time>` with the desired time.

   - Breaking News Endpoint with Both Date and Time Filter:

     ```http
     http://localhost:8000/breaking-news?date=<date>&time=<time>
     ```

     Replace `<date>` and `<time>` with the desired date and time.

   - Breaking News Endpoint without Filters:

     ```http
     http://localhost:8000/breaking-news
     ```


5. **Run Tests (Optional)**

   run the tests using `pytest`:

   ```bash
   pytest
   ```
