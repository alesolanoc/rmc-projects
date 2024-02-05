import time

from behave import when, then

from Constants.variables import VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG
from Pages.catalog_listing_page_dictionary import cataloglistingPage


@when(u'Add feature button was pressed')
def press_feature_add_button(context):
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['add_feature_button'])
    context.element.click()
    time.sleep(2)

@then(u'Bullet can be added')
def add_media_row(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_title'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[11])
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_description'])
    context.element.clear()
    context.element.send_keys(VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[12])
    time.sleep(2)

@when(u'remove a bullet')
def remove_bullet(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['remove_bullet_button'])
    context.element.click()
    time.sleep(2)

