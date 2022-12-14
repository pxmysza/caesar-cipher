from functionality.validators import Validator
from functionality.file_utils_handler import FileUtils


class SaveBufferUtils:
    @staticmethod
    def save_whole_buffer(text: str, obj: 'Buffer'):
        """Saves the entire buffer content to a file and clears buffer"""
        try:
            filename = input("Enter file name: ")
            FileUtils.save_buffer_to_file(text, filename)
        except (TypeError, ValueError) as e:
            raise e("Problem with filename check it!")
        else:
            obj.clear_buffer()
            print("Buffer was cleared")

    @staticmethod
    def save_word_from_buffer(obj: 'Buffer'):
        """Saves choosen word from buffer to a file and deletes item from buffer"""
        try:
            num = int(input("What word would you like to save? Enter number: "))
            num = Validator.validate_if_elem_exists(num, obj.get_elements_num())
            text = obj.take_word_from_buffer(num - 1)
            filename = input("Enter file name: ")
            FileUtils.save_buffer_to_file(text, filename)
        except (TypeError, ValueError) as e:
            raise e
        else:
            deleted = obj.delete_from_buffer(num - 1)
            print(f"{deleted} was deleted from buffer")

