from selenium.webdriver.common.keys import Keys
from basepage import BasePage


# Добавить проверку логина и разлогина раздела администратора.
def test_login_admin(browser):
    admin_page = BasePage(browser, "/admin/")
    assert admin_page.title() == "Administration"
    username = admin_page.find_elem("input-username")
    password = admin_page.find_elem("input-password")
    # логинимся
    username.send_keys("admin")
    password.send_keys("1" + Keys.ENTER)
    # загрузилось
    # wait = WebDriverWait(browser, timeout=3)
    admin_page.wait_title("Dashboard")
    # wait.until(EC.title_is("Dashboard"))
    admin_page.wait_elem(method="link", value="Logout")
    # wait.until(lambda bro: bro.find_element_by_link_text("Logout"))
    # проверяем что это я
    profile = admin_page.find_elem("user-profile")
    # profile = browser.find_element_by_id("user-profile")
    assert profile.get_attribute("alt") == "Benedict Cumberbatch"
    # разлогинимся
    admin_page.find_elem(method="link", value="Logout").click()
    # browser.find_element_by_link_text("Logout").click()
    admin_page.wait_title("Administration")
    # wait.until(EC.title_is("Administration"))


# 3.2 Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами.
def test_product_list(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=18")
    wait = WebDriverWait(browser, timeout=3)
    wait.until(EC.title_is("Laptops & Notebooks"))
    wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "MacBook Pro")))
