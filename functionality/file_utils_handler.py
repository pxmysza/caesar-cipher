from functionality.file_operations import FileHandler
from functionality.validators import Validator
from functionality.rot_factory import RotFactory
from functionality.sentence import Sentence
from functionality.json_converter import JsonConverter


class FileUtils:
    @staticmethod
    def save_buffer_to_file(text: str, filename: str):
        """Main method that saves to a file. If file already exists it invokes a methods
        that can append or overwrite file. If file does not exist it creates one"""
        if FileHandler.file_exists(filename):
            overwrite = Validator.validate_choice(
                input("File already exists. Do you want to overwrite it? (y/n): ").lower())
            if overwrite == "y":
                FileUtils.save_text_and_override(text, filename)
            else:
                FileUtils.save_text_and_append(text, filename)
        else:
            FileUtils.create_new_file(filename, text)

    @staticmethod
    def save_text_and_override(text: str, filename: str):
        """Overwrites existing file. User is asked if text is encrypted, if not it asks if user wants to encrypt"""
        cipher_type = Validator.validate_type(input("Enter cipher type: ").lower())
        print(f"Text to save: \"{text}\"")
        is_encrypted = Validator.validate_choice(
            input("Is text displayed above encrypted or not? Type 'y' or 'n': ").lower())
        encryption_status = Validator.validate_encryption(is_encrypted)
        if is_encrypted == "n":
            should_encrypt = Validator.validate_choice(input("Do you want to encrypt it? Type 'y' or 'n': ").lower())
            if should_encrypt == "y":
                rot = RotFactory.get_rot(cipher_type, text)
                text = rot.encode()
                encryption_status = "encrypted"
        s = Sentence(cipher_type, text, encryption_status)
        s_json = JsonConverter.convert_to_json(s)
        FileHandler.save_to_file(filename, s_json)

    @staticmethod
    def save_text_and_append(text_to_append: str, filename: str):
        """Method that modifies existing file. Takes text to append to existing file
        It reads file content, decrypts ciphertext if necessary, appends text, decrypt and saves again"""
        s_json = FileHandler.read_file_content(filename)
        s_obj = JsonConverter.convert_from_json(s_json)
        if s_obj.status == "encrypted":
            rot = RotFactory.get_rot(s_obj.cipher_type, s_obj.text)
            s_obj.text = rot.encode()
            s_obj.text += text_to_append
            rot = RotFactory.get_rot(s_obj.cipher_type, s_obj.text)
            s_obj.text = rot.encode()
            s_json = JsonConverter.convert_to_json(s_obj)
            FileHandler.save_to_file(filename, s_json)
        else:
            s_obj.text += text_to_append
            s_json = JsonConverter.convert_to_json(s_obj)
            FileHandler.save_to_file(filename, s_json)

    @staticmethod
    def create_new_file(filename: str, text: str):
        """Create new file and save json object to this new file"""
        cipher_type = Validator.validate_type(input("Enter cipher type: ").lower())
        should_encrypt = Validator.validate_choice(input("Do you want to encrypt it? Type 'y' or 'n': ").lower())
        if should_encrypt == "y":
            rot = RotFactory.get_rot(cipher_type, text)
            text = rot.encode()
            encryption_status = "encrypted"
        else:
            encryption_status = "decrypted"
        s = Sentence(cipher_type, text, encryption_status)
        s_json = JsonConverter.convert_to_json(s)
        FileHandler.save_to_file(filename, s_json)