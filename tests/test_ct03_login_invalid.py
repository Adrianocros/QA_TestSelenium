import time
import pytest
import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalid(self):
        driver = conftest.driver
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("zzzzzzz")
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0

        time.sleep(3)
