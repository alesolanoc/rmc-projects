from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage

MAIN_MANAGE = "Manage"
MAIN_SUPPORT = "Support"
tab_manage_field = '//li[text()=\'%s\']' % MAIN_MANAGE
tab_support_field = '//li[text()=\'%s\']' % MAIN_SUPPORT

class MainTabs(FormPage, ActionPage):

    def __init__(self, driver):
        super().__init__(driver)

        actions = {
            "Select Manage tab": lambda: self.select_manage(),
            "Select Support tab": lambda: self.select_support()
        }
        self.update_actions(**actions)

    def select_manage(self, value):
        self.click(tab_manage_field)

    def select_support(self, value):
        self.click(tab_support_field)
