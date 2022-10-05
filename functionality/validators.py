
class Validator:
    @staticmethod
    def validate_if_elem_exists(num: int, no_of_buffer_elements: int) -> int:
        """Validates if element number is correct. If not raises ValueError"""
        if not isinstance(num, int):
            raise ValueError("Value must be integer!")
        if num < 0 or num > no_of_buffer_elements:
            raise ValueError("Out of range!")
        return num

    @staticmethod
    def validate_type(cipher_type: str) -> str:
        """Validates if cipher_type is 'rot13' or 'rot47' (strings).
        Other values are not allowed - ValueError is raised"""
        if cipher_type != "rot13" and cipher_type != "rot47":
            raise ValueError("Incorrect value! Must be 'rot13' or 'rot47'")
        return cipher_type

    @staticmethod
    def validate_should_save(choice: str) -> str:
        """Validates if user input equals to 'save' or 'discard' string
        Other values are not allowed - ValueError is raised"""
        if choice != "save" and choice != "discard":
            raise ValueError("Incorrect input")
        return choice

    @staticmethod
    def validate_encryption(is_encrypted: str):
        if is_encrypted != "y" and is_encrypted != "n":
            raise TypeError("Incorrect answer! Must be 'y' or 'n'")
        if is_encrypted == "y":
            return "encrypted"
        if is_encrypted == "n":
            return "decrypted"

    @staticmethod
    def validate_choice(choice):
        if choice != "y" and choice != "n":
            raise TypeError("Incorrect answer! Must be 'y' or 'n'")
        return choice