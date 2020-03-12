import pytest


class TestCheckString:

    def test_add_string(self):
        some_string = 'Hello'
        some_string += ' world'
        assert some_string == 'Hello world'

    def test_multiplication_string(self):
        some_string = 'friend' * 5
        assert len(some_string) == 30
        assert some_string.count('friend') == 5

    def test_check_slices(self):
        some_string = 'Hello'
        some_string_2 = some_string[2:-2]
        assert some_string_2 == 'l'

    def test_check_valid_error(self):
        some_string = 'hello'
        with pytest.raises(TypeError):
            some_string[1] = 'h'

    @pytest.mark.parametrize('param', ['string', "string"])
    def test_check_parametrization(self, param):
        assert type(param) == str
        assert param == 'string'
