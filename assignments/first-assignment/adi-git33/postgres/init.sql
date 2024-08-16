CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(50),
    email VARCHAR(100),
);