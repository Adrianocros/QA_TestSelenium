import time
import pytest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalid(self):
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        # Instantiates the objects to be used in the test
        login_page = LoginPage()
        home_page = HomePage()

        # Perform the login
        login_page.todo_login("standard_user", "secretsauce")

        #Check if login failed and error message
        login_page.verify_error_login()

        #Check the text of the error message
        login_page.verify_text_message_error_login(expected_error_message)


