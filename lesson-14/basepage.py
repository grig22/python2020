from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
import allure


class BasePage:

    @allure.step
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        self.wait = WebDriverWait(self.driver, timeout=3)

    @allure.step("Открываем URL {1}")
    def open(self, url):
        self.logger.info(f"Opening url '{url}'")
        self.driver.get(url)

    def title(self):
        title = self.driver.title
        self.logger.info(f"Title is '{title}'")
        return title

    @allure.step("Кликаем элемент {1}")
    def click(self, locator):
        self.logger.info(f"Clicking element '{locator}'")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.step("Вводим значение {2} в элемент {1}")
    def input_and_submit(self, locator, value):
        self.logger.info(f"Input '{value}' in field '{locator}'")
        # find_field = self.driver.find_element(locator)
        find_field = self.wait.until(EC.visibility_of_element_located(locator))
        find_field.send_keys(value)
        find_field.send_keys(Keys.ENTER)

    @allure.step("Ищем элемент {1}")
    def is_present(self, locator):
        self.logger.info(f"Check if element visible '{locator}'")
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Элемент ушёл {1}")
    def disappear(self, locator):
        self.logger.info(f"Check if element invisible '{locator}'")
        element = self.wait.until(EC.invisibility_of_element_located(locator))