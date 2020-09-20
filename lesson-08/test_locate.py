import time


# 1.3
def test_title(browser):
    assert browser.title == 'GRIG22 HAPPY STORE'
    time.sleep(2)


# 2.5 Страницу логина в админку /admin/
# https://github.com/konflic/pyhton_qa_element_search/blob/master/tests/test_find_element_by.py
# https://selenium-python.com/locating-web-elements
# https://www.selenium.dev/documentation/en/getting_started_with_webdriver/locating_elements/
def test_admin_page(browser):
    browser.get(browser.url + "/admin/")
    browser.find_element_by_id("input-username")
    browser.find_element_by_name("password")
    browser.find_element_by_css_selector("button[type='submit']")
    browser.find_element_by_link_text("Forgotten Password")
    browser.find_element_by_xpath("//*[text()='OpenCart']")
    time.sleep(2)


# 2.1 Главную /
def test_main_page(browser):
    elem_ids = ["logo", "search", "cart", "menu", "content"]
    for elem_id in elem_ids:
        browser.find_element_by_id(elem_id)
    time.sleep(2)


# 2.2 Каталог /index.php?route=product/category&path=20


# 2.3 Карточку товара /index.php?route=product/product&path=57&product_id=49

# 2.4 Страницу логина /index.php?route=account/login