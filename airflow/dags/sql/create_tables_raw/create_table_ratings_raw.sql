CREATE TABLE IF NOT EXISTS ratings_raw (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    movie_id INTEGER REFERENCES movies_raw(movie_id),
    rating FLOAT,
    timestamp INTEGER
);