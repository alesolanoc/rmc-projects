from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage


MANAGE_ACCOUNT = "Account"
MANAGE_BILLING = "Billing and usage"
tab_account_field = '#account-menu'
tab_billing_field = '#billing-menu'

class ManageTabs(FormPage, ActionPage):

    def __init__(self, driver):
        super().__init__(driver)

        actions = {
            "Select Account tab": lambda: self.select_account(),
            "Select Billing tab": lambda: self.select_billing()
        }
        self.update_actions(**actions)

    def select_account(self, value):
        self.click(tab_account_field)

    def select_billing(self, value):
        self.click(tab_billing_field)