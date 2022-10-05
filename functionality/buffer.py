from typing import Any


class Buffer:
    def __init__(self) -> None:
        self.__buffer = []

    def get_elements_num(self) -> int:
        return len(self.__buffer)

    def convert_buffer_to_text(self) -> str:
        return " ".join(self.__buffer)

    def add_to_buffer(self, text: str) -> None:
        self.__buffer.append(text)

    def delete_from_buffer(self, num: int) -> Any:
        return self.__buffer.pop(num)

    def display_buffer(self) -> str:
        content = ""
        if len(self.__buffer) == 0:
            return "Buffer is empty"
        else:
            for i in range(len(self.__buffer)):
                content += f"{i + 1}: {self.__buffer[i]}\n"
        return content.rstrip()

    def clear_buffer(self) -> None:
        self.__buffer = []

    def is_empty(self) -> int:
        """Returns '0' if buffer is empty"""
        return len(self.__buffer)

    def take_word_from_buffer(self, num: int) -> Any:
        return self.__buffer[num]

