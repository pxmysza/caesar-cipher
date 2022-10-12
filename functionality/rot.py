from abc import ABC, abstractmethod


class Rot(ABC):
    def __init__(self, text: str):
        self.__text = text

    @property
    def text(self):
        """text property"""
        return self.__text

    @abstractmethod
    def encode(self) -> str:
        """Caesar cipher is reversible, the same function
        is being used both for encryption and decryption"""
        pass

    def shift_by_key(self, start: str, char: str, shift: int, alph_len: int):
        """universal function, works for ROT13 and ROT47, returns character
        shifted by a given number"""
        val = ord(char) - ord(start)
        val = (val + shift) % alph_len
        return chr(ord(start) + val)


class Rot47(Rot):
    def __init__(self, text: str):
        super().__init__(text)

    def encode(self) -> str:
        res = ""
        for t in self.text:
            if ord(t) == 32:
                res += t
            if 33 <= ord(t) <= 126:
                res += self.shift_by_key('!', t, 47, 94)
        return res


class Rot13(Rot):
    def __init__(self, text: str):
        super().__init__(text)

    def encode(self) -> str:
        res = ""
        for t in self.text:
            if ord(t) == 32:
                res += t
            if 97 <= ord(t) <= 122:
                res += self.shift_by_key('a', t, 13, 26)
            if 65 <= ord(t) <= 90:
                res += self.shift_by_key('A', t, 13, 26)
        return res
