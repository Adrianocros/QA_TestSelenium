import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_inventory = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")

    def product_cart_exist(self, name_item):
        item = (self.item_inventory[0], self.item_inventory[1].format(name_item))
        self.check_element_exists(item)


