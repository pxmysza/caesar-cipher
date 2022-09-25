from functionality.menu import Menu
import string
import json
import os
JSON_PATH = "functionality/text_files"


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


def read_file_content(files_dict: dict) -> None:
    file_number = int(input("Enter file number: "))
    file_name = files_dict.get(file_number)
    with open(JSON_PATH + "/" + file_name) as json_file:
        data = json.load(json_file)
        return data


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


def save_to_file():
    cipher_types = {
        13: "rot13",
        47: "rot47"
    }

    filename = input("Enter file name: ")
    if filename in [file for file in os.listdir(JSON_PATH) if file.endswith(".json")]:
        print("File already exists")
        return
    text = input("Enter plain text: ")
    cipher = int(input("Enter cipher type-13 or 47: "))

    json_text = {
        "cipher type": cipher_types[cipher],
        "cipher text": rot_n(text, cipher),
        "status": "decrypted"
    }
    filename = filename + ".json"

    with open(JSON_PATH + "/" + filename, 'w') as f:
        json.dump(json_text, f, indent=4)


def display_menu():
    print("1. Get files from directory\n2. Save to file\n3. Read from file")


def worker(option):
    if option == 1:
        print(read_files_from_dir())
    if option == 2:
        save_to_file()
    if option == 3:
        print("Available files: ")
        print(read_files_from_dir())
        print(read_file_content(read_files_from_dir()))


def main():
    display_menu()
    option = int(input("Select action: "))
    worker(option)

    #TODO read ciphertext/plaintext from file and decrypt/encrypt it


if __name__ == "__main__":
    main()