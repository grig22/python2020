from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, url=""):
        self.driver = driver
        self.webdr_wait = WebDriverWait(self.driver, timeout=3)
        self.driver.get(self.driver.url + "/" + url)

    def find_elem(self, value, method="id"):
        if method == "id":
            return self.driver.find_element_by_id(value)
        elif method == "link":
            return self.driver.find_element_by_link_text(value)
        else:
            raise ValueError(f'unsupported method "{method}"')

    def title(self):
        return self.driver.title

    def wait_title(self, title):
        self.webdr_wait.until(EC.title_is(title))

    def wait_elem(self, value, method="id"):
        """If the condition fails, e.g. a truthful return value from the condition is never reached,
         the wait will throw/raise an error/exception called a timeout error."""
        if method == "id":
            locator = By.ID
        elif method == "link":
            locator = By.LINK_TEXT
        else:
            raise ValueError(f'unsupported method "{method}"')
        self.webdr_wait.until(EC.visibility_of_element_located((locator, value)))
