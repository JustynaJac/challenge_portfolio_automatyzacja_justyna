import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    header_xpath = "h6.MuiTypography-h6"
    button_main_page_xpath = "//*[text()='Strona główna']"
    button_players_xpath = "//*[text()='Players']"
    language_select_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
selectors
    sign_out_xpath = "//*[@id ='__next']/div[1]/div/div/div/ul[2]/iv[2]/div[1]"
    sign_out_button_xpath = "//span[text()='Wyloguj']"
    logo_futbol_xpath = "//div[@class='MuiCardMedia-root jss8']"
    button_devteam_xpath = "//*[text()='Dev team contact']"
    header_activity_xpath = "//h2[contains(@class,'MuiTypography-root') and contains(@class,'MuiTypography-h5') and contains(@class,'MuiTypography-gutterBottom') and text()='Aktywnosć']"
    button_add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    def click_button_add_player(self):
        add_player_button = self.driver.find_element(By.XPATH, self.button_add_player_xpath)
        add_player_button.click()

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    sign_out_xpath = "//*[@id ='__next']/div[1]/div/div/div/ul[2]/ iv[2]/div[1]"
    sign_out_button_xpath = "// span[text() = 'Wyloguj']"
    logo_futbol_xpath = "//div[ @class ='MuiCardMedia-root jss8']"
    button_devteam_xpath =  "//*[text()='Dev team contact']"
    header_activity_xpath = "//h2[contains( @class,'MuiTypography-root')andcontains(@class,'MuiTypography-h5')and contains(@ class,'MuiTypography-gutterBottom')andtext()='Aktywnosć']"
    button_addplayer_xpath = "//a[@href='/pl/players/add']/button"
 main
