import pytest
import requests


@pytest.fixture
def options(request):
    url = request.config.getoption("--url")
    status = request.config.getoption("--status_code")
    return url, status


def test_url_code(options):
    url = options[0]
    status = int(options[1])
    response = requests.get(url)
    assert response.status_code == status
