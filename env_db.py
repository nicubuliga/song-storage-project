DB_PATH = r"db\songs.db"

INSERT_SONG_SQL = "INSERT INTO songs(filename,artist,song_name,date) VALUES(?,?,?,?);"
INSERT_TAG_SQL = "INSERT INTO tags(song_id,tag) VALUES(?,?);"
DELETE_SONG_SQL = "DELETE FROM songs WHERE id=?;"
DELETE_TAGS_SQL = "DELETE FROM tags WHERE song_id=?;"
DELETE_SPECIFIC_TAG_SQL = "DELETE FROM tags WHERE song_id=? and tag=?;"
UPDATE_SONG_SQL = "UPDATE songs SET "
SEARCH_SONGS = "SELECT * FROM songs WHERE artist=? and filename LIKE ?"
SEARCH_SONG_BY_ID = "SELECT filename FROM songs WHERE id=?;"
SEARCH_SONG_BY_ARTIST = "SELECT * FROM songs WHERE artist=?;"
SEARCH_SONG_BY_FORMAT = "SELECT * FROM songs WHERE filename LIKE ?;"
SEARCH_TAGS = "SELECT tag FROM tags WHERE song_id=?;"

DROP_SONGS = "DROP table IF EXISTS songs;"
DROP_TAGS = "DROP table IF EXISTS tags;"

CREATE_SONGS_TABLE = """
CREATE TABLE songs (
    id integer primary key autoincrement,
    filename text NOT NULL,
    artist text,
    song_name text,
    date text,
    CHECK(filename <> '')
)
"""

CREATE_TAGS_TABLE = """
CREATE TABLE tags (
    id integer primary key autoincrement,
    song_id integer NOT NULL,
    tag text NOT NULL,
    FOREIGN KEY (song_id) REFERENCES songs (id)
)
"""
