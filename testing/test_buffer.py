from unittest.mock import patch

import pytest

import functionality.file_utils_handler
from functionality.buffer import Buffer
from unittest import mock

class TestBuffer:

    @pytest.fixture
    def instance(self):
        return Buffer()

    @pytest.fixture
    def buffer_patcher(self, mocker):
        mocker.patch("functionality.buffer.Buffer.buffer", ["dwa", "elementy"])


    def test_if_returns_number_of_elements(self, instance, buffer_patcher):
        expected = 2
        assert instance.get_elements_num() == expected

    def test_if_converts_to_text(self, instance, buffer_patcher):
        expected = " ".join(["dwa", "elementy"])
        assert instance.convert_buffer_to_text() == expected

    def test_if_adds_new_element_to_buffer(self, instance, buffer_patcher):
        expected_before = 2
        expected_after = 3
        before = instance.get_elements_num()
        instance.add_to_buffer("trzy")
        after = instance.get_elements_num()
        assert before == expected_before
        assert expected_after == expected_after

    def test_if_correctly_displays_buffer(self, instance):
        expected_before = "Buffer is empty"
        expected_after = "1: test"
        assert instance.display_buffer() == expected_before
        instance.add_to_buffer("test")
        assert instance.display_buffer() == expected_after

    def test_if_clears_buffer(self, instance, buffer_patcher):
        expected = 0
        instance.clear_buffer()
        assert instance.get_elements_num() == expected

    def test_if_returns_zero_if_buffer_empty(self, instance, buffer_patcher):
        expected = 0
        instance.clear_buffer()
        actual = instance.is_empty()
        assert expected == actual

    def test_if_gets_word_from_buffer_by_its_position(self, instance, buffer_patcher):
        expected = "dwa"
        actual = instance.take_word_from_buffer(0)
        assert expected == actual