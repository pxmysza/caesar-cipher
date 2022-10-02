from functionality.rot import Rot47, Rot13


class RotFactory:
    @classmethod
    def get_rot(cls, cipher_type: str, text: str):
        if cipher_type == "rot47":
            return Rot47(text)
        elif cipher_type == "rot13":
            return Rot13(text)
