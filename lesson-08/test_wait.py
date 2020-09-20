import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 3.1
def test_login_admin(browser):
    # https://www.selenium.dev/documentation/en/webdriver/waits/
    browser.get(browser.url + "/admin/")
    assert browser.title == "Administration"
    username = browser.find_element_by_id("input-username")
    password = browser.find_element_by_id("input-password")
    # логинимся
    username.send_keys("admin")
    password.send_keys("1" + Keys.ENTER)
    # загрузилось
    wait = WebDriverWait(browser, timeout=3)
    wait.until(EC.title_is("Dashboard"))
    wait.until(lambda bro: bro.find_element_by_link_text("Logout"))
    # проверяем что это я
    profile = browser.find_element_by_id("user-profile")
    assert profile.get_attribute("alt") == "Benedict Cumberbatch"
    assert profile.get_property("alt") == "Benedict Cumberbatch"
    # разлогинимся
    browser.find_element_by_link_text("Logout").click()
    wait.until(EC.title_is("Administration"))
