# Build Python dependencies
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Verify npm installation
RUN npm --version

# Install Node.js dependencies
COPY package*.json ./
RUN npm install

# Command to run the lambda processor
CMD ["npx", "serverless", "offline", "start", "--config", "serverless.yml"]
