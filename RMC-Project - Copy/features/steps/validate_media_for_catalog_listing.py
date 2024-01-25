import time

from behave import when, then
from selenium.webdriver.common.keys import Keys

from Constants.variables import VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG
from Pages.catalog_listing_page_dictionary import cataloglistingPage


@when(u'Add media button was pressed')
def press_feature_add_button(context):
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['add_media_button'])
    context.element.click()
    time.sleep(2)

@then(u'Media can be added')
def add_media_row(context):
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_type'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_option'])
    context.element.click()
#    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[13])
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_thumbnail'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[14])
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_url'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[15])
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_caption'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[16])
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['save_button'])
    context.element.send_keys(Keys.PAGE_UP)
    time.sleep(2)

@when(u'remove a media')
def remove_bullet(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['remove_media'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['save_button'])
    context.element.send_keys(Keys.PAGE_UP)
    time.sleep(2)

