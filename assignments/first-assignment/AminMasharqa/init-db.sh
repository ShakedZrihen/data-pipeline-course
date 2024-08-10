#!/bin/bash
set -e

# Create a new table and insert some initial data
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );

    INSERT INTO users (username, email)
    VALUES ('admin', 'admin@example.com')
    ON CONFLICT (username) DO NOTHING;
EOSQL
