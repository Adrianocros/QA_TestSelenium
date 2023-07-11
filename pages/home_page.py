from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH,"//span[@class='title']")
        self.item_inventory = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.add_to_cart = (By.XPATH, "//*[text()='Add to cart']")


    def verif_successfull_login(self):
        self.check_element_exists(self.title_page)


    # Add products to cart
    def add_item_cart(self,name_item):
        item = (self.item_inventory[0],self.item_inventory[1].format(name_item))
        self.click(item)
        self.click(self.add_to_cart)
