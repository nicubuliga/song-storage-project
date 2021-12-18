import sys
import json
import env
import os
import shutil
import webbrowser
import db_util as db
from zipfile import ZipFile

INFO_VALIDATE = """
Script should be called with exactly one parameter: song_util.py <action>
<action> should be one of "add", "delete", "modify", "search", "save_list", "play"
"""

INFO_MISSING_JSON = "You should create a json file {} with necessary parameters"


class SongStorage:

    def add_song(self):
        add_obj = get_from_json(env.ADD_SONG)

        #  Copy song to <Storage> folder
        new_song_path = os.path.join("Storage", add_obj["filename"])
        shutil.copy(add_obj["song_filepath"], new_song_path)

        # Add metadata to db
        song_id = db.add(add_obj)
        print("Song added succesfully!")

        return song_id

    def delete_song(self):
        delete_obj = get_from_json(env.DELETE_SONG)

        db.delete(delete_obj["ID"])

        print("Song and tags removed successfully!")

    def modify_song(self):
        modify_obj = get_from_json(env.MODIFY_SONG)

        db.modify(modify_obj)

        print("Song updated successfully!")

    def search_songs(self):
        search_obj = get_from_json(env.SEARCH_SONG)

        search_result = db.search(search_obj)

        with open("search_result.json", "w") as fd:
            json.dump(search_result, fd, indent=4)

        print("Your songs are at: search_result.json")

    def create_savelist(self):
        savelist_obj = get_from_json(env.CREATE_SAVE_LIST)

        search_obj = {
            "artist": savelist_obj["artist"],
            "song_format": savelist_obj["song_format"]
        }

        songs = db.search(search_obj)

        with ZipFile(savelist_obj["archive_path"], 'w') as zip_fd:
            for song in songs:
                song_path = os.path.join("Storage", song["filename"])
                zip_fd.write(song_path, arcname=os.path.basename(song_path))

        print("Your savelist is ready at your specified path!")


def validate_action():
    assert (len(sys.argv) > 1), INFO_VALIDATE

    action = sys.argv[1]
    assert (action in ["add", "delete", "modify",
            "search", "save_list", "play"]), INFO_VALIDATE


def get_from_json(json_path):
    assert (os.path.exists(json_path)), INFO_MISSING_JSON.format(json_path)

    with open(json_path, "r") as fd:
        obj = json.load(fd)

    return obj


def play_song():
    play_obj = get_from_json(env.PLAY_SONG)
    song_path = os.path.join(".", "Storage", play_obj["filename"])
    webbrowser.open(song_path)


def execute_action(action, song_storage):
    if action == "add":
        song_id = song_storage.add_song()
        print("Your song id is: {}".format(song_id))

    elif action == "delete":
        song_storage.delete_song()

    elif action == "modify":
        song_storage.modify_song()

    elif action == "search":
        song_storage.search_songs()

    elif action == "save_list":
        song_storage.create_savelist()

    elif action == "play":
        play_song()


if __name__ == "__main__":
    try:
        song_storage = SongStorage()
        validate_action()
        execute_action(sys.argv[1], song_storage)
    except Exception as e:
        print(e)
        sys.exit()
