from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_select_xpath = "div[role='button'][aria-haspopup='listbox']"
    logo_image_xpath = "///*[text()='Scouts Panel']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.driver.find_element(By.XPATH, self.sign_in_button_xpath).click()
