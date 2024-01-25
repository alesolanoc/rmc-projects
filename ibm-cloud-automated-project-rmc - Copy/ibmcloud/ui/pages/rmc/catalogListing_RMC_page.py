import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants
from core.ui.variables.constants import VALIDATE_REQUIRED_FIELDS_SERVICE, TARGET_RELEASE_LEVEL, CURRENT_DATE, \
    FUTURE_DATE, VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG

POSITION = 0

class CatalogListingRMCPage(FormPage,ActionPage):
    global POSITION
    catalog_dictionary = {
        'listing_page_tab': 'div.bx--tabs__nav-link',
        'resurce_displaye_name': '//input[@id="service/metadata/displayName"]',
        'short_description': '//input[@id="service/description"]',
        'author': '//input[@id="service/metadata/providerDisplayName"]',
        'detailed_description': '//textarea[@id="service/metadata/longDescription"]',
        'service_icon_url': '//input[@id="service/metadata/featuredImageUrl"]',
        'documentation_url': '//input[@id="service/metadata/documentationUrl"]',
        'terms_url': '//input[@id="service/metadata/termsUrl"]',
        'settings_tab': '//div[@id="content"]/div/div/div[3]/div/nav/div/div[2]/div',
        'management_type': '//select[@id="service/metadata/type"]',
        'public_option': '//select[@id="service/metadata/type"]/option',
        'instructions_url': '//input[@id="service/metadata/instructionsUrl"]',
        'support_url': '//input[@id="service/metadata/supportUrl"]',
        'provisionable_through': '//div[@id="content"]/div/div/div[3]/div/div/div/div/form/div[4]/div/label/span',
        'provisionable_behind': '//div[@id="content"]/div/div/div[3]/div/div/div/div/form/div[4]/div/label[2]/span',
        'bindable_yes': '//div[@id="content"]/div/div/div[3]/div/div/div/div/form/div[5]/div/label/span',
        'plan_changes_yes': '//div[@id="content"]/div/div/div[3]/div/div/div/div/form/div[6]/div/label/span',
        'requires_unique_yes': '//div[@id="content"]/div/div/div[3]/div/div/div/div/form/div[7]/div/label/span',
        'resources_keys_yes': '//div[@id="content"]/div/div/div[3]/div/div/div/div/form/div[8]/div/label/span',
        'support_email': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form/div/div/input',
        'custom_url': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form/div[2]/div/input',
        'save_button': '#serviceMetadataSaveButton',
        'global_catalog_link': 'div.descr > a.bx--link',
        'add_feature_button': 'div.whitePanel > button.bx--btn.bx--btn--primary',
        'bullet_title': '//input[@id="service/metadata/bullets/0/title"]',
        'bullet_description': '//input[@id="service/metadata/bullets/0/description"]',
        'remove_bullet_button': 'div.feature-bullet > button.bx--btn.bx--btn--primary',
        'add_media_button': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/button[2]',
        'media_type': '//select[@id="service/metadata/media/0/type"]',
        'media_option': '//option[@value="image"]',
        'thumbnail_url': '//input[@id="service/metadata/media/0/thumbnailUrl"]',
        'media_url': '//input[@id="service/metadata/media/0/url"]',
        'media_caption': '//input[@id="service/metadata/media/0/caption"]',
        'remove_media': 'svg[name="close"]',
        'ai_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[1]/span',
        'ai_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(1) path',
        'ai_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(1) .bx--checkbox-checkmark',
        'analytics_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[2]/span',
        'analytics_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(2) path',
        'analytics_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(2) .bx--checkbox-checkmark',
#        'apidocs_enabled_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[3]/span',
#        'apidocs_enabled_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(3) path',
#        'apidocs_enabled_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(3) .bx--checkbox-checkmark',
        'blockchain_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[3]/span',
        'blockchain_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(3) path',
        'blockchain_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(3) .bx--checkbox-checkmark',
        'compute_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[4]/span',
        'compute_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(4) path',
        'compute_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(4) .bx--checkbox-checkmark',
        'containers_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[5]/span',
        'containers_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(5) path',
        'containers_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(5) .bx--checkbox-checkmark',
        'databases_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[6]/span',
        'databases_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(6) path',
        'databases_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(6) .bx--checkbox-checkmark',
        'devops_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[7]/span',
        'devops_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(7) path',
        'devops_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(7) .bx--checkbox-checkmark',
#        'hipaa_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[9]/span',
#        'hipaa_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(9) path',
#        'hipaa_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(9) .bx--checkbox-checkmark',
#        'ibm_created_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[8]/span',
#        'ibm_created_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(8) path',
#        'ibm_created_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(8) .bx--checkbox-checkmark',
        'integration_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[9]/span',
        'integration_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(9) path',
        'integration_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(9) .bx--checkbox-checkmark',
        'iot_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[10]/span',
        'iot_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(10) path',
        'iot_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(10) .bx--checkbox-checkmark',
        'logging_monitoring_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[11]/span',
        'logging_monitoring_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(11) path',
        'logging_monitoring_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(11) .bx--checkbox-checkmark',
        'migration_tools_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[12]/span',
        'migration_tools_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(12) path',
        'migration_tools_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(12) .bx--checkbox-checkmark',
        'mobile_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[13]/span',
        'mobile_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(13) path',
        'mobile_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(13) .bx--checkbox-checkmark',
        'network_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[14]/span',
        'network_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(14) path',
        'network_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(14) .bx--checkbox-checkmark',
        'platform_services_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[15]/span',
        'platform_services_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(15) path',
        'platform_services_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(15) .bx--checkbox-checkmark',
#        'rc_compatible_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[16]/span',
#        'rc_compatible_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(16) path',
#        'rc_compatible_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(16) .bx--checkbox-checkmark',
        'security_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[16]/span',
        'security_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(16) path',
        'security_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(16) .bx--checkbox-checkmark',
        'storage_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[17]/span',
        'storage_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(17) path',
        'storage_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(17) .bx--checkbox-checkmark',
#        'supports_syndication_checkbox': '//div[@id="content"]/div/div/div[3]/div/div/div/div[2]/form[3]/div/div/label[21]/span',
#        'supports_syndication_checkbox_checked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(21) path',
#        'supports_syndication_checkbox_unchecked': '.bx--form:nth-child(4) .bx--checkbox-label:nth-child(21) .bx--checkbox-checkmark'
        'json_View_button': 'div.bssBtnGroup.flex-end.offering-btn-row > div > button.bx--btn.bx--btn--secondary',
        'import_from_GC_button': 'div.bssBtnGroup.flex-end.offering-btn-row > button.bx--btn.bx--btn--secondary',
        'import_from_GC_button111': 'div.bssBtnGroup.flex-end.offering-btn-row > button.bx--btn.bx--btn--secondary11'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "resource_name_field": lambda value: self.set_resource_name_field(value),
            "short_field": lambda value: self.set_short(value),
            "author_field": lambda value: self.set_author(value),
            "detailed_field": lambda value: self.set_detailed(value),
            "service_url_field": lambda value: self.set_service_url(value),
            "documentation_url_field": lambda value: self.set_documentation_url(value),
            "terms_url_field": lambda value: self.set_terms_url(value),
            "instructions_url_field": lambda value: self.set_instructions_url(value),
            "support_url_field": lambda value: self.set_support_url(value),
            "support_email": lambda value: self.set_support_email(value),
            "custom_url": lambda value: self.set_custom_url(value),
            "bullet_title": lambda value: self.set_bullet_title(value),
            "bullet_description": lambda value: self.set_bullet_description(value),
            "thumbnail_url": lambda value: self.set_thumbnail_url(value),
            "media_url": lambda value: self.set_media_url(value),
            "media_caption": lambda value: self.set_media_caption(value),
            "go_page": lambda value: self.page(value)
        }
        actions = {
            "select tab": lambda value: self.select_tab(value),
            "management type": lambda value: self.set_management(value),
            "provisionable type": lambda value: self.set_provisionable(value),
            "bindable": lambda value: self.set_bindable(value),
            "plan changes": lambda value: self.set_plan_changes(value),
            "requires unique": lambda value: self.set_require_unique(value),
            "resource kwys": lambda value: self.set_resource_keys(value),
            "press save button": lambda: self.save_button(),
            "global catalog link": lambda: self.is_there_link(),
            "get values from": lambda value: self.is_there_required_fields(value),
            "press add feature": lambda: self.add_feature(),
            "get bullet values":  lambda: self.bullet_values(),
            "press remove feature": lambda: self.remove_feature(),
            "bullets removed": lambda: self.is_there_bullets(),
            "press add media": lambda: self.add_media(),
            "select media type": lambda value: self.select_media(value),
            "get media values": lambda: self.media_values(),
            "press revmove media": lambda: self.remove_media(),
            "media revmoved": lambda: self.is_there_media(),
            "tag_check": lambda value: self.tag_check(value),
            "tag_checked": lambda value: self.tag_checked(value),
            "tag_uncheck": lambda value: self.tag_uncheck(value),
            "tag_unchecked": lambda value: self.tag_unchecked(value),
            "press_view_json": lambda: self.view_json(),
            "get_listing_page_values": lambda: self.get_listing_page_values(),
            "get_settings_values": lambda: self.get_settings_values(),
            "validate_catalog_listing_agains_json_modal": lambda: self.validate_catalog_listing_agains_json_modal(),
            "go_to_GC": lambda: self.go_to_GC(),
            "press import button": lambda: self.import_from_GC(),
            "get_listing_page_values12": lambda: self.import_from_GC1(),
            "validate_global_catalog_agains_catalog_listing": lambda: self.validate_gc_against_cl(),
            "Validate_Json_script_from_GC_against_catalog_listing": lambda: self.validate_json_gc_against_cl(),
            "Verify_that_json_script_modal_values_are_equal_than_json_script_from_GC": lambda: self.validate_jsonm_gc_against_jsonModal(),
            "Updates_all_values_from_catalog_listing": lambda value1,value2: self.Updates_all_values_from_catalog_listing(value1,value2)
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)


    def select_tab(self,value):
        time.sleep(2)
        if (value == "LISTING PAGE"):
            self.click(CatalogListingRMCPage.catalog_dictionary['listing_page_tab'])
            time.sleep(2)
        elif (value == "SETTINGS"):
            self.click(CatalogListingRMCPage.catalog_dictionary['settings_tab'])
            time.sleep(2)

    def set_resource_name_field(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name'], value + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0])
        time.sleep(2)

    def set_short(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['short_description'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['short_description'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['short_description'], value)
        time.sleep(2)

    def set_author(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['author'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['author'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['author'], value)
        time.sleep(2)

    def set_detailed(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['detailed_description'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'], value)
        time.sleep(2)

    def set_service_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'], value)
        time.sleep(2)

    def set_documentation_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['documentation_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['documentation_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['documentation_url'], value)
        time.sleep(2)

    def set_terms_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['terms_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['terms_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['terms_url'], value)
        time.sleep(2)

    def set_management(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['management_type'])
        if (value == 'PUBLIC'):
            self.click(CatalogListingRMCPage.catalog_dictionary['public_option'])
            time.sleep(2)

    def set_instructions_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['instructions_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['instructions_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['instructions_url'], value)
        time.sleep(2)

    def set_support_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['support_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['support_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['support_url'], value)
        time.sleep(2)

    def set_provisionable(self,value):
        if (value == "PROVISION-THROUGH"):
            self.click(CatalogListingRMCPage.catalog_dictionary['provisionable_through'])
            time.sleep(2)

    def set_bindable(self,value):
        if (value == "YES"):
            self.click(CatalogListingRMCPage.catalog_dictionary['bindable_yes'])
            time.sleep(2)

    def set_plan_changes(self,value):
        if (value == "YES"):
            self.click(CatalogListingRMCPage.catalog_dictionary['plan_changes_yes'])
            time.sleep(2)

    def set_require_unique(self,value):
        if (value == "YES"):
            self.click(CatalogListingRMCPage.catalog_dictionary['requires_unique_yes'])
            time.sleep(2)

    def set_resource_keys(self,value):
        if (value == "YES"):
            self.click(CatalogListingRMCPage.catalog_dictionary['resources_keys_yes'])
            time.sleep(2)

    def set_support_email(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['support_email'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['support_email'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['support_email'], value)
        time.sleep(2)

    def set_custom_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['custom_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['custom_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['custom_url'], value)
        time.sleep(2)

    def save_button(self):
        self.click(CatalogListingRMCPage.catalog_dictionary['save_button'])
        time.sleep(30)

    def is_there_link(self):
        if not self.is_existing(CatalogListingRMCPage.catalog_dictionary['global_catalog_link']):
            raise AssertionError("---> ERROR: Global Catalog was not there")

    def is_there_required_fields(self,value):
        if (value.upper() == "LISTING PAGE"):
            time.sleep(2)
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[0] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[1] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['short_description'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[1] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['short_description']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[2] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['author'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[2] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['author']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[3] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[3] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['detailed_description']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[4] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[4] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[5] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['documentation_url'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[5] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['documentation_url']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[6] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['terms_url'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[6] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['terms_url']))
        elif (value.upper() == "SETTINGS"):
            time.sleep(2)
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[7] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['instructions_url'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[7] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['instructions_url']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[8] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_url'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[8] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_url']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[9] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_email'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[9] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_email']))
            if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[10] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['custom_url'])):
                raise AssertionError ("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[10] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['custom_url']))

    def add_feature(self):
        time.sleep(2)
        self.click(CatalogListingRMCPage.catalog_dictionary['add_feature_button'])
        time.sleep(2)

    def set_bullet_title(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['bullet_title'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['bullet_title'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['bullet_title'], value)
        time.sleep(2)

    def set_bullet_description(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['bullet_description'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'], value)
        time.sleep(2)

    def bullet_values(self):
        if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[11] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_title'])):
            raise AssertionError("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[11] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_title']))
        if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[12] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'])):
            raise AssertionError("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[12] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_description']))

    def remove_feature(self):
        time.sleep(2)
        self.click(CatalogListingRMCPage.catalog_dictionary['remove_bullet_button'])
        time.sleep(2)

    def is_there_bullets(self):
        if (self.is_existing(CatalogListingRMCPage.catalog_dictionary['bullet_title'])):
            raise AssertionError("---> ERROR: bullet was not removed")
        if (self.is_existing(CatalogListingRMCPage.catalog_dictionary['bullet_description'])):
            raise AssertionError("---> ERROR: bullet was not removed")

    def add_media(self):
        time.sleep(2)
        self.click(CatalogListingRMCPage.catalog_dictionary['add_media_button'])
        time.sleep(2)

    def select_media(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['media_type'])
        time.sleep(2)
        if (value.upper() == "IMAGE"):
            self.click(CatalogListingRMCPage.catalog_dictionary['media_option'])
            time.sleep(2)

    def set_thumbnail_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'], value)
        time.sleep(2)

    def set_media_url(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['media_url'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['media_url'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['media_url'], value)
        time.sleep(2)

    def set_media_caption(self,value):
        self.click(CatalogListingRMCPage.catalog_dictionary['media_caption'])
        self.clear_value(CatalogListingRMCPage.catalog_dictionary['media_caption'])
        self.set_value(CatalogListingRMCPage.catalog_dictionary['media_caption'], value)
        time.sleep(2)

    def media_values(self):
        if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[13] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_type'])):
            raise AssertionError("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[13] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_type']))
        if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[14] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])):
            raise AssertionError("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[14] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url']))
        if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[15] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_url'])):
            raise AssertionError("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[15] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_url']))
        if (VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[16] not in self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_caption'])):
            raise AssertionError("---> ERROR: " + VALIDATE_REQUIRED_FIELDS_SERVICE_CATALOG[16] + " --Not in " + self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_caption']))

    def page(self,value):
        if (value.upper() == "PAGE UP"):
            elemen = self.find_element(CatalogListingRMCPage.catalog_dictionary['save_button'])
            elemen.send_keys(Keys.PAGE_UP)
            time.sleep(2)

    def remove_media(self):
        self.click(CatalogListingRMCPage.catalog_dictionary['remove_media'])
        time.sleep(2)

    def is_there_media(self):
        if (self.is_existing(CatalogListingRMCPage.catalog_dictionary['media_option'])):
            raise AssertionError("---> ERROR: media was not removed")
        if (self.is_existing(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])):
            raise AssertionError("---> ERROR: media was not removed")
        if (self.is_existing(CatalogListingRMCPage.catalog_dictionary['media_url'])):
            raise AssertionError("---> ERROR: media was not removed")
        if (self.is_existing(CatalogListingRMCPage.catalog_dictionary['media_caption'])):
            raise AssertionError("---> ERROR: media was not removed")

    def tag_check(self,value):
        if (value.upper() == "ai".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ai_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['ai_checkbox'])
                time.sleep(1)
        elif (value.upper() == "analytics".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "apidocs".upper()):
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['apidocs_enabled_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['apidocs_enabled_checkbox'])
        elif (value.upper() == "blockchain".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox'])
                time.sleep(1)
        elif (value.upper() == "compute".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['compute_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['compute_checkbox'])
                time.sleep(1)
        elif (value.upper() == "containers".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['containers_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['containers_checkbox'])
                time.sleep(1)
        elif (value.upper() == "databases".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['databases_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['databases_checkbox'])
                time.sleep(1)
        elif (value.upper() == "devops".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['devops_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['devops_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "hipaa".upper()):
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['hipaa_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['hipaa_checkbox'])
#        elif (value.upper() == "ibm_created".upper()):
#            print(value)
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ibm_created_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['ibm_created_checkbox'])
        elif (value.upper() == "integration".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['integration_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['integration_checkbox'])
                time.sleep(1)
        elif (value.upper() == "iot".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['iot_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['iot_checkbox'])
                time.sleep(1)
        elif (value.upper() == "logging_monitoring".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox'])
                time.sleep(1)
        elif (value.upper() == "migration_tools".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox'])
                time.sleep(1)
        elif (value.upper() == "mobile".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox'])
                time.sleep(1)
        elif (value.upper() == "network".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['network_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['network_checkbox'])
                time.sleep(1)
        elif (value.upper() == "platform_services".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "rc_compatible".upper()):
#            print(value)
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['rc_compatible_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['rc_compatible_checkbox'])
        elif (value.upper() == "security".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['security_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['security_checkbox'])
                time.sleep(1)
        elif (value.upper() == "storage".upper()):
            print(value)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['storage_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['storage_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "supports_syndication".upper()):
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['supports_syndication_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['supports_syndication_checkbox'])

    def tag_checked(self,value):
        if (value.upper() == "ai".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ai_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "analytics".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "blockchain".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "compute".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['compute_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "containers".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['containers_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "databases".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['databases_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "devops".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['devops_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "integration".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['integration_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "iot".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['iot_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "logging_monitoring".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "migration_tools".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "mobile".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "network".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['network_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "platform_services".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "security".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['security_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")
        elif (value.upper() == "storage".upper()):
            time.sleep(1)
            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['storage_checkbox_unchecked'])):
                raise AssertionError("---> ERROR: " + value + " is unchecked")

    def tag_uncheck(self,value):
        if (value.upper() == "ai".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ai_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['ai_checkbox'])
                time.sleep(1)
        elif (value.upper() == "analytics".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "apidocs".upper()):
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['apidocs_enabled_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['apidocs_enabled_checkbox'])
        elif (value.upper() == "blockchain".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox'])
                time.sleep(1)
        elif (value.upper() == "compute".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['compute_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['compute_checkbox'])
                time.sleep(1)
        elif (value.upper() == "containers".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['containers_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['containers_checkbox'])
                time.sleep(1)
        elif (value.upper() == "databases".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['databases_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['databases_checkbox'])
                time.sleep(1)
        elif (value.upper() == "devops".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['devops_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['devops_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "hipaa".upper()):
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['hipaa_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['hipaa_checkbox'])
#        elif (value.upper() == "ibm_created".upper()):
#            print(value)
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ibm_created_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['ibm_created_checkbox'])
        elif (value.upper() == "integration".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['integration_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['integration_checkbox'])
                time.sleep(1)
        elif (value.upper() == "iot".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['iot_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['iot_checkbox'])
                time.sleep(1)
        elif (value.upper() == "logging_monitoring".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox'])
                time.sleep(1)
        elif (value.upper() == "migration_tools".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox'])
                time.sleep(1)
        elif (value.upper() == "mobile".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox'])
                time.sleep(1)
        elif (value.upper() == "network".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['network_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['network_checkbox'])
                time.sleep(1)
        elif (value.upper() == "platform_services".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "rc_compatible".upper()):
#            print(value)
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['rc_compatible_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['rc_compatible_checkbox'])
        elif (value.upper() == "security".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['security_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['security_checkbox'])
                time.sleep(1)
        elif (value.upper() == "storage".upper()):
            print(value)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['storage_checkbox_checked'])):
                self.click(CatalogListingRMCPage.catalog_dictionary['storage_checkbox'])
                time.sleep(1)
#        elif (value.upper() == "supports_syndication".upper()):
#            if not (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['supports_syndication_checkbox_checked'])):
#                self.click(CatalogListingRMCPage.catalog_dictionary['supports_syndication_checkbox'])

    def tag_unchecked(self,value):
        if (value.upper() == "ai".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ai_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "analytics".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "blockchain".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "compute".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['compute_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "containers".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['containers_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "databases".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['databases_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "devops".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['devops_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "integration".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['integration_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "iot".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['iot_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "logging_monitoring".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "migration_tools".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "mobile".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "network".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['network_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "platform_services".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "security".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['security_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")
        elif (value.upper() == "storage".upper()):
            time.sleep(1)
            if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['storage_checkbox_checked'])):
                raise AssertionError("---> ERROR: " + value + " is checked")

    def view_json(self):
        time.sleep(2)
        self.click(CatalogListingRMCPage.catalog_dictionary['json_View_button'])
        time.sleep(2)

    def get_listing_page_values(self):
        constants.VALUES_FROM_CATALOG_LISTING.update({'displayName': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'description': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['short_description'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'providerDisplayName': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['author'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'longDescription': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'featuredImageUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'documentationUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['documentation_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'termsUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['terms_url'])})
        constants.VALUES_FROM_CATALOG_LISTING['bullets'] = []
        constants.VALUES_FROM_CATALOG_LISTING['bullets'].append({'bullet_title': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_title']),'bullet_description': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'])})
        constants.VALUES_FROM_CATALOG_LISTING['media'] = []
        constants.VALUES_FROM_CATALOG_LISTING['media'].append({'type': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_option']),'thumbnailUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url']),'url': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_url']),'caption': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_caption'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'] = {}
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_longDescription': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_displayName': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['resurce_displaye_name'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_bullet_title': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_title'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_bullet_description': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_caption': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_caption'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_type': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_option'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_url': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_url'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_thumbnailUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])})
        constants.VALUES_FROM_CATALOG_LISTING['en'].update({'i18n_description': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['short_description'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'imageUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'smallImageUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'mediumImageUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])})

    def get_settings_values(self):
        constants.VALUES_FROM_CATALOG_LISTING.update({'management_type': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['management_type'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'instructionsUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['instructions_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'supportUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'supportEmail': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_email'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'catalogDetailsUrl': self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['custom_url'])})
        constants.VALUES_FROM_CATALOG_LISTING.update({'bindable': 'true'})
        constants.VALUES_FROM_CATALOG_LISTING.update({'plan_updateable': 'true'})
        constants.VALUES_FROM_CATALOG_LISTING.update({'unique_api_key': 'true'})
        constants.VALUES_FROM_CATALOG_LISTING.update({'provisionable': 'true'})
        constants.VALUES_FROM_CATALOG_LISTING['tags'] = []
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['ai_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('ai')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['analytics_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('analytics')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['blockchain_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('blockchain')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['compute_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('compute')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['containers_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('containers')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['databases_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('databases')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['devops_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('devops')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['integration_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('integration')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['iot_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('iot')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['logging_monitoring_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('logging_monitoring')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['migration_tools_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('migration_tools')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['mobile_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('mobile')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['network_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('network')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['platform_services_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('platform_services')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['security_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('security')
        if (self.is_displayed(CatalogListingRMCPage.catalog_dictionary['storage_checkbox_checked'])):
            constants.VALUES_FROM_CATALOG_LISTING['tags'].append('storage')
        print(constants.VALUES_FROM_CATALOG_LISTING)
        print(constants.VALUES_FROM_GLOBAL_CATALOG)

    def validate_catalog_listing_agains_json_modal(self):

        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'] , constants.JSON_SCRIPT['metadata']['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['displayName'] != constants.JSON_SCRIPT['metadata']['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['displayName'])
#        print(constants.VALUES_FROM_CATALOG_LISTING['description'] , constants.JSON_SCRIPT['metadata']['en']['description'])
#        if (constants.VALUES_FROM_CATALOG_LISTING['description'] != constants.JSON_SCRIPT['metadata']['en']['description']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['i18n']['en']['description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] , constants.JSON_SCRIPT['metadata']['providerDisplayName'])

        if (constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] != constants.JSON_SCRIPT['metadata']['providerDisplayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['providerDisplayName'])
        print (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] , constants.JSON_SCRIPT['metadata']['longDescription'])

        if (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] != constants.JSON_SCRIPT['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['longDescription'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['longDescription'])
        print (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] , constants.JSON_SCRIPT['metadata']['featuredImageUrl'])

        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.JSON_SCRIPT['metadata']['featuredImageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['featuredImageUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] , constants.JSON_SCRIPT['metadata']['documentationUrl'])

        if (constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] != constants.JSON_SCRIPT['metadata']['documentationUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['documentationUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] , constants.JSON_SCRIPT['metadata']['termsUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] != constants.JSON_SCRIPT['metadata']['termsUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['termsUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] , constants.JSON_SCRIPT['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] != constants.JSON_SCRIPT['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['bullets'][0]['title'])
        print (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] , constants.JSON_SCRIPT['metadata']['bullets'][0]['description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] != constants.JSON_SCRIPT['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['bullets'][0]['description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] , constants.JSON_SCRIPT['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] != constants.JSON_SCRIPT['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['type'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] , constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] != constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] , constants.JSON_SCRIPT['metadata']['media'][0]['url'])

        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] != constants.JSON_SCRIPT['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] , constants.JSON_SCRIPT['metadata']['media'][0]['caption'])

        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] != constants.JSON_SCRIPT['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['caption'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_longDescription'] , constants.JSON_SCRIPT['metadata']['longDescription'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_longDescription'] != constants.JSON_SCRIPT['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_longDescription'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['longDescription'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_displayName'] , constants.JSON_SCRIPT['metadata']['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_displayName'] != constants.JSON_SCRIPT['metadata']['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_displayName'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['displayName'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_title'] , constants.JSON_SCRIPT['metadata']['bullets'][0]['title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_title'] != constants.JSON_SCRIPT['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_title'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['bullets'][0]['title'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_description'] , constants.JSON_SCRIPT['metadata']['bullets'][0]['description'])

        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_description'] != constants.JSON_SCRIPT['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['bullets'][0]['description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_caption'] , constants.JSON_SCRIPT['metadata']['media'][0]['caption'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_caption'] != constants.JSON_SCRIPT['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_caption'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['caption'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_type'] , constants.JSON_SCRIPT['metadata']['media'][0]['type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_type'] != constants.JSON_SCRIPT['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['type'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_url'] , constants.JSON_SCRIPT['metadata']['media'][0]['url'])

        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_url'] != constants.JSON_SCRIPT['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_thumbnailUrl'] , constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_thumbnailUrl'] != constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['media'][0]['thumbnailUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] , constants.JSON_SCRIPT['metadata']['smallImageUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] != constants.JSON_SCRIPT['metadata']['smallImageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['smallImageUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] , constants.JSON_SCRIPT['metadata']['imageUrl'])

        if (constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] != constants.JSON_SCRIPT['metadata']['imageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['imageUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] , constants.JSON_SCRIPT['metadata']['mediumImageUrl'])

        if (constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] != constants.JSON_SCRIPT['metadata']['mediumImageUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['mediumImageUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['management_type'] , constants.JSON_SCRIPT['metadata']['type'])

        if (constants.VALUES_FROM_CATALOG_LISTING['management_type'].upper() != constants.JSON_SCRIPT['metadata']['type'].upper()):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['management_type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['type'])
        print (constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] , constants.JSON_SCRIPT['metadata']['instructionsUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] != constants.JSON_SCRIPT['metadata']['instructionsUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['instructionsUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['supportUrl'] , constants.JSON_SCRIPT['metadata']['supportUrl'])
        if (constants.VALUES_FROM_CATALOG_LISTING['supportUrl'] != constants.JSON_SCRIPT['metadata']['supportUrl']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['supportUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['supportUrl'])
        print (constants.VALUES_FROM_CATALOG_LISTING['supportEmail'] , constants.JSON_SCRIPT['metadata']['supportEmail'])
        if (constants.VALUES_FROM_CATALOG_LISTING['supportEmail'] != constants.JSON_SCRIPT['metadata']['supportEmail']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['supportEmail'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['supportEmail'])
        print (constants.VALUES_FROM_CATALOG_LISTING['bindable'] , str(constants.JSON_SCRIPT['bindable']))
        if (bool(constants.VALUES_FROM_CATALOG_LISTING['bindable']) != constants.JSON_SCRIPT['bindable']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bindable'] + " -not equal- " + str(constants.JSON_SCRIPT['bindable']))
        print (constants.VALUES_FROM_CATALOG_LISTING['plan_updateable'] , str(constants.JSON_SCRIPT['plan_updateable']))
        if (bool(constants.VALUES_FROM_CATALOG_LISTING['plan_updateable']) != constants.JSON_SCRIPT['plan_updateable']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['plan_updateable'] + " -not equal- " + str(constants.JSON_SCRIPT['plan_updateable']))
        print (constants.VALUES_FROM_CATALOG_LISTING['unique_api_key'] , str(constants.JSON_SCRIPT['unique_api_key']))
        if (bool(constants.VALUES_FROM_CATALOG_LISTING['unique_api_key']) != constants.JSON_SCRIPT['unique_api_key']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['unique_api_key'] + " -not equal- " + str(constants.JSON_SCRIPT['unique_api_key']))
        print (constants.VALUES_FROM_CATALOG_LISTING['provisionable'] , str(constants.JSON_SCRIPT['provisionable']))
        if (bool(constants.VALUES_FROM_CATALOG_LISTING['provisionable']) != constants.JSON_SCRIPT['provisionable']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['provisionable'] + " -not equal- " + str(constants.JSON_SCRIPT['provisionable']))
        for word in constants.VALUES_FROM_CATALOG_LISTING['tags']:
            print(word)
            if (word not in constants.JSON_SCRIPT['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in JSON script")
        print(constants.VALUES_FROM_CATALOG_LISTING['management_type'][1][1], constants.JSON_SCRIPT['metadata']['type'])

    def go_to_GC(self):
        time.sleep(2)
#        window_before = constants.BROWSER.window_handles[0]
        constants.window_before = constants.BROWSER.window_handles[0]
        elemen = self.find_element(CatalogListingRMCPage.catalog_dictionary['global_catalog_link'])
        self.click(CatalogListingRMCPage.catalog_dictionary['global_catalog_link'])
        time.sleep(2)
        link = self.get_attribute_href(CatalogListingRMCPage.catalog_dictionary['global_catalog_link'])
        window_after = constants.BROWSER.window_handles[1]
        constants.BROWSER.switch_to_window(window_after)
        time.sleep(10)
        print(link)

    def import_from_GC(self):
        self.click(CatalogListingRMCPage.catalog_dictionary['import_from_GC_button'])
        time.sleep(3)

    def validate_gc_against_cl(self):
        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'] , constants.VALUES_FROM_GLOBAL_CATALOG['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['displayName'] != constants.VALUES_FROM_GLOBAL_CATALOG['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['displayName'])
        print(constants.VALUES_FROM_CATALOG_LISTING['description'] , constants.VALUES_FROM_GLOBAL_CATALOG['short_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['description'] != constants.VALUES_FROM_GLOBAL_CATALOG['short_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['description'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['short_description'])
#        print (constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] , constants.VALUES_FROM_GLOBAL_CATALOG['author'])
#        if (constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] != constants.VALUES_FROM_GLOBAL_CATALOG['author']):
#            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['providerDisplayName'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['author'])
        print (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] , constants.VALUES_FROM_GLOBAL_CATALOG['long_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] != constants.VALUES_FROM_GLOBAL_CATALOG['long_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['longDescription'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['long_description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['feature_media_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['documentation_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['terms_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['terms_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] , constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] != constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'])
        print (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] , constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] != constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] , constants.VALUES_FROM_GLOBAL_CATALOG['media_type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] != constants.VALUES_FROM_GLOBAL_CATALOG['media_type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['media_type'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] , constants.VALUES_FROM_GLOBAL_CATALOG['media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] != constants.VALUES_FROM_GLOBAL_CATALOG['media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['media_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] , constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] != constants.VALUES_FROM_GLOBAL_CATALOG['caption_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_longDescription'] , constants.VALUES_FROM_GLOBAL_CATALOG['long_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_longDescription'] != constants.VALUES_FROM_GLOBAL_CATALOG['long_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_longDescription'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['long_description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_displayName'] , constants.VALUES_FROM_GLOBAL_CATALOG['displayName'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_displayName'] != constants.VALUES_FROM_GLOBAL_CATALOG['displayName']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_displayName'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['displayName'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_title'] , constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_title'] != constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_title'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['bullet_title'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_description'] , constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_description'] != constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_bullet_description'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['bullet_description'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_caption'] , constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_caption'] != constants.VALUES_FROM_GLOBAL_CATALOG['caption_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_caption'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['caption_image'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_type'] , constants.VALUES_FROM_GLOBAL_CATALOG['media_type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_type'] != constants.VALUES_FROM_GLOBAL_CATALOG['media_type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_type'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['media_type'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_url'] , constants.VALUES_FROM_GLOBAL_CATALOG['media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_url'] != constants.VALUES_FROM_GLOBAL_CATALOG['media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_url'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['media_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_thumbnailUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_thumbnailUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['en']['i18n_thumbnailUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['thumbnail_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['semall_media_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['image_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['image_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['image_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['medium_media_url'])
        print (constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] , constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] != constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'] + " -not equal- " + constants.VALUES_FROM_GLOBAL_CATALOG['instructions_url'])
        for word in constants.VALUES_FROM_CATALOG_LISTING['tags']:
            print(word)
            if (word not in constants.VALUES_FROM_GLOBAL_CATALOG['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in catalog listing")
        print(constants.VALUES_FROM_CATALOG_LISTING['instructionsUrl'][1][1])


    def validate_json_gc_against_cl(self):
        print(constants.VALUES_FROM_CATALOG_LISTING)
        print(constants.VALUES_FROM_CATALOG_LISTING['displayName'],constants.JSON_SCRIPT['overview_ui']['en']['display_name'])
        if (constants.VALUES_FROM_CATALOG_LISTING['displayName'] != constants.JSON_SCRIPT['overview_ui']['en']['display_name']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_CATALOG_LISTING['displayName'] + " -not equal- " + constants.JSON_SCRIPT['overview_ui']['en']['display_name'])
        print(constants.VALUES_FROM_CATALOG_LISTING['description'],constants.JSON_SCRIPT['overview_ui']['en']['description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['description'] != constants.JSON_SCRIPT['overview_ui']['en']['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['description'] + " -not equal- " + constants.JSON_SCRIPT['overview_ui']['en']['description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['longDescription'],constants.JSON_SCRIPT['overview_ui']['en']['long_description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['longDescription'] != constants.JSON_SCRIPT['overview_ui']['en']['long_description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['longDescription'] + " -not equal- " + constants.JSON_SCRIPT['overview_ui']['en']['long_description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'],constants.JSON_SCRIPT['images']['feature_image'])
        if (constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] != constants.JSON_SCRIPT['images']['feature_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['featuredImageUrl'] + " -not equal- " + constants.JSON_SCRIPT['images']['feature_image'])
        print(constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'],constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] != constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['documentationUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['termsUrl'], constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] != constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url']):
            raise AssertionError("---> ERROR: ",constants.VALUES_FROM_CATALOG_LISTING['termsUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'],constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_title'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'])
        print(constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'], constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'])
        if (constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['bullets'][0]['bullet_description'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'], constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'], constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['thumbnailUrl'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'], constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'])
        print(constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'], constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'])
        if (constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] != constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'])
        print(constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'], constants.JSON_SCRIPT['images']['small_image'])
        if (constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] != constants.JSON_SCRIPT['images']['small_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['smallImageUrl'] + " -not equal- " + constants.JSON_SCRIPT['images']['small_image'])
        print(constants.VALUES_FROM_CATALOG_LISTING['imageUrl'], constants.JSON_SCRIPT['images']['image'])
        if (constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] != constants.JSON_SCRIPT['images']['image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['imageUrl'] + " -not equal- " + constants.JSON_SCRIPT['images']['image'])
        print(constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'], constants.JSON_SCRIPT['images']['medium_image'])
        if (constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] != constants.JSON_SCRIPT['images']['medium_image']):
            raise AssertionError("---> ERROR: ", constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'] + " -not equal- " + constants.JSON_SCRIPT['images']['medium_image'])
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
        for word in constants.VALUES_FROM_CATALOG_LISTING['tags']:
            print(word)
            if (word not in constants.JSON_SCRIPT['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in catalog listing")
        print(constants.VALUES_FROM_CATALOG_LISTING['mediumImageUrl'][1][1])

    def validate_jsonm_gc_against_jsonModal(self):
        print(constants.JSON_SCRIPT)
        print(constants.JSON_SCRIPT_MODALEDITOR)

#        print(constants.JSON_SCRIPT_MODALEDITOR['name'] , constants.JSON_SCRIPT['metadata']['displayName'])
#        if (constants.JSON_SCRIPT_MODALEDITOR['name'] != constants.JSON_SCRIPT['metadata']['displayName']):
#            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT_MODALEDITOR['name'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['displayName'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['display_name'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['displayName'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['display_name'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['displayName']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['display_name'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['displayName'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['long_description'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['longDescription'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['long_description'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['long_description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['longDescription'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['description'], constants.JSON_SCRIPT_MODALEDITOR['description'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['description'] != constants.JSON_SCRIPT_MODALEDITOR['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['description'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['description'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['description'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['description'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['description'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['description'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['description'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['description'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['description'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['long_description'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['longDescription'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['long_description'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['longDescription']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['long_description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['longDescription'])
        print(constants.JSON_SCRIPT['overview_ui']['en']['display_name'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['displayName'])
        if (constants.JSON_SCRIPT['overview_ui']['en']['display_name'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['displayName']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['overview_ui']['en']['display_name'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['displayName'])
        print(constants.JSON_SCRIPT['images']['feature_image'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['featuredImageUrl'])
        if (constants.JSON_SCRIPT['images']['feature_image'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['featuredImageUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['images']['feature_image'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['featuredImageUrl'])
        print(constants.JSON_SCRIPT['images']['image'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['imageUrl'])
        if (constants.JSON_SCRIPT['images']['image'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['imageUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['images']['image'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['imageUrl'])
        print(constants.JSON_SCRIPT['images']['medium_image'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['mediumImageUrl'])
        if (constants.JSON_SCRIPT['images']['medium_image'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['mediumImageUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['images']['medium_image'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['mediumImageUrl'])
        print(constants.JSON_SCRIPT['images']['small_image'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['smallImageUrl'])
        if (constants.JSON_SCRIPT['images']['small_image'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['smallImageUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['images']['small_image'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['smallImageUrl'])
#        print(constants.JSON_SCRIPT_MODALEDITOR['metadata']['providerDisplayName'], constants.JSON_SCRIPT['metadata']['providerDisplayName'])
#        if (constants.JSON_SCRIPT_MODALEDITOR['metadata']['providerDisplayName'] not in constants.JSON_SCRIPT['metadata']['providerDisplayName']):
#            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT_MODALEDITOR['metadata']['providerDisplayName'] + " -not equal- " + constants.JSON_SCRIPT['metadata']['providerDisplayName'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['bullets'][0]['description'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['caption'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['bullets'][0]['description'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['bullets'][0]['description']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['description'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['bullets'][0]['description'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['bullets'][0]['title'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['bullets'][0]['title']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['bullets'][0]['title'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['bullets'][0]['title'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['caption'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['caption']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['caption'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['caption'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['thumbnail_url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['thumbnailUrl'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['type'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['type']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['type'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['type'])
        print(constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['url'])
        if (constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['url']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['strings']['en']['media'][0]['url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['i18n']['en']['metadata']['media'][0]['url'])
        print(constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['documentationUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['documentationUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['urls']['doc_url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['documentationUrl'])
        print(constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['instructionsUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['instructionsUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['urls']['instructions_url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['instructionsUrl'])
        print(constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'], constants.JSON_SCRIPT_MODALEDITOR['metadata']['termsUrl'])
        if (constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'] != constants.JSON_SCRIPT_MODALEDITOR['metadata']['termsUrl']):
            raise AssertionError("---> ERROR: ", constants.JSON_SCRIPT['metadata']['ui']['urls']['terms_url'] + " -not equal- " + constants.JSON_SCRIPT_MODALEDITOR['metadata']['termsUrl'])
        for word in constants.JSON_SCRIPT['tags']:
            print(word)
            if (word not in constants.JSON_SCRIPT_MODALEDITOR['tags']):
                raise AssertionError("---> ERROR: ", word + " --is not present in json script from CL")
        print(constants.JSON_SCRIPT['metadata'][1][1]['ui']['urls']['terms_url'])

    def Updates_all_values_from_catalog_listing(self,value1,value2):
        if (value1.upper() == "LISTING PAGE"):
            time.sleep(2)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['short_description']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['short_description'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['short_description'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['short_description'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['author']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['author'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['author'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['author'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['detailed_description']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['detailed_description'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['detailed_description'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['service_icon_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['documentation_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['documentation_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['documentation_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['documentation_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['terms_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['terms_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['terms_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['terms_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_title']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['bullet_title'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['bullet_title'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['bullet_title'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['bullet_description']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['bullet_description'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['bullet_description'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['thumbnail_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['media_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['media_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['media_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['media_caption']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['media_caption'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['media_caption'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['media_caption'], tempValue)
            time.sleep(2)
        elif (value1.upper() == "SETTINGS"):
            time.sleep(2)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['instructions_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['instructions_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['instructions_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['instructions_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['support_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['support_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['support_url'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['support_email']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['support_email'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['support_email'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['support_email'], tempValue)
            tempValue = self.get_attribute_value(CatalogListingRMCPage.catalog_dictionary['custom_url']) + value2
            self.click(CatalogListingRMCPage.catalog_dictionary['custom_url'])
            self.clear_value(CatalogListingRMCPage.catalog_dictionary['custom_url'])
            self.set_value(CatalogListingRMCPage.catalog_dictionary['custom_url'], tempValue)
            time.sleep(2)


    def import_from_GC1(self):
        self.click(CatalogListingRMCPage.catalog_dictionary['import_from_GC_button111'])
        time.sleep(3)

