# обязательно должно быть в файле conftest.py


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/",
        help="request url"
    )

    parser.addoption(
        "--status_code",
        default="200",
        help="expected status code"
    )
