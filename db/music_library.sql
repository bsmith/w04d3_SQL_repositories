DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

INSERT INTO artists (name) VALUES ('Beetles');

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    genre VARCHAR (255),
    artist_id INT REFERENCES artists(id)
);

INSERT INTO albums (title, genre, artist_id)
            VALUES ('Sgt Pepper', 'pop', 1);
