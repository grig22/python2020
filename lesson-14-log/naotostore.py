from basepage import BasePage
from selenium.webdriver.common.by import By


class NaotoStore(BasePage):
    ORIGINAL_ART = (By.LINK_TEXT, "Original Art")
    NAVIGATE_NEXT = (By.CLASS_NAME, "nav-next")

    def goto_original_art(self):
        self.click(self.ORIGINAL_ART)

    def navigate_next(self):
        self.click(self.NAVIGATE_NEXT)
