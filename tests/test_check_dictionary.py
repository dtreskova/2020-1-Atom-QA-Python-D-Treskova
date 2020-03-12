import pytest


@pytest.fixture()
def dictionary_fixture():
    rating = {1: 'poor', 2: 'good', 3: 'excellent'}
    return rating


class TestCheckDictionary:

    @pytest.mark.smoke
    def test_check_type_empty_dictionary(self):
        empty_dict = {}
        assert type(empty_dict) == dict

    @pytest.mark.smoke
    def test_check_length_empty_dictionary(self):
        empty_dict = dict()
        assert len(empty_dict) == 0

    @pytest.mark.regress
    def test_copy_dict(self, dictionary_fixture):
        some_dict = dictionary_fixture
        copy_some_dict = some_dict.copy()
        assert some_dict == copy_some_dict

    @pytest.mark.regress
    def test_check_accessory(self, dictionary_fixture):
        some_dict = dictionary_fixture
        assert 'good' in some_dict.values()

    @pytest.mark.regress
    @pytest.mark.parametrize('param', [{}, {1: 'one', 2: 'two', 3: 'three'}, dict(),
                                       dict(short='dict', long='dictionary')])
    def test_check_parametrization(self, param):
        some_dict = param
        some_dict.clear()
        assert len(some_dict) == 0
