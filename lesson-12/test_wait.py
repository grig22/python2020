from selenium.webdriver.common.keys import Keys
from basepage import BasePage


# Добавить проверку логина и разлогина раздела администратора.
def test_po_login_admin(browser):
    admin_page = BasePage(browser, "/admin/")
    assert admin_page.title() == "Administration"
    username = admin_page.find_elem("input-username")
    password = admin_page.find_elem("input-password")
    # логинимся
    username.send_keys("admin")
    password.send_keys("1" + Keys.ENTER)
    # загрузилось
    admin_page.wait_title("Dashboard")
    admin_page.wait_elem(method="link", value="Logout")
    # проверяем что это я
    profile = admin_page.find_elem("user-profile")
    assert profile.get_attribute("alt") == "Benedict Cumberbatch"
    # разлогинимся
    admin_page.find_elem(method="link", value="Logout").click()
    admin_page.wait_title("Administration")


# Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами.
def test_po_product_list(browser):
    product_page = BasePage(browser, "/index.php?route=product/category&path=18")
    product_page.wait_title("Laptops & Notebooks")
    product_page.wait_elem("content")
    product_page.wait_elem(method="link", value="MacBook Pro")