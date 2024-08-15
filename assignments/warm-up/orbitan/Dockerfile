# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Install the Serverless Framework globally
RUN npm install -g serverless

# Copy the rest of the application code
COPY . .

# Set environment variables for Serverless credentials
ENV SERVERLESS_ACCESS_KEY=your_access_key

# Expose the port that the Serverless Offline server will run on
EXPOSE 3001

# Command to run Serverless Offline
CMD ["serverless", "offline", "start"]
