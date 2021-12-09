import sys
from colorama import Fore, Back, Style

import env

INFO_STRING = """
Script should be called with exactly one parameter: song_util.py <action>
<action> should be one of "add", "delete", "modify", "search", "save_list"
"""


def validate_action():
    assert (len(sys.argv) > 1), INFO_STRING

    action = sys.argv[1]
    assert (action in ["add", "delete", "modify", "search", "save_list"]), INFO_STRING


def execute_action(action):
    if action == "add":
        pass
    elif action == "delete":
        pass
    elif action == "modify":
        pass
    elif action == "search":
        pass
    elif action == "save_list":
        pass


if __name__ == "__main__":
    try:
        validate_action()
        execute_action(sys.argv[1])
    except Exception as e:
        print(Fore.RED + str(e))
        sys.exit()
