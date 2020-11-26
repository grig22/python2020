from unittest import TestCase
from unittest.mock import patch

some_breeds = {
    'message': {'australian': ['shepherd'], 'lhasa': [], 'mastiff': ['bull', 'english', 'tibetan'], 'rottweiler': []},
    'status': 'success'
}

def imga(num):
    return {
        'message': ['https://images.dog.ceo/breeds/dachshund/dachshund-2033796_640.jpg']*num,
        'status': 'success'
    }


class TestImages(TestCase):
    @patch('mock_doge.Doge.random_images', side_effect=imga)
    def test_images(self, random_images):
        self.assertEqual(len(random_images(150)["message"]), 150)


@patch('mock_doge.Doge')
def test_breeds(lazy_doge):
    doge = lazy_doge()
    doge.all_breeds.return_value = some_breeds
    assert doge.all_breeds() == some_breeds
