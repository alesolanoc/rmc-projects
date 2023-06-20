import datetime
import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants
from core.ui.variables.constants import VALIDATE_REQUIRED_FIELDS_SERVICE

class ImportFromRMCPage(FormPage,ActionPage):
    import_dictionary = {
        'import_button': 'button.bx--btn.bx--btn--primary.myBtn'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
#            "target_release_version": lambda value: self.set_targerReleaseValue(value)
        }
        actions = {
            "press import confirm button": lambda: self.press_import_button()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def press_import_button(self):
        time.sleep(2)
        self.click(ImportFromRMCPage.import_dictionary['import_button'])
        time.sleep(15)

