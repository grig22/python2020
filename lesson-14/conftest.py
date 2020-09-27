import pytest
from selenium import webdriver
import logging
# import sys

# https://docs.python.org/3/library/logging.html
# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
# noinspection PyArgumentList
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s %(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug22.log"),
        logging.StreamHandler()
        # logging.StreamHandler(sys.stdout)
    ]
)


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope='session')
def browser(request):
    test_name = request.node.name
    logger = logging.getLogger("browser_fixture")
    logger.info(f"Started test {test_name}")
    desired = request.config.getoption("--browser")

    if desired == "chrome":
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/chromium"
        driver = webdriver.Chrome(options=options)
    elif desired == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = None
        assert not f"BROWSER {desired} NOT SUPPORTED SORRY"

    def fin():
        driver.quit()
        logger.info(f"Closed browser '{driver.name}'")
        logger.info(f"Finished test {test_name}")

    request.addfinalizer(fin)
    logger.info(f"Opened browser '{driver.name}'")
    driver.maximize_window()
    return driver
