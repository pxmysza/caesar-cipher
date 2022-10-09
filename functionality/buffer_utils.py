from functionality.rot_factory import RotFactory
from functionality.file_operations import FileHandler


class BufferUtil:
    @staticmethod
    def buffer_enciphering(cipher_type: str, text: str) -> tuple:
        """Displays encrypted (if item is decrypted)
        or decrypted (if item is encrypted) text"""
        cipher = RotFactory.get_rot(cipher_type, text)
        decoded_text = cipher.encode()
        return text, decoded_text

    @staticmethod
    def load_file_to_buffer(filename: str, obj: 'Buffer') -> None:
        """Loads 'text' value from object in file to buffer"""
        s_obj = FileHandler.read_file_content(filename)
        text = s_obj["text"]
        obj.add_to_buffer(text)
