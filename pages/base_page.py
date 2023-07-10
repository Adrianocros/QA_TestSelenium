#To optimize basic commands
import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def element_find(self, locator):
        return self.driver.find_element(*locator)

    def elements_find(self,locator):
        return self.driver.find_elements()

    def to_write(self, locator, text):
        self.element_find(locator).send_keys(text)

    def click(self, locator):
        self.element_find(locator).click()


    def check_element_exists(self,locator):
        assert self.element_find(locator).is_displayed(), f"Element '{locator}' not found on canvas."

    #method that returns the text of the element
    def get_text_element(self,locator):
        return self.element_find(locator).text
