import sys
from env import *
from song_storage import SongStorage


def validate_action():
    """ This function checks if the specified action is possible
    Possible actions are:
    1. add       - add new song
    2. delete    - delete a song by id
    3. modify    - modify a song
    4. search    - search a song
    5. save_list - create a savelist
    5. play      - play a song
    """
    assert (len(sys.argv) > 1), INFO_VALIDATE

    action = sys.argv[1]
    assert (action in ["add", "delete", "modify",
            "search", "save_list", "play"]), INFO_VALIDATE


def execute_action(action):
    """
    This function executes the specified action using SongStorage util
    """
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
