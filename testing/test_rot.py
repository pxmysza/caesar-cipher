import pytest

from functionality.rot import Rot47, Rot13

class TestRot:

    @pytest.fixture
    def rot13_instance(self):
        return Rot13("text")

    @pytest.fixture
    def rot47_instance(self):
        return Rot47("text")


    def test_if_rot_returns_correctly_ciphered_text(self, rot13_instance, rot47_instance):
        assert rot13_instance.encode() == "grkg"
        assert rot47_instance.encode() == "E6IE"

