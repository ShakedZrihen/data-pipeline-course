# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the main requirements.txt file and install packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install AWS CLI
RUN apt-get update && \
    apt-get install -y awscli && \
    rm -rf /var/lib/apt/lists/*
    
ENV AWS_ACCESS_KEY_ID=local
ENV AWS_SECRET_ACCESS_KEY=local
ENV AWS_DEFAULT_REGION=us-west-1
ENV AWS_ENDPOINT_URL=http://sqs:9324
# Copy the rest of the application code
COPY . /app/

# Copy the services directory from the parent directory
COPY ../services /app/services
COPY ../resources /app/resources

# Command to run the application
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "3000"]
