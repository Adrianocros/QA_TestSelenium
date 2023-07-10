from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.error_login = (By.XPATH,"//*[@data-test='error']")

    def todo_login(self,user, password):
        self.to_write(self.username_field,user)
        self.to_write(self.password_field,password)
        self.click(self.login_button)

    def verify_error_login(self):
        self.check_element_exists(self.error_login)

    #login error message is the same as expected text
    def verify_text_message_error_login(self,expected_text):
        found_text = self.get_text_element(self.error_login)
        assert found_text == expected_text, f"The text return is '{expected_text}' but expected the text '{found_text}'."
