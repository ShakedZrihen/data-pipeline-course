# Install Python dependencies
pip install -r requirements.txt

# Install Serverless
npm install -g serverless

# Install node modules
npm i

# Run FastAPI locally
uvicorn main:app --reload

# run it as serverless-offline application:
./node_modules/.bin/serverless offline start


# Run tests
pytest

# Deploy to AWS Lambda
serverless deploy


# URLS LAMBDA 
 - https://0cnedql1q4.execute-api.us-east-1.amazonaws.com/health
 - https://0cnedql1q4.execute-api.us-east-1.amazonaws.com/breaking-news?date=2024-07-31&time=14:40
 - https://0cnedql1q4.execute-api.us-east-1.amazonaws.com/breaking-news?date=2024-07-31
 - https://0cnedql1q4.execute-api.us-east-1.amazonaws.com/breaking-news?time=14:40
