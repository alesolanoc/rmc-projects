import time

from behave import given, when, then

from Constants.variables import RESOURCE_NAME_AS_SERVICE, RESOURCE_TYPES, RESOURCE_COMPOSITE_TAG, \
    RESOURCE_CONTAINED_TYPES, RESOURCE_NAME_AS_COMPOSITE, RESOURCES, RESOURCE_NAME_AS_OPERATIONS
from Pages.create_resource_popup_dictionary import createResourcePopup
from Pages.dashboard_page_dictionary import dashboardPage
from Pages.summary_page_dictionary import summaryPage


@given(u'New resource button was pressed')
def press_new_resource_button(context):
    time.sleep(25)
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_new_resource_button'])
    context.element.click()
    time.sleep(4)

@when(u'Create new resource popup is displayed')
def create_new_resource_popup(context):
    context.element = context.web.find_element(*createResourcePopup.locator_dictionary['create_new_resource_title'])
    try: assert createResourcePopup.create_new_resource_title_label == context.element.text
    except AssertionError as e: print(str(e))

@then(u'Would you like to import your services from your service broker {option}')
def select_No_for_Would(context,option):
    option = option[1:-1]
    if (option.upper() == "YES"):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['would_you_like_impor_broker_yes'])
    elif (option.upper() == "NO"):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['would_you_like_impor_broker_no'])
    context.element.click()
    time.sleep(2)

@then(u'Is your resource going to be a child of a composite parent service {option}')
def select_No_for_Is_your(context,option):
    option = option[1:-1]
    if (option.upper() == "YES"):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['is_your_resource_going_to_be_child_yes'])
    elif (option.upper() == "NO"):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['is_your_resource_going_to_be_child_no'])
    context.element.click()
    time.sleep(2)

@then(u'Fill resource name {resource}')
def fill_resource(context,resource):
    resource = resource[1:-1].upper()
    if (resource == RESOURCES['service']):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_name'])
        context.element.clear()
        context.element.send_keys(RESOURCE_NAME_AS_SERVICE)
    elif (resource == RESOURCES['operations only']):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_name'])
        context.element.clear()
        context.element.send_keys(RESOURCE_NAME_AS_OPERATIONS)
    elif (resource == RESOURCES['composite']):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_name'])
        context.element.clear()
        context.element.send_keys(RESOURCE_NAME_AS_COMPOSITE)
    elif (resource == RESOURCES['parent']):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['composite_parent_name'])
        context.element.clear()
        context.element.send_keys(RESOURCE_NAME_AS_COMPOSITE)
        time.sleep(2)
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['composite_child_name'])
        context.element.clear()
        context.element.send_keys(RESOURCE_CONTAINED_TYPES)
    time.sleep(2)


@then(u'Select resource type "{resource_type}"')
def select_resource_type(context,resource_type):
    context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_type_dropdown'])
    context.element.click()
    time.sleep(1)
    if (resource_type.upper() == RESOURCE_TYPES[0].upper()):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_type_service'])
        context.element.click()
        time.sleep(1)
    elif (resource_type.upper() == RESOURCE_TYPES[1].upper()):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_type_operations_only'])
        context.element.click()
        time.sleep(1)
    elif(resource_type.upper() == RESOURCE_TYPES[2].upper()):
        context.element = context.web.find_element(*createResourcePopup.locator_dictionary['resource_type_composite'])
        context.element.click()
        time.sleep(10)



@then(u'Press Submit button')
def press_submit_button(context):
    context.element = context.web.find_element(*createResourcePopup.locator_dictionary['submit_button'])
    context.element.click()
    time.sleep(10)

@then(u'New resource "{resource_type}" should be displayed in summary page')
def new_resource(context,resource_type):
    time.sleep(5)
    if (resource_type.upper() == RESOURCE_TYPES[0].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['resource_name_label'])
        if (context.element.text.find(RESOURCE_NAME_AS_SERVICE) == -1):
            raise AssertionError("ERROR: ", RESOURCE_NAME_AS_SERVICE , context.element.text)
    elif (resource_type.upper() == RESOURCE_TYPES[1].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['type_dropdown_menu'])
        if (context.element.get_attribute("value") != "operations_only"):
            raise AssertionError("ERROR: ", context.element.get_attribute("value") , "operations_only")
    elif (resource_type.upper() == RESOURCE_TYPES[2].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['type_dropdown_menu'])
        if (context.element.get_attribute("value") != "composite"):
            raise AssertionError("ERROR: ", context.element.get_attribute("value") , "composite")
    elif (resource_type.upper() == RESOURCE_TYPES[4].upper()):
        context.element = context.web.find_element(*summaryPage.locator_dictionary['resource_name_label'])
        if ("(" + RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES + ")" != context.element.text):
            raise AssertionError("ERROR: ", "(" + RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES + ")" , context.element.text)
    time.sleep(2)


@then(u'Fill composite tag')
def fill_composite_tage(context):
    context.element = context.web.find_element(*createResourcePopup.locator_dictionary['composite_tag'])
    context.element.send_keys(RESOURCE_COMPOSITE_TAG)
    time.sleep(2)

@then(u'Fill contained resource types')
def fill_contained_resource_types(context):
    context.element = context.web.find_element(*createResourcePopup.locator_dictionary['contained_resource_types'])
    context.element.send_keys(RESOURCE_CONTAINED_TYPES)
    time.sleep(2)


