from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_select_xpath = "div[role='button'][aria-haspopup='listbox']"
    logo_image_xpath = "///*[text()='Scouts Panel']"
    email_field_xpath = "///*[text()='E-mail']"
    back_to_sign_in_xpath = "///*[text()='Back to sign in']"
    send_button__xpath = "///*[text()='Send']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
