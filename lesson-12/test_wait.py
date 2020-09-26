from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# https://www.selenium.dev/documentation/en/webdriver/waits/


# 3.1 Добавить проверку логина и разлогина раздела администратора.
def test_login_admin(browser):
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


# 3.2 Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами.
def test_product_list(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=18")
    wait = WebDriverWait(browser, timeout=3)
    wait.until(EC.title_is("Laptops & Notebooks"))
    wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "MacBook Pro")))
