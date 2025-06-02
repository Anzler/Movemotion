CREATE TABLE movies (
  movie_id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  release_date DATE,
  studio TEXT,
  genre TEXT,
  box_office NUMERIC
);