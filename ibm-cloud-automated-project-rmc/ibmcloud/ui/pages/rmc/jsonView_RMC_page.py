import json
import time

import pyperclip as pyperclip
from selenium.webdriver.common.keys import Keys
from core.ui.pages.action_page import ActionPage
from core.ui.variables import constants

class jsonViewRMCPage(ActionPage):
    jsonModal_dictionary = {
        'json_view_modal': 'textarea.ace_text-input',
        'close_button': 'div.bx--modal-container.widerModal > div.bx--modal-header > button.bx--modal-close > svg.bx--modal-close__icon > path',
        'save_button': '#save-edit-btn',
        'cancel_button': '#cancel-edit-btn'
    }

    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "copy values": lambda: self.copy_values(),
            "copy values from GC": lambda: self.copy_values_from_GC(),
            "press_close_button": lambda: self.close_button(),
            "update json values": lambda value: self.update_json(value),
            "press save button": lambda: self.save_button(),
            "press_cancel_button": lambda: self.cancel_button(),
            "update_translation_values": lambda value: self.update_translation(value),
            "copy values from translation": lambda: self.copy_values_translation(),
            "copy values updated from translation": lambda value: self.copy_values_updated_translation(value),
            "copy values new language from translation": lambda value: self.copy_values_translation_new_language(value),
            "copy values new language from translation with no updates": lambda value: self.copy_values_translation_new_language_no_updates(value),
            "update_language": lambda value1,value2: self.update_language(value1,value2)
        }
        self.update_actions(**actions)

    def copy_values(self):
        constants.JSON_SCRIPT = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.CONTROL, "C")
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
#        constants.JSON_SCRIPT.update(json_script_view)
        constants.JSON_SCRIPT = json_script_view
        time.sleep(3)

    def copy_values_from_GC(self):
        constants.JSON_SCRIPT_MODALEDITOR = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.CONTROL, "C")
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
        constants.JSON_SCRIPT_MODALEDITOR.update(json_script_view)
        time.sleep(3)

    def update_json(self,value):
        constants.JSON_SCRIPT['overview_ui']['en']['description'] = constants.JSON_SCRIPT['overview_ui']['en']['description'] + value
        constants.JSON_SCRIPT['overview_ui']['en']['long_description'] = constants.JSON_SCRIPT['overview_ui']['en']['long_description'] + value
        constants.JSON_SCRIPT['images']['feature_image'] = constants.JSON_SCRIPT['images']['feature_image'] + value
        constants.JSON_SCRIPT['images']['image'] = constants.JSON_SCRIPT['images']['image'] + value
        constants.JSON_SCRIPT['images']['medium_image'] = constants.JSON_SCRIPT['images']['medium_image'] + value
        constants.JSON_SCRIPT['images']['small_image'] = constants.JSON_SCRIPT['images']['small_image'] + value
        constants.JSON_SCRIPT['provider']['name'] = constants.JSON_SCRIPT['provider']['name'] + value
        constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'] = constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'] + value
        constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'] = constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'] + value
        constants.JSON_SCRIPT['metadata']['ui']['urls']['catalog_details_url'] = constants.JSON_SCRIPT['metadata']['ui']['urls']['catalog_details_url'] + value
        constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'] = constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'] + value
        constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] = constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] + value
        constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] =  constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] + value
        constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] = constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] + value
        constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] = constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] + value
        constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] = constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] + value
        time.sleep(3)
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        elemen.send_keys(json.dumps(constants.JSON_SCRIPT))
        time.sleep(2)

    def close_button(self):
        print(constants.JSON_SCRIPT)
        print(constants.JSON_SCRIPT_MODALEDITOR)
        self.click(jsonViewRMCPage.jsonModal_dictionary['close_button'])

    def save_button(self):
        self.click(jsonViewRMCPage.jsonModal_dictionary['save_button'])
        time.sleep(10)

    def cancel_button(self):
        self.click(jsonViewRMCPage.jsonModal_dictionary['cancel_button'])
        time.sleep(2)

    def update_translation(self,value):
        constants.JSON_SCRIPT['en']['description'] = constants.JSON_SCRIPT['en']['description'] + value
        constants.JSON_SCRIPT['en']['longDescription'] = constants.JSON_SCRIPT['en']['longDescription'] + value
        constants.JSON_SCRIPT['en']['metadata']['bullets'][0]['title'] = constants.JSON_SCRIPT['en']['metadata']['bullets'][0]['title'] + value
        constants.JSON_SCRIPT['en']['metadata']['bullets'][0]['description'] = constants.JSON_SCRIPT['en']['metadata']['bullets'][0]['description'] + value
        constants.JSON_SCRIPT['en']['metadata']['longDescription'] = constants.JSON_SCRIPT['en']['metadata']['longDescription'] + value
        constants.JSON_SCRIPT['en']['metadata']['media'][0]['thumbnailUrl'] = constants.JSON_SCRIPT['en']['metadata']['media'][0]['thumbnailUrl'] + value
        constants.JSON_SCRIPT['en']['metadata']['media'][0]['url'] = constants.JSON_SCRIPT['en']['metadata']['media'][0]['url'] + value
        constants.JSON_SCRIPT['en']['metadata']['media'][0]['caption'] = constants.JSON_SCRIPT['en']['metadata']['media'][0]['caption'] + value
        time.sleep(3)


    def copy_values_updated_translation(self,value):
        constants.JSON_SCRIPT_TRANSLATION = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
        constants.JSON_SCRIPT_TRANSLATION.update(json_script_view)
        time.sleep(2)
        constants.JSON_SCRIPT_TRANSLATION['en']['description'] = constants.JSON_SCRIPT_TRANSLATION['en']['description'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'] = constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'] = constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'] = constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription'] = constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'] = constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'] = constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'] + value
        constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'] = constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'] + value
        elemen.send_keys(json.dumps(constants.JSON_SCRIPT_TRANSLATION))
        time.sleep(2)

    def copy_values_translation(self):
        constants.JSON_SCRIPT_TRANSLATION = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
        constants.JSON_SCRIPT_TRANSLATION.update(json_script_view)
        time.sleep(2)
        elemen.send_keys(json.dumps(constants.JSON_SCRIPT_TRANSLATION))
        time.sleep(2)

    def copy_values_translation_new_language(self,value):
        constants.JSON_SCRIPT_TRANSLATION = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
        newjsonscript = json_script_view.copy()
        newjsonscript[value] = newjsonscript['en']
        del newjsonscript['en']
        newjsonscript[value]['description'] = newjsonscript[value]['description'] + value
        newjsonscript[value]['longDescription'] = newjsonscript[value]['longDescription'] + value
        newjsonscript[value]['metadata']['longDescription'] = newjsonscript[value]['metadata']['longDescription'] + value
        newjsonscript[value]['metadata']['bullets'][0]['title'] = newjsonscript[value]['metadata']['bullets'][0]['title'] + value
        newjsonscript[value]['metadata']['bullets'][0]['description'] = newjsonscript[value]['metadata']['bullets'][0]['description'] + value
        newjsonscript[value]['metadata']['media'][0]['thumbnailUrl'] = newjsonscript[value]['metadata']['media'][0]['thumbnailUrl'] + value
        newjsonscript[value]['metadata']['media'][0]['url'] = newjsonscript[value]['metadata']['media'][0]['url'] + value
        newjsonscript[value]['metadata']['media'][0]['caption'] = newjsonscript[value]['metadata']['media'][0]['caption'] + value
        time.sleep(3)
        json_script_view.update(newjsonscript)
        constants.JSON_SCRIPT_TRANSLATION = json_script_view
        elemen.send_keys(json.dumps(constants.JSON_SCRIPT_TRANSLATION))
        time.sleep(2)


    def copy_values_translation_new_language_no_updates(self,value):
        constants.JSON_SCRIPT_TRANSLATION = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
        newjsonscript = json_script_view.copy()
        newjsonscript[value] = newjsonscript['en']
        del newjsonscript['en']
        newjsonscript[value]['description'] = newjsonscript[value]['description']
        newjsonscript[value]['longDescription'] = newjsonscript[value]['longDescription']
        newjsonscript[value]['metadata']['longDescription'] = newjsonscript[value]['metadata']['longDescription']
        newjsonscript[value]['metadata']['bullets'][0]['title'] = newjsonscript[value]['metadata']['bullets'][0]['title']
        newjsonscript[value]['metadata']['bullets'][0]['description'] = newjsonscript[value]['metadata']['bullets'][0]['description']
        newjsonscript[value]['metadata']['media'][0]['thumbnailUrl'] = newjsonscript[value]['metadata']['media'][0]['thumbnailUrl']
        newjsonscript[value]['metadata']['media'][0]['url'] = newjsonscript[value]['metadata']['media'][0]['url']
        newjsonscript[value]['metadata']['media'][0]['caption'] = newjsonscript[value]['metadata']['media'][0]['caption']
        time.sleep(3)
        json_script_view.update(newjsonscript)
        constants.JSON_SCRIPT_TRANSLATION = json_script_view
        elemen.send_keys(json.dumps(constants.JSON_SCRIPT_TRANSLATION))
        time.sleep(2)

    def update_language(self,value1,value2):
        constants.JSON_SCRIPT_TRANSLATION = {}
        time.sleep(2)
        global elemen
        elemen = self.find_element(jsonViewRMCPage.jsonModal_dictionary['json_view_modal'])
        elemen.send_keys(Keys.CONTROL, "A")
        time.sleep(2)
        elemen.send_keys(Keys.CONTROL, "C")
        time.sleep(2)
        elemen.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        json_script_view = json.loads(pyperclip.paste())
        newjsonscript = json_script_view.copy()
        newjsonscript[value1]['description'] = newjsonscript[value1]['description'] + value2
        newjsonscript[value1]['longDescription'] = newjsonscript[value1]['longDescription'] + value2
        newjsonscript[value1]['metadata']['longDescription'] = newjsonscript[value1]['metadata']['longDescription'] + value2
        newjsonscript[value1]['metadata']['bullets'][0]['title'] = newjsonscript[value1]['metadata']['bullets'][0]['title'] + value2
        newjsonscript[value1]['metadata']['bullets'][0]['description'] = newjsonscript[value1]['metadata']['bullets'][0]['description'] + value2
        newjsonscript[value1]['metadata']['media'][0]['thumbnailUrl'] = newjsonscript[value1]['metadata']['media'][0]['thumbnailUrl'] + value2
        newjsonscript[value1]['metadata']['media'][0]['url'] = newjsonscript[value1]['metadata']['media'][0]['url'] + value2
        newjsonscript[value1]['metadata']['media'][0]['caption'] = newjsonscript[value1]['metadata']['media'][0]['caption'] + value2
        time.sleep(3)
#        json_script_view.update(newjsonscript)
        constants.JSON_SCRIPT_TRANSLATION = newjsonscript
        elemen.send_keys(json.dumps(constants.JSON_SCRIPT_TRANSLATION))
        time.sleep(2)