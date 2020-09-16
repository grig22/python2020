import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost/")


@pytest.fixture(scope='session')
def browser(request):
    desired = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if desired == "chrome":
        driver = webdriver.Chrome()
    elif desired == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = None
        assert not f"BROWSER {desired} NOT SUPPORTED SORRY"
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.get(url)
    driver.url = url
    return driver
