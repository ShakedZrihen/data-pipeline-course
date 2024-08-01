# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Install serverless globally
RUN npm install -g serverless

# Copy the Python dependencies file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose port 8000 for FastAPI and 3000 for serverless-offline
EXPOSE 8000
EXPOSE 3000

# Command to run serverless offline and FastAPI
# CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & serverless offline"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
