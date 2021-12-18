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
    conn = create_connection(DB_PATH)

    if conn == None:
        raise Exception("Error at connection to database!")

    cursor = conn.cursor()
    update_str = ""

    # Update song
    if "filename" in obj:
        update_str += "filename = '{}',".format(obj["filename"])
    if "artist" in obj:
        update_str += "artist = '{}',".format(obj["artist"])

    if "song_name" in obj:
        update_str += "song_name = '{}',".format(obj["song_name"])

    if "date" in obj:
        update_str += "date = '{}',".format(obj["date"])

    if len(update_str) > 0:
        update_str = update_str[:-1]
        cursor.execute(UPDATE_SONG_SQL + update_str +
                       " WHERE id = ?", (obj["ID"],))

    # Update tags
    for tag in obj["tags"]:
        if tag != "":
            if obj["tags_operation"] == "add":
                cursor.execute(INSERT_TAG_SQL, (obj["ID"], tag))

            elif obj["tags_operation"] == "delete":
                cursor.execute(DELETE_SPECIFIC_TAG_SQL, (obj["ID"], tag))

    conn.commit()
    conn.close()


def search(obj):
    conn = create_connection(DB_PATH)

    if conn == None:
        raise Exception("Error at connection to database!")

    cursor = conn.cursor()

    res = cursor.execute(
        SEARCH_SONGS, (obj["artist"], "%" + obj["song_format"]))
    search_result = []

    # Get tags
    for r in res.fetchall():
        tmp_obj = {
            "ID": 0,
            "filename": "###",
            "artist": "###",
            "song_name": "###",
            "date": "###",
        }
        for index, key in enumerate(tmp_obj):
            tmp_obj[key] = r[index]
        id = r[0]
        cursor.execute(SEARCH_TAGS, (id,))
        tmp_obj["tags"] = [x[0] for x in cursor.fetchall()]

        search_result.append(tmp_obj)

    return search_result


if __name__ == '__main__':
    conn = create_connection(r"db\songs.db")
    create_tables(conn)
    if conn != None:
        conn.close()
