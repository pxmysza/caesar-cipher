import mock
from unittest.mock import patch
from unittest import TestCase
from functionality.manager import Manager
import functionality.manager

class TestManager:

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

