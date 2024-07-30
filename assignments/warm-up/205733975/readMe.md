# Breaking News API

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

## Setup and Run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd 205733975
