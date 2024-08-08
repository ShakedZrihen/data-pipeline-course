# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file from the parent directory and install packages
COPY ../requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt



# Copy the main application code from the current directory
COPY . /app/

# Command to run the application
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8003"]
