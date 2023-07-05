from pages.base_page import BasePage

class Dashboard(BasePage):
    header_xpath = "h6.MuiTypography-h6"
    button_main_page_xpath = "//*[text()='Strona główna']"
    button_players_xpath = "//*[text()='Players']"
    language_select_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_xpath = "//*[@id ='__next']/div[1]/div/div/div/ul[2]/ iv[2]/div[1]"
    sign_out_button_xpath = "// span[text() = 'Wyloguj']"
    logo_futbol_xpath = "//div[ @class ='MuiCardMedia-root jss8']"
    button_devteam_xpath =  "//*[text()='Dev team contact']"
    header_activity_xpath = "//h2[contains( @class,'MuiTypography-root')andcontains(@class,'MuiTypography-h5')and contains(@ class,'MuiTypography-gutterBottom')andtext()='Aktywnosć']"
    button_addplayer_xpath = "//a[@href='/pl/players/add']/button"
    pass



