from basepage import BasePage


def test_po_title(browser):
    page = BasePage(browser)
    page.open("http://yandex.ru")
    assert page.title() == "Яндекс"
