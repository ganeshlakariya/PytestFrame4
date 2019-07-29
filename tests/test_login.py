from selenium import webdriver
import pytest
from pages.homepage import homepage
from pages.login import login
from utils import utils as utils
import moment
import allure

@pytest.mark.usefixtures("test_setup")
class TestLogin():


    def test_login(self):
        try:
            driver =self.driver
            driver.get(utils.URL)
            log = login(driver)
            log.usernamebox(utils.username)
            log.passwordbox(utils.password)
            log.logintab()
            x = driver.title()
            assert x == "Ganesh"
        except AssertionError as error:
            print("exception occurred")
            ctime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            filename = "screenshot_" + ctime
            allure.attach(self.driver.get_screenshot_as_png(),name=filename, attachment_type=allure.attachment_type.PNG)
            raise


    def test_logout(self):
        driver = self.driver
        logout = homepage(driver)
        logout.logouttab()

