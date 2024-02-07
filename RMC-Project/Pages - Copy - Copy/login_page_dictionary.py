import time
from selenium.webdriver.common.by import By

class LoginPage():
    locator_dictionary = {
        "username": (By.ID, 'userid'),
        "usernamebutton": (By.CSS_SELECTOR, 'button[name=\"login\"] > div'),
        "password": (By.ID, 'password'),
        "passwordbutton": (By.CSS_SELECTOR, 'div.login-form__user-id-wrapper.login-form__user-id-wrapper--password.login-form__fluid-input-label.login-form__fluid-input-label--align-top > div.login-form__login-button-wrapper > button[name=\"login\"] > span')
        }



