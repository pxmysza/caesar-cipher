from functionality.buffer_utils import BufferUtil
from functionality.buffer import Buffer
from functionality.rot import Rot13, Rot47
import pytest


class TestBufferUtils:

    @pytest.fixture
    def instance(self):
        return Buffer()

    @pytest.fixture
    def buffer_patcher(self, mocker):
        mocker.patch("functionality.buffer.Buffer.buffer", ["dwa", "elementy"])

    def test_if_loads_from_file_to_buffer(self, mocker, buffer_patcher, instance):
        expected_len = 3
        expected_val = "ala ma kota"
        s_obj = {
            "cipher_type": "rot13",
            "text": "ala ma kota",
            "status": "decrypted"
        }
        # Mock for FileHandler.read_file_content method, if not used then existing file can be used for testing
        mocker.patch('functionality.buffer_utils.FileHandler.read_file_content', return_value=s_obj)
        BufferUtil.load_file_to_buffer("test.json", instance)
        actual_val = instance.take_word_from_buffer(2)
        actual_len = instance.get_elements_num()
        assert expected_len == actual_len
        assert expected_val == actual_val


    def test_if_returns_plaintext_and_ciphertext_tuple(self, mocker):
        plaintext = "ala ma kota"
        cipher_13 = "rot13"
        cipher_47 = "rot47"
        ciphertext_13 = "nyn zn xbgn"
        ciphertext_47 = "2=2 >2 <@E2"

        assert BufferUtil.buffer_enciphering(cipher_13, plaintext) == (plaintext, ciphertext_13)
        assert BufferUtil.buffer_enciphering(cipher_13, ciphertext_13) == (ciphertext_13, plaintext)
        assert BufferUtil.buffer_enciphering(cipher_47, plaintext) == (plaintext, ciphertext_47)
        assert BufferUtil.buffer_enciphering(cipher_47, ciphertext_47) == (ciphertext_47, plaintext)





