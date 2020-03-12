import pytest


class TestCheckInt:

    def test_check_type(self):
        num = 5
        assert type(num) == int

    def test_check_invalid_conversion(self):
        some_string = 'hello'
        with pytest.raises(ValueError):
            assert int(some_string)

    def test_check_valid_conversion(self):
        some_string = '1'
        num = int(some_string)
        assert num == 1

    @pytest.mark.parametrize('param', [0, 1, 100, 1000])
    def test_check_parametrization(self, param):
        num = 1 ** param
        assert num == 1

    def test_check_division(self):
        num = 10 / 5
        assert type(num) != int
