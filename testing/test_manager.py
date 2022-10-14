import mock
import pytest
from unittest.mock import patch


import functionality.manager
import functionality.file_operations
from functionality.manager import Manager
from functionality.buffer import Buffer

class TestManager:

    @pytest.fixture
    def instance(self):
        return Buffer()

    @pytest.fixture
    def buffer_patcher(self, mocker):
        mocker.patch("functionality.buffer.Buffer.buffer", ["element"])

    @pytest.fixture
    def mock_path(self, mocker):
        return mocker.patch.object(functionality.file_operations, 'FILE_PATH',
                                   "/home/pawel/python_projects/caesar-cipher/testing/test_files")

    @mock.patch("builtins.input", create=True)
    def test_add_to_buffer(self, mocked_input):
        mocked_input.side_effect = ["test entry"]
        expected = "test entry"
        m = Manager()
        # Accessing private method
        m._Manager__add_to_buffer()
        assert m.buffer.is_empty() == True
        assert m.buffer.take_word_from_buffer(0) == expected

    def test_save_when_buffer_is_empty(self, capsys):
        expected = "Buffer is empty\n"
        m = Manager()
        m._Manager__save()
        captured = capsys.readouterr()
        assert captured.out == expected

    @mock.patch("builtins.input", create=True)
    def test_if_saves_all(self, mocked_input):
        # with patch.object(functionality.file_utils.SaveBufferUtils, "save_whole_buffer") as mock_method:
        with patch.object(functionality.manager.SaveBufferUtils, "save_whole_buffer") as mock_method:
            mocked_input.side_effect = ["all"]
            m = Manager()
            m.buffer.add_to_buffer("test")
            m._Manager__save()
            mock_method.assert_called()

    @mock.patch("builtins.input", create=True)
    def test_if_saves_word_only(self, mocked_input, capsys):
        with patch.object(functionality.manager.SaveBufferUtils, "save_word_from_buffer") as mock_method:
            mocked_input.side_effect = ["word"]
            m = Manager()
            m._Manager__save()
            out, err = capsys.readouterr()
            m.buffer.add_to_buffer("raz")
            m.buffer.add_to_buffer("dwa")
            m._Manager__save()
            mock_method.assert_called()
            assert out == "Buffer is empty\n"

    @mock.patch("builtins.input", create=True)
    def test_if_save_handles_incorrect_choice(self, mocked_input, capsys):
        mocked_input.side_effect = ["words"]
        m = Manager()
        m.buffer.add_to_buffer("test")
        m._Manager__save()
        out, err = capsys.readouterr()
        assert out == "Incorrect choice!\n"

    @mock.patch("builtins.input", create=True)
    @mock.patch.object(functionality.manager.FileHandler, "display_all_files")
    @mock.patch.object(functionality.manager.FileHandler, "file_exists")
    def test_display_file_content(self, mock_exists, mock_display, mocked_input, mock_path, capsys):
        mock_exists.return_value = True
        mock_display.return_value = None
        mocked_input.side_effect = ["test.json"]
        m = Manager()
        m._Manager__display_file_content()
        out1, err1 = capsys.readouterr()
        assert str(out1) == "Cipher type: rot47, text: D57D52D57E6DE, status: encrypted\n"

    @mock.patch("builtins.input", create=True)
    @mock.patch.object(functionality.manager.FileHandler, "display_all_files")
    @mock.patch.object(functionality.manager.FileHandler, "file_exists")
    def test_display_file_content_when_filename_incorrect(self, mock_exists, mock_display, mock_path, capsys):
        mock_exists.return_value = False
        mock_display.return_value = None
        m = Manager()
        m._Manager__display_file_content()
        out1, err1 = capsys.readouterr()
        assert str(out1) == "Could not display file content. Incorrect name?\n"

    @mock.patch("builtins.input", create=True)
    def test_read_file_to_buffer(self, mock_input, mock_path):
        mock_input.side_effect = ["test.json"]
        m = Manager()
        elements_before = m.buffer.get_elements_num()
        m._Manager__read_file_to_buffer()
        elements_after = m.buffer.get_elements_num()
        assert m.buffer.convert_buffer_to_text() == "D57D52D57E6DE"
        assert elements_before == 0
        assert elements_after == 1

    @mock.patch("builtins.input", create=True)
    @mock.patch.object(functionality.manager.FileHandler, "display_all_files")
    def test_read_file_to_buffer_when_filename_incorrect(self, mock_display_all, mock_input, mock_path, capsys):
        mock_display_all.return_value = None
        m = Manager()
        mock_input.side_effect = ["random.json"]
        m._Manager__read_file_to_buffer()
        out, err = capsys.readouterr()
        assert out == "Could not read file content. Incorrect name?\n"

    @mock.patch("builtins.input", create=True)
    @mock.patch.object(functionality.manager.FileHandler, "display_all_files")
    def test_if_displays_encrypted_content(self, mock_display_all, mock_input, mock_path, capsys):
        mock_display_all.return_value = None
        mock_input.side_effect = ["test.json"]
        m = Manager()
        m._Manager__display_decrypted_file_content()
        out, err = capsys.readouterr()
        expected = "Decrypted text: sdfsdasdftest\n"
        assert out == expected

    @mock.patch("builtins.input", create=True)
    @mock.patch.object(functionality.manager.FileHandler, "display_all_files")
    def test_displays_encrypted_content_when_filename_incorrect(self, mock_display_all, mock_input, mock_path, capsys):
        mock_display_all.return_value = None
        mock_input.side_effect = ["nonexistentfile.json"]
        m = Manager()
        m._Manager__display_decrypted_file_content()
        out, err = capsys.readouterr()
        expected = "Could not read file content. Incorrect name?\n"
        assert out == expected


    @mock.patch("builtins.input", create=True)
    def test_decrypts_buffer_content(self, mock_input, capsys):
        mock_input.side_effect = [1, "rot47"]
        m = Manager()
        m.buffer.add_to_buffer("ala ma kota a kot ma ale")
        m._Manager__display_encrypted_buffer()
        out = capsys.readouterr()
        # This should not be done this way but I dont know how to capture specific stdout, there are 3 in tested method
        assert "Original text: ala ma kota a kot ma ale\nAfter cipher operation: 2=2 >2 <@E2 2 <@E >2 2=6\n" in out.out