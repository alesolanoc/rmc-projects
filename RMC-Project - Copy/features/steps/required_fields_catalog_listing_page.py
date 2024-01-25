import time

from behave import when, then

from Constants.variables import RESOURCE_NAME_AS_SERVICE, VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG, RESOURCES, \
    RESOURCE_NAME_AS_COMPOSITE, RESOURCE_CONTAINED_TYPES
from Pages.catalog_listing_page_dictionary import cataloglistingPage


@when(u'Go to catalgo listing page')
def go_to_catalog_listing(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['catalog_listing_option'])
    context.element.click()
    time.sleep(5)

@when(u'Go to listing page tab')
def go_to_listing_tab(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
    context.element.click()
    time.sleep(2)

@then(u'resource name should be filled {typeresouce}')
def resource_name_displayed(context,typeresouce):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_display_name'])
    context.element.clear()
    typeresouce = typeresouce[1:-1].upper()
    if (typeresouce == RESOURCES['service']):
        context.element.send_keys(RESOURCE_NAME_AS_SERVICE+VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0])
        time.sleep(2)
        context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_name_header'])
        if (context.element.text != RESOURCE_NAME_AS_SERVICE + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " (" + RESOURCE_NAME_AS_SERVICE + ")"):
            raise AssertionError("ERROR: ", context.element.text , RESOURCE_NAME_AS_SERVICE + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " (" + RESOURCE_NAME_AS_SERVICE + ")")
    elif (typeresouce == RESOURCES['composite']):
        context.element.send_keys(RESOURCE_NAME_AS_COMPOSITE+VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0])
        time.sleep(2)
        context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_name_header'])
        if (context.element.text != RESOURCE_NAME_AS_COMPOSITE + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " (" + RESOURCE_NAME_AS_COMPOSITE + ")"):
            raise AssertionError("ERROR: ", context.element.text , RESOURCE_NAME_AS_COMPOSITE + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " (" + RESOURCE_NAME_AS_COMPOSITE + ")")
    elif (typeresouce == RESOURCES['child']):
        context.element.send_keys(RESOURCE_NAME_AS_COMPOSITE+"."+RESOURCE_CONTAINED_TYPES+VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0])
        time.sleep(2)
        context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_name_header'])
        if (context.element.text != RESOURCE_NAME_AS_COMPOSITE +"."+RESOURCE_CONTAINED_TYPES+ VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " (" + RESOURCE_NAME_AS_COMPOSITE +"."+RESOURCE_CONTAINED_TYPES+ ")"):
            raise AssertionError("ERROR: ", context.element.text != RESOURCE_NAME_AS_COMPOSITE +"."+RESOURCE_CONTAINED_TYPES+ VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " (" + RESOURCE_NAME_AS_COMPOSITE +"."+RESOURCE_CONTAINED_TYPES+ ")")

@then(u'short description should be filled')
def resource_name_displayed(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['short_description'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[1])
    time.sleep(2)

@then(u'author should be filled')
def author(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['author'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[2])
    time.sleep(2)

@then(u'detailed description should be filled')
def detailed_descriptin(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['detailted_description'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[3])
    time.sleep(2)

@then(u'service icon url should be filled')
def service_icon_url(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['service_icon_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[4])
    time.sleep(2)

@then(u'documentation url should be filled')
def documnentation_url(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['documentation_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[5])
    time.sleep(2)

@then(u'terms of agreenment should be filled')
def terms_url(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['terms_of_agreenment_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[6])
    time.sleep(2)

@when(u'Go to settings tab')
def go_to_settings_tag(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['settings_tab'])
    context.element.click()
    time.sleep(2)

@then(u'from management type dropdown menu select public')
def select_public_from_management(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['management_type_dropdown_menu'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['management_type_public_option'])
    context.element.click()
    time.sleep(2)

@then(u'instruction url should be filled')
def instruction_url(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['instructions_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[7])
    time.sleep(2)

@then(u'supported url should be filled')
def supported_url(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['supported_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[8])
    time.sleep(2)

@then(u'select yes for bindable')
def bindable_yes(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bindable_yes'])
    context.element.click()
    time.sleep(2)

@then(u'select yes for required unique')
def required_unique_yes(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['require_unique_yes'])
    context.element.click()
    time.sleep(2)

@then(u'select yes for provisionable')
def provisionable_yes(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['provisionable_yes'])
    context.element.click()
    time.sleep(2)

@then(u'select yes for plan changes')
def plan_changes_yes(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['plan_changes_yes'])
    context.element.click()
    time.sleep(2)

@then(u'select yes for resource type API')
def resource_type_api_yes(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_keys_yes'])
    context.element.click()
    time.sleep(2)

@then(u'support email should be filled')
def support_email(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['supported_email'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[9])
    time.sleep(2)

@then(u'custom provisioning url should be filled')
def custom_provisioning_url(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['custom_provisioning_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[10])
    time.sleep(2)

@when(u'save button is pressed')
def press_save_button(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(30)

@then(u'success message is displayed and review offering in global catalog is displayed')
def review_offering_link(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['review_offering_link'])
    if (context.element.is_displayed() != True):
        raise AssertionError("ERROR: ", context.element.is_displayed() , True)
    time.sleep(10)

@then(u'Required fields should be displayed filled in catalog listing page')
def validte_required_fields_catalog_listing_page(context):
    time.sleep(5)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['catalog_listing_option'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_display_name'])
    if (RESOURCE_NAME_AS_SERVICE + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", RESOURCE_NAME_AS_SERVICE + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['short_description'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[1] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[1] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['author'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[2] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[2] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['detailted_description'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[3] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[3] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['service_icon_url'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[4] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[4] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['documentation_url'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[5] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[5] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['terms_of_agreenment_url'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[6] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[6] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['settings_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['instructions_url'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[7] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[7] , context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['supported_url'])
    if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[8] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[8] , context.element.get_attribute("value"))
