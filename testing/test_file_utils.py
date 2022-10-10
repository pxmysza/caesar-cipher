import mock
import pytest
import os
from functionality.buffer import Buffer
from functionality.file_utils import SaveBufferUtils
import functionality.file_utils_handler
import functionality.file_operations


class TestSaveBufferUtils():
    @pytest.fixture
    def instance(self):
        return Buffer()

    @pytest.fixture
    def mock_path(self, mocker):
        return mocker.patch.object(functionality.file_operations, 'JSON_PATH',
                                   "/home/pawel/python_projects/caesar-cipher/testing/test_files")

    @pytest.fixture
    def buffer_patcher(self, mocker):
        mocker.patch("functionality.buffer.Buffer.buffer", ["dwa", "elementy"])


    @pytest.fixture
    def validator_patcher(self, mocker):
        mocker.patch("functionality.file_utils_handler.Validator.validate_type", return_value="fourth.json")

    @mock.patch("builtins.input", create=True)
    # I mock all 'inputs' not only those from my modules, not sure if that's the right way though
    def test_if_saves_whole_buffer(self, mocked_data, instance, buffer_patcher, mock_path):
        expected_filename = "test_filename.json"
        cipher_mode = "rot47"
        mocked_data.side_effect = [expected_filename, cipher_mode, "y"]
        SaveBufferUtils.save_whole_buffer("third", instance)
        assert expected_filename in [file for file in os.listdir(mock_path)]


    @mock.patch("builtins.input", create=True)
    def test_if_saves_word_only(self, mocked_data, instance, buffer_patcher, mock_path):
        expected_filename = "test_filename2.json"
        pass
