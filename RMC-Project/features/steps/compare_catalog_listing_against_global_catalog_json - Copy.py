import json
import time
import pyperclip

from behave import then, when
from selenium.webdriver.common.keys import Keys
from Constants.variables import UPDATEVALUEJSONSCRIPT, RESOURCE_NAME_AS_COMPOSITE, RESOURCE_CONTAINED_TYPES, \
    RESOURCE_COMPOSITE_TAG, UPDATEGLOBALCATALOG
from Pages.catalog_listing_page_dictionary import cataloglistingPage
from Pages.dashboard_page_dictionary import dashboardPage
from Pages.global_catalog_page_dictionary import globalcatalogPage
from Pages.import_popup_dictionary import importfromGCPage
from Pages.import_success_dictionary import importfromGCSuccessPage
from Pages.json_view_modal_dictionary import jsonviewPage

global jsonscript


@then(u'get catalog list values')
def get_catalog_list_values(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
    context.element.click()
    time.sleep(2)
    global RESOURCE_CATALOG_LIST
    RESOURCE_CATALOG_LIST = []
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['resource_display_name'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['short_description'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['author'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['detailted_description'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['service_icon_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['documentation_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['terms_of_agreenment_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['settings_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['instructions_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['supported_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['custom_provisioning_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['listing_page_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_title'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['bullet_description'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_type'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_thumbnail'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_url'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['media_caption'])
    RESOURCE_CATALOG_LIST.append(context.element.get_attribute("value"))

@then(u'go to global catalog')
def go_to_global_catalog(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['review_offering_link'])
    context.element.click()
    time.sleep(2)
    link = context.element.get_attribute('href')
    global window_before
    window_before = context.web.window_handles[0]
    context.element.send_keys(Keys.CONTROL + Keys.PAGE_UP)
    time.sleep(15)
    window_after = context.web.window_handles[1]
    context.web.switch_to.window(window_after)
    time.sleep(5)
    context.web.get(link)
    time.sleep(2)

@then(u'json editor should be displayed')
def json_editor_is_displayed(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['json_view_modal'])
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.CONTROL, "C")
    time.sleep(2)
#    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    time.sleep(3)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(3)
    context.web.switch_to.window(main_page)
    time.sleep(3)


@then(u'validate catalog listing page against global catalog')
def validate_catalog_listing_against_global_catalog(context):
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['display_name'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[0]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[0])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[0])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[1]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[1])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[1])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[3]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[3])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[3])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[15]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[15])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[15])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_type'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[12]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[12])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[12])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[14]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[14])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[14])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[10]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[10])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[10])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[11]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[11])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[11])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['overview_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['author'])
    if context.element.text != RESOURCE_CATALOG_LIST[2]:
        raise AssertionError("ERROR: ", context.element.text , RESOURCE_CATALOG_LIST[2])
    print(context.element.text , RESOURCE_CATALOG_LIST[2])

#    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['provisioning_url'])
#    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[9]):
#        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[9])
#    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[9])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['documentaton_url'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[5]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[5])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[5])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['terms_url'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[6]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[6])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[6])

    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['instructions_url'])
    if (context.element.get_attribute("value") != RESOURCE_CATALOG_LIST[7]):
        raise AssertionError("ERROR: ", context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[7])
    print(context.element.get_attribute("value") , RESOURCE_CATALOG_LIST[7])

    time.sleep(2)


@then(u'select three dots')
def select_three_dots(context):
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['three_dots_menu'])
    context.element.click()
    time.sleep(2)


@then(u'select edit option of three dots dropdown menu')
def select_edit_option(context):
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['edit_option'])
    context.element.click()
    time.sleep(2)

@then(u'update json script in json editor')
def update_json_script(context):
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
    jsonscript['overview_ui']['en']['description'] = jsonscript['overview_ui']['en']['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['overview_ui']['en']['long_description'] = jsonscript['overview_ui']['en']['long_description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['urls']['doc_url'] = jsonscript['metadata']['ui']['urls']['doc_url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['urls']['terms_url'] = jsonscript['metadata']['ui']['urls']['terms_url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['urls']['instructions_url'] = jsonscript['metadata']['ui']['urls']['instructions_url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['title'] = jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['description'] = jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['strings']['en']['media'][0]['url'] = jsonscript['metadata']['ui']['strings']['en']['media'][0]['url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['metadata']['ui']['strings']['en']['media'][0]['caption'] = jsonscript['metadata']['ui']['strings']['en']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPT
    time.sleep(3)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(3)
    context.web.switch_to.window(main_page)
    time.sleep(3)


@then(u'get global catalog values')
def get_catalog_list_values(context):
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['overview_tab'])
    context.element.click()
    time.sleep(4)
    global RESOURCE_GLOBAL_CATALOG_LIST
    RESOURCE_GLOBAL_CATALOG_LIST = []
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['author'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.text)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['documentaton_url'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['terms_url'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['instructions_url'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['provisioning_url'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['resource_name'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(4)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['display_name'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_type'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url'])
    RESOURCE_GLOBAL_CATALOG_LIST.append(context.element.get_attribute("value"))


@then(u'validate global catalog page against global catalog json script')
def validate_catalog_listing_against_json_script(context):
    time.sleep(2)

    if (jsonscript['overview_ui']['en']['display_name'] != RESOURCE_GLOBAL_CATALOG_LIST[6]):
        raise AssertionError("ERROR: ", jsonscript['overview_ui']['en']['display_name'] , RESOURCE_GLOBAL_CATALOG_LIST[6])
    print(jsonscript['overview_ui']['en']['display_name'] , RESOURCE_GLOBAL_CATALOG_LIST[6])

    if (jsonscript['overview_ui']['en']['description'] != RESOURCE_GLOBAL_CATALOG_LIST[7]):
        raise AssertionError("ERROR: ", jsonscript['overview_ui']['en']['description'] != RESOURCE_GLOBAL_CATALOG_LIST[7])
    print(jsonscript['overview_ui']['en']['description'] , RESOURCE_GLOBAL_CATALOG_LIST[7])

    if (jsonscript['provider']['name'] != RESOURCE_GLOBAL_CATALOG_LIST[0]):
        raise AssertionError("ERROR: ", jsonscript['provider']['name'] , RESOURCE_GLOBAL_CATALOG_LIST[0])
    print(jsonscript['provider']['name'] , RESOURCE_GLOBAL_CATALOG_LIST[0])

    if (jsonscript['overview_ui']['en']['long_description'] != RESOURCE_GLOBAL_CATALOG_LIST[8]):
        raise AssertionError("ERROR: ", jsonscript['overview_ui']['en']['long_description'] , RESOURCE_GLOBAL_CATALOG_LIST[8])
    print(jsonscript['overview_ui']['en']['long_description'] , RESOURCE_GLOBAL_CATALOG_LIST[8])

#    if (jsonscript['images']['feature_image'] != RESOURCE_CATALOG_LIST[4]):
#        raise AssertionError("ERROR: ", jsonscript['images']['feature_image'] , RESOURCE_CATALOG_LIST[4])
#    print(jsonscript['images']['feature_image'] , RESOURCE_CATALOG_LIST[4])

    if (jsonscript['metadata']['ui']['urls']['doc_url'] != RESOURCE_GLOBAL_CATALOG_LIST[1]):
        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['urls']['doc_url'] , RESOURCE_GLOBAL_CATALOG_LIST[1])
    print(jsonscript['metadata']['ui']['urls']['doc_url'] , RESOURCE_GLOBAL_CATALOG_LIST[1])

    if (jsonscript['metadata']['ui']['urls']['terms_url'] != RESOURCE_GLOBAL_CATALOG_LIST[2]):
        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['urls']['terms_url'] , RESOURCE_GLOBAL_CATALOG_LIST[2])
    print(jsonscript['metadata']['ui']['urls']['terms_url'] , RESOURCE_GLOBAL_CATALOG_LIST[2])

#    if (jsonscript['metadata']['ui']['urls']['instructions_url'] != RESOURCE_GLOBAL_CATALOG_LIST[3]):
#        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['urls']['instructions_url'] , RESOURCE_GLOBAL_CATALOG_LIST[3])
#    print(jsonscript['metadata']['ui']['urls']['instructions_url'] , RESOURCE_GLOBAL_CATALOG_LIST[3])

    if (jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['title'] != RESOURCE_GLOBAL_CATALOG_LIST[9]):
        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['title'] , RESOURCE_GLOBAL_CATALOG_LIST[9])
    print(jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['title'] , RESOURCE_GLOBAL_CATALOG_LIST[9])

    if (jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['description'] != RESOURCE_GLOBAL_CATALOG_LIST[10]):
        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['description'] , RESOURCE_GLOBAL_CATALOG_LIST[10])
    print(jsonscript['metadata']['ui']['strings']['en']['bullets'][0]['description'] , RESOURCE_GLOBAL_CATALOG_LIST[10])

#    if (jsonscript['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] != RESOURCE_CATALOG_LIST[13]):
#        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] , RESOURCE_CATALOG_LIST[13])
#    print(jsonscript['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] , RESOURCE_CATALOG_LIST[13])

    if (jsonscript['metadata']['ui']['strings']['en']['media'][0]['url'] != RESOURCE_GLOBAL_CATALOG_LIST[13]):
        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['strings']['en']['media'][0]['url'] , RESOURCE_GLOBAL_CATALOG_LIST[13])
    print(jsonscript['metadata']['ui']['strings']['en']['media'][0]['url'] , RESOURCE_GLOBAL_CATALOG_LIST[13])

    if (jsonscript['metadata']['ui']['strings']['en']['media'][0]['caption'] != RESOURCE_GLOBAL_CATALOG_LIST[11]):
        raise AssertionError("ERROR: ", jsonscript['metadata']['ui']['strings']['en']['media'][0]['caption'] , RESOURCE_GLOBAL_CATALOG_LIST[11])
    print(jsonscript['metadata']['ui']['strings']['en']['media'][0]['caption'] , RESOURCE_GLOBAL_CATALOG_LIST[11])


@when(u'Import from global catalog')
def import_from_global_catalo(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['import_from_gc'])
    context.element.click()
    time.sleep(3)
    main_page1 = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*importfromGCPage.locator_dictionary['import_button'])
    context.element.click()
    time.sleep(15)
    context.web.switch_to.window(main_page1)
    main_page2 = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*importfromGCSuccessPage.locator_dictionary['close_button'])
    context.element.click()
    time.sleep(2)
    context.web.switch_to.window(main_page2)
    time.sleep(2)



@when(u'go to global catalog and update JSon script')
def go_to_global_catalog_and_update_json_script(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['review_offering_link'])
    context.element.click()
    time.sleep(2)
    link = context.element.get_attribute('href')
    window_before = context.web.window_handles[0]
    context.element.send_keys(Keys.CONTROL + Keys.PAGE_UP)
    time.sleep(15)
    window_after = context.web.window_handles[1]
    context.web.switch_to.window(window_after)
    time.sleep(5)
    context.web.get(link)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['three_dots_menu'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['edit_option'])
    context.element.click()
    time.sleep(2)
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['json_view_modal'])
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.CONTROL, "C")
    time.sleep(2)
    jsonscriptGC = json.loads(pyperclip.paste())
    jsonscriptGC['overview_ui']['en']['description'] = jsonscriptGC['overview_ui']['en']['description'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['overview_ui']['en']['long_description'] = jsonscriptGC['overview_ui']['en']['long_description'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['urls']['doc_url'] = jsonscriptGC['metadata']['ui']['urls']['doc_url'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['urls']['terms_url'] = jsonscriptGC['metadata']['ui']['urls']['terms_url'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['urls']['instructions_url'] = jsonscriptGC['metadata']['ui']['urls']['instructions_url'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['strings']['en']['bullets'][0]['title'] = jsonscriptGC['metadata']['ui']['strings']['en']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['strings']['en']['bullets'][0]['description'] = jsonscriptGC['metadata']['ui']['strings']['en']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['strings']['en']['media'][0]['url'] = jsonscriptGC['metadata']['ui']['strings']['en']['media'][0]['url'] + UPDATEVALUEJSONSCRIPT
    jsonscriptGC['metadata']['ui']['strings']['en']['media'][0]['caption'] = jsonscriptGC['metadata']['ui']['strings']['en']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPT
    time.sleep(3)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscriptGC))
    time.sleep(2)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(3)
    context.web.switch_to.window(main_page)
    time.sleep(3)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['overview_tab'])
    context.element.click()
    time.sleep(2)
    context.element.send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
    context.web.switch_to.window(window_before)
    time.sleep(10)

@then(u'filter a resource by parent')
def filter_resource_by_name(context):
    time.sleep(15)
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['dashboard_filter_input'])
    context.element.clear()
    context.element.send_keys(RESOURCE_NAME_AS_COMPOSITE)
    context.element.send_keys(Keys.ENTER)
    time.sleep(4)
    context.element = context.web.find_element(*dashboardPage.locator_dictionary['first_resource'])
    context.element.click()
    time.sleep(10)


@then(u'validate that json script has {child} {servicetype} reference')
def update_json_script(context,child,servicetype):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*jsonviewPage.locator_dictionary['json_view_modal'])
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.CONTROL, "C")
    time.sleep(2)
    jsonscript2 = json.loads(pyperclip.paste())
    child = child[1:-1]
    servicetype = servicetype[1:-1]
    if (servicetype == "service"):
        if (jsonscript2['name'] != RESOURCE_NAME_AS_COMPOSITE):
            raise AssertionError("ERROR: ", jsonscript2['name'] , RESOURCE_NAME_AS_COMPOSITE)
        print(jsonscript2['name'] , RESOURCE_NAME_AS_COMPOSITE)
        if (jsonscript2['metadata']['other']['composite']['children'][0]['kind'] != "service"):
            raise AssertionError("ERROR: ", jsonscript2['metadata']['other']['composite']['children'][0]['kind'] , "service")
        print(jsonscript2['metadata']['other']['composite']['children'][0]['kind'] , "service")
        if (jsonscript2['metadata']['other']['composite']['children'][0]['name'] != RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES):
            raise AssertionError("ERROR: ", jsonscript2['metadata']['other']['composite']['children'][0]['name'] , RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES)
        print(jsonscript2['metadata']['other']['composite']['children'][0]['name'] , RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES)
        if (jsonscript2['metadata']['other']['composite']['composite_tag'] != RESOURCE_COMPOSITE_TAG):
            raise AssertionError("ERROR: ", jsonscript2['metadata']['other']['composite']['composite_tag'] , RESOURCE_COMPOSITE_TAG)
        print(jsonscript2['metadata']['other']['composite']['composite_tag'] , RESOURCE_COMPOSITE_TAG)
        if (jsonscript2['kind'] != "composite"):
            raise AssertionError("ERROR: ", jsonscript2['kind'] , "composite")
        print(jsonscript2['kind'] , "composite")

    elif (servicetype == "composite"):
        if (jsonscript2['name'] != RESOURCE_NAME_AS_COMPOSITE):
            raise AssertionError("ERROR: ", jsonscript2['name'] , RESOURCE_NAME_AS_COMPOSITE)
        print(jsonscript2['name'] , RESOURCE_NAME_AS_COMPOSITE)
        if (jsonscript2['metadata']['other']['composite']['children'][0]['kind'] != "composite"):
            raise AssertionError("ERROR: ", jsonscript2['metadata']['other']['composite']['children'][0]['kind'] , "composite")
        print(jsonscript2['metadata']['other']['composite']['children'][0]['kind'] , "composite")
        if (jsonscript2['metadata']['other']['composite']['children'][0]['name'] != RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES):
            raise AssertionError("ERROR: ", jsonscript2['metadata']['other']['composite']['children'][0]['name'] , RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES)
        print(jsonscript2['metadata']['other']['composite']['children'][0]['name'] , RESOURCE_NAME_AS_COMPOSITE + "." + RESOURCE_CONTAINED_TYPES)
        if (jsonscript2['metadata']['other']['composite']['composite_tag'] != RESOURCE_COMPOSITE_TAG):
            raise AssertionError("ERROR: ", jsonscript2['metadata']['other']['composite']['composite_tag'] , RESOURCE_COMPOSITE_TAG)
        print(jsonscript2['metadata']['other']['composite']['composite_tag'] , RESOURCE_COMPOSITE_TAG)
        if (jsonscript2['kind'] != "composite"):
            raise AssertionError("ERROR: ", jsonscript2['kind'] , "composite")
        print(jsonscript2['kind'] , "composite")

    context.web.switch_to.window(main_page)
    time.sleep(3)




@when(u'go to global catalog and update its values')
def go_to_global_catalog_and_update_its_values(context):
    context.element = context.web.find_element(*cataloglistingPage.locator_dictionary['review_offering_link'])
    context.element.click()
    time.sleep(2)
    link = context.element.get_attribute('href')
    window_before = context.web.window_handles[0]
    context.element.send_keys(Keys.CONTROL + Keys.PAGE_UP)
    time.sleep(15)
    window_after = context.web.window_handles[1]
    context.web.switch_to.window(window_after)
    time.sleep(5)
    context.web.get(link)
    time.sleep(2)
    global GLOBALCATALOGVALUES
    GLOBALCATALOGVALUES = []
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['overview_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['documentaton_url'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['terms_url'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['instructions_url'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['provisioning_url'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
#    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field'])
#    context.element.click()
#    time.sleep(3)
#    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title'])
#    oldvalue = context.element.get_attribute("value")
#    context.element.clear()
#    context.element.send_keys(UPDATEGLOBALCATALOG)
#    time.sleep(2)
#    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field'])
#    context.element.click()
#    time.sleep(3)
#    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description'])
#    oldvalue = context.element.get_attribute("value")
#    context.element.clear()
#    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
#    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url'])
    oldvalue = context.element.get_attribute("value")
    context.element.clear()
    context.element.send_keys(oldvalue + UPDATEGLOBALCATALOG)
    time.sleep(3)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['save_button'])
    context.element.send_keys(Keys.PAGE_UP)
    time.sleep(3)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(10)
    context.element.send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
    context.web.switch_to.window(window_before)
    time.sleep(10)
