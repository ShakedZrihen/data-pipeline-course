
# Final Assignment

## Description

For the final assignment, you need to enhance your Lambda Scraper to be triggered every 6 hours, scrape data from a **given website**, and put the scraped data into the SQS. Additionally, the Lambda Processor should format this data and save it into PostgreSQL using the CRUD Lambda.

### Requirements

1. **Lambda Scraper**:
   - Modify the Lambda Scraper to be triggered every 6 hours.
   - Scrape data from a **specified website**.
   - Put the scraped data into the SQS queue `data-raw-q`.

2. **Lambda Processor**:
   - Triggered by SQS events.
   - Format the data and save it into the PostgreSQL database using the CRUD Lambda.

3. **Lambda CRUD**:
   - Expose additional routes:
     - GET `/data` - Return data from PostgreSQL.
     - POST `/data` - Save data into PostgreSQL.

### DoD

your personal data pipeline should be able to run locally and:

- scrape
- save
- serve data
