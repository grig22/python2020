class BasePage:

    def __init__(self, driver, url = ""):
        self.driver = driver
        self.driver.get(self.driver.url + "/" + url)



    def find_elem(self, value, method = "id"):
        if method == "id":
            return self.driver.find_element_by_id(value)
        elif method == "link":
            return self.driver.find_element_by_link_text(value)
        else:
            return None

    def title(self):
        return self.driver.title
