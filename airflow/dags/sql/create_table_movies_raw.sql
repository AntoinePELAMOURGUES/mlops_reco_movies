CREATE TABLE IF NOT EXISTS movies_raw (
    id UUID PRIMARY KEY,
    movie_id INTEGER UNIQUE,
    title VARCHAR(200),
    genres VARCHAR(200)
);