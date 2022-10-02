from functionality.sentence import Sentence


class Buffer:
    def __init__(self):
        self.__buffer = []

    def convert_buffer_to_text(self):
        return " ".join(self.__buffer)

    def add_to_buffer(self, text: str) -> None:
        self.__buffer.append(text)

    def delete_from_buffer(self, num: int) -> None:
        self.__buffer.pop(num)

    def display_buffer(self) -> None:
        if len(self.__buffer) == 0:
            print("Buffer is empty")
        else:
            for i in range(len(self.__buffer)):
                print(f"{i + 1}: {self.__buffer[i]}")

    def clear_buffer(self) -> None:
        self.__buffer = []

    def is_empty(self):
        return len(self.__buffer)

    def take_word_from_buffer(self, num: int):
        return self.__buffer.pop(num)
