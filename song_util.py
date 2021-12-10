import sys
import json
import env
import os
import shutil
import webbrowser

INFO_VALIDATE = """
Script should be called with exactly one parameter: song_util.py <action>
<action> should be one of "add", "delete", "modify", "search", "save_list", "play"
"""

INFO_MISSING_JSON = "You should create a json file {} with necessary parameters"


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


def add_song():
    add_obj = get_from_json(env.ADD_SONG)

    #  Copy song to <Storage> folder
    new_song_path = os.path.join("Storage", add_obj["filename"])
    shutil.copy(add_obj["song_filepath"], new_song_path)


def play_song():
    play_obj = get_from_json(env.PLAY_SONG)
    song_path = os.path.join(".", "Storage", play_obj["filename"])
    webbrowser.open(song_path)


def execute_action(action):
    if action == "add":
        id = add_song()
    elif action == "delete":
        pass
    elif action == "modify":
        pass
    elif action == "search":
        pass
    elif action == "save_list":
        pass
    elif action == "play":
        play_song()


if __name__ == "__main__":
    try:
        validate_action()
        execute_action(sys.argv[1])
    except Exception as e:
        print(str(e))
        sys.exit()
