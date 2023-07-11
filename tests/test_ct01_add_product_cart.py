import time

import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage



@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
class TestCT01:
    def test_ct01_add_product_cart(self):
        login_page  = LoginPage()
        home_page   = HomePage()
        cart_page = CartPage()

        #Products
        procut01 = "Sauce Labs Backpack"
        procut02 = "Sauce Labs Fleece Jacket"
        procut03 = "Sauce Labs Bike Light"

        #Login
        login_page.todo_login("standard_user","secret_sauce")


        #Add products from cart from home page
        home_page.add_item_cart(procut01)

        #Click from shopping cart and verify prodcut exist from cart
        home_page.access_cart()
        cart_page.product_cart_exist(procut01)

        #Back to home screen
        cart_page.click_continue_shopping()

        #Add another item to cart
        # Add products from cart from home page
        home_page.add_item_cart(procut02)

        # Click from shopping cart and verify prodcut exist from cart
        home_page.access_cart()
        cart_page.product_cart_exist(procut02)

        # Back to home screen
        cart_page.click_continue_shopping()

        # Add products from cart from home page
        home_page.add_item_cart(procut03)

        # Click from shopping cart and verify prodcut exist from cart
        home_page.access_cart()
        cart_page.product_cart_exist(procut03)

        # Back to home screen
        cart_page.click_continue_shopping()

        # Click from shopping cart and verify prodcut exist from cart
        home_page.access_cart()
        cart_page.product_cart_exist(procut01)
        cart_page.product_cart_exist(procut02)
        cart_page.product_cart_exist(procut03)

        time.sleep(3)

        # #Clicking on cart
        # home_page.access_cart()
        # assert driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        #
        # #Validating the cart
        # assert driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Test.allTheThings() T-Shirt (Red)']").is_displayed()
        #
        # #Clickind on checkout
        # driver.find_element(By.XPATH,"//*[@id='checkout']").click()
        # assert driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()
        #
        #
        # #fill in the fields
        # driver.find_element(By.XPATH,"//*[@id='first-name']").send_keys("Adriano")
        #
        #
        # driver.find_element(By.XPATH,"//*[@id='last-name']").send_keys("Bianchi")
        #
        #
        # driver.find_element(By.XPATH,"//*[@id='postal-code']").send_keys("07097420")
        #
        #
        # driver.find_element(By.XPATH,"//*[@id='continue']").click()
        #
        #
        # assert driver.find_element(By.XPATH,"//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        #
        # #clicking finish
        # driver.find_element(By.XPATH,"//*[@id='finish']").click()
        #
        # #Checks if the order has been completed
        # assert driver.find_element(By.XPATH,"//h2[@class='complete-header' and text()='Thank you for your order!']").is_displayed()
        # driver.find_element(By.XPATH,"//*[@class='btn btn_primary btn_small']").click()
