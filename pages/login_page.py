from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")

    def todo_login(self,user, password):
        self.to_write(self.username_field,user)
        self.to_write(self.password_field,password)
        self.click(self.login_button)
