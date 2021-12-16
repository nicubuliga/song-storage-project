import sys
import json
import env
import os
import shutil
import webbrowser
import db_util as db

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
        pass

    elif action == "save_list":
        pass

    elif action == "play":
        play_song()


if __name__ == "__main__":
    try:
        song_storage = SongStorage()
        validate_action()
        execute_action(sys.argv[1], song_storage)
    except Exception as e:
        print(str(e))
        sys.exit()
