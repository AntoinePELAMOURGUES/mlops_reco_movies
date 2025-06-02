CREATE TABLE IF NOT EXISTS links (
    id SERIAL PRIMARY KEY,
    movieid INTEGER REFERENCES movies(movieid),
    imdbid INTEGER,
    tmdbid INTEGER
);