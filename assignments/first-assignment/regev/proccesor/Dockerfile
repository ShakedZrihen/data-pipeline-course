# Use an official runtime as a parent image
FROM python:3

# Set the working directory in the container

# Copy the current directory contents into the container at /app
COPY . /app

WORKDIR /app

# Install any needed packages specified in requirements.txt


RUN pip install -r requirement.txt
RUN apt update
RUN apt install -y nodejs npm 
RUN npm install 
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run server
CMD ["/bin/bash", "-c", "./node_modules/.bin/serverless offline start"]
