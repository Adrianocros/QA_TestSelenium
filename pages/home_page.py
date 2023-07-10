from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH,"//span[@class='title']")

    def verif_successfull_login(self):
        self.check_element_exists(self.title_page)


