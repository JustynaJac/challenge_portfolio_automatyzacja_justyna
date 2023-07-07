from pages.base_page import BasePage


class AddingMatch(BasePage):
    header_xpath = "h6.MuiTypography-h6"
    button_main_page_xpath = "//*[text()='Strona główna']"
    button_matches_xpath = "//*[text()='Mecze']"
    button_reports_xpath = "//*[text()='Raporty']"
    datetime_xpath = "//input[ @ name='date']"
    my_team_xpath = "//*[name='myTeam']"
    enemy_team_xpath = "//*[name='enemyTeam']"
    submit_xpath = "//button[contains(@class,'MuiButton-containedPrimary')and.//span[text()='Submit']]"
    clear_xpath = "//button[contains(@class,'MuiButton-containedSecondary')and.//span[text()='Clear']]"
    legend_xpath = "//fieldset/legend"
    label_xpath = "//fieldset//div/label[2]"
    date_required_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/p"
    tshirt_color_xpath = "//*[name='tshirt']"
    rating_xpath = "//*[name='rating']"
