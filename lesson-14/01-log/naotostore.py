from basepage import BasePage
from selenium.webdriver.common.by import By


class NaotoStore(BasePage):
    ORIGINAL_ART = (By.LINK_TEXT, "Original Art")
    NAVIGATE_NEXT = (By.CLASS_NAME, "nav-next")
    DETAILS = (By.CLASS_NAME, "ProductDetails")
    THUMB_IMAGE = (By.CLASS_NAME, "ProductThumbImage")
    SEARCH_BUTTON = (By.XPATH, '//*[@title="search"]')
    SEARCH_QUERY = (By.ID, "search_query")

    def goto_original_art(self):
        self.click(self.ORIGINAL_ART)

    def navigate_next(self):
        self.click(self.NAVIGATE_NEXT)

    def select_random_product(self):
        self.click(self.DETAILS)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def search(self, request):
        self.input_and_submit(self.SEARCH_QUERY, request)

    def click_link(self, text):
        self.click((By.PARTIAL_LINK_TEXT, text))

    def search_gone(self):
        self.disappear(self.SEARCH_QUERY)
