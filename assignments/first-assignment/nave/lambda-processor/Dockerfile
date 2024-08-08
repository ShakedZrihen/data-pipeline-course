FROM python:3.11-slim

RUN apt-get update && apt-get install -y nodejs npm

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN npm install

CMD ["/bin/bash", "-c", "node_modules/.bin/serverless offline start"]
