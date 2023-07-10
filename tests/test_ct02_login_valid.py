import pytest
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valid(self):
        #Instantiates the objects to be used in the test
        login_page = LoginPage()
        home_page = HomePage()

        #Perform the login
        login_page.todo_login("standard_user","secret_sauce")

        #Check if the login was successfull
        home_page.verif_successfull_login()

