import pytest


class TestGet:
    di = {'one': 1, 'two': 2, 'three': 3}

# 1
    def test_get_1(self):
        assert self.di.get('two') == 2

# 2
    def test_get_2(self):
        assert self.di.get('million') is None

# 3
    def test_get_3(self):
        assert self.di.get('zero', 'foam') == 'foam'


class TestKeysValues:
    di = {'mine': 'sun', 'your': 'gold', 'their': 'amber'}

# 4
    def test_keys_1(self):
        assert self.di.keys() == {'mine', 'your', 'their'}

# 5
    def test_values_1(self):
        assert 'gold' in self.di.values()

# 6
    def test_values_2(self):
        assert 'dirt' not in self.di.values()


@pytest.fixture(params=['ssh', 'ssl', 'pgp', 'gpg'])
def crypto(request):
    return request.param


# 7
def test_pop(crypto):
    di = {'ssh': 1, 'ssl': 0, 'pgp': 1, 'gpg': 0}
    assert di.pop(crypto) in [0, 1]
