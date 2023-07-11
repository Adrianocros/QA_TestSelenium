import time

import pytest
from selenium.webdriver.common.by import By

import conftest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
class TestCT01:
    def test_ct01_add_product_cart(self):
        driver = conftest.driver
        login_page  = LoginPage()
        home_page   = HomePage()
        cart_page = CartPage()

        #Login
        login_page.todo_login("standard_user","secret_sauce")


        #Add products from cart from home page
        home_page.add_item_cart("Sauce Labs Backpack")

        #Click from shopping cart and verify prodcut exist from cart
        home_page.access_cart()
        cart_page.product_cart_exist("Sauce Labs Backpack")

        #Back to home screen
        driver.find_element(By.XPATH,"//*[@id='continue-shopping']").click()



        #Add another item to cart
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Test.allTheThings() T-Shirt (Red)']").click()
        driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()

        #Clicking on cart
        home_page.access_cart()
        cart_page
        assert driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        #Validating the cart
        assert driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Test.allTheThings() T-Shirt (Red)']").is_displayed()

        #Clickind on checkout
        driver.find_element(By.XPATH,"//*[@id='checkout']").click()
        assert driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()


        #fill in the fields
        driver.find_element(By.XPATH,"//*[@id='first-name']").send_keys("Adriano")


        driver.find_element(By.XPATH,"//*[@id='last-name']").send_keys("Bianchi")


        driver.find_element(By.XPATH,"//*[@id='postal-code']").send_keys("07097420")


        driver.find_element(By.XPATH,"//*[@id='continue']").click()


        assert driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        #clicking finish
        driver.find_element(By.XPATH,"//*[@id='finish']").click()

        #Checks if the order has been completed
        assert driver.find_element(By.XPATH,"//h2[@class='complete-header' and text()='Thank you for your order!']").is_displayed()
        driver.find_element(By.XPATH,"//*[@class='btn btn_primary btn_small']").click()
