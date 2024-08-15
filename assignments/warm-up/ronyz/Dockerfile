FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

RUN npm install
RUN npm install -g serverless@3 serverless-offline

EXPOSE 3000

CMD ["./node_modules/.bin/serverless", "offline", "start","--host","0.0.0.0"]
