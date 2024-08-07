# Build Python dependencies
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install AWS CLI and Boto3 for SQS
RUN pip install awscli-local boto3

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Verify npm installation
RUN npm --version

# Set environment variables to point to LocalStack
ENV AWS_ACCESS_KEY_ID="test"
ENV AWS_SECRET_ACCESS_KEY="test"
ENV AWS_DEFAULT_REGION="us-east-1"
ENV LOCALSTACK_HOSTNAME="localhost"
ENV LOCALSTACK_EDGE_PORT="4566"

# Install Node.js dependencies
COPY package*.json ./
RUN npm install

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run serverless offline when the container launches
CMD ["npx", "serverless", "offline", "start", "--config", "serverless.yml"]
