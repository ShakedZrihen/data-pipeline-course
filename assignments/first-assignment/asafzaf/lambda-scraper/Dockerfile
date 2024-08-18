# Use an official runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 3000 available to the world outside this container
EXPOSE 4000

# Set the command to run the Python application
# CMD ["serverless", "offline", "app.py"]
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "4000"]