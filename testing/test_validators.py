import pytest

from functionality.validators import Validator


class TestValidator:
    def test_if_validates_if_element_exists(self):
        expected = 2
        actual = Validator.validate_if_elem_exists(2, 4)
        assert actual == expected

    @pytest.mark.buffer_el_validator
    @pytest.mark.parametrize("test_params", [(["2", 4], [2, "4"])])
    def test_if_string_arguments_throw_error(self, test_params):
        for par in test_params:
            with pytest.raises(TypeError):
                Validator.validate_if_elem_exists(par[0], par[1])

    @pytest.mark.buffer_el_validator
    def test_if_throws_error_when_buffer_elem_not_exist(self):
        with pytest.raises(ValueError):
            Validator.validate_if_elem_exists(4, 2)

    @pytest.mark.cipher_mode_validator
    @pytest.mark.parametrize("test_params", [(["rot12", "rot48", 4])])
    def test_if_throws_error_when_incorrect_cipher(self, test_params):
        for par in test_params:
            with pytest.raises(ValueError):
                Validator.validate_type(par)

    @pytest.mark.cipher_mode_validator
    @pytest.mark.parametrize("test_params", [(["rot13", "rot47"])])
    def test_if_returns_correct_value(self, test_params):
        for par in test_params:
            assert par == Validator.validate_type(par)


    @pytest.mark.should_save_validator
    @pytest.mark.parametrize("test_params", [(["sage", "discarp", 123])])
    def test_if_should_save_validator_throws_exception_when_incorrect_argument(self, test_params):
        for par in test_params:
            with pytest.raises(ValueError):
                Validator.validate_should_save(par)

    @pytest.mark.should_save_validator
    @pytest.mark.parametrize("test_params", [(["save", "discard"])])
    def test_if_should_save_returns_valid_values_for_correct_argument(self, test_params):
        for par in test_params:
            assert par == Validator.validate_should_save(par)


    @pytest.mark.validate_should_encrypt_prompt
    @pytest.mark.parametrize("test_params", [(["yes", "sd", 234])])
    def test_validate_encryption_throws_error_when_incorrect_argument(self, test_params):
        for par in test_params:
            with pytest.raises(TypeError):
                Validator.validate_encryption(par)

    @pytest.mark.validate_should_encrypt_prompt
    def test_validate_should_encrypt_returns_same_value_as_argument(self):
        assert "encrypted" == Validator.validate_encryption("y")
        assert "decrypted" == Validator.validate_encryption("n")

    @pytest.mark.validate_choice
    @pytest.mark.parametrize("test_params", [(["yes", "sd", 234])])
    def test_validate_choice_throws_error_when_incorrect_argument(self, test_params):
        for par in test_params:
            with pytest.raises(TypeError):
                Validator.validate_choice(par)

    @pytest.mark.validate_choice
    def test_validate_choice_returns_same_value_as_argument(self):
        assert "y" == Validator.validate_choice("y")
        assert "n" == Validator.validate_choice("n")



