import time

from behave import when, then

from Constants.variables import CONTRIBUTOR_EMAIL
from Pages.remove_contributor_popup_dictionary import removeContritutorPage
from Pages.summary_page_dictionary import summaryPage

@when(u'go to contributor section and select remove icon for the second row')
def select_remove_icon(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['contributor_remove_icon'])
    context.element.click()

@when(u'confirm remove')
def confirm_remove_contributor(context):
    time.sleep(2)
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*removeContritutorPage.locator_dictionary['confirm_remove_button'])
    context.element.click()
    time.sleep(10)
    context.web.switch_to.window(main_page)

@then(u'the contributor should be removed')
def contributor_should_be_removed(context):
    dataSize = len(context.web.find_elements_by_xpath("//td[normalize-space(text())='" + CONTRIBUTOR_EMAIL + "']"))
    presence = False
    if (dataSize > 0):
        presence = True
    if (presence != False):
        raise AssertionError("ERROR: ", presence , False)