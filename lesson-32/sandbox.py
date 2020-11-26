from unittest.mock import patch, Mock
from mock_doge import Doge


@patch('mock_doge.Doge')
def mock_breeds(lazy_doge):
    doge = lazy_doge()
    doge.all_breeds.return_value = {
        'message': {
            'australian': ['shepherd'],
            'labrador': [],
            'lhasa': [],
            'mastiff': ['bull', 'english', 'tibetan'],
            'rottweiler': [],
        },
        'status': 'success'
    }
    resp = doge.all_breeds()
    print(resp)


mock_breeds()
