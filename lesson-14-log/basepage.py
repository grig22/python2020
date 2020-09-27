from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        self.wait = WebDriverWait(self.driver, timeout=3)

    def open(self, url):
        self.logger.info(f"Opening url '{url}'")
        self.driver.get(url)

    def title(self):
        title = self.driver.title
        self.logger.info(f"Title is '{title}'")
        return title

    def click(self, locator):
        self.logger.info(f"Clicking element '{locator}'")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    # def find_elem(self, value, method="id"):
    #     if method == "id":
    #         return self.driver.find_element_by_id(value)
    #     elif method == "link":
    #         return self.driver.find_element_by_link_text(value)
    #     else:
    #         raise ValueError(f'unsupported method "{method}"')

    # def wait_title(self, title):
    #     self.wait.until(EC.title_is(title))

    # def wait_elem(self, value, method="id"):
    #     """If the condition fails, e.g. a truthful return value from the condition is never reached,
    #      the wait will throw/raise an error/exception called a timeout error."""
    #     if method == "id":
    #         locator = By.ID
    #     elif method == "link":
    #         locator = By.LINK_TEXT
    #     else:
    #         raise ValueError(f'unsupported method "{method}"')
    #     return self.wait.until(EC.visibility_of_element_located((locator, value)))
