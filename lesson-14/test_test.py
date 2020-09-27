from basepage import BasePage


def test_po_title(browser):
    main_page = BasePage(browser)
    assert main_page.title() == 'GRIG22 HAPPY STORE'
