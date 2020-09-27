from naotostore import NaotoStore


def test_naoto_store(browser):
    store = NaotoStore(browser)
    store.open("https://www.naotohattori.com/")
    assert store.title() == "Naoto Hattori Online Store"
    store.goto_original_art()
    assert "Original Art" in store.title()
    assert "Page 1" in store.title()
    store.navigate_next()
    assert "Page 2" in store.title()
