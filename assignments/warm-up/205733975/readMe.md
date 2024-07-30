# Breaking News API- Amit Ronen

## Overview

This FastAPI project scrapes breaking news from Ynet and provides an API to access the latest news.

## Project Structure
``` plaintext
205733975/
├── app.py 
├── services/
│ └── breaking_news.py 
├── tests.py
├── package.json
├── package-lock.json
├── requirements.txt
└── serverless.yml
```

## Endpoints

- **/health**: GET - Check API status.
- **/breaking-news**: GET - Retrieve breaking news. Optional query parameters: `date` (YYYY-MM-DD), `time`.

## Setup & Run

1. **install python requirements**:
   ```bash
    pip install -r requirements.txt
2. **install serverless (node) requirements:**
   ```bash
   nvm use # to config the specific node version
    npm i
3. **run it as serverless-offline application:**
   ```bash
   ./node_modules/.bin/serverless offline start

**Or run it as a stand-alone server:**
```bash
    uvicorn app:app --reload
```

## Commands 
1. http://127.0.0.1:8000/health 
2. http://127.0.0.1:8000/breaking-news 
3. http://127.0.0.1:8000/breaking-news?date= 
4. http://127.0.0.1:8000/breaking-news?time= 
5. http://127.0.0.1:8000/breaking-news?date=&time= 

