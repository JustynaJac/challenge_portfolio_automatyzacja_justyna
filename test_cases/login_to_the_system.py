import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = "C:/Users/justy/Documents/GitHub/challenge_portfolio_automatyzacja_justyna/drivers/"
        os.chmod(driver_path, 755)
        cls.driver_service = Service(executable_path=driver_path)
        cls.driver = webdriver.Chrome(service=cls.driver_service)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()