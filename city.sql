CREATE TABLE city (
    id VARCHAR(255) PRIMARY KEY,
    updated_at DATETIME,
    created_at DATETIME,
    state_id VARCHAR(255),
    name VARCHAR(255),
    FOREIGN KEY (state_id) REFERENCES state(id)
);