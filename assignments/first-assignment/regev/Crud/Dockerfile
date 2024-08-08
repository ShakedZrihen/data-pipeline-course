# Use an official runtime as a parent image
FROM python:3

# Set the working directory in the container

# Copy the current directory contents into the container at /app
COPY . /app

WORKDIR /app

# Install any needed packages specified in requirements.txt


RUN pip install -r requirement.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
