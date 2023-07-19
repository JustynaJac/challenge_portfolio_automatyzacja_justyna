from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    @staticmethod
    def assert_element_text(driver, xpath, expected_text, selector_type=By.XPATH):
        element = driver.find_element(selector_type, xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_to_be_visible(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def type_in_element(self, selector, value, locator_type=By.XPATH):
        element = self.driver.find_element(locator_type, selector)
        element.clear()
        element.send_keys(value)

    def select_dropdown_option(self, selector, option_text, locator_type=By.XPATH):
        from selenium.webdriver.support.ui import Select
        dropdown = Select(self.driver.find_element(locator_type, selector))
        dropdown.select_by_visible_text(option_text)
