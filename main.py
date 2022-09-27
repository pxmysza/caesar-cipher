from functionality.menu import Menu
import string
import json
import os
JSON_PATH = "functionality/text_files"
from typing import Optional
from functionality.CipherText import CipherText, TextManager


def read_files_from_dir() -> dict:
    files_list = []
    files_dict = {}
    for file_name in [file for file in os.listdir(JSON_PATH) if file.endswith(".json")]:
        files_list.append(file_name)
        dict_item = {
            len(files_list) - 1: file_name
        }
        files_dict.update(dict_item)
    return files_dict


def read_directory_content(files_dict: dict) -> None:
    file_number = int(input("Enter file number: "))
    file_name = files_dict.get(file_number)
    with open(JSON_PATH + "/" + file_name) as json_file:
        data = json.load(json_file)
        return data


def read_ciphertext(filename: str) -> tuple:
    with open(JSON_PATH + "/" + filename) as json_file:
        data = json.load(json_file)
        cipher_mode = data["cipher_type"]
        cipher_text = data["text"]
        cipher_num = 13 if cipher_mode == "rot13" else 47
        return rot_n(cipher_text, cipher_num), cipher_num


def rot_13(text: str) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    translate = str.maketrans(uppercase + lowercase, uppercase[13:] + uppercase[:13] + lowercase[13:] + lowercase[:13])
    return str.translate(text, translate)


def rot_47(text: str) -> str:
    str1 = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    str2 = 'PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO'
    translate = str.maketrans(str1, str2)
    return str.translate(text, translate)


def rot_n(text: str, cipher: int):
    if cipher == 13:
        return rot_13(text)
    if cipher == 47:
        return rot_47(text)


def save_to_file(filename: str, plain_text: str, cipher: int, status: [Optional] = "encrypted"):
    cipher_types = {
        13: "rot13",
        47: "rot47"
    }
    if status == "encrypted":
        json_text = {
            "cipher_type": cipher_types[cipher],
            "text": rot_n(plain_text, cipher),
            "status": status
        }
    else:
        json_text = {
            "cipher_type": "plain_text",
            "text": rot_n(plain_text, cipher),
            "status": status
        }

    with open(JSON_PATH + "/" + filename, 'w') as f:
        json.dump(json_text, f, indent=4)


def add_new_entry():
    filename = input("Enter file name: ")
    filename = filename + ".json"
    if filename in [file for file in os.listdir(JSON_PATH) if file.endswith(".json")]:
        reply = input("File already exists, do you want to modify it or overwrite? (m/o)? ")
        plain_text, cipher = read_ciphertext(filename)
        while True:
            if reply.lower() == "m":
                # read text from file, decipher, display and let user add lines
                print(plain_text)
                text = input("Enter plain text to append to existing text: ")
                save_to_file(filename, plain_text + text, cipher)
                break
            elif reply.lower() == "o":
                text = input("Enter plain text: ")
                save_to_file(filename, text, cipher)
                # Do nothing, return to menu
                break
            else:
                reply = input("Incorrect choice, try again: ")
    else:
        text = input("Enter plain text: ")
        cipher = int(input("Enter cipher type-13 or 47: "))
        save_to_file(filename, text, cipher)


def display_menu():
    print("1. Get files from directory\n2. Save to file\n3. Read from file")


# def manager(option):
#     if option == 1:
#         print(read_files_from_dir())
#     if option == 2:
#         add_new_entry()
#     if option == 3:
#         print("Available files: ")
#         print(read_files_from_dir())
#         print(read_directory_content(read_files_from_dir()))

# TODO - GET FILE CONTENT, DECRYPT, SAVE
def decrypt_file():
    pass

def main():
    # display_menu()
    # option = int(input("Select action: "))
    # manager(option)
    text = CipherText("rot13", "ala ma kota")
    m = TextManager(text)
    m.manager(1)

    #TODO read ciphertext/plaintext from file and decrypt/encrypt it


if __name__ == "__main__":
    main()
