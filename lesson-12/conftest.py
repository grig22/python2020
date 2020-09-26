import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost/")


@pytest.fixture(scope='session')
def browser(request):
    desired = request.config.getoption("--browser")
    # 1.2
    url = request.config.getoption("--url")
    if desired == "chrome":
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/chromium"
        driver = webdriver.Chrome(options=options)
    elif desired == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = None
        assert not f"BROWSER {desired} NOT SUPPORTED SORRY"
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.url = url
    return driver
