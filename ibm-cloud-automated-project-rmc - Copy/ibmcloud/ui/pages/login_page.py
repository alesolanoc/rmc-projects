import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage
from ibmcloud.ui.pages.dashboard.dashboard_page import DashboardPage

username_field = '#userid'

continue_button = 'button[name=\"login\"]'
password_field = '#password'
#signin_button = 'button[name=\"login\"]'
#signin_button = 'button[class=\'login-form__button bx--btn bx--btn--primary\']'
#signin_button = '//span[text()=\'Iniciar sesión\']/parent::button'
signin_button = '//html/body/main/div[2]/div/div/div[1]/form[1]/div[2]/div[2]/div[2]/div[2]/button'
#signin_button = '//div[contains(@class,\'login-form__login-button-wrapper\')]/child::button'


class LoginPage(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "sign_in_as": lambda value: self.set_username(value),
            "password": lambda value: self.set_password(value)
        }
        actions = {
            "Sign In": lambda: self.sign_in()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def set_username(self, value):
        self.click(username_field)
        self.clear_value(username_field)
        self.set_value(username_field, value)
        self.click(continue_button)

    def set_password(self, value):
        self.click(password_field)
        self.clear_value(password_field)
        self.set_value(password_field, value)
#            self.click(signin_button)

    def sign_in(self):
        self.click(signin_button)
        #return DashboardPage(self._driver)


