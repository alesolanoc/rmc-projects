import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants


class TranslationRMCPage(FormPage,ActionPage):
    translation_dictionary = {
        'expand_example_script_button': 'button.accordion_button',
        'copy_button': 'div.bx--snippet.bx--snippet--code > button.bx--snippet-button > svg.bx--snippet__icon',
        'save_button': '//button[contains(.,"Save JSON")]',
        'discard_changes': 'div.jsonDisplay > div > button.bx--btn.bx--btn--primary'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
#            "target_release_version": lambda value: self.set_targerReleaseValue(value)
        }
        actions = {
            "expand_sample_json": lambda: self.expand_sample_json(),
            "copy_sample": lambda: self.copy_sample(),
            "press_save_button": lambda: self.save_button_translation(),
            "verify_translation_script_equal_CL": lambda: self.verify_translation_equal_CL(),
            "verify_translation_script_equal_json_from_CL": lambda: self.verify_translation_equal_json_CL(),
            "verify_translation_script_equal_than_GC": lambda: self.verify_translation_equal_GC(),
            "verify_translation_equal_than_json_script_from_gc": lambda: self.verify_translation_equal_json_GC(),
            "verify_translation_with_new_language_equal_than_json_script_from_CL": lambda value: self.verify_translation_added_equal_json_CL(value),
            "verify_translation_with_new_language_equal_than_global_catalog_values": lambda value: self.verify_translation_added_equal_GC(value),
            "verify_translation_with_new_language_equal_than_json_script_from_gc": lambda value: self.verify_translation_added_equal_json_GC(value),
            "press_discard_changes_button": lambda: self.discard_changes(),
            "verify11": lambda: self.verify11()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def expand_sample_json(self):
        time.sleep(2)
        self.click(TranslationRMCPage.translation_dictionary['expand_example_script_button'])
        time.sleep(2)

    def copy_sample(self):
        time.sleep(2)
        self.click(TranslationRMCPage.translation_dictionary['copy_button'])
        time.sleep(2)

    def save_button_translation(self):
        time.sleep(2)
        self.click(TranslationRMCPage.translation_dictionary['save_button'])
        time.sleep(20)

    def verify_translation_equal_CL(self):
        print(constants.VALUES_FROM_CATALOG_LISTING)
        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'],constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['displayName'] != constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.VALUES_FROM_CATALOG_LISTING['description'],constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['longDescription'],constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        if (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] != constants.JSON_SCRIPT_TRANSLATION['en']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        print(constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        print(constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['displayName'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['displayName']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['displayName'])
        print(constants.VALUES_FROM_CATALOG_LISTING['longDescription'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription'])
        if (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription'])
        print(constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'][1][1])


    def verify_translation_equal_json_CL(self):
        print(constants.JSON_SCRIPT)
        print(constants.JSON_SCRIPT['metadata']['displayName'],constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.JSON_SCRIPT['metadata']['displayName'] != constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ",constants.JSON_SCRIPT['metadata']['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.JSON_SCRIPT['name'],constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.JSON_SCRIPT['name'] not in constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ",constants.JSON_SCRIPT['name'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.JSON_SCRIPT['description'],constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        if (constants.JSON_SCRIPT['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        print(constants.JSON_SCRIPT['metadata']['longDescription'],constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        if (constants.JSON_SCRIPT['metadata']['longDescription'] != constants.JSON_SCRIPT_TRANSLATION['en']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['bullets'][0]['title'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['bullets'][0]['title'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['bullets'][0]['description'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['bullets'][0]['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        print(constants.JSON_SCRIPT['metadata']['media'][0]['type'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['media'][0]['type'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['media'][0]['url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['media'][0]['url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['media'][0]['caption'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['media'][0]['caption'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        print(constants.JSON_SCRIPT['name'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['displayName'])
        if (constants.JSON_SCRIPT['name'] not in  constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['displayName']):
            raise AssertionError("---> ERROR: ",constants.JSON_SCRIPT['name'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['displayName'])
        print(constants.JSON_SCRIPT['metadata']['longDescription'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription'])
        if (constants.JSON_SCRIPT['metadata']['longDescription'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['longDescription'])

        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['description'],constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['displayName'],constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['displayName'] != constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['longDescription'],constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['longDescription'] != constants.JSON_SCRIPT_TRANSLATION['en']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['title'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['title'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['description'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['type'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['type'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['caption'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['caption'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['longDescription'], constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['longDescription'] != constants.JSON_SCRIPT_TRANSLATION['en']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['displayName'], constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['displayName'] != constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.JSON_SCRIPT['mediumImageUrl'][1][1])

    def verify_translation_equal_GC(self):
        print(constants.VALUES_FROM_GLOBAL_CATALOG)
        print(constants.VALUES_FROM_GLOBAL_CATALOG['displayName'],constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] != constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['short_description'],constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] != constants.JSON_SCRIPT_TRANSLATION['en']['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['long_description'],constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] != constants.JSON_SCRIPT_TRANSLATION['en']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['media_type'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['media_url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['mediumImageUrl'][1][1])

    def verify_translation_equal_json_GC(self):
        print(constants.JSON_SCRIPT)
        print(constants.JSON_SCRIPT['overview_ui']['en']['display_name'],constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['display_name'] != constants.JSON_SCRIPT_TRANSLATION['en']['displayName']):
            raise AssertionError("---> ERROR: ",constants.JSON_SCRIPT['overview_ui']['en']['display_name'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['displayName'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['description'],constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['description'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['long_description'],constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['long_description'] != constants.JSON_SCRIPT_TRANSLATION['en']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['long_description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'],constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['bullets'][0]['description'])

        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'], constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] != constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION['en']['metadata']['media'][0]['caption'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['mediumImageUrl'][1][1])

    def verify_translation_added_equal_json_CL(self,value):
        print(constants.JSON_SCRIPT)
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['description'],constants.JSON_SCRIPT_TRANSLATION[value]['description'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['description'] != constants.JSON_SCRIPT_TRANSLATION[value]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['description'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['displayName'],constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['displayName'] != constants.JSON_SCRIPT_TRANSLATION[value]['displayName']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['longDescription'],constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['longDescription'] != constants.JSON_SCRIPT_TRANSLATION[value]['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['bullets'][0]['title'],constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['bullets'][0]['title'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['bullets'][0]['description'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['bullets'][0]['description'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['type'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['type'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['thumbnailUrl'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['thumbnailUrl'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['url'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['url'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['caption'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['caption'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['longDescription'], constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['longDescription'] != constants.JSON_SCRIPT_TRANSLATION[value]['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['longDescription'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['displayName'], constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        if (constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['displayName'] != constants.JSON_SCRIPT_TRANSLATION[value]['displayName']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['i18n'][value]['metadata']['displayName'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])

    def verify_translation_added_equal_GC(self,value):
        print("alejo ",constants.VALUES_FROM_GLOBAL_CATALOG)
        tempValue = value + "_displayName"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue],constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['displayName']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        tempValue = value + "_short_description"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue],constants.JSON_SCRIPT_TRANSLATION[value]['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['description'])
        tempValue = value + "_long_description"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue],constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        tempValue = value + "_bullet_title"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue],constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title'])
        tempValue = value + "_bullet_description"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description'])
        tempValue = value + "_media_type"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type'])
        tempValue = value + "_thumbnail_url"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl'])
        tempValue = value + "_media_url"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url'])
        tempValue = value + "_caption_image"
        print(constants.VALUES_FROM_GLOBAL_CATALOG[tempValue], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG[tempValue] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption'])
#        print(constants.VALUES_FROM_GLOBAL_CATALOG['mediumImageUrl'][1][1])

    def verify_translation_added_equal_json_GC(self,value):
        print(constants.JSON_SCRIPT['overview_ui'][value]['display_name'],constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        if (constants.JSON_SCRIPT['overview_ui'][value]['display_name'] != constants.JSON_SCRIPT_TRANSLATION[value]['displayName']):
            raise AssertionError("---> ERROR: ",constants.JSON_SCRIPT['overview_ui'][value]['display_name'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['displayName'])
        print(constants.JSON_SCRIPT['overview_ui'][value]['description'],constants.JSON_SCRIPT_TRANSLATION[value]['description'])
        if (constants.JSON_SCRIPT['overview_ui'][value]['description'] != constants.JSON_SCRIPT_TRANSLATION[value]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui'][value]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['description'])
        print(constants.JSON_SCRIPT['overview_ui'][value]['long_description'],constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        if (constants.JSON_SCRIPT['overview_ui'][value]['long_description'] != constants.JSON_SCRIPT_TRANSLATION[value]['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui'][value]['long_description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['longDescription'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['bullets'][0]['title'],constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['bullets'][0]['title'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['bullets'][0]['description'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['bullets'][0]['description'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['bullets'][0]['description'])

        print(constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['type'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['type'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['thumbnail_url'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['thumbnail_url'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['url'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['url'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['caption'], constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['caption'] != constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings'][value]['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_TRANSLATION[value]['metadata']['media'][0]['caption'])

    def discard_changes(self):
        time.sleep(2)
        self.click(TranslationRMCPage.translation_dictionary['discard_changes'])
        time.sleep(2)


    def verify11(self):
#        print(constants.JSON_SCRIPT['mediumImageUrl'][1][1])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['mediumImageUrl'][1][1])
