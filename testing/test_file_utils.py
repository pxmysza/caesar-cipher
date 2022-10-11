import mock
import pytest
import os
import json
from functionality.buffer import Buffer
from functionality.file_utils import SaveBufferUtils
import functionality.file_utils_handler
import functionality.file_operations
from datetime import datetime


class TestSaveBufferUtils:
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
    def test_if_saves_whole_buffer(self, mocked_data, instance, mock_path):
        expected_filename = "test_file" + str(datetime.now()) + ".json"
        cipher_mode = "rot47"
        mocked_data.side_effect = [expected_filename, cipher_mode, "y"]
        SaveBufferUtils.save_whole_buffer("example", instance)
        assert expected_filename in [file for file in os.listdir(mock_path)]

    @mock.patch("builtins.input", create=True)
    def test_if_saves_word_only(self, mocked_data, instance, mock_path, buffer_patcher):
        expected_filename = "test_file" + str(datetime.now()) + ".json"
        cipher_mode = "rot47"
        mocked_data.side_effect = [0, expected_filename, cipher_mode, "y"]
        print(instance.convert_buffer_to_text())
        SaveBufferUtils.save_word_from_buffer(instance)
        with open(mock_path + "/" + expected_filename, mode='r') as f:
            data = json.load(f)
            assert data["text"] == "6=6>6?EJ"

    @mock.patch("builtins.input", create=True)
    def test_if_saves_word_throws_exception_when_out_of_range(self, mocked_data, instance, buffer_patcher):
        with pytest.raises(ValueError) as info:
            expected_filename = "test_file" + str(datetime.now()) + ".json"
            cipher_mode = "rot47"
            mocked_data.side_effect = [5, expected_filename, cipher_mode, "y"]
            SaveBufferUtils.save_word_from_buffer(instance)
        assert "Out of range!" in str(info.value)


    def test_clear_test_files_dir_after_test(self, mock_path):
        # Removes all files created during this test execution
        for file_name in [file for file in os.listdir(mock_path) if file.endswith(".json") and file.startswith("test_file")]:
            os.remove(mock_path + "/" + file_name)