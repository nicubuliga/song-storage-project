import sqlite3
from env_db import *


def create_tables(conn):
    if conn == None:
        raise Exception("Error at connection to database!")

    c = conn.cursor()
    c.execute(DROP_SONGS)
    c.execute(DROP_TAGS)
    c.execute(CREATE_SONGS_TABLE)
    c.execute(CREATE_TAGS_TABLE)


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Exception as e:
        print(e)

    return conn


def add(obj):
    conn = create_connection(DB_PATH)

    if conn == None:
        raise Exception("Error at connection to database!")

    try:
        cursor = conn.cursor()
        row_data = (obj["filename"], obj["artist"],
                    obj["song_name"], obj["date"])
        cursor.execute(INSERT_SONG_SQL, row_data)
        song_id = cursor.lastrowid

        for tag in obj["tags"]:
            if tag != "":
                cursor.execute(INSERT_TAG_SQL, (song_id, tag))

        conn.commit()

        return song_id
    except sqlite3.Error as e:
        raise Exception(
            "Check your json file parameters, probably it's something wrong with them!")
    finally:
        conn.close()


def delete(song_id):
    conn = create_connection(DB_PATH)

    if conn == None:
        raise Exception("Error at connection to database!")

    try:
        cursor = conn.cursor()
        cursor.execute(DELETE_SONG_SQL, (song_id,))
        cursor.execute(DELETE_TAGS_SQL, (song_id,))

        conn.commit()

        conn.close()
    except sqlite3.Error as e:
        raise Exception(
            "There was an error at deleting, please try again!")
    finally:
        conn.close()


def modify(obj):
    pass


if __name__ == '__main__':
    conn = create_connection(r"db\songs.db")
    create_tables(conn)
    if conn != None:
        conn.close()
