# import basepage
from basepage import BasePage

def test_po_title(browser):
    main_page = BasePage(browser)
    assert main_page.title() == 'GRIG22 HAPPY STORE'


def test_po_admin_page(browser):
    admin_page = BasePage(browser, "/admin/")
    assert admin_page.find_elem("input-username")
    # browser.get(browser.url + "/admin/")
    # browser.find_element_by_id("input-username")
    # browser.find_element_by_name("password")
    # browser.find_element_by_css_selector("button[type='submit']")
    # browser.find_element_by_link_text("Forgotten Password")
    # browser.find_element_by_xpath("//*[text()='OpenCart']")
    # time.sleep(2)


def test_main_page(browser):
    main_page = BasePage(browser)
    elem_ids = ["logo", "search", "cart", "menu", "content"]
    for elem_id in elem_ids:
        assert main_page.find_elem(elem_id)


def test_catalog_page(browser):
    catalog_page = BasePage(browser, "/index.php?route=product/category&path=20")
    elem_ids = ["product-category", "column-left", "list-view", "input-sort", "content"]
    for elem_id in elem_ids:
        assert catalog_page.find_elem(elem_id)


def test_product_page(browser):
    product_page = BasePage(browser, "/index.php?route=product/product&path=57&product_id=49")
    assert product_page.find_elem("Samsung Galaxy Tab 10.1", method = "link")
    elem_ids = ["content", "tab-description", "input-quantity", "button-cart", "menu"]
    for elem_id in elem_ids:
        assert product_page.find_elem(elem_id)


def test_login_page(browser):
    login_page = BasePage(browser, "/index.php?route=account/login")
    elem_ids = ["input-email", "input-password", "column-right", "content", "menu"]
    for elem_id in elem_ids:
        assert login_page.find_elem(elem_id)
