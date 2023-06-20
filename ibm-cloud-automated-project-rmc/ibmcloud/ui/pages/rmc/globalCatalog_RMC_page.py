import time

from selenium.webdriver.common.keys import Keys

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants
from ibmcloud.ui.pages.rmc.catalogListing_RMC_page import CatalogListingRMCPage


class GlobalCatalogRMCPage(FormPage,ActionPage):
    globalCatalogContent_dictionary = {
        'content_tab': '#content-link',
        'overview_tab': '#overview-link',
        'tags_tab': '#tags-link',
        'en_tab': '//ul[@id="content-languages-list"]/li/a',
        'fr_tab': '//ul[@id="content-languages-list"]/li[2]/a',
        'display_name': '#en-display-name-input',
        'shot_description': '#en-desc-textarea',
        'long_description': '#en-long-desc-textarea',
        'thumbnail': '#en-0-media-thumbnail-url',
        'thumbnail_url': '//div[@id="en-0-media"]/div/div[3]/input',
        'caption_image': '//div[@id="en-0-media"]/div[2]/input',
        'media_type': '//select[@id="en-0-media-type-input"]',
        'media_url': '//input[@id="en-0-media-url-input"]',
        'bullet_title': '//div[@id="en-0-bullet-title"]',
        'bullet_title_field': '//input[@id="en-0-bullet-title-input"]',
        'bullet_description': '//div[@id="en-0-bullet-desc"]',
        'bullet_description_field': '//textarea[@id="en-0-bullet-desc-input"]',
        'en_display_name': '#en-display-name-input',
        'en_shot_description': '#en-desc-textarea',
        'en_long_description': '#en-long-desc-textarea',
        'en_thumbnail': '#en-0-media-thumbnail-url',
        'en_thumbnail_url': '//div[@id="en-0-media"]/div/div[3]/input',
        'en_caption_image': '//div[@id="en-0-media"]/div[2]/input',
        'en_media_type': '//select[@id="en-0-media-type-input"]',
        'en_media_url': '//input[@id="en-0-media-url-input"]',
        'en_bullet_title': '//div[@id="en-0-bullet-title"]',
        'en_bullet_title_field': '//input[@id="en-0-bullet-title-input"]',
        'en_bullet_description': '//div[@id="en-0-bullet-desc"]',
        'en_bullet_description_field': '//textarea[@id="en-0-bullet-desc-input"]',
        'fr_display_name': '#fr-display-name-input',
        'fr_shot_description': '#fr-desc-textarea',
        'fr_long_description': '#fr-long-desc-textarea',
        'fr_thumbnail': '#fr-0-media-thumbnail-url',
        'fr_thumbnail_url': '//div[@id="fr-0-media"]/div/div[3]/input',
        'fr_caption_image': '//div[@id="fr-0-media"]/div[2]/input',
        'fr_media_type': '//select[@id="fr-0-media-type-input"]',
        'fr_media_url': '//input[@id="fr-0-media-url-input"]',
        'fr_bullet_title': '//div[@id="fr-0-bullet-title"]',
        'fr_bullet_title_field': '//input[@id="fr-0-bullet-title-input"]',
        'fr_bullet_description': '//div[@id="fr-0-bullet-desc"]',
        'fr_bullet_description_field': '//textarea[@id="fr-0-bullet-desc-input"]',
        'programmatic_name': '#name-input',
        'author': '//div[@id="overview-panel"]/div/div/div[3]/div[2]/p',
        'feature_image': '#feature-img',
        'feature_image_field': '//div[@id="images-section"]/div/div[2]/input',
        'image': '#image-img',
        'image_field': '//div[@id="images-section"]/div[2]/div[2]/input',
        'medium_image': '#medium-img',
        'medium_image_field': '//div[@id="images-section"]/div[3]/div[2]/input',
        'small_image': '#small-img',
        'small_image_field': '//div[@id="images-section"]/div[4]/div[2]/input',
        'documentation_url': '#doc-url-input',
        'terms_url': '#terms-url-input',
        'instructions_url': '#instructions-url-input',
        'custom_url': '#catalog-details-url-input',
        'ai': '//div[@id="tags-container"]/span',
        'analytics': '//div[@id="tags-container"]/span[2]',
        'Blockchain': '//div[@id="tags-container"]/span[3]',
        'compute': '//div[@id="tags-container"]/span[4]',
        'containers': '//div[@id="tags-container"]/span[5]',
        'databases': '//div[@id="tags-container"]/span[6]',
        'DevOps': '//div[@id="tags-container"]/span[7]',
        'Integration': '//div[@id="tags-container"]/span[8]',
        'iot': '//div[@id="tags-container"]/span[9]',
        'logging_monitoring': '//div[@id="tags-container"]/span[10]',
        'migration_tools': '//div[@id="tags-container"]/span[11]',
        'Mobile': '//div[@id="tags-container"]/span[12]',
        'Network': '//div[@id="tags-container"]/span[13]',
        'platform_services': '//div[@id="tags-container"]/span[14]',
        'Security': '//div[@id="tags-container"]/span[15]',
        'Storage': '//div[@id="tags-container"]/span[16]',
        'tree_dots': 'circle',
        'edit_action': '#edit-json-btn',
        'save_button': '#save-btn',
        'get_composite_label': '.bx--label-description.bx--label-sub-header'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "update_content_values": lambda value: self.update_content_values(value),
            "update_overview_values": lambda value: self.update_overview_values(value)
        }
        actions = {
            "go to tab in GC": lambda value: self.select_content_tab(value),
            "go to language tab": lambda value: self.select_language_tab(value),
            "get content values": lambda: self.get_content_values(),
            "get content values fr": lambda value: self.get_content_values_fr_language(value),
            "get content values1": lambda: self.get_content_value1s(),
            "get overview values": lambda: self.get_overview_values(),
            "get tag values": lambda: self.get_tag_values(),
            "verify CL against GC": lambda: self.verify_CL_against_GC(),
            "press_tree_dots": lambda: self.press_tree_dots(),
            "press_edit_action": lambda: self.press_edit_Action(),
            "verify jsonGC against GC": lambda: self.verify_jsonGC_against_GC(),
            "press save button": lambda: self.press_save_button(),
            "go back to RMC": lambda: self.go_to_RMC(),
            "verify GC against Json script view modal": lambda: self.verify_GC_against_js_modal_view(),
            "get_composite_label": lambda value: self.get_composite_label(value),
            "validate_reference": lambda value,value1,value2,value3: self.validate_type(value,value1,value2,value3),
            "validate_service_reference": lambda value1,value2,value3: self.validate_service(value1,value2,value3)
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)


    def select_content_tab(self,value):
        if (value.upper() == "CONTENT"):
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['content_tab'])
            time.sleep(2)
        elif (value.upper() == "OVERVIEW"):
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['overview_tab'])
            time.sleep(2)
        elif (value.upper() == "TAGS"):
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['tags_tab'])
            time.sleep(2)

    def select_language_tab(self,value):
        if (value.upper() == "EN"):
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['en_tab'])
            time.sleep(2)
        elif (value.upper() == "FR"):
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['fr_tab'])
            time.sleep(2)

    def get_content_values(self):
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG={}
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'displayName': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['display_name'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'short_description': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['shot_description'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'long_description': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['long_description'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'thumbnail_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail_url'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'media_type': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_type'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_url'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'caption_image': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['caption_image'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'bullet_title': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title_field'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'bullet_description': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description_field'])})

    def get_overview_values(self):
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'pragmmaticName': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['programmatic_name'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'author': self.get_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['author'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'feature_media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image_field'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'image_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image_field'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'medium_media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image_field'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image'])
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'semall_media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'documentation_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['documentation_url'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'terms_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['terms_url'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'instructions_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['instructions_url'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'custom_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'])})

    def get_tag_values(self):
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG['tags'] = []
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['ai'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('ai')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['analytics'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('analytics')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['Blockchain'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('blockchain')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['compute'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('compute')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['containers'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('containers')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['databases'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('databases')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['DevOps'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('devops')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['Integration'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('integration')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['iot'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('iot')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['logging_monitoring'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('logging_monitoring')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['migration_tools'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('migration_tools')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['Mobile'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('mobile')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['Network'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('network')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['platform_services'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('platform_services')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['Security'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('security')
        if (self.is_existing(GlobalCatalogRMCPage.globalCatalogContent_dictionary['Storage'])):
            constants.VALUES_FROM_GLOBAL_CATALOG['tags'].append('storage')
        print(constants.VALUES_FROM_GLOBAL_CATALOG)

    def verify_CL_against_GC(self):
        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'] , constants.VALUES_FROM_GLOBAL_CATALOG['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['displayName'] != constants.VALUES_FROM_GLOBAL_CATALOG['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['displayName'])
        print(constants.VALUES_FROM_CATALOG_LISTING['description'] , constants.VALUES_FROM_GLOBAL_CATALOG['short_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['description'] != constants.VALUES_FROM_GLOBAL_CATALOG['short_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['description'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['short_description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['longDescription'] , constants.VALUES_FROM_GLOBAL_CATALOG['long_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] != constants.VALUES_FROM_GLOBAL_CATALOG['long_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['longDescription'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['long_description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] , constants.VALUES_FROM_GLOBAL_CATALOG['media_type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] != constants.VALUES_FROM_GLOBAL_CATALOG['media_type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['media_type'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] , constants.VALUES_FROM_GLOBAL_CATALOG['media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] != constants.VALUES_FROM_GLOBAL_CATALOG['media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['media_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] , constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] != constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'])
        print(constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] , constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] != constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'] , constants.VALUES_FROM_GLOBAL_CATALOG['pragmmaticName'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['pragmmaticName'] not in constants.VALUES_FROM_CATALOG_LISTING['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['pragmmaticName'])
        print(constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] , constants.VALUES_FROM_GLOBAL_CATALOG['author'])
        if (constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] != constants.VALUES_FROM_GLOBAL_CATALOG['author']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['author'])
        print(constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['image_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['image_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['imagfeaturedImageUrle_url'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['image_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['terms_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['catalogDetailsUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['custom_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['catalogDetailsUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['custom_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['catalogDetailsUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['custom_url'])
        for word in constants.VALUES_FROM_CATALOG_LISTING['tags']:
            print(word)
            if (word not in constants.VALUES_FROM_GLOBAL_CATALOG['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in Global Catalog")
        print(constants.VALUES_FROM_CATALOG_LISTING['catalogDetailsUrl'][1][1],constants.VALUES_FROM_GLOBAL_CATALOG['custom_url'])

    def press_tree_dots(self):
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['tree_dots'])
        time.sleep(2)

    def press_edit_Action(self):
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['edit_action'])
        time.sleep(2)

    def verify_jsonGC_against_GC(self):
        print(constants.VALUES_FROM_GLOBAL_CATALOG)
        print(constants.JSON_SCRIPT)
        print(constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] , constants.JSON_SCRIPT['overview_ui']['en']['display_name'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] != constants.JSON_SCRIPT['overview_ui']['en']['display_name']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] + " -not equal- " + constants.JSON_SCRIPT['overview_ui']['en']['display_name'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] , constants.JSON_SCRIPT['overview_ui']['en']['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] != constants.JSON_SCRIPT['overview_ui']['en']['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] + " -not equal- " + constants.JSON_SCRIPT['overview_ui']['en']['description'])
#        print (constants.VALUES_FROM_GLOBAL_CATALOG['author'] , constants.JSON_SCRIPT['provider']['name'])
#        if (constants.VALUES_FROM_GLOBAL_CATALOG['author'] != constants.JSON_SCRIPT['provider']['name']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['author'] + " -not equal- " + constants.JSON_SCRIPT['provider']['name'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] , constants.JSON_SCRIPT['overview_ui']['en']['long_description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] != constants.JSON_SCRIPT['overview_ui']['en']['long_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] + " -not equal- " + constants.JSON_SCRIPT['overview_ui']['en']['long_description'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'] , constants.JSON_SCRIPT['images']['feature_image'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'] != constants.JSON_SCRIPT['images']['feature_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'] + " -not equal- " + constants.JSON_SCRIPT['images']['feature_image'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'] , constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'] != constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'] , constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'] != constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] , constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] , constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] , constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] , constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] , constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] , constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'] , constants.JSON_SCRIPT['images']['small_image'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'] != constants.JSON_SCRIPT['images']['small_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'] + " -not equal- " + constants.JSON_SCRIPT['images']['small_image'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['image_url'] , constants.JSON_SCRIPT['images']['image'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['image_url'] != constants.JSON_SCRIPT['images']['image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['image_url'] + " -not equal- " + constants.JSON_SCRIPT['images']['image'])
        print (constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'] , constants.JSON_SCRIPT['images']['medium_image'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'] != constants.JSON_SCRIPT['images']['medium_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'] + " -not equal- " + constants.JSON_SCRIPT['images']['medium_image'])

#        print (constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'] , constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'])
#        if (constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'] != constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'])
#        print (constants.VALUES_FROM_GLOBAL_CATALOG['custom_url'] , constants.JSON_SCRIPT['metadata']['ui']['urls']['catalog_details_url'])
#        if (constants.VALUES_FROM_GLOBAL_CATALOG['custom_url'] != constants.JSON_SCRIPT['metadata']['ui']['urls']['catalog_details_url']):
 #           raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['custom_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['urls']['catalog_details_url'])

#        print (constants.VALUES_FROM_CATALOG_LISTING['bindable'] , str(constants.JSON_SCRIPT['bindable']))
#        if (bool(constants.VALUES_FROM_CATALOG_LISTING['bindable']) != constants.JSON_SCRIPT['bindable']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bindable'] + " -not equal- " + str(constants.JSON_SCRIPT['bindable']))
#        print (constants.VALUES_FROM_GLOBAL_CATALOG['plan_updateable'] , str(constants.JSON_SCRIPT['metadata']['service']['plan_updateable']))
#        if (bool(constants.VALUES_FROM_GLOBAL_CATALOG['plan_updateable']) != constants.JSON_SCRIPT['metadata']['service']['plan_updateable']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['plan_updateable'] + " -not equal- " + str(constants.JSON_SCRIPT['metadata']['service']['plan_updateable']))
#        print (constants.VALUES_FROM_CATALOG_LISTING['unique_api_key'] , str(constants.JSON_SCRIPT['metadata']['service']['unique_api_key']))
#        if (bool(constants.VALUES_FROM_CATALOG_LISTING['unique_api_key']) != constants.JSON_SCRIPT['metadata']['service']['unique_api_key']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['unique_api_key'] + " -not equal- " + str(constants.JSON_SCRIPT['metadata']['service']['unique_api_key']))
#        print (constants.VALUES_FROM_CATALOG_LISTING['provisionable'] , str(constants.JSON_SCRIPT['provisionable']))
#        if (bool(constants.VALUES_FROM_CATALOG_LISTING['provisionable']) != constants.JSON_SCRIPT['provisionable']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['provisionable'] + " -not equal- " + str(constants.JSON_SCRIPT['provisionable']))
        for word in constants.VALUES_FROM_GLOBAL_CATALOG['tags']:
            print(word)
            if (word not in constants.JSON_SCRIPT['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in JSON script")
        print(constants.JSON_SCRIPT['overview_ui'][1][1]['en']['display_name'])

    def update_content_values(self,value):
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG={}
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'displayName': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['display_name'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['shot_description'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['shot_description'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['shot_description'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['shot_description'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'short_description': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['shot_description'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['long_description'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['long_description'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['long_description'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['long_description'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'long_description': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['long_description'])})

        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail'])
        time.sleep(2)

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail_url'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail_url'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail_url'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail_url'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'thumbnail_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['thumbnail_url'])})

        constants.VALUES_FROM_GLOBAL_CATALOG.update({'media_type': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_type'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_url'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_url'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_url'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_url'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['media_url'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['caption_image'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['caption_image'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['caption_image'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['caption_image'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'caption_image': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['caption_image'])})

        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title'])
        time.sleep(2)

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title_field'])
        tempValue = str(tempValue) + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title_field'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title_field'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title_field'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'bullet_title': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_title_field'])})

        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description'])
        time.sleep(2)

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description_field'])
        tempValue = str(tempValue) + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description_field'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description_field'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description_field'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'bullet_description': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['bullet_description_field'])})
        time.sleep(2)
        elemen = self.find_element(GlobalCatalogRMCPage.globalCatalogContent_dictionary['overview_tab'])
        elemen.send_keys(Keys.PAGE_UP)
        time.sleep(2)

    def update_overview_values(self,value):
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'pragmmaticName': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['programmatic_name'])})
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'author': self.get_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['author'])})
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image'])
        time.sleep(2)

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image_field'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image_field'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image_field'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image_field'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'feature_media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['feature_image_field'])})

        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image'])
        time.sleep(2)
        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image_field'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image_field'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image_field'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image_field'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'image_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['image_field'])})

        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image'])
        time.sleep(2)
        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image_field'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image_field'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image_field'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image_field'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'medium_media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['medium_image_field'])})

        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image'])
        time.sleep(2)
        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'semall_media_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['documentation_url'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['documentation_url'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['documentation_url'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['documentation_url'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'documentation_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['documentation_url'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['terms_url'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['terms_url'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['terms_url'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['terms_url'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'terms_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['terms_url'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['instructions_url'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['instructions_url'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['instructions_url'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['instructions_url'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'instructions_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['instructions_url'])})

        tempValue = self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'])
        tempValue = tempValue + value
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'])
        self.clear_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'])
        self.set_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'], tempValue)
        time.sleep(2)
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'custom_url': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'])})

    def press_save_button(self):
        self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary['save_button'])
        time.sleep(10)

    def go_to_RMC(self):
        elemen = self.find_element(GlobalCatalogRMCPage.globalCatalogContent_dictionary['custom_url'])
        elemen.send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
        constants.BROWSER.switch_to_window(constants.window_before)
        time.sleep(10)

    def get_content_value1s(self):
        constants.VALUES_FROM_GLOBAL_CATALOG.update({'semall_media_url11': self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['small_image_field11'])})

    def verify_GC_against_js_modal_view(self):
        print(constants.VALUES_FROM_GLOBAL_CATALOG)
        print(constants.JSON_SCRIPT)
        print(constants.VALUES_FROM_GLOBAL_CATALOG['displayName'], constants.JSON_SCRIPT['metadata']['displayName'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] != constants.JSON_SCRIPT['metadata']['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['displayName'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['short_description'], constants.JSON_SCRIPT['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] != constants.JSON_SCRIPT['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] + " -not equal- " + constants.JSON_SCRIPT['description'])
        #        print (constants.VALUES_FROM_GLOBAL_CATALOG['author'] , constants.JSON_SCRIPT['provider']['name'])
        #        if (constants.VALUES_FROM_GLOBAL_CATALOG['author'] != constants.JSON_SCRIPT['provider']['name']):
        #            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['author'] + " -not equal- " + constants.JSON_SCRIPT['provider']['name'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['long_description'], constants.JSON_SCRIPT['metadata']['longDescription'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] != constants.JSON_SCRIPT['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['longDescription'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'], constants.JSON_SCRIPT['metadata']['featuredImageUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'] != constants.JSON_SCRIPT['metadata']['featuredImageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['featuredImageUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'], constants.JSON_SCRIPT['metadata']['documentationUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'] != constants.JSON_SCRIPT['metadata']['documentationUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['documentationUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'], constants.JSON_SCRIPT['metadata']['termsUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'] != constants.JSON_SCRIPT['metadata']['termsUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['termsUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'], constants.JSON_SCRIPT['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] != constants.JSON_SCRIPT['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['bullets'][0]['title'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'], constants.JSON_SCRIPT['metadata']['bullets'][0]['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] != constants.JSON_SCRIPT['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['bullets'][0]['description'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['media_type'], constants.JSON_SCRIPT['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] != constants.JSON_SCRIPT['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['type'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'], constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] != constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['media_url'], constants.JSON_SCRIPT['metadata']['media'][0]['url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] != constants.JSON_SCRIPT['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['url'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'], constants.JSON_SCRIPT['metadata']['media'][0]['caption'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] != constants.JSON_SCRIPT['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['caption'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'], constants.JSON_SCRIPT['metadata']['smallImageUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'] != constants.JSON_SCRIPT['metadata']['smallImageUrl']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['smallImageUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['image_url'], constants.JSON_SCRIPT['metadata']['imageUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['image_url'] != constants.JSON_SCRIPT['metadata']['imageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['image_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['imageUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'], constants.JSON_SCRIPT['metadata']['mediumImageUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'] != constants.JSON_SCRIPT['metadata']['mediumImageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['mediumImageUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['author'], constants.JSON_SCRIPT['metadata']['providerDisplayName'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['author'] != constants.JSON_SCRIPT['metadata']['providerDisplayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['author'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['providerDisplayName'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['long_description'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['longDescription'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['long_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['longDescription'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['displayName'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['displayName'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['displayName'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['displayName'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['title'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['bullets'][0]['description'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['media_type'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['type'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['media_url'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['url'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['media_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['url'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'], constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['caption'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['metadata']['media'][0]['caption'])
        print(constants.VALUES_FROM_GLOBAL_CATALOG['short_description'], constants.JSON_SCRIPT['metadata']['i18n']['en']['description'])
        if (constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] != constants.JSON_SCRIPT['metadata']['i18n']['en']['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_GLOBAL_CATALOG['short_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['description'])

        for word in constants.VALUES_FROM_GLOBAL_CATALOG['tags']:
            print(word)
            if (word not in constants.JSON_SCRIPT['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in JSON script")
        print(constants.JSON_SCRIPT['metadata'][1][1]['en']['display_name'])


    def get_composite_label(self,value):
        composite = self.get_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary['get_composite_label'])
        print(composite)
        if (value.upper() not in composite.upper()):
            raise AssertionError("---> ERROR: Composite service was not published")

    def validate_type(self,value,value1,value2,value3):
        if (value.upper() == "COMPOSITE"):
            print(constants.JSON_SCRIPT['kind'])
            if (constants.JSON_SCRIPT['kind'] != "composite"):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['kind'] + " -not equal- " + "composite" )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['kind'])
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['kind'] != value2):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['kind'] + " -not equal- " + value2 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'], value1)
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'] != value1):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'] + " -not equal- " + value1 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'], value1)
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'] != value1):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'] + " -not equal- " + value1 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['composite_kind'], value2)
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['composite_kind'] != value2):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['composite_kind'] + " -not equal- " + value2 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['composite_tag'], value3)
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['composite_tag'] != value3):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['composite_tag'] + " -not equal- " + value3 )
        elif (value.upper() == "MULTIPLE"):
            print(constants.JSON_SCRIPT['kind'])
            if (constants.JSON_SCRIPT['kind'] != "composite"):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['kind'] + " -not equal- " + "composite" )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['kind'])
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['kind'] != value2):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['kind'] + " -not equal- " + value2 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'], value1)
            if (value1 not in constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name']):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'] + " -not equal- " + value1 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['children'][0]['name'], value1)
            if (value1 not in constants.JSON_SCRIPT['metadata']['other']['composite']['children'][1]['name']):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['children'][1]['name'] + " -not equal- " + value1 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['composite_kind'], value2)
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['composite_kind'] != value2):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['composite_kind'] + " -not equal- " + value2 )
            print(constants.JSON_SCRIPT['metadata']['other']['composite']['composite_tag'], value3)
            if (constants.JSON_SCRIPT['metadata']['other']['composite']['composite_tag'] != value3):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['other']['composite']['composite_tag'] + " -not equal- " + value3 )
        elif (value.upper() == "SERVICE") or (value.upper() == "PLATFORM"):
            print(constants.JSON_SCRIPT['kind'])
            if (constants.JSON_SCRIPT['kind'] != value2):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['kind'] + " -not equal- " + value2)
            print(constants.JSON_SCRIPT['name'])
            if (value1 not in constants.JSON_SCRIPT['name']):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['name'] + " -not equal- " + value1 )
            print(constants.JSON_SCRIPT['tags'], value3)
            if (value3 not in constants.JSON_SCRIPT['tags']):
                raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['tags'] + " -not equal- " + value3 )

    def get_content_values_fr_language(self,value):
            time.sleep(2)
            constants.VALUES_FROM_GLOBAL_CATALOG = {}
            tempValue1 = value + "_" + "displayName"
            tempValue2 = value + "_" + "display_name"
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "short_description"
            tempValue2 = value + "_" + "shot_description"
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "long_description"
            tempValue2 = value + "_" + "long_description"
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "thumbnail_url"
            tempValue2 = value + "_" + "thumbnail_url"
            tempValue = value + "_" + "thumbnail"
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue])
            time.sleep(2)
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "media_type"
            tempValue2 = value + "_" + "media_type"
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "media_url"
            tempValue2 = value + "_" + "media_url"
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "caption_image"
            tempValue2 = value + "_" + "caption_image"
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "bullet_title"
            tempValue2 = value + "_" + "bullet_title_field"
            tempValue = value + "_" + "bullet_title"
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue])
            time.sleep(2)
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})

            tempValue1 = value + "_" + "bullet_description"
            tempValue2 = value + "_" + "bullet_description_field"
            tempValue = value + "_" + "bullet_description"
            self.click(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue])
            time.sleep(2)
            constants.VALUES_FROM_GLOBAL_CATALOG.update({tempValue1: self.get_attribute_value(GlobalCatalogRMCPage.globalCatalogContent_dictionary[tempValue2])})
