import json
from env import *
import os
import shutil
import webbrowser
import db_util as db
from zipfile import ZipFile


def get_from_json(json_path):
    assert (os.path.exists(json_path)), INFO_MISSING_JSON.format(json_path)

    with open(json_path, "r") as fd:
        obj = json.load(fd)

    return obj


class SongStorage:

    def add_song():
        add_obj = get_from_json(ADD_SONG)

        # Add metadata to db
        song_id = db.add(add_obj)

        #  Copy song to <Storage> folder
        new_song_path = os.path.join("Storage", add_obj["filename"])
        shutil.copy(add_obj["song_filepath"], new_song_path)

        print("Song added succesfully!")

        return song_id

    def delete_song():
        delete_obj = get_from_json(DELETE_SONG)

        filename = db.delete(delete_obj["ID"])

        # Remove file from Storage
        full_path = os.path.join("Storage", filename)
        os.remove(full_path)

        print("Song and tags removed successfully!")

    def modify_song():
        modify_obj = get_from_json(MODIFY_SONG)

        db.modify(modify_obj)

        print("Song updated successfully!")

    def search_songs():
        search_obj = get_from_json(SEARCH_SONG)

        search_result = db.search(search_obj)

        with open("search_result.json", "w") as fd:
            json.dump(search_result, fd, indent=4)

        print("Your songs are at: search_result.json")

    def create_savelist():
        savelist_obj = get_from_json(CREATE_SAVE_LIST)

        songs = db.search(savelist_obj)

        with ZipFile(savelist_obj["archive_path"], 'w') as zip_fd:
            for song in songs:
                song_path = os.path.join("Storage", song["filename"])
                zip_fd.write(song_path, arcname=os.path.basename(song_path))

        print("Your savelist is ready at your specified path!")

    def play_song():
        play_obj = get_from_json(PLAY_SONG)
        song_path = os.path.join(".", "Storage", play_obj["filename"])

        if os.path.exists(song_path):
            webbrowser.open(song_path)
        else:
            raise Exception("Your song filename doesn't exist!")
