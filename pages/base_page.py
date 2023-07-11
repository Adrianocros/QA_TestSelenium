#To optimize basic commands
import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

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

    #method to check whether the element exists or not
    def check_element_exists(self,locator):
        assert self.element_find(locator), f"Element '{locator}' does not exist but is expected to exist!"

    def check_element_not_exists(self,locator):
        assert len(self.elements_find(locator)) == 0, f"Element '{locator}' exist  but is not expected to exist! "

    #Double click and right click
    def click_double(self, locator):
        element = self.wait_element_appear(locator)
        ActionChains(self.driver).double_click().perform()

    def click_right(self,locator):
        element = self.wait_element_appear(locator)
        ActionChains(self.driver).context_click(element).perform()

    #Press keyboard key (Enter, Space, Arrows, F1, F2, etc...)
    def press_key(self,locator, key):
        element = self.wait_element_appear(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == 'SPACE':
            element.send_keys(Keys.SPACE)

