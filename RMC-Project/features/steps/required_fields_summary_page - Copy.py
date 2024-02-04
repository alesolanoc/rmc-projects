import datetime
import time

from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from Constants.variables import RESOURCE_NAME_AS_SERVICE, VALIDATE_REQUIRED_FIELDS_SERVICE, RESOURCE_TYPES, \
    RESOURCE_NAME_AS_OPERATIONS, RESOURCE_NAME_AS_COMPOSITE
from Pages.dashboard_page_dictionary import dashboardPage
from Pages.getting_start_page_dictionary import gettingStartPage
from Pages.summary_page_dictionary import summaryPage


@given(u'filter a resource by name: {resourceName}')
def filter_resource_by_name(context,resourceName):
#    time.sleep(25)
    resourceName = resourceName[1:-1].upper()
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_filter_input'])
    context.element.clear()
    if (resourceName == RESOURCE_TYPES[0]):
        context.element.send_keys(RESOURCE_NAME_AS_SERVICE)
    elif (resourceName == RESOURCE_TYPES[1]):
        context.element.send_keys(RESOURCE_NAME_AS_OPERATIONS)
    elif (resourceName == RESOURCE_TYPES[2]):
        context.element.send_keys(RESOURCE_NAME_AS_COMPOSITE)
    context.element.send_keys(Keys.ENTER)
    time.sleep(4)
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['first_resource'])
    context.element.click()
    time.sleep(10)

@when(u'summary page is displayed')
def new_resource(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['resource_name_label'])
    if (context.element.text.find(RESOURCE_NAME_AS_SERVICE) == -1):
        raise AssertionError("ERROR: ", RESOURCE_NAME_AS_SERVICE , context.element.text)
    time.sleep(2)

@when(u'GA was selected for Target release level')
def select_ga(context):
    time.sleep(5)
    context.element = context.web.find_element(*summaryPage.locator_dictionary['target_version_dropdown_menu'])
    context.element.click()
    context.element = context.web.find_element(*summaryPage.locator_dictionary['target_version_GA'])
    context.element.click()
    time.sleep(2)

@when(u'3Q2020 was selected for Service Framework Version')
def select_3Q2020(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['service_framework_dropdown_menu'])
    context.element.click()
    context.element = context.web.find_element(*summaryPage.locator_dictionary['service_framework_3Q2020'])
    context.element.click()
    time.sleep(2)

@when(u'A date was selected for Release date')
def select_date(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['release_date'])
    context.element.click()
    time.sleep(2)
    today = datetime.date.today()
    currentDay = int(today.day)
    i = 1
    while (i < 43):
        day = context.web.find_element_by_xpath("//span[" + str(i) + "]").text
        if (day.isnumeric()):
            if (int(day) == currentDay):
                break
        i = i + 1
    daySelected = context.web.find_element_by_xpath("//span[" + str(i) + "]").text
    time.sleep(2)
    context.web.find_element_by_xpath("//span[" + str(i) + "]").click()

@when(u'{serviceType} type was selected')
def serve_type_selected(context,serviceType):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['type_dropdown_menu'])
    context.element.click()
    if (serviceType.upper() == RESOURCE_TYPES[0].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['service_type_option'])
    elif (serviceType.upper() == RESOURCE_TYPES[1].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['operations_only_type_option'])
    elif (serviceType.upper() == RESOURCE_TYPES[2].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['composite_type_option'])
    context.element.click()
    time.sleep(2)

@when(u'3rd Party was selected for Offering category')
def third_party_option(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['offering_category_dropdown_menu'])
    context.element.click()
    context.element = context.web.find_element(*summaryPage.locator_dictionary['3rd_party_option'])
    context.element.click()
    time.sleep(2)

@when(u'84 Codes was selected for Sub-category')
def codes_option(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['sub_brand_dropdown_menu'])
    context.element.click()
    context.element = context.web.find_element(*summaryPage.locator_dictionary['84_codes'])
    context.element.click()
    time.sleep(2)

@then(u'Success message should be displayed after pressed save button')
def press_save_button(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(10)
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*gettingStartPage.locator_dictionary['getting_start_close_button'])
    context.element.click()
    context.web.switch_to.window(main_page)
    time.sleep(2)

@then(u'Go back to resource list')
def go_back_to_resource_list(context):
    context.element = context.web.find_element(*summaryPage.locator_dictionary['all_resources'])
    context.element.click()
    time.sleep(10)

@then(u'Required fields should be displayed filled in summary page')
def validte_required_fields_summary_page(context):
    time.sleep(10)
    context.element = context.web.find_element(*summaryPage.locator_dictionary['target_version_dropdown_menu'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE[0] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE[0] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*summaryPage.locator_dictionary['service_framework_dropdown_menu'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE[1] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE[1] != context.element.get_attribute("value"))
    context.element = context.web.find_element(*summaryPage.locator_dictionary['type_dropdown_menu'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE[2] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE[2] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*summaryPage.locator_dictionary['offering_category_dropdown_menu'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE[3] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE[3] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*summaryPage.locator_dictionary['sub_brand_dropdown_menu'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE[4] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE[4] , context.element.get_attribute("value"))
