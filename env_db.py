DB_PATH = r"db\songs.db"

INSERT_SONG_SQL = '''INSERT INTO songs(filename,artist,song_name,date) VALUES(?,?,?,?);'''
INSERT_TAG_SQL = '''INSERT INTO tags(song_id,tag) VALUES(?,?);'''
DELETE_SONG_SQL = '''DELETE FROM songs WHERE id=?;'''
DELETE_TAGS_SQL = '''DELETE FROM tags WHERE song_id=?;'''

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
