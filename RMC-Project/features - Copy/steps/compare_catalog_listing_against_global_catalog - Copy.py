import time

from behave import then
from selenium.webdriver.common.keys import Keys
from Pages.catalog_listing_page_dictionary import cataloglistingPage
from Pages.global_catalog_page_dictionary import globalcatalogPage

@then(u'validate catalog listing page against global catalog expired')
def validate_catalog_listing_against_global_catalog_expired(context):
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
#    context.element.click()
#    time.sleep(2)
#    RESOURCE_CATALOG_LIST = []
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_display_name'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['short_description'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['author'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['detailted_description'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['service_icon_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['documentation_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['terms_of_agreenment_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['settings_tab'])
#    context.element.click()
#    time.sleep(2)
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['instructions_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['supported_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['custom_provisioning_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
#    context.element.click()
#    time.sleep(2)
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_title'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_description'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_type'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_thumbnail'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_url'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_caption'])
#    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))

#    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['review_offering_link'])
#    context.element.click()
#    time.sleep(2)
#    link = context.element.get_attribute('href')
#    window_before = context.web.window_handles[0]
#    context.element.send_keys(Keys.CONTROL + Keys.PAGE_UP)
#    time.sleep(15)
#    window_after = context.web.window_handles[1]
#    context.web.switch_to.window(window_after)
#    time.sleep(5)
#    context.web.get(link)
#    time.sleep(2)

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['display_name'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[0]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[1]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[3]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[15]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_type'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[11]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[14]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[10]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[11]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['overview_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['author'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[2]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['provisioning_url'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[9]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['documentaton_url'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[5]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['terms_url'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[6]
    except AssertionError as e: print(str(e))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['instructions_url'])
    try: assert context.element.get_attribute("value") == RESOURCE_CATALOG_LIST[7]
    except AssertionError as e: print(str(e))
    time.sleep(2)

