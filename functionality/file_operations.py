import json
import os
from typing import Any
JSON_PATH = "functionality/text_files"

class FileHandler:
    @staticmethod
    def read_file_content(filename: str) -> Any:
        """Reads file content"""
        with open(JSON_PATH + "/" + filename, mode='r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def save_to_file(filename: str, dict_obj: dict) -> None:
        """Saves 'json' object to a file"""
        with open(JSON_PATH + "/" + filename, mode='w') as f:
            json.dump(dict_obj, f, indent=4)

    @staticmethod
    def file_exists(filename: str) -> bool:
        """Returns 'true' if file exists in directory"""
        if filename in [file for file in os.listdir(JSON_PATH)]:
            return True
        return False

    @staticmethod
    def __read_all_files() -> dict:
        """Reads all files from directory and returns as dictionary"""
        files = {}
        i = 1
        for file_name in [file for file in os.listdir(JSON_PATH) if file.endswith(".json")]:
            tmp_file = {
                i: file_name
            }
            files.update(tmp_file)
            i += 1
        return files

    @staticmethod
    def display_all_files() -> None:
        """Invokes '__read_all_files' private method to read and display all files from directory
         in a user-friendly way"""
        files = FileHandler.__read_all_files()
        print(f"All files from \"{JSON_PATH}\" directory:")
        for key, value in files.items():
            print(f"{key}: {value}")