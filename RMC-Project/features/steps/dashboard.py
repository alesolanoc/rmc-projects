import time

from behave import given, when, then
from Pages.dashboard_page_dictionary import dashboardPage
from Pages.getting_start_page_dictionary import gettingStartPage


@then(u'Title label should be displayed')
def title_label_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_title'])
    if (context.element.text != dashboardPage.dashboard_title_label):
        raise AssertionError("ERROR: ", context.element.text , dashboardPage.dashboard_title_label)
    print(context.element.text , dashboardPage.dashboard_title_label)

@then(u'Filter label should be displayed')
def filter_label_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_filter'])
    if (context.element.text != dashboardPage.dashboard_filter_label):
        raise AssertionError("ERROR: ", context.element.text , dashboardPage.dashboard_filter_label)

@then(u'Filter input field should be displayed')
def filter_input_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_filter_input'])
    if (context.element.text != dashboardPage.dashboard_filter_input_field):
        raise AssertionError("ERROR: ", context.element.text , dashboardPage.dashboard_filter_input_field)

@then(u'Resource name header should be displayed')
def resource_name_header_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_resource_name_column'])
    if (context.element.text != dashboardPage.dashboard_resource_name_column_title):
        raise AssertionError("ERROR: ", context.element.text , dashboardPage.dashboard_resource_name_column_title)

@then(u'Owner header should be displayed')
def owner_header_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_resource_owner_column'])
    if (context.element.text != dashboardPage.dashboard_resource_owner_column_title):
        raise AssertionError("ERROR: ", context.element.text , dashboardPage.dashboard_resource_owner_column_title)

@then(u'Release date header should be displayed')
def date_header_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_resource_date_column'])
    if (context.element.text != dashboardPage.dashboard_resource_date_column_title):
        raise AssertionError("ERROR: ", context.element.text , dashboardPage.dashboard_resource_date_column_title)

@then(u'New resource button should be displayed')
def new_resource_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_new_resource_button'])
    if (True != context.element.is_displayed()):
        raise AssertionError("ERROR: ", True , context.element.is_displayed())

@then(u'All resource should be displayed')
def all_resources_should_be_displayed(context):
    noOfRows = len(context.web.find_elements_by_xpath("//tr")) - 1
    # get number of columns
    noOfColumns = len(context.web.find_elements_by_xpath("//tr[2]/td"))
    allData = []
    # iterate over the rows, to ignore the headers we have started the i with '1'
    for i in range(2, noOfRows):
        # reset the row data every time
        ro = []
        # iterate over columns
        for j in range(1, noOfColumns):
            # get text from the i th row and j th column
            ro.append(context.web.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text)
        # add the row data to allData of the self.table
        allData.append(ro)
    if (len(allData) < 0):
        raise AssertionError("ERROR: ", len(allData) , 0)

@then(u'Getting started popup is displayed after clicked getting started link')
def getting_started_popup_should_be_displayed(context):
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_getting_start_link'])
    context.element.click()
    time.sleep(5)
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*gettingStartPage.locator_dictionary['getting_start_link_title'])
    if (context.element.text != gettingStartPage.getting_start_link_title_label):
        raise AssertionError("ERROR: ", context.element.text , gettingStartPage.getting_start_link_title_label)
    context.element = context.web.find_element(*gettingStartPage.locator_dictionary['getting_start_close_button'])
    context.element.click()
    context.web.switch_to.window(main_page)
    time.sleep(5)





