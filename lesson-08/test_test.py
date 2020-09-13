import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-fullscreen");
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser
    print("finalize driver")
    browser.quit()


def test_title(driver):
    driver.get('http://localhost')
    assert driver.title == 'GRIG22 HAPPY STORE'
