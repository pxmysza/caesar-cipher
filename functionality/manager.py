from functionality.menu import Menu
from functionality.buffer import Buffer
from functionality.file_operations import FileHandler
from functionality.json_converter import JsonConverter
from functionality.file_utils import SaveBufferUtils
from functionality.validators import Validator
from functionality.buffer_utils import BufferUtil

PROMPT_FOR_FILENAME = "Enter file name: "

class Manager:
    def __init__(self):
        self.buffer = Buffer()
        self.functions_dict = {
            "1": FileHandler.display_all_files,
            "2": self.__add_to_buffer,
            "3": self.__save,
            "4": self.__display_file_content,
            "5": self.__display_buffer_content,
            "6": self.buffer.clear_buffer,
            "7": self.__read_file_to_buffer,
            "8": self.__display_decrypted_file_content,
            "9": self.__display_encrypted_buffer,
            "99": self.__quit
        }

    def run(self) -> None:
        """Method that runs during program execution.
        Works in loop as long as user does not decide to quit program"""
        should_quit = True
        while should_quit:
            Menu.display_menu()
            choice = input("What would you like to do?: ")
            if choice not in self.functions_dict.keys():
                print("Incorrect choice!")
            elif choice == "99":
                should_quit = self.__quit()
            else:
                self.functions_dict[choice]()

    def __add_to_buffer(self):
        """Adds another word to buffer"""
        word = input("Enter text: ")
        self.buffer.add_to_buffer(word)

    def __save(self):
        """This method saves buffer or a part of buffer to file
        If file exists, user is asked whether to overwrite or append to a file"""
        if not self.buffer.is_empty():
            print("Buffer is empty")
        else:
            what_to_save = input("Do you want to save the entire buffer or just a word/sentence? "
                                 "(type 'all' or 'word'): ")
            if what_to_save == "all":
                text = self.buffer.convert_buffer_to_text()
                SaveBufferUtils.save_whole_buffer(text, self.buffer)
            elif what_to_save == "word":
                print(f"Buffer content:\n{self.buffer.display_buffer()}")
                SaveBufferUtils.save_word_from_buffer(self.buffer)
            else:
                print("Incorrect choice!")

    def __display_file_content(self) -> None:
        """Displays all files in a directory"""
        FileHandler.display_all_files()
        filename = input(PROMPT_FOR_FILENAME)
        if FileHandler.file_exists(filename):
            s_obj = FileHandler.read_file_content(filename)
            print(JsonConverter.convert_from_json(s_obj))
        else:
            print("Could not display file content. Incorrect name?")

    def __display_buffer_content(self) -> None:
        """Method to display buffer content"""
        print(self.buffer.display_buffer())

    def __read_file_to_buffer(self) -> None:
        """Loads text from file to buffer"""
        FileHandler.display_all_files(),
        filename = input(PROMPT_FOR_FILENAME)
        if FileHandler.file_exists(filename):
            BufferUtil.load_file_to_buffer(filename, self.buffer)
        else:
            print("Could not read file content. Incorrect name?")

    def __display_decrypted_file_content(self) -> None:
        """Displays decrypted file content"""
        FileHandler.display_all_files(),
        filename = input(PROMPT_FOR_FILENAME)
        if FileHandler.file_exists(filename):
            decrypted = FileHandler.decrypt_file_content(filename)
            print(f"Decrypted text: {decrypted}")
        else:
            print("Could not read file content. Incorrect name?")

    def __display_encrypted_buffer(self):
        """Displays buffer item after encryption/decryption. Cipher mode is entered by user"""
        print(f"Buffer content:\n{self.buffer.display_buffer()}")
        try:
            num = int(input("What word would you like to encrypt/decrypt? Enter number: "))
            cipher_type = Validator.validate_type(input("Enter cipher type: ").lower())
            num = Validator.validate_if_elem_exists(num, self.buffer.get_elements_num())
            text = self.buffer.take_word_from_buffer(num - 1)
        except ValueError as e:
            print(e)
        else:
            original, decoded = BufferUtil.buffer_enciphering(cipher_type, text)
            print(f"Original text: {original}\nAfter cipher operation: {decoded}")

    def __quit(self) -> bool:
        """Quits program if right option was chosen by user.
        If buffer is not empty it can invoke 'save' method to save buffer or its part"""
        if self.buffer.is_empty():
            should_save = input("Buffer is not empty, do you want to save or discard changes? "
                                "type 'save' or 'discard': ").lower()
            try:
                should_save = Validator.validate_should_save(should_save)
            except ValueError as e:
                print(e)
                return True
            else:
                if should_save == "save":
                    self.__save()
                else:
                    self.buffer.clear_buffer()
                    return False

