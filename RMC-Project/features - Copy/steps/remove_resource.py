import time

from behave import then, given
from selenium.webdriver.common.keys import Keys

from Constants.variables import RESOURCE_NAME_AS_SERVICE
from Pages.dashboard_page_dictionary import dashboardPage
from Pages.remove_resource_dictionary import removeresourcePage

@given(u'filter a resource to be removed')
def filter_resource(context):
    time.sleep(25)
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_filter_input'])
    context.element.clear()
    context.element.send_keys(RESOURCE_NAME_AS_SERVICE)
    context.element.send_keys(Keys.ENTER)
    time.sleep(4)


@then(u'press remove icon')
def press_remove_icon(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['remove_icon'])
    context.element.click()
    time.sleep(2)


@then(u'confirm remove')
def confirm_remove(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*removeresourcePage.locator_dictionary['remove_input'])
    context.element.send_keys(RESOURCE_NAME_AS_SERVICE)
    time.sleep(4)
    context.element = context.web.find_element(*removeresourcePage.locator_dictionary['remove_confirm_button'])
    context.element.click()
    time.sleep(15)
    context.web.switch_to.window(main_page)


@then(u'resource should not be displayed in dashboard')
def resource_should_not_be(context):
    time.sleep(25)
    context.element = context.web.find_elements_by_xpath("//td[normalize-space(text())='" + RESOURCE_NAME_AS_SERVICE + "']")
    dataSize = len(context.web.find_elements_by_xpath("//td[normalize-space(text())='" + RESOURCE_NAME_AS_SERVICE + "']"))
    presence = False
    if (dataSize > 0):
        presence = True
    if (presence == False):
        raise AssertionError("ERROR: ", presence, True)
