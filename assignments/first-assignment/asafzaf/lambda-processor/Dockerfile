# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the worker script into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the worker script
CMD ["python", "handler.py"]