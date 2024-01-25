import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants

class ContributorRMCPage(FormPage,ActionPage):
    contributor_dictionary = {
        'input_contributor_field': 'input.bx--text-input.bx--text__input',
        'add_button': 'div.relativePosition > button.bx--btn.bx--btn--primary',
        'remove_button': 'button.bx--btn.bx--btn--danger--primary.myBtn'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "input_contributor": lambda value: self.set_newContributorValue(value)
        }
        actions = {
            "press add button": lambda: self.press_add_button(),
            "press remove button": lambda: self.press_remove_button()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def set_newContributorValue(self,value):
        self.click(ContributorRMCPage.contributor_dictionary['input_contributor_field'])
        self.clear_value(ContributorRMCPage.contributor_dictionary['input_contributor_field'])
        self.set_value(ContributorRMCPage.contributor_dictionary['input_contributor_field'], value)
        time.sleep(2)

    def press_add_button(self):
        self.click(ContributorRMCPage.contributor_dictionary['add_button'])
        time.sleep(20)

    def press_remove_button(self):
        self.click(ContributorRMCPage.contributor_dictionary['remove_button'])
        time.sleep(20)
