CREATE TABLE IF NOT EXISTS ratings_raw (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies_raw(movie_id),
    tag_id INTEGER REFERENCES genome_tags_raw(tag_id),
    relevance FLOAT
);
