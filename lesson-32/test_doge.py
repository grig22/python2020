from unittest import TestCase
from unittest.mock import patch
import pytest

some_breeds = {
    'message': {'australian': ['shepherd'], 'lhasa': [], 'mastiff': ['bull', 'english', 'tibetan'], 'rottweiler': []},
    'status': 'success'
}

some_sub_breeds = {'message': ['bull', 'english', 'tibetan', 'doge'], 'status': 'success'}


def imga(num):
    return {
        'message': ['https://images.dog.ceo/breeds/dachshund/dachshund-2033796_640.jpg']*num,
        'status': 'success'
    }


class TestImages(TestCase):
    @patch('real_doge.Doge.random_images', side_effect=imga)
    def test_images(self, random_images):
        self.assertEqual(len(random_images(150)["message"]), 150)


@patch('real_doge.Doge')
def test_breeds(lazy_doge):
    doge = lazy_doge()
    doge.all_breeds.return_value = some_breeds
    assert doge.all_breeds() == some_breeds


@pytest.mark.parametrize("name", some_breeds['message'].keys())
def test_sub_breeds(name):
    with patch('real_doge.Doge.sub_breeds', return_value=some_sub_breeds) as mock:
        assert mock(name) == some_sub_breeds
        mock.assert_called_once_with(name)
