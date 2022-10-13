import mock
import pytest
import os
import json
from datetime import datetime
from functionality.buffer import Buffer
from functionality.file_utils_handler import FileUtils
import functionality.file_operations

FILENAME = "test_file" + str(datetime.now()) + ".json"

class TestFileUtils:
    # def __init__(self):
    #     self.

    @pytest.fixture
    def instance(self):
        return Buffer()

    @pytest.fixture
    def mock_path(self, mocker):
        return mocker.patch.object(functionality.file_operations, "FILE_PATH",
                                   "/home/pawel/python_projects/caesar-cipher/testing/test_files")

    @mock.patch("builtins.input", create=True)
    def test_saves_text_to_file(self, mocked_input, instance, mock_path):
        text = "temp"
        temp_filename = FILENAME
        # creates and saves non-existing file
        mocked_input.side_effect = ["rot47", "y"]
        FileUtils.save_buffer_to_file(text, temp_filename)

        text = "test_saves_text_to_file"
        # Overwrites existing file
        mocked_input.side_effect = ["y", "rot47", "n", "y"]
        FileUtils.save_buffer_to_file(text, temp_filename)

        assert FILENAME in [file for file in os.listdir(mock_path)]
        with open(mock_path + "/" + FILENAME, mode='r') as f:
            data = json.load(f)
            assert data["text"] == "E6DE0D2G6D0E6IE0E@07:=6"
            assert data["status"] == "encrypted"

    @mock.patch("builtins.input", create=True)
    def test_if_saves_encrypted_and_overrides(self, mocked_input, mock_path):
        text = "test_if_saves_and_overrides"
        mocked_input.side_effect = ["rot47", "n", "y"]
        FileUtils.save_text_and_override(text, FILENAME)
        assert FILENAME in [file for file in os.listdir(mock_path)]
        with open(mock_path + "/" + FILENAME, mode='r') as f:
            data = json.load(f)
            assert data["text"] == "E6DE0:70D2G6D02?50@G6CC:56D"
            assert data["status"] == "encrypted"

    @mock.patch("builtins.input", create=True)
    def test_if_saves_decrypted_and_overrides(self, mocked_input, mock_path):
        text = "test_if_saves_and_overrides"
        mocked_input.side_effect = ["rot47", "n", "n"]
        FileUtils.save_text_and_override(text, FILENAME)
        assert FILENAME in [file for file in os.listdir(mock_path)]
        with open(mock_path + "/" + FILENAME, mode='r') as f:
            data = json.load(f)
            assert data["text"] == "test_if_saves_and_overrides"
            assert data["status"] == "decrypted"

    @mock.patch("builtins.input", create=True)
    def test_if_saves_encrypted_and_append(self, mocked_input, mock_path):
        temp_text = "temp"
        temp_filename = "test_file" + str(datetime.now()) + ".json"
        # creates and saves non-existing file
        mocked_input.side_effect = ["rot47", "y"]
        FileUtils.save_buffer_to_file(temp_text, temp_filename)
        text = "test_if_saves_encrypted_and_append"
        FileUtils.save_text_and_append(text, temp_filename)
        with open(mock_path + "/" + temp_filename, mode='r') as f:
            data = json.load(f)
            assert data["text"] == "E6>AE6DE0:70D2G6D06?4CJAE6502?502AA6?5"
            assert data["status"] == "encrypted"

    @mock.patch("builtins.input", create=True)
    def test_if_saves_decrypted_and_append(self, mocked_input, mock_path):
        temp_text = "temp"
        temp_filename = "test_file" + str(datetime.now()) + ".json"
        # creates and saves non-existing file
        mocked_input.side_effect = ["rot47", "n"]
        FileUtils.save_buffer_to_file(temp_text, temp_filename)
        text = "test_if_saves_decrypted_and_append"
        FileUtils.save_text_and_append(text, temp_filename)
        with open(mock_path + "/" + temp_filename, mode='r') as f:
            data = json.load(f)
            assert data["text"] == "temptest_if_saves_decrypted_and_append"
            assert data["status"] == "decrypted"

    def test_clear_test_files_dir_after_test(self, mock_path):
        # Removes all files created during this test execution
        for file_name in [file for file in os.listdir(mock_path) if file.endswith(".json") and file.startswith("test_file")]:
            os.remove(mock_path + "/" + file_name)