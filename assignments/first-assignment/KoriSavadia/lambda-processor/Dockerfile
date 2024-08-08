FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs
# Install Node.js dependencies
RUN npm install

CMD ["node", "--inspect=0.0.0.0:9229", "./node_modules/.bin/serverless", "offline", "start", "--config", "serverless.yml", "--dockerHost", "host.docker.internal", "--dockerHostServicePath", "${PWD}", "--host", "0.0.0.0", "--noPrependStageInUrl", "--stage", "local"]