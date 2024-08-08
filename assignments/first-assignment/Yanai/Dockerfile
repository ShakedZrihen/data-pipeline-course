# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the main requirements.txt file and install packages
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the port based on the service
RUN cd lambda-processor

# Command to run the application
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "3000"]
