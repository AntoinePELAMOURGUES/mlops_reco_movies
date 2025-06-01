CREATE TABLE IF NOT EXISTS ratings (
    id SERIAL PRIMARY KEY,
    userid INTEGER,
    movieid INTEGER REFERENCES movies(movieid),
    rating FLOAT NOT NULL,
    timestamp INTEGER
);