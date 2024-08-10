## Setup

1. **Build and to start the Docker Images**.
    ```bash
    docker-compose up --build
    ```


## Testing

### PostgreSQL Service

1. **Connect to PostgreSQL**:
    ```bash
    docker exec -it <postgres-container-id> psql -U postgres -d your_database_name
    ```

2. **Check Tables**:
    ```sql
    \dt
    ```

3. **Query Data**:
    ```sql
    SELECT * FROM your_table_name;
    ```

## **Postman test**:
    Lambda Scraper: POST /scrape at http://localhost:8000/scrape
    Lambda CRUD: GET /health at http://localhost:8001/health