from functionality.menu import Menu
from functionality.buffer import Buffer
from functionality.file_operations import FileHandler
from functionality.sentence import Sentence


class Manager:
    def __init__(self):
        self.buffer = Buffer()
        self.functions_dict = {
            "1": FileHandler.display_all_files,
            "2": self.__create_sentence,
            "3": FileHandler.save_buffer_to_file,
            "4": FileHandler.read_file_content,
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

    def __create_sentence(self):
        cipher_type = self.__validate_type(input("Enter cipher type: ").lower())
        text = input("Enter plain or encrypted text: ")
        is_encrypted = self.__validate_is_encrypted(
            input("Is text entered above encrypted or not? Type 'y' or 'n'").lower()
        )
        s = Sentence(cipher_type, text, is_encrypted)
        self.buffer.add_to_buffer(s)

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

