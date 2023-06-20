import datetime
import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants
from core.ui.variables.constants import VALIDATE_REQUIRED_FIELDS_SERVICE

class SuccessRMCPage(FormPage,ActionPage):
    success_dictionary = {
        'success_msg': 'strong',
        'close_button': 'div.relativePosition > button.bx--btn.bx--btn--secondary'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
#            "target_release_version": lambda value: self.set_targerReleaseValue(value)
        }
        actions = {
            "success msg": lambda value: self.is_there_success(value),
            "press close button": lambda: self.press_close_button()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def is_there_success(self,value):
        if (self.get_value(SuccessRMCPage.success_dictionary['success_dictionary']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value(SuccessRMCPage.success_dictionary['success_dictionary']) + " --Not equals-- " + value)

    def press_close_button(self):
        time.sleep(2)
        self.click(SuccessRMCPage.success_dictionary['close_button'])
        time.sleep(10)

