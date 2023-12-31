import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import IMPLICITLY_WAIT

class Test(unittest.TestCase):

    @classmethod

    def setUp(self):
        driver_path = "C:/Users/justyna/Documents/GitHub/challenge_portfolio_automatyzacja_justyna/drivers/"
        os.chmod(driver_path, 755)
        self.driver_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

class TestMediumPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = "C:/Users/justy/Documents/GitHub/challenge_portfolio_automatyzacja_justyna/drivers/"
        os.chmod(driver_path, 755)
        cls.driver_service = Service(executable_path=driver_path)
        cls.driver = webdriver.Chrome(service=cls.driver_service)
        cls.driver.get('https://medium.com/')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com/')
        expected_title = 'Medium – Where good ideas find you.'
        self.assertEqual(actual_title, expected_title)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
