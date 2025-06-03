CREATE TABLE IF NOT EXISTS links_raw (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies_raw(movie_id),
    imdb_id INTEGER,
    tmdb_id INTEGER
);