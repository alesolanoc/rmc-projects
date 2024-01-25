import time

from selenium import webdriver
from Constants.variables import FIREFOX_WEBDRIVER_PATH, read_credentials
from Pages.login_page_dictionary import LoginPage


def before_scenario(context,dashboard):
    context.web = webdriver.Firefox(executable_path=FIREFOX_WEBDRIVER_PATH)
    context.web.maximize_window()
    time.sleep(10)
    credential_record = read_credentials()
    context.web.get(credential_record['dev_Staging_Dashboard'])
    time.sleep(10)
    context.element = context.web.find_element(*LoginPage.locator_dictionary['username'])
    context.element.send_keys(credential_record['dev_Staging_User'])
    time.sleep(2)
    context.element = context.web.find_element(*LoginPage.locator_dictionary['usernamebutton'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*LoginPage.locator_dictionary['password'])
    context.element.send_keys(credential_record['dev_Staging_Password'])
    time.sleep(4)
    context.element = context.web.find_element(*LoginPage.locator_dictionary['passwordbutton'])
    context.element.click()
    time.sleep(30)

def after_step(context,step):
    if (step.status == "failed"):
        print("Scenario Name: " + context.scenario.name + "     Step Name: " + step.name)

def after_scenario(context,dashboard):
    context.web.close()
    context.web.quit()
