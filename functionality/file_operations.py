import json
import os
from functionality.buffer import Buffer
JSON_PATH = "functionality/text_files"

class FileHandler:

    @staticmethod
    def save_buffer_to_file(buffer: Buffer):
        pass

    @staticmethod
    def save_sentence_to_file(self):
        pass

    def read_file_content(self):
        pass

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