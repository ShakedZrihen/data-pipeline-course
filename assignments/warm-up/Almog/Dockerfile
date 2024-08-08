# Use the official Python image for FastAPI
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Node.js and npm using NodeSource (npm is included with Node.js)
RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Install Serverless Framework globally
RUN npm install -g serverless

# Install Serverless plugins with --legacy-peer-deps and --force
RUN npm install --legacy-peer-deps --force serverless-wsgi serverless-python-requirements serverless-offline

# Verify that serverless is in the PATH
RUN which serverless

# Expose the port for the FastAPI app
EXPOSE 8000

# Default command to run Serverless offline
CMD ["serverless", "offline", "--host", "0.0.0.0"]
