
# Project Setup and Testing Guide

## Overview

This guide provides instructions for setting up and testing the project environment using Docker Compose and Postman.

## Prerequisites

Ensure the following software is installed on your system:
- Docker
- Docker Compose
- Postman
- Python
- Node.js

## Setup Instructions

1. **Start Docker**:
   - Ensure Docker is running on your desktop.

2. **Run Docker Commands**:
   - In the terminal, navigate to the project directory and execute the following commands to build and run the Docker containers:
     ```bash
     docker-compose build
     docker-compose up
     ```

## Testing with Postman

1. **POST Request**:
   - **URL**: `http://localhost:7000/scrape`
   - **Method**: POST
   - **Expected Response**:
     ```json
     {
       "message": "62 items scraped and sent to SQS"
     }
     ```

2. **GET Request to Retrieve News**:
   - **URL**: `http://localhost:8000/check_sqs`
   - **Method**: GET
   - **Expected Response**:
     ```json
     {
       "messages": [
           {
               "hour": "18:20",
               "title": "נזק כבד מכטב"מים לקריה הטיפולית לנכים במבואות החרמון: "היה פיצוץ אדיר, הכל הלך"
           },
           {
               "hour": "18:13",
               "title": "סמוטריץ' עונה למתקפה מארה"ב: "תכבדו את הדמוקרטיה הישראלית""
           }
           // more messages
       ]
     }
     ```

3. **GET Request to Check Health**:
   - **URL**: `http://localhost:9000/health`
   - **Method**: GET
   - **Expected Response**:
     ```json
     {
       "status": "This works :)"
     }
     ```

## Checking Data in SQS Queue

To verify if the data is saved in the SQS queue, run the `check_Sqs.py` script:
1. In the terminal, navigate to the directory where `check_Sqs.py` is located.
2. Execute the script with the following command:
   ```bash
   python check_Sqs.py
   ```

## Database Postgres Validation

### Environment Variables
Ensure the following environment variables are set for PostgreSQL:
  - **POSTGRES_USER**: `myPOSTGRES`    
  - **POSTGRES_PASSWORD**: `myPOSTGRES`  
  - **POSTGRES_DB**: `mydatabase`

### Run Database Test
1. In the terminal, execute the following command to access the PostgreSQL database:
   ```bash
   docker run -it --rm postgres:13 psql -h host.docker.internal -U myPOSTGRES -d mydatabase
   ```
2. Enter the password when prompted:
   ```
   Password for user myPOSTGRES: myPOSTGRES
   ```
3. Once connected, the prompt will display:
   ```
   mydatabase=#
   ```
4. To list the tables, run:
   ```sql
   \dt
   ```
   Expected output:
   ```
       List of relations
    Schema | Name  | Type  |   Owner
   --------+-------+-------+------------
    public | users | table | myPOSTGRES
   (1 row)
   ```
5. To view the contents of the `users` table, run:
   ```sql
   SELECT * FROM users;
   ```
   Expected output:
   ```
   id | username |        email         |         created_at
   ----+----------+----------------------+----------------------------
   1  | ebraheem | ebraheem@aboraya.com | 2024-08-10 00:39:05.238028
   (1 row)
   ```
