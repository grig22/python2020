from basepage import BasePage
from selenium.webdriver.common.by import By
import allure


class NaotoStore(BasePage):
    ORIGINAL_ART = (By.LINK_TEXT, "Original Art")
    NAVIGATE_NEXT = (By.CLASS_NAME, "nav-next")
    DETAILS = (By.CLASS_NAME, "ProductDetails")
    THUMB_IMAGE = (By.CLASS_NAME, "ProductThumbImage")
    SEARCH_BUTTON = (By.XPATH, '//*[@title="search"]')
    SEARCH_QUERY = (By.ID, "search_query")

    @allure.step("Переходим в раздел")
    def goto_original_art(self):
        self.click(self.ORIGINAL_ART)

    @allure.step("Переходим на следующую страницу")
    def navigate_next(self):
        self.click(self.NAVIGATE_NEXT)

    @allure.step("Выбираем любой продукт")
    def select_random_product(self):
        self.click(self.DETAILS)

    @allure.step("Нажимаем кнопку поиск")
    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    @allure.step("Ищем строку '{1}'")
    def search(self, request):
        self.input_and_submit(self.SEARCH_QUERY, request)

    @allure.step("Кликаем первый попавшийся")
    def click_css(self, text):
        self.click((By.CSS_SELECTOR, text))

    @allure.step("Форма поиска ушла")
    def search_gone(self):
        self.disappear(self.SEARCH_QUERY)
