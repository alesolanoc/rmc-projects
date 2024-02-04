import time

from behave import given, when, then
from selenium.webdriver.common.keys import Keys

from Constants.variables import RESOURCE_NAME_AS_SERVICE, read_credentials, CONTRIBUTOR_EMAIL
from Pages.contributor_popup_dictionary import contributorPage
from Pages.dashboard_page_dictionary import dashboardPage
from Pages.summary_page_dictionary import summaryPage


#@given(u'filter a resource by name')
#def filter_resource_by_name(context):
#    time.sleep(25)
#    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_filter_input'])
#    context.element.clear()
#    context.element.send_keys(RESOURCE_NAME_AS_SERVICE)
#    context.element.send_keys(Keys.ENTER)
#    time.sleep(2)
#    context.element = context.web.find_element(*dashboardPage.locator_dictionary['first_resource'])
#    context.element.click()
#    time.sleep(10)

#@when(u'summary page is displayed')
#def new_resource(context):
#    context.element = context.web.find_element(*summaryPage.locator_dictionary['resource_name_label'])
#    try: assert "(" + RESOURCE_NAME_AS_SERVICE + ")" == context.element.text
#    except AssertionError as e: print(str(e))
#    time.sleep(2)

@when(u'owner of the resource should be the same user as logged')
def owner_same_as_logged(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['contributor_owner_row'])
    credential_record = read_credentials()
    if (credential_record['dev_Staging_User'] != context.element.text):
        raise AssertionError("ERROR: ", credential_record['dev_Staging_User'] , context.element.text)
    time.sleep(2)

@when(u'Press Add button')
def press_add_contributor(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['contributor_add_button'])
    context.element.click()
    time.sleep(2)

@then(u'Add contributor popup is displayed')
def contributor_popup_displayed(context):
    global main_page
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*contributorPage.locator_dictionary['contributor_header_label'])
    if (contributorPage.contributor_Label != context.element.text):
        raise AssertionError("ERROR: ", contributorPage.contributor_Label , context.element.text)

@when(u'filled a new contributor')
def insert_contributor(context):
    context.element = context.web.find_element(*contributorPage.locator_dictionary['contributor_input_field'])
    context.element.clear()
    context.element.send_keys(CONTRIBUTOR_EMAIL)

@when(u'Pressed Add button')
def press_submit_button(context):
    context.element = context.web.find_element(*contributorPage.locator_dictionary['contributor_submit_button'])
    context.element.click()
    time.sleep(10)
    context.web.switch_to.window(main_page)
    time.sleep(10)

@then(u'a new contributor should be added and displayed in contributor table')
def new_contributor_displayed(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['contributor_added_row'])
    if (CONTRIBUTOR_EMAIL != context.element.text):
        raise AssertionError("ERROR: ", CONTRIBUTOR_EMAIL , context.element.text)
