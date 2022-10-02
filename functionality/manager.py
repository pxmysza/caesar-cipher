from functionality.menu import Menu
from functionality.buffer import Buffer
from functionality.file_operations import FileHandler
from functionality.sentence import Sentence
from functionality.json_converter import JsonConverter
from functionality.rot_factory import RotFactory


class Manager:
    def __init__(self):
        self.buffer = Buffer()
        self.functions_dict = {
            "1": FileHandler.display_all_files,
            "2": self.__add_to_buffer,
            "3": self.__save_buffer_to_file,
            "4": self.__display_file_content,
            "5": self.buffer.display_buffer,
            "6": self.__quit
        }

    def run(self) -> None:
        while True:
            Menu.display_menu()
            choice = input("What would you like to do?: ")
            self.functions_dict[choice]()
            if choice == "6":
                break

    def __add_to_buffer(self):
        """Adds another word to buffer"""
        word = input("Enter text: ")
        self.buffer.add_to_buffer(word)

    def __display_file_content(self):
        """Method that displays all files in a directory"""
        FileHandler.display_all_files()
        filename = input("Enter file name: ")
        if FileHandler.file_exists(filename):
            s_obj = FileHandler.read_file_content(filename)
            print(JsonConverter.convert_from_json(s_obj))
        else:
            print("Could not display file content. Incorrect name?")

    def __create_obj_and_save_to_existing_file(self, text: str, filename: str):
        """Method that overwrites existing file. User is asked if text shuld be encrypted or not"""
        cipher_type = self.__validate_type(input("Enter cipher type: ").lower())
        print(f"Buffer content: {self.buffer.convert_buffer_to_text()}")
        is_encrypted = input("Is text displayed above encrypted or not? Type 'y' or 'n': ").lower()
        encryption_status = self.__validate_is_encrypted(is_encrypted)
        if is_encrypted == "n":
            should_encrypt = input("Do you want to encrypt it? Type 'y' or 'n': ")
            if should_encrypt == "y":
                rot = RotFactory.get_rot(cipher_type, text)
                text = rot.encode()
                encryption_status = "encrypted"
        s = Sentence(cipher_type, text, encryption_status)
        s_json = JsonConverter.convert_to_json(s)
        FileHandler.save_to_file(filename, s_json)

    def __modify_obj_and_save_to_existing_file(self, text_to_append: str, filename: str):
        """Method that modifies existing file. Takes text to append to existing file
        It reads file content, decrypts ciphertext if necessary, appends text, decrypt and saves again"""
        s_json = FileHandler.read_file_content(filename)
        s = JsonConverter.convert_from_json(s_json)
        if s.status == "encrypted":
            rot = RotFactory.get_rot(s.cipher_type, s.text)
            s.text = rot.encode()
            s.text += text_to_append
            rot = RotFactory.get_rot(s.cipher_type, s.text)
            s.text = rot.encode()
            s_json = JsonConverter.convert_to_json(s)
            FileHandler.save_to_file(filename, s_json)
        else:
            s.text += text_to_append
            s_json = JsonConverter.convert_to_json(s)
            FileHandler.save_to_file(filename, s_json)


    def __save_buffer_to_file(self):
        """This method saves buffer or a part of buffer to file
        If file exists, user is asked whether to overwrite or append to a file"""
        what_to_save = input("Do you want to save the entire buffer or just a word/sentence? (type 'all' or 'word'): ")
        if what_to_save == "all":
            text = self.buffer.convert_buffer_to_text()
            filename = input("Enter file name: ")
            if FileHandler.file_exists(filename):
                overwrite = input("File already exists. Do you want to overwrite it? (y/n): ").lower()
                if overwrite == "y":
                    self.__create_obj_and_save_to_existing_file(text, filename)
                    self.buffer.clear_buffer()
                else:
                    self.__modify_obj_and_save_to_existing_file(text, filename)
                    self.buffer.clear_buffer()
            else:
                self.__create_new_file(filename, text)  # TODO save all buffer content to file
        # TODO modify take_word_from_buffer, __create_obj_and_save_to_existing_file should be used both for word and for all
        if what_to_save == "word":
            print(f"Buffer content: {self.buffer.display_buffer()}")
            num = int(input("What word would you like to save? Enter number: "))
            word = self.buffer.take_word_from_buffer(num - 1)
            filename = input("Enter file name: ")
            if FileHandler.file_exists(filename):
                overwrite = input("File already exists. Do you want to overwrite it? (y/n): ").lower()
                if overwrite == "y":
                    self.__create_obj_and_save_to_existing_file(word, filename)
                    self.buffer.clear_buffer()
                else:
                    self.__modify_obj_and_save_to_existing_file(word, filename)
                    self.buffer.clear_buffer()
            else:
                self.__create_new_file(filename, word)  # TODO word to a file

    def __create_new_file(self, filename: str, text: str):
        """Create new file and save json object to it"""
        pass

    def __quit(self) -> None:
        if self.buffer.is_empty():
            should_save = input("Buffer is not empty, do you want to save or discard changes? "
                                "type 'save' or 'discard': ")
            if should_save == "save":
                FileHandler.save_buffer_to_file(self.buffer)
            else:
                self.buffer.clear_buffer()

    def __validate_type(self, cipher_type: str) -> str:
        if cipher_type != "rot13" and cipher_type != "rot47":
            raise ValueError("Incorrect value! Must be 'rot13' or 'rot47'")
        return cipher_type

    def __validate_is_encrypted(self, is_encrypted: str):
        if is_encrypted != "y" and is_encrypted != "n":
            raise TypeError("Incorrect answer! Must be 'y' or 'n'")
        if is_encrypted == "y":
            return "encrypted"
        if is_encrypted == "n":
            return "decrypted"

    def __validate_overwrite(self, overwrite):
        if overwrite != "y" and overwrite != "n":
            raise TypeError("Incorrect answer! Must be 'y' or 'n'")
        return overwrite