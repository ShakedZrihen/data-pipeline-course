# Use an official runtime as a parent image
FROM node:20-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN npm i

RUN npm install -g nodemon

# Make port 8000 available to the world outside this container
EXPOSE 3000

# Run server
CMD ["nodemon", "server.js"]
