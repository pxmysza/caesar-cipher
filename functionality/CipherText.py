import json
import typing
import string
import os
JSON_PATH = "functionality/text_files"


class CipherText:
    """This class represents json object that will be saved to a file"""
    def __init__(self, cipher_type: str, plaintext: str):
        self.cipher_type = cipher_type
        self.plaintext = plaintext

    def __str__(self):
        return f"Cipher: {self.get_cipher()}, text: {self.get_plaintext()}"

    def get_cipher(self):
        return self.cipher_type

    def get_plaintext(self):
        return self.plaintext


class TextManager:

    def manager(self, user_choice: int) -> None:
        if user_choice == 1:
            self.__add_new_entry()
        # TODO view files, decrypt text from file, quit

    def __serializer(self, text: CipherText) -> str:
        if text.get_cipher() == "rot13":
            return self.__serialize_to_json(text.get_plaintext(), 13)
        if text.get_cipher() == "rot47":
            return self.__serialize_to_json(text.get_plaintext(), 47)

    def __serialize_to_json(self, plaintext, cipher_mode: int) -> str:
        payload = {
            "type": "rot13" if cipher_mode == 13 else "rot47",
            "word": self.__rot_n(plaintext, cipher_mode),
            "status": "decrypted"
        }
        return json.dumps(payload, indent=4)

    def __rot_n(self, text: str, cipher: int):
        if cipher == 13:
            return self.__rot_13(text)
        if cipher == 47:
            return self.__rot_47(text)

    def __rot_47(self, text: str):
        str1 = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        str2 = 'PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO'
        translate = str.maketrans(str1, str2)
        return str.translate(text, translate)

    def __rot_13(self, text: str) -> str:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        translate = str.maketrans(uppercase + lowercase, uppercase[13:] + uppercase[:13] + lowercase[13:] + lowercase[:13])
        return str.translate(text, translate)

    def __add_new_entry(self):
        """Adds new file with encrypted text, if file exists, asks if overwrite or append"""
        filename = input("Enter file name: ")
        filename = filename + ".json"
        if filename in [file for file in os.listdir(JSON_PATH) if file.endswith(".json")]:
            reply = input("File already exists, do you want to modify it or overwrite? (m/o)? ")
            while True:
                if reply == "m":
                    text_to_append = input("Enter text to append: ")
                    # Should I here create new CipherText and work on this object????
                    plain, cipher_num = self.__decrypt_from_file(filename)
                    text = CipherText(cipher_num, plain + text_to_append)
                    json_object = self.__serializer(text)
                    self.__save_to_file(json_object, filename)
                    break
                if reply == "o":
                    plain = input("Enter text: ")
                    cipher_num = input("'rot13' or 'rot47': ")
                    text = CipherText(cipher_num, plain)
                    json_object = self.__serializer(text)
                    self.__save_to_file(json_object, filename)
                    break
        else:
            plain = input("Enter text: ")
            cipher_num = input("'rot13' or 'rot47': ")
            text = CipherText(cipher_num, plain)
            json_object = self.__serializer(text)
            self.__save_to_file(json_object, filename)

    def __decrypt_from_file(self, filename: str) -> tuple:
        with open(JSON_PATH + "/" + filename) as json_file:
            data = json.load(json_file)
            cipher_mode = data["type"]
            cipher_text = data["word"]
            cipher_num = 13 if cipher_mode == "rot13" else 47
            return self.__rot_n(cipher_text, cipher_num), cipher_num

    def __save_to_file(self, text_json, filename: str) -> None:
        with open(JSON_PATH + "/" + filename, 'w') as f:
            f.write(text_json)
