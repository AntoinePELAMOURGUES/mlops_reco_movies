CREATE TABLE IF NOT EXISTS genome_tags_raw (
    id SERIAL PRIMARY KEY,
    tag_id INTEGER,
    tag VARCHAR(255)
);