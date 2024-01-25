import json
import time
import pyperclip

from behave import then
from selenium.webdriver.common.keys import Keys

from Constants.variables import UPDATEVALUEJSONSCRIPT, UPDATEVALUEJSONSCRIPTLANGUAGE
from Pages.getting_start_page_dictionary import gettingStartPage
from Pages.global_catalog_page_dictionary import globalcatalogPage
from Pages.translation_page_dictionary import translationPage


@then(u'select translation option')
def select_translation_option(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['translation_option'])
    context.element.click()
    time.sleep(2)

@then(u'expand translation json sample')
def expand_translation(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['expand_example_script_button'])
    context.element.click()
    time.sleep(5)

@then(u'copy translation from json sample')
def copy_translation(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['copy_button'])
    context.element.click()
    time.sleep(5)

@then(u'paste json example into json editor')
def paste_json_example(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*translationPage.locator_dictionary['json_view_modal'])
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    jsonscript['en']['description'] = jsonscript['en']['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['longDescription'] = jsonscript['en']['longDescription'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['longDescription'] = jsonscript['en']['metadata']['longDescription'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['bullets'][0]['title'] = jsonscript['en']['metadata']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['bullets'][0]['description'] = jsonscript['en']['metadata']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['thumbnailUrl'] = jsonscript['en']['metadata']['media'][0]['thumbnailUrl'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['url'] = jsonscript['en']['metadata']['media'][0]['url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['caption'] = jsonscript['en']['metadata']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPT
    time.sleep(3)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(3)

@then(u'paste json example into json editor with new language')
def paste_json_example(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*translationPage.locator_dictionary['json_view_modal'])
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    newjsonscript = jsonscript.copy()
    newjsonscript['fr'] = newjsonscript['en']
    del newjsonscript['en']
    newjsonscript['fr']['description'] = newjsonscript['fr']['description'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['longDescription'] = newjsonscript['fr']['longDescription'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['longDescription'] = newjsonscript['fr']['metadata']['longDescription'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['bullets'][0]['title'] = newjsonscript['fr']['metadata']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['bullets'][0]['description'] = newjsonscript['fr']['metadata']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['thumbnailUrl'] = newjsonscript['fr']['metadata']['media'][0]['thumbnailUrl'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['url'] = newjsonscript['fr']['metadata']['media'][0]['url'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['caption'] = newjsonscript['fr']['metadata']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    time.sleep(3)
    jsonscript.update(newjsonscript)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(3)


@then(u'save json script')
def save_json_script(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(20)

@then(u'press close button')
def close_success_popup(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*gettingStartPage.locator_dictionary['getting_start_close_button'])
    context.element.click()
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(2)


@then(u'go to {language} language tab')
def go_to_language_tag(context,language):
    time.sleep(2)
    language = language[1:-1]
    if (language == "fr"):
        context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['fr_languaje'])
        context.element.click()
        time.sleep(2)
    elif (language == "en"):
        context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['en_languaje'])
        context.element.click()
        time.sleep(2)


@then(u'get global catalog values from {language} to be compared with translations')
def get_catalog_list_values(context,language):
    language = language[1:-1]
    global RESOURCE_GLOBAL_CATALOG_LIST1
    RESOURCE_GLOBAL_CATALOG_LIST1 = []
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(4)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['display_name-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field-' + language])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field-' + language])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))



@then(u'validate {language} translate language against global catalog')
def validate_trans_against_gc(context,language):
    language = language[1:-1]
    if (jsonscript[language]['description'] != RESOURCE_GLOBAL_CATALOG_LIST1[1]):
        raise AssertionError("ERROR: ", jsonscript[language]['description'] , RESOURCE_GLOBAL_CATALOG_LIST1[1])
    print(jsonscript[language]['description'], RESOURCE_GLOBAL_CATALOG_LIST1[1])

    if (jsonscript[language]['longDescription'] != RESOURCE_GLOBAL_CATALOG_LIST1[2]):
        raise AssertionError("ERROR: ", jsonscript[language]['longDescription'] , RESOURCE_GLOBAL_CATALOG_LIST1[2])
    print(jsonscript[language]['longDescription'], RESOURCE_GLOBAL_CATALOG_LIST1[2])

    if (jsonscript[language]['metadata']['bullets'][0]['title'] != RESOURCE_GLOBAL_CATALOG_LIST1[3]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['bullets'][0]['title'] , RESOURCE_GLOBAL_CATALOG_LIST1[3])
    print(jsonscript[language]['metadata']['bullets'][0]['title'], RESOURCE_GLOBAL_CATALOG_LIST1[3])

    if (jsonscript[language]['metadata']['bullets'][0]['description'] != RESOURCE_GLOBAL_CATALOG_LIST1[4]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['bullets'][0]['description'] , RESOURCE_GLOBAL_CATALOG_LIST1[4])
    print(jsonscript[language]['metadata']['bullets'][0]['description'], RESOURCE_GLOBAL_CATALOG_LIST1[4])

    if (jsonscript[language]['metadata']['media'][0]['caption'] != RESOURCE_GLOBAL_CATALOG_LIST1[5]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['media'][0]['caption'] , RESOURCE_GLOBAL_CATALOG_LIST1[5])
    print(jsonscript[language]['metadata']['media'][0]['caption'], RESOURCE_GLOBAL_CATALOG_LIST1[5])

    if (jsonscript[language]['metadata']['media'][0]['url'] != RESOURCE_GLOBAL_CATALOG_LIST1[6]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['media'][0]['url'] , RESOURCE_GLOBAL_CATALOG_LIST1[6])
    print(jsonscript[language]['metadata']['media'][0]['url'], RESOURCE_GLOBAL_CATALOG_LIST1[6])


@then(u'select translation option')
def select_translation_option(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['translation_option'])
    context.element.click()
    time.sleep(2)

@then(u'expand translation json sample')
def expand_translation(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['expand_example_script_button'])
    context.element.click()
    time.sleep(5)

@then(u'copy translation from json sample')
def copy_translation(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['copy_button'])
    context.element.click()
    time.sleep(5)

@then(u'paste json example into json editor')
def paste_json_example(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*translationPage.locator_dictionary['json_view_modal'])
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    jsonscript['en']['description'] = jsonscript['en']['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['longDescription'] = jsonscript['en']['longDescription'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['longDescription'] = jsonscript['en']['metadata']['longDescription'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['bullets'][0]['title'] = jsonscript['en']['metadata']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['bullets'][0]['description'] = jsonscript['en']['metadata']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['thumbnailUrl'] = jsonscript['en']['metadata']['media'][0]['thumbnailUrl'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['url'] = jsonscript['en']['metadata']['media'][0]['url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['caption'] = jsonscript['en']['metadata']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPT
    time.sleep(3)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(3)

@then(u'paste json example into json editor with new language')
def paste_json_example(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*translationPage.locator_dictionary['json_view_modal'])
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    newjsonscript = jsonscript.copy()
    newjsonscript['fr'] = newjsonscript['en']
    del newjsonscript['en']
    newjsonscript['fr']['description'] = newjsonscript['fr']['description'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['longDescription'] = newjsonscript['fr']['longDescription'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['longDescription'] = newjsonscript['fr']['metadata']['longDescription'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['bullets'][0]['title'] = newjsonscript['fr']['metadata']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['bullets'][0]['description'] = newjsonscript['fr']['metadata']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['thumbnailUrl'] = newjsonscript['fr']['metadata']['media'][0]['thumbnailUrl'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['url'] = newjsonscript['fr']['metadata']['media'][0]['url'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['caption'] = newjsonscript['fr']['metadata']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    time.sleep(3)
    jsonscript.update(newjsonscript)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(3)


@then(u'save json script')
def save_json_script(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(20)

@then(u'press close button')
def close_success_popup(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*gettingStartPage.locator_dictionary['getting_start_close_button'])
    context.element.click()
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(2)


@then(u'go to {language} language tab')
def go_to_language_tag(context,language):
    time.sleep(2)
    language = language[1:-1]
    if (language == "fr"):
        context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['fr_languaje'])
        context.element.click()
        time.sleep(2)
    elif (language == "en"):
        context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['en_languaje'])
        context.element.click()
        time.sleep(2)


@then(u'get global catalog values from {language} to be compared with translations')
def get_catalog_list_values(context,language):
    language = language[1:-1]
    global RESOURCE_GLOBAL_CATALOG_LIST1
    RESOURCE_GLOBAL_CATALOG_LIST1 = []
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(4)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['display_name-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field-' + language])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field-' + language])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))



@then(u'validate {language} translate language against global catalog')
def validate_trans_against_gc(context,language):
    language = language[1:-1]
    if (jsonscript[language]['description'] != RESOURCE_GLOBAL_CATALOG_LIST1[1]):
        raise AssertionError("ERROR: ", jsonscript[language]['description'] , RESOURCE_GLOBAL_CATALOG_LIST1[1])
    print(jsonscript[language]['description'], RESOURCE_GLOBAL_CATALOG_LIST1[1])

    if (jsonscript[language]['longDescription'] != RESOURCE_GLOBAL_CATALOG_LIST1[2]):
        raise AssertionError("ERROR: ", jsonscript[language]['longDescription'] , RESOURCE_GLOBAL_CATALOG_LIST1[2])
    print(jsonscript[language]['longDescription'], RESOURCE_GLOBAL_CATALOG_LIST1[2])

    if (jsonscript[language]['metadata']['bullets'][0]['title'] != RESOURCE_GLOBAL_CATALOG_LIST1[3]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['bullets'][0]['title'] , RESOURCE_GLOBAL_CATALOG_LIST1[3])
    print(jsonscript[language]['metadata']['bullets'][0]['title'], RESOURCE_GLOBAL_CATALOG_LIST1[3])

    if (jsonscript[language]['metadata']['bullets'][0]['description'] != RESOURCE_GLOBAL_CATALOG_LIST1[4]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['bullets'][0]['description'] , RESOURCE_GLOBAL_CATALOG_LIST1[4])
    print(jsonscript[language]['metadata']['bullets'][0]['description'], RESOURCE_GLOBAL_CATALOG_LIST1[4])

    if (jsonscript[language]['metadata']['media'][0]['caption'] != RESOURCE_GLOBAL_CATALOG_LIST1[5]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['media'][0]['caption'] , RESOURCE_GLOBAL_CATALOG_LIST1[5])
    print(jsonscript[language]['metadata']['media'][0]['caption'], RESOURCE_GLOBAL_CATALOG_LIST1[5])

    if (jsonscript[language]['metadata']['media'][0]['url'] != RESOURCE_GLOBAL_CATALOG_LIST1[6]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['media'][0]['url'] , RESOURCE_GLOBAL_CATALOG_LIST1[6])
    print(jsonscript[language]['metadata']['media'][0]['url'], RESOURCE_GLOBAL_CATALOG_LIST1[6])


@then(u'select translation option')
def select_translation_option(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['translation_option'])
    context.element.click()
    time.sleep(2)

@then(u'expand translation json sample')
def expand_translation(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['expand_example_script_button'])
    context.element.click()
    time.sleep(5)

@then(u'copy translation from json sample')
def copy_translation(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['copy_button'])
    context.element.click()
    time.sleep(5)

@then(u'paste json example into json editor')
def paste_json_example(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*translationPage.locator_dictionary['json_view_modal'])
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    jsonscript['en']['description'] = jsonscript['en']['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['longDescription'] = jsonscript['en']['longDescription'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['longDescription'] = jsonscript['en']['metadata']['longDescription'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['bullets'][0]['title'] = jsonscript['en']['metadata']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['bullets'][0]['description'] = jsonscript['en']['metadata']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['thumbnailUrl'] = jsonscript['en']['metadata']['media'][0]['thumbnailUrl'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['url'] = jsonscript['en']['metadata']['media'][0]['url'] + UPDATEVALUEJSONSCRIPT
    jsonscript['en']['metadata']['media'][0]['caption'] = jsonscript['en']['metadata']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPT
    time.sleep(3)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(3)

@then(u'paste json example into json editor with new language')
def paste_json_example(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    time.sleep(2)
    context.element = context.web.find_element(*translationPage.locator_dictionary['json_view_modal'])
    global jsonscript
    jsonscript = json.loads(pyperclip.paste())
    newjsonscript = jsonscript.copy()
    newjsonscript['fr'] = newjsonscript['en']
    del newjsonscript['en']
    newjsonscript['fr']['description'] = newjsonscript['fr']['description'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['longDescription'] = newjsonscript['fr']['longDescription'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['longDescription'] = newjsonscript['fr']['metadata']['longDescription'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['bullets'][0]['title'] = newjsonscript['fr']['metadata']['bullets'][0]['title'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['bullets'][0]['description'] = newjsonscript['fr']['metadata']['bullets'][0]['description'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['thumbnailUrl'] = newjsonscript['fr']['metadata']['media'][0]['thumbnailUrl'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['url'] = newjsonscript['fr']['metadata']['media'][0]['url'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    newjsonscript['fr']['metadata']['media'][0]['caption'] = newjsonscript['fr']['metadata']['media'][0]['caption'] + UPDATEVALUEJSONSCRIPTLANGUAGE
    time.sleep(3)
    jsonscript.update(newjsonscript)
    context.element.send_keys(Keys.CONTROL, "A")
    time.sleep(2)
    context.element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    context.element.send_keys(json.dumps(jsonscript))
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(3)


@then(u'save json script')
def save_json_script(context):
    context.element = context.web.find_element(*translationPage.locator_dictionary['save_button'])
    context.element.click()
    time.sleep(20)

@then(u'press close button')
def close_success_popup(context):
    main_page = context.web.current_window_handle
    main_window_handle = None
    context.element = context.web.find_element(*gettingStartPage.locator_dictionary['getting_start_close_button'])
    context.element.click()
    time.sleep(2)
    context.web.switch_to.window(main_page)
    time.sleep(2)


@then(u'go to {language} language tab')
def go_to_language_tag(context,language):
    time.sleep(2)
    language = language[1:-1]
    if (language == "fr"):
        context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['fr_languaje'])
        context.element.click()
        time.sleep(2)
    elif (language == "en"):
        context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['en_languaje'])
        context.element.click()
        time.sleep(2)


@then(u'get global catalog values from {language} to be compared with translations')
def get_catalog_list_values(context,language):
    language = language[1:-1]
    global RESOURCE_GLOBAL_CATALOG_LIST1
    RESOURCE_GLOBAL_CATALOG_LIST1 = []
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['content_tab'])
    context.element.click()
    time.sleep(4)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['display_name-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['long_description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title_field-' + language])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_title-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description_field-' + language])
    context.element.click()
    time.sleep(2)
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['bullet_description-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_caption-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))
    context.element = context.web.find_element(*globalcatalogPage.locator_dictionary['media_url-' + language])
    RESOURCE_GLOBAL_CATALOG_LIST1.append(context.element.get_attribute("value"))



@then(u'validate {language} translate language against global catalog')
def validate_trans_against_gc(context,language):
    language = language[1:-1]
    if (jsonscript[language]['description'] != RESOURCE_GLOBAL_CATALOG_LIST1[1]):
        raise AssertionError("ERROR: ", jsonscript[language]['description'] , RESOURCE_GLOBAL_CATALOG_LIST1[1])
    print(jsonscript[language]['description'], RESOURCE_GLOBAL_CATALOG_LIST1[1])

    if (jsonscript[language]['longDescription'] != RESOURCE_GLOBAL_CATALOG_LIST1[2]):
        raise AssertionError("ERROR: ", jsonscript[language]['longDescription'] , RESOURCE_GLOBAL_CATALOG_LIST1[2])
    print(jsonscript[language]['longDescription'], RESOURCE_GLOBAL_CATALOG_LIST1[2])

    if (jsonscript[language]['metadata']['bullets'][0]['title'] != RESOURCE_GLOBAL_CATALOG_LIST1[3]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['bullets'][0]['title'] , RESOURCE_GLOBAL_CATALOG_LIST1[3])
    print(jsonscript[language]['metadata']['bullets'][0]['title'], RESOURCE_GLOBAL_CATALOG_LIST1[3])

    if (jsonscript[language]['metadata']['bullets'][0]['description'] != RESOURCE_GLOBAL_CATALOG_LIST1[4]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['bullets'][0]['description'] , RESOURCE_GLOBAL_CATALOG_LIST1[4])
    print(jsonscript[language]['metadata']['bullets'][0]['description'], RESOURCE_GLOBAL_CATALOG_LIST1[4])

    if (jsonscript[language]['metadata']['media'][0]['caption'] != RESOURCE_GLOBAL_CATALOG_LIST1[5]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['media'][0]['caption'] , RESOURCE_GLOBAL_CATALOG_LIST1[5])
    print(jsonscript[language]['metadata']['media'][0]['caption'], RESOURCE_GLOBAL_CATALOG_LIST1[5])

    if (jsonscript[language]['metadata']['media'][0]['url'] != RESOURCE_GLOBAL_CATALOG_LIST1[6]):
        raise AssertionError("ERROR: ", jsonscript[language]['metadata']['media'][0]['url'] , RESOURCE_GLOBAL_CATALOG_LIST1[6])
    print(jsonscript[language]['metadata']['media'][0]['url'], RESOURCE_GLOBAL_CATALOG_LIST1[6])

