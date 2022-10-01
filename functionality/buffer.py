from functionality.sentence import Sentence


class Buffer:
    def __init__(self):
        self.__buffer = []

    def add_to_buffer(self, text: Sentence) -> None:
        self.__buffer.append(text)

    def delete_from_buffer(self, text: Sentence) -> None:
        for b in self.__buffer:
            if text == b:
                self.__buffer.remove(text)

    def display_buffer(self) -> None:
        for b in self.__buffer:
            print(b)

    def clear_buffer(self) -> None:
        self.__buffer = []

    def is_empty(self):
        return len(self.__buffer)