#To optimize basic commands
import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    #method that returns the text await of the element appear
    def get_text_element(self,locator):
        self.wait_element_appear(locator)
        return self.element_find(locator).text


    #method to wait for the element to appear
    def wait_element_appear(self, locator, timeout=60):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(*locator))

