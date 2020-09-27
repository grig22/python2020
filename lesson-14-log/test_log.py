from naotostore import NaotoStore
import time


def test_random_product(browser):
    store = NaotoStore(browser)
    store.open("https://www.naotohattori.com/")
    assert store.title() == "Naoto Hattori Online Store"
    store.goto_original_art()
    assert "Original Art" in store.title()
    assert "Page 1" in store.title()
    store.navigate_next()
    assert "Page 2" in store.title()
    store.select_random_product()
    assert "Original Artwork" in store.title()
    store.is_present(store.THUMB_IMAGE)
    store.logger.info("Look at that beauty")
    time.sleep(2)
