import datetime

import pytest
import mock
import os
from functionality.file_operations import FileHandler
import functionality.file_operations

class TestFileHandler:

    @pytest.fixture
    def mock_path(self, mocker):
        return mocker.patch.object(functionality.file_operations, 'JSON_PATH',
                                   "/home/pawel/python_projects/caesar-cipher/testing/test_files")

    def gen_filename(self):
        return "test_file_handler" + str(datetime.datetime.now()) + ".json"

    def test_if_reads_file_content_and_returns_json(self, mock_path):
        expected = {
            "cipher_type": "rot47",
            "text": "D57D52D57E6DE",
            "status": "encrypted"
        }
        actual = FileHandler.read_file_content("test.json")
        assert expected == actual

    def test_if_incorrect_path_throws_error(self, mocker):
        mocker.patch.object(functionality.file_operations, 'JSON_PATH', "/home/pawel/python_projects/path/that/doesnt/exists")
        expected = {
            "cipher_type": "rot47",
            "text": "D57D52D57E6DE",
            "status": "encrypted"
        }
        with pytest.raises(FileNotFoundError):
            FileHandler.read_file_content("test.json")

    def test_if_saves_to_file(self, mock_path):
        filename = self.gen_filename()
        json_obj = {
            "cipher_type": "rot47",
            "text": "D57D52D57E6DE",
            "status": "encrypted"
        }
        FileHandler.save_to_file(filename, json_obj)
        assert filename in [file for file in os.listdir(mock_path)]

    def test_if_correctly_checks_if_file_exists(self, mock_path):
        filename = self.gen_filename()
        json_obj = {
            "cipher_type": "rot47",
            "text": "D57D52D57E6DE",
            "status": "encrypted"
        }

        FileHandler.save_to_file(filename, json_obj)
        assert FileHandler.file_exists(filename)

    def test_if_correctly_displays_decrypted_file_content(self, mocker):
        json_obj = {
            "cipher_type": "rot47",
            "text": "ala ma kota",
            "status": "decrypted"
        }
        expected = "ala ma kota"
        mocker.patch("functionality.file_operations.FileHandler.read_file_content", return_value=json_obj)
        actual = FileHandler.decrypt_file_content("dummy_file.json")
        assert expected == actual

    @pytest.mark.parametrize("objects", [({
            "cipher_type": "rot47",
            "text": "2=2 >2 <@E2",
            "status": "encrypted"
        },{
            "cipher_type": "rot13",
            "text": "nyn zn xbgn",
            "status": "encrypted"
        })])
    def test_if_correctly_decrypts_file_content(self, mocker, objects):
        expected = "ala ma kota"
        print(len(objects))
        for obj in objects:
            mocker.patch("functionality.file_operations.FileHandler.read_file_content", return_value=obj)
            actual = FileHandler.decrypt_file_content("dummy_file.json")
            assert expected == actual

    def test_clear_test_files_dir_after_test(self, mock_path):
        # Removes all files created during this test execution
        for file_name in [file for file in os.listdir(mock_path) if file.endswith(".json") and file.startswith("test_file")]:
            os.remove(mock_path + "/" + file_name)