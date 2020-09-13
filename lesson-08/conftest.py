import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://localhost/")


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("start-fullscreen");
        # options.headless = False
        driver = webdriver.Chrome(options=options)
    else:
        driver = None
        assert "ONLY CHROME SUPPORTED SORRY" == driver
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.get(url)
    driver.url = url
    return driver
