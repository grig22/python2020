import pytest
from selenium import webdriver
import logging
import sys

# https://docs.python.org/3/library/logging.html
# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
# noinspection PyArgumentList
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug22.log"),
        logging.StreamHandler()
        # logging.StreamHandler(sys.stdout)
    ]
)


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost/")


@pytest.fixture(scope='session')
def browser(request):
    logging.warning('!!!! START LESSON 14 !!!!')
    logging.info('Useful message')
    logging.error('Something bad happened')
    desired = request.config.getoption("--browser")
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
