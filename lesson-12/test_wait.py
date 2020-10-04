from selenium.webdriver.common.keys import Keys
from basepage import BasePage
# https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000424900-Very-frustrated-PyCharm-says-local-import-is-unresolved-reference


# Добавить проверку логина и разлогина раздела администратора.
def test_po_login_admin(browser):
    admin_page = BasePage(browser, "/admin/")
    admin_page.wait_title("Administration")
    username = admin_page.find_elem("input-username")
    password = admin_page.find_elem("input-password")
    # логинимся
    username.send_keys("admin")
    password.send_keys("1" + Keys.ENTER)
    # загрузилось
    admin_page.wait_title("Dashboard")
    # logout = admin_page.wait_elem(method="link", value="Logout")
    logout = admin_page.wait_elem(method="css", value=".hidden-xs")
    assert logout.text == "Logout"
    # проверяем что это я
    profile = admin_page.find_elem("user-profile")
    assert profile.get_attribute("alt") == "Benedict Cumberbatch"
    # разлогинимся
    logout.click()
    admin_page.wait_title("Administration")


# Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами.
def test_po_product_list(browser):
    product_page = BasePage(browser, "/index.php?route=product/category&path=18")
    product_page.wait_title("Laptops & Notebooks")
    product_page.wait_elem("content")
    # product_page.wait_elem(method="link", value="MacBook Pro")
    assert product_page.wait_elem(method="css", value="div.product-layout:nth-child(4) > div:nth-child(1) >\
     div:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > a:nth-child(1)").text == "MacBook Pro"
