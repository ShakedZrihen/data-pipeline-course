 # Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 3001 to the outside world
EXPOSE 3001

# Command to run the FastAPI application
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "3001"]
