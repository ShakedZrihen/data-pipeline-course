Here's a `README.md` file that outlines the steps for running your code, testing it with Postman, and validating the database setup. Feel free to adjust any details as needed:

Project Setup and Testing Guide

## Overview

This project involves setting up a Docker environment and testing various APIs using Postman. Follow the instructions below to get everything up and running.

## Prerequisites

Ensure you have the following installed:
- Docker
- Docker Compose
- Postman

## Setup Instructions

1. **Start Docker**:
   Make sure Docker is running on your machine.

2. **Run Docker Commands**:
   Open a terminal and navigate to the project's root directory. Execute the following commands in order:
   
   ```bash
   docker-compose down
   docker-compose build
   docker-compose up
   ```

   These commands will stop any running containers, build the Docker images, and start the containers.

## Testing with Postman

1. **POST Request**:
   - **URL**: `http://localhost:8003/scrape`
   - **Method**: POST
   - **Expected Response**:
     ```json
     {
       "message": "Data sent to local SQS"
     }
     ```

2. **GET Request to Retrieve News**:
   - **URL**: `http://localhost:8002/process`
   - **Method**: GET
   - **Expected Response**: A JSON object containing the news extracted from the SQS queue.

3. **GET Request to Check Health**:
   - **URL**: `http://localhost:8001/health`
   - **Method**: GET
   - **Expected Response**:
     ```json
     {
       "status": "Healthy"
     }
     ```

## Database Validation

1. **Run Database Test**:
   Open a new terminal window and execute the following command while Docker Compose is running:

   python test_db.py

## Notes

- Ensure all services are properly running and listening on their respective ports.
- Adjust any configurations in the `docker-compose.yml` file as needed for your specific setup.

## Troubleshooting

If you encounter any issues:
- Verify Docker and Docker Compose are properly installed and running.
- Check container logs for any errors using `docker-compose logs`.
- Consult the project's documentation or contact the development team for further assistance.

---

Happy testing!
```
