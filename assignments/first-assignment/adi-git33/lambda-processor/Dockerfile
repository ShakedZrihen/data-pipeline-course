FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

COPY package*.json ./

RUN npm install

CMD ["npx", "serverless", "offline", "start", "--config", "serverless.yml"]