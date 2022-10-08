from functionality.rot import Rot47, Rot13


class RotFactory:
    """Class that returns 'Rot47' or 'Rot13' decrypted/encrypted text
    it takes 2 variables \n
    - 'cipher_type': 'rot13' or 'rot47'
    - 'text': text to encrypt/decrypt"""
    @classmethod
    def get_rot(cls, cipher_type: str, text: str):
        if cipher_type == "rot47":
            return Rot47(text)
        elif cipher_type == "rot13":
            return Rot13(text)
