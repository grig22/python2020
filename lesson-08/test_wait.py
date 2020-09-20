import time
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 3.1
def test_login_admin(browser):
    # https://www.selenium.dev/documentation/en/webdriver/waits/
    browser.get(browser.url + "/admin/")
    username = browser.find_element_by_id("input-username")
    password = browser.find_element_by_id("input-password")
    username.send_keys("admin")
    password.send_keys("1" + Keys.ENTER)
    assert browser.title == "Dashboard"
    WebDriverWait(browser, timeout=3).until(lambda bro: bro.find_element_by_link_text("Logout"))




