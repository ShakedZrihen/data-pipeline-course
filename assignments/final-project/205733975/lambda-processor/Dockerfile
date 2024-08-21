# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Install Node.js and npm (if not already installed in python:3.11-slim)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs


# Install Node.js dependencies
RUN npm init -y
RUN npm cache clean -f
RUN npm i -g serverless@3
RUN npm install --save-dev serverless@3 serverless-python-requirements serverless-offline-sqs@6 serverless-offline@8
RUN npm list -g serverless


# Command to run the FastAPI application
CMD ["node", "--inspect=0.0.0.0:9229", "./node_modules/.bin/serverless", "offline", "start", "--config", "serverless.yml", "--dockerHost", "host.docker.internal", "--dockerHostServicePath", "${PWD}", "--host", "0.0.0.0", "--noPrependStageInUrl", "--stage", "local"]
