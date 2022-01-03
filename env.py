ADD_SONG = r".\files_util\add_song.json"
DELETE_SONG = r".\files_util\delete_song.json"
MODIFY_SONG = r".\files_util\modify_song.json"
SEARCH_SONG = r".\files_util\search_song.json"
CREATE_SAVE_LIST = r".\files_util\create_save_list.json"
PLAY_SONG = r".\files_util\play_song.json"
INFO_VALIDATE = """
Script should be called with exactly one parameter: song_util.py <action>
<action> should be one of "add", "delete", "modify", "search", "save_list", "play"
"""

INFO_MISSING_JSON = "You should create a json file {} with necessary parameters"
