from pages.base_page import BasePage


class AddingMatch(BasePage):
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    header_xpath = "h6.MuiTypography-h6"
    button_main_page_xpath = "//*[text()='Strona główna']"
    button_players_xpath = "//*[text()='Gracze']"
    button_language_xpath = "button[aria-label='Dodaj język']"
    button_submit_xpath = "button[type='submit']"
    button_clear_xpath = "//button[contains(@class,'MuiButton-containedSecondary')]"
    button_add_link_to_youtube_xpath = "// button[contains(@aria-label'Dodaj link z Youtube')]"
    age_field_xpath = "//input[@name='age']"

    def assert_add_player_page_loaded(self):
        assert self.get_page_title(self.add_a_player_url) == 'Add player'

    def click_add_player_button(self):
        dashboard = Dashboard(self.driver)
        dashboard.click_button_add_player()