import pytest


class TestCheckSet:
    def test_check_intersection(self):
        some_set = {1, 2, 3, 4}
        some_set_2 = {1, 8, 6, 4}
        assert some_set & some_set_2 == {1, 4}

    def test_add_set(self):
        some_set = {'a', 'c', 'b'}
        some_set_2 = {1, 2, 3, 'a'}
        assert some_set | some_set_2 == {'a', 'b', 'c', 1, 2, 3}

    def test_add_existing_element(self):
        some_set = {1, 2, 3, 4}
        some_set.add(4)
        assert len(some_set) == 4

    def test_remove_element(self):
        some_set = {1, 2, 3, 4}
        some_set.remove(4)
        assert some_set == {1, 2, 3}

    @pytest.mark.parametrize('param', [{1, 2, 3}, {'a', 'b', 'c'}])
    def test_check_parametrization(self, param):
        assert type(param) == set
