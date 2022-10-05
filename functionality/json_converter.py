from functionality.sentence import Sentence
from typing import Any
import json


class JsonConverter:
    @staticmethod
    def convert_to_json(text: Sentence):
        """Converts 'Sentence' object to 'json'"""
        payload = {
            "cipher_type": text.cipher_type,
            "text": text.text,
            "status": text.status
        }
        return payload

    @staticmethod
    def convert_from_json(text: Any) -> Sentence:
        """Converts 'json' object to 'Sentence' object"""
        s = Sentence(text["cipher_type"], text["text"], text["status"])
        return s
