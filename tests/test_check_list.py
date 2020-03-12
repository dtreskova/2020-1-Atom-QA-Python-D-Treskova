import pytest


class TestCheckList:

    def test_check_empty_list(self):
        some_list = []
        assert type(some_list) == list

    def test_check_append(self):
        some_list = list()
        some_list.append("hello")
        assert "hello" in some_list

    def test_remove_element(self):
        some_list = [1, 2, 3, 4, 5]
        some_list.remove(5)
        assert 5 not in some_list

    @pytest.mark.parametrize('param', list(range(5)))
    def test_check_parametrization(self, param):
        a = [1, 9, 3, 4, 5, 6, 7]
        a.insert(param, 2)
        assert a[param] == 2

    def test_reverse_list(self):
        some_list = [1, 2, 3, 4]
        some_list.reverse()
        assert some_list == [4, 3, 2, 1]
