import json
import os
from functionality.buffer import Buffer
JSON_PATH = "functionality/text_files"

class FileHandler:

    @staticmethod
    def read_file_content(filename: str):
        with open(JSON_PATH + "/" + filename, mode='r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def save_to_file(filename: str, dict_obj: dict):
        with open(JSON_PATH + "/" + filename, mode='w') as f:
            json.dump(dict_obj, f, indent=4)

    @staticmethod
    def file_exists(filename: str) -> bool:
        """Returns 'true' if file exists in directory"""
        if filename in [file for file in os.listdir(JSON_PATH)]:
            return True
        return False

    @staticmethod
    def read_all_files() -> dict:
        f_dict = {}
        i = 1
        for file_name in [file for file in os.listdir(JSON_PATH) if file.endswith(".json")]:
            temp_obj = {
                i: file_name
            }
            f_dict.update(temp_obj)
            i += 1
        return f_dict

    @staticmethod
    def display_all_files() -> None:
        files = FileHandler.read_all_files()
        print(f"All files from \"{JSON_PATH}\" directory:")
        for key, value in files.items():
            print(f"{key}: {value}")