from unittest.mock import patch

import pytest
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
