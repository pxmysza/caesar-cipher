import pytest

from functionality.sentence import Sentence
from functionality.json_converter import JsonConverter

class TestJsonConverter:

    @pytest.fixture
    def instance(self):
        return Sentence("rot47", "ala ma kota", "decrypted")

    def test_conversion_to_json(self, instance):
        expected = {
            "cipher_type": "rot47",
            "text": "ala ma kota",
            "status": "decrypted"
        }
        actual = JsonConverter.convert_to_json(instance)
        assert expected == actual

    def test_conversion_from_json_to_object(self, instance):
        var = {
            "cipher_type": "rot47",
            "text": "ala ma kota",
            "status": "decrypted"
        }
        print(instance)
        actual = JsonConverter.convert_from_json(var)
        assert actual.__str__() == instance.__str__()