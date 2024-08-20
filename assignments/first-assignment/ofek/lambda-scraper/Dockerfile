# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean


COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN npm init -y



RUN npm i
RUN npm install -g serverless@3 serverless-offline

EXPOSE 3000 9229


CMD ["serverless", "offline", "start", "--host", "0.0.0.0"]
