import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer

class TestAddAPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = "C:/Users/justy/Documents/GitHub/challenge_portfolio_automatyzacja_justyna/drivers/"
        os.chmod(driver_path, 755)
        cls.driver_service = Service(executable_path=driver_path)
        cls.driver = webdriver.Chrome(service=cls.driver_service)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_a_player_button()
        add_player_page = AddAPlayer(self.driver)
        add_player_page.type_in_email()
        add_player_page.type_in_name()
        add_player_page.type_in_surname()
        add_player_page.type_in_phone()
        add_player_page.type_in_weight()
        add_player_page.type_in_height()
        add_player_page.type_in_age()
        add_player_page.select_leg()
        add_player_page.type_in_club()
        add_player_page.type_in_level()
        add_player_page.type_in_main_position()
        add_player_page.type_in_second_position()
        add_player_page.select_district()
        add_player_page.type_in_achievements()
        add_player_page.click_submit_button()


    @classmethod
    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
