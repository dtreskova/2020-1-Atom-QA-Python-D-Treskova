import pytest


class TestsCheckList:

    def test_check_empty_list(self):
        some_list = []
        assert type(some_list) == list
        assert len(some_list) == 0

    def test_check_append(self):
        some_list = list()
        some_list.append("hello")
        assert some_list.__contains__("hello")

    def test_remove_element(self):
        some_list = [1, 2, 3, 4, 5]
        some_list.remove(5)
        assert not some_list.__contains__(5)

    @pytest.mark.parametrize('param', list(range(5)))
    def test_check_parametrization(self, param):
        a = [1, 2, 3, 4, 5, 6, 7]
        b = a[:]
        b.insert(b[param], 2)
        assert b[param + 1] == 2
        assert len(a) == len(b) - 1

    def test_reverse_list(self):
        some_list = [1, 2, 3, 4]
        some_list.reverse()
        assert some_list == [4, 3, 2, 1]
