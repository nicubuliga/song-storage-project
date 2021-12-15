import sqlite3


DROP_SONGS = "DROP table IF EXISTS songs;"
CREATE_SONGS_TABLE = """
CREATE TABLE songs (
    id integer primary key autoincrement,
    filename text,
    artist text,
    song_name text,
    date text,
    tags text
)
"""


def create_table(conn):
    if conn == None:
        print("Error at connection!")
        return

    c = conn.cursor()
    c.execute(DROP_SONGS)
    c.execute(CREATE_SONGS_TABLE)


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Exception as e:
        print(e)

    return conn


if __name__ == '__main__':
    conn = create_connection(r"db\songs.db")
    create_table(conn)
    if conn != None:
        conn.close()
