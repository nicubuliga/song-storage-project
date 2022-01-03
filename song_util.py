import sys
from env import *
from song_storage import SongStorage


def validate_action():
    assert (len(sys.argv) > 1), INFO_VALIDATE

    action = sys.argv[1]
    assert (action in ["add", "delete", "modify",
            "search", "save_list", "play"]), INFO_VALIDATE


def execute_action(action):
    if action == "add":
        song_id = SongStorage.add_song()
        print("Your song id is: {}".format(song_id))

    elif action == "delete":
        SongStorage.delete_song()

    elif action == "modify":
        SongStorage.modify_song()

    elif action == "search":
        SongStorage.search_songs()

    elif action == "save_list":
        SongStorage.create_savelist()

    elif action == "play":
        SongStorage().play_song()


if __name__ == "__main__":
    try:
        validate_action()
        execute_action(sys.argv[1])
    except Exception as e:
        print(e)
