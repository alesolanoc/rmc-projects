import json
import time
import pyperclip as pyperclip

from behave import when, then
from selenium.webdriver.common.keys import Keys

from Constants.variables import RESOURCE_NAME_AS_SERVICE, VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG
from Pages.catalog_listing_page_dictionary import cataloglistingPage
from Pages.json_view_modal_dictionary import jsonviewPage

@when(u'pressed view json button')
def press_view_json_button(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['view_json'])
    context.element.click()
    time.sleep(2)

@then(u'json editor modal should be displayed')
def json_editor_is_displayed(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['json_view_modal'])
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.CONTROL, "C")
    time.sleep(2)
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    time.sleep(3)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['close_json_view'])
    context.element.click()
    time.sleep(3)
    context.web.switch_to.window(main_page)
    time.sleep(3)

@then(u'validate catalog listing page against json view modal')
def validate_catalog_listing_against_json_view(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_display_name'])
    if (jsonscript['metadata']['displayName'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['displayName'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['displayName'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['short_description'])
    if (jsonscript['description'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['description'] , context.element.get_attribute("value"))
    print(jsonscript['description'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['author'])
    if (jsonscript['metadata']['providerDisplayName'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['providerDisplayName'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['providerDisplayName'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['detailted_description'])
    if (jsonscript['metadata']['longDescription'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['longDescription'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['longDescription'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['service_icon_url'])
    if (jsonscript['metadata']['featuredImageUrl'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['featuredImageUrl'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['featuredImageUrl'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['documentation_url'])
    if (jsonscript['metadata']['documentationUrl'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['documentationUrl'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['documentationUrl'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['terms_of_agreenment_url'])
    if (jsonscript['metadata']['termsUrl'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['termsUrl'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['termsUrl'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['settings_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['instructions_url'])
    if (jsonscript['metadata']['instructionsUrl'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['instructionsUrl'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['instructionsUrl'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['supported_url'])
    if (jsonscript['metadata']['supportUrl'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['supportUrl'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['supportUrl'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_title'])
    if (jsonscript['metadata']['bullets'][0]['title'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['bullets'][0]['title'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['bullets'][0]['title'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_description'])
    if (jsonscript['metadata']['bullets'][0]['description'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['bullets'][0]['description'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['bullets'][0]['description'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_type'])
    if (jsonscript['metadata']['media'][0]['type'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['media'][0]['type'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['media'][0]['type'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_thumbnail'])
    if (jsonscript['metadata']['media'][0]['thumbnailUrl'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['media'][0]['thumbnailUrl'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['media'][0]['thumbnailUrl'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_url'])
    if (jsonscript['metadata']['media'][0]['url'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['media'][0]['url'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['media'][0]['url'] , context.element.get_attribute("value"))

    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_caption'])
    if (jsonscript['metadata']['media'][0]['caption'] != context.element.get_attribute("value")):
        raise AssertionError("ERROR: ", jsonscript['metadata']['media'][0]['caption'] , context.element.get_attribute("value"))
    print(jsonscript['metadata']['media'][0]['caption'] , context.element.get_attribute("value"))