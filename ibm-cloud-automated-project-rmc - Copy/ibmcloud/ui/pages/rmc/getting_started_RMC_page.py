from core.ui.pages.action_page import ActionPage

class GettingStartedRMCPage(ActionPage):
    gettingStarted_dictionary = {
        'gettingSTarted_RMC_page_header_label': 'h2.learningTileHeader',
        'gettingStarted_RMC_close_button': 'div.relativePosition > button.bx--btn.bx--btn--secondary'
    }

    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "getting started title header": lambda value: self.is_there_getting_started_label(value),
            "getting started close button": lambda: self.close_button()
        }
        self.update_actions(**actions)

    def is_there_getting_started_label(self, value):
        if (self.get_value(GettingStartedRMCPage.gettingStarted_dictionary['gettingSTarted_RMC_page_header_label']).upper() != value):
            raise AssertionError ("---> ERROR: " + self.get_value((GettingStartedRMCPage.gettingStarted_dictionary['gettingSTarted_RMC_page_header_label']).upper()) + " --Not equals-- " + value)

    def close_button(self):
        self.click(GettingStartedRMCPage.gettingStarted_dictionary['gettingStarted_RMC_close_button'])


