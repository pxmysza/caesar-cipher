from typing import Any
from functionality.validators import Validator

class Buffer:
    def __init__(self) -> None:
        self.__buffer = []

    @property
    def buffer(self):
        return self.__buffer

    def get_elements_num(self) -> int:
        return len(self.buffer)

    def convert_buffer_to_text(self) -> str:
        return " ".join(self.buffer)

    def add_to_buffer(self, text: str) -> None:
        self.buffer.append(text)

    def delete_from_buffer(self, num: int) -> Any:
        return self.buffer.pop(num)

    def display_buffer(self) -> None:
        content = ""
        if len(self.buffer) == 0:
            print("Buffer is empty")
        else:
            for i in range(len(self.buffer)):
                content += f"{i + 1}: {self.buffer[i]}\n"
        print(content.rstrip())

    def clear_buffer(self) -> None:
        self.buffer.clear()

    def is_empty(self) -> int:
        """Returns '0' if buffer is empty"""
        return len(self.buffer)

    def take_word_from_buffer(self, num: int) -> Any:
        return self.buffer[num]

