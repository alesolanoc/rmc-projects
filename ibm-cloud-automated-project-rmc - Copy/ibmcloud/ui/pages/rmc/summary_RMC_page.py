import datetime
import time

from selenium.webdriver.common.keys import Keys

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants
from core.ui.variables.constants import VALIDATE_REQUIRED_FIELDS_SERVICE, TARGET_RELEASE_LEVEL, CURRENT_DATE, \
    FUTURE_DATE, COMPOSITE_RESOURCE

POSITION = 0

class SummaryRMCPage(FormPage,ActionPage):
    global POSITION
    summary_dictionary = {
#        'summary_tab': 'span.leftNav__tab-name',
#        'catalog_listing_tab': '//div[@id="root"]/div/div[2]/nav/ul/li[3]/span/a',
#        'translation_tab': '//div[@id="root¨]/div/div[2]/nav/ul/li[14]/span/a/span',
        'summary_tab': 'li:nth-child(2) .leftNav__tab-name',
        'catalog_listing_tab': 'li:nth-child(3) .leftNav__tab-name',
        'pricing_plans_tab': 'li:nth-child(4) .leftNav__tab-name',
        'translation_tab': 'li:nth-child(14) .leftNav__tab-name',
        'resource_name_label': 'h1.bx--detail-page-header-title',
        'version_selected_label': '#version-select',
        'type_selected_label': '#type',
        'first_contributor': '//tr[@id="0column"]/td',
        'all_resources_link': 'div.bx--breadcrumb-item > a.bx--link',
        'add_contributor_button': 'div.contributorsHeader > button.bx--btn.bx--btn--primary',
        'second_contributor': '//tr[@id="1column"]/td',
        'first_resource': 'tr.bx--table-row.bx--parent-row.bx--parent-row--even > td',
        'remove_contributor': '//tr[@id="1column"]/td',
        'target_release_level': '#version-select',
        'target_option': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[0][POSITION] + '"]',
        'service_franework': '#serviceFramework',
        'framework_option': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[1][POSITION] + '"]',
        'release_date': 'svg[name="calendar"]',
        'service_selected': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[2][POSITION] + '"]',
        'offering_category': '#brand',
        'select_offering_category': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[3][POSITION] + '"]',
        'sub_offering_category': '#subBrand',
        'select_sub_offering_category': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[4][POSITION] + '"]',
        'save_button': '#summarySaveButton',
        "calendar_date": '//div/div/div/input',
        "label_at_top": 'span.bx--tag.bx--tag--beta.top-nav__tag',
        "maturity_label": 'div.next-maturity > div > div > p',
        "target_maturity_label": '//div[2]/div/div/p[2]',
        "current_date": '[aria-label="' + CURRENT_DATE + '"]',
        "future_date": '[aria-label="' + FUTURE_DATE + '"]',
        "composite_tag": '#compositeTag',
        "contained_resource_types": '#containedResourceTypes'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
#            "target_release_version": lambda value: self.set_targerReleaseValue(value)
        }
        actions = {
            "select tab": lambda value: self.select_tab(value),
            "resource name label": lambda value: self.is_there_resource_name(value),
            "version selected label": lambda value: self.is_there_version_selected(value),
            "type selected label": lambda value: self.is_there_type_selected(value),
            "first contributor": lambda value: self.is_there_first_contributor(value),
            "all resources link": lambda: self.all_resources_link(),
            "press add contributor button": lambda :self.add_contributor(),
            "second contributor": lambda value: self.is_there_second_contributor(value),
            "select first resource": lambda: self.is_there_first_resource(),
            "press remove contributor": lambda: self.is_there_remove_button(),
            "contributor was removed": lambda: self.contributor_was_removed(),
            "select target release version": lambda value: self.select_targerReleaseValue(value),
            "select service framework": lambda value: self.select_serviceFramework(value),
            "select release date": lambda value: self.select_release_date(value),
            "select type of service": lambda value: self.select_type_service(value),
            "select category": lambda value: self.select_category(value),
            "select sub category": lambda value: self.select_sub_category(value),
            "press save button": lambda: self.press_save(),
            "verify_inputs": lambda value1,value2,value3,value4,value5,value6: self.verify_inputs(value1,value2,value3,value4,value5,value6),
            "label_at_top": lambda value1,value2: self.is_label_at_top(value1,value2),
            "maturity_label": lambda value1,value2: self.is_maturity_label(value1,value2),
            "target_label": lambda value1,value2: self.is_target_maturity_label(value1,value2),
            "composite_tag": lambda value: self.is_composite_tag(value),
            "contaned_resource_types": lambda value: self.is_contained(value),
            "contaned_resource_types2": lambda value: self.is_contained2(value)
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def all_resources_link(self):
        time.sleep(2)
        self.click(SummaryRMCPage.summary_dictionary['all_resources_link'])
        time.sleep(5)

    def select_tab(self,value):
        time.sleep(5)
        if (value.upper() == 'SUMMARY'):
            self.click(SummaryRMCPage.summary_dictionary['summary_tab'])
            time.sleep(2)
        elif (value.upper() == 'CATALOG LISTING'):
            self.click(SummaryRMCPage.summary_dictionary['catalog_listing_tab'])
            time.sleep(2)
        elif (value.upper() == 'TRANSLATION'):
            self.click(SummaryRMCPage.summary_dictionary['translation_tab'])
            time.sleep(2)
        elif (value.upper() == 'PRICING PLANS'):
            self.click(SummaryRMCPage.summary_dictionary['pricing_plans_tab'])
            time.sleep(2)

    def is_there_resource_name(self,value):
        if (value not in self.get_value(SummaryRMCPage.summary_dictionary['resource_name_label'])):
            raise AssertionError ("---> ERROR: " + self.get_value(SummaryRMCPage.summary_dictionary['resource_name_label']) + " --Not equals-- " + value)

    def is_there_version_selected(self,value):
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['version_selected_label']) != value):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['version_selected_label'])) + " --Not equals-- " + value)

    def is_there_type_selected(self,value):
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['type_selected_label']) != value):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['type_selected_label'])) + " --Not equals-- " + value)

    def is_there_first_contributor(self,value):
        if (self.get_value(SummaryRMCPage.summary_dictionary['first_contributor']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value((SummaryRMCPage.summary_dictionary['first_contributor'])) + " --Not equals-- " + value)

    def add_contributor(self):
        time.sleep(2)
        self.click(SummaryRMCPage.summary_dictionary['add_contributor_button'])
        time.sleep(2)

    def is_there_second_contributor(self,value):
        if (self.get_value(SummaryRMCPage.summary_dictionary['second_contributor']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value((SummaryRMCPage.summary_dictionary['second_contributor'])) + " --Not equals-- " + value)

    def is_there_first_resource(self):
        time.sleep(2)
        self.click(SummaryRMCPage.summary_dictionary['first_resource'])
        time.sleep(15)

    def is_there_remove_button(self):
        time.sleep(2)
        self.click(SummaryRMCPage.summary_dictionary['remove_contributor'])
        time.sleep(10)

    def contributor_was_removed(self):
        if self.is_existing(SummaryRMCPage.summary_dictionary['remove_contributor']):
            raise AssertionError("---> ERROR: contributor was not removed")

    def select_targerReleaseValue(self,value):
        summary_dictionary_update1 = {'target_option': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[0][int(value)] + '"]'}
        SummaryRMCPage.summary_dictionary.update(summary_dictionary_update1)
        self.click(SummaryRMCPage.summary_dictionary['target_release_level'])
        time.sleep(1)
        self.click(SummaryRMCPage.summary_dictionary['target_option'])
        time.sleep(1)

    def select_serviceFramework(self,value):
        summary_dictionary_update2 = {'framework_option': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[1][int(value)] + '"]'}
        SummaryRMCPage.summary_dictionary.update(summary_dictionary_update2)
        self.click(SummaryRMCPage.summary_dictionary['service_franework'])
        time.sleep(1)
        self.click(SummaryRMCPage.summary_dictionary['framework_option'])
        time.sleep(1)

    def select_release_date(self,value):
        self.click(SummaryRMCPage.summary_dictionary['release_date'])
        time.sleep(2)
        if (value.upper() == 'CURRENT'):
            self.click(SummaryRMCPage.summary_dictionary['current_date'])
            time.sleep(3)
        else:
            self.click(SummaryRMCPage.summary_dictionary['future_date'])

    def select_type_service(self,value):
        summary_dictionary_update3 = {'service_selected': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[2][POSITION] + '"]'}
        SummaryRMCPage.summary_dictionary.update(summary_dictionary_update3)
        self.click(SummaryRMCPage.summary_dictionary['type_selected_label'])
        time.sleep(1)
        self.click(SummaryRMCPage.summary_dictionary['service_selected'])
        time.sleep(1)

    def select_category(self,value):
        summary_dictionary_update4 = {'select_offering_category': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[3][POSITION] + '"]'}
        SummaryRMCPage.summary_dictionary.update(summary_dictionary_update4)
        self.click(SummaryRMCPage.summary_dictionary['offering_category'])
        time.sleep(1)
        self.click(SummaryRMCPage.summary_dictionary['select_offering_category'])
        time.sleep(1)

    def select_sub_category(self,value):
        summary_dictionary_update4 = {'select_sub_offering_category': '//option[@value=' + '"' + VALIDATE_REQUIRED_FIELDS_SERVICE[4][POSITION] + '"]'}
        SummaryRMCPage.summary_dictionary.update(summary_dictionary_update4)
        self.click(SummaryRMCPage.summary_dictionary['sub_offering_category'])
        time.sleep(1)
        self.click(SummaryRMCPage.summary_dictionary['select_sub_offering_category'])
        time.sleep(2)

    def press_save(self):
        self.click(SummaryRMCPage.summary_dictionary['save_button'])
        time.sleep(20)

    def verify_inputs(self,value1,value2,value3,value4,value5,value6):
        time.sleep(5)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['version_selected_label']) != value1):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['version_selected_label'])) + " --Not equals-- " + value1)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['service_franework']) != value2):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['service_franework'])) + " --Not equals-- " + value2)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['type_selected_label']) != value3):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['type_selected_label'])) + " --Not equals-- " + value3)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['offering_category']) != value4):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['offering_category'])) + " --Not equals-- " + value4)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['sub_offering_category']) != value5):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['sub_offering_category'])) + " --Not equals-- " + value5)
        if (value6.upper() == 'CURRENT_DATE'):
            value6 = datetime.date.today()
            value6 = value6.strftime("%m/%d/%Y")
            if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['calendar_date']) != value6):
                raise AssertionError ("---> ERROR: " + self.get_attribute_value((SummaryRMCPage.summary_dictionary['calendar_date'])) + " --Not equals-- " + value6)

    def is_label_at_top(self,value1,value2):
        time.sleep(2)
        if (value1 != 'EXPERIMENTAL'):
            if (self.get_value(SummaryRMCPage.summary_dictionary['label_at_top']) != TARGET_RELEASE_LEVEL[value2]['top']):
                raise AssertionError ("---> ERROR: " + self.get_value(SummaryRMCPage.summary_dictionary['label_at_top']) + " --Not equals-- " + TARGET_RELEASE_LEVEL[value2]['top'])
            time.sleep(2)

    def is_maturity_label(self,value1,value2):
        time.sleep(2)
        if (self.get_value(SummaryRMCPage.summary_dictionary['maturity_label']).upper() != TARGET_RELEASE_LEVEL[value2]['CURRENT MATURITY']):
            raise AssertionError ("---> ERROR: " + self.get_value(SummaryRMCPage.summary_dictionary['maturity_label']).upper() + " --Not equals-- " + TARGET_RELEASE_LEVEL[value2]['CURRENT MATURITY'] + " for: " + value2)
        time.sleep(2)


    def is_target_maturity_label(self,value1,value2):
        time.sleep(2)
        if (self.get_value(SummaryRMCPage.summary_dictionary['target_maturity_label']).upper() != TARGET_RELEASE_LEVEL[value2]['TARGET MATURITY']):
            raise AssertionError ("---> ERROR: " + self.get_value(SummaryRMCPage.summary_dictionary['target_maturity_label']).upper() + " --Not equals-- " + TARGET_RELEASE_LEVEL[value2]['TARGET MATURITY'] + " for: " + value2)
        time.sleep(2)


    def is_composite_tag(self,value):
        elemen = self.find_element(SummaryRMCPage.summary_dictionary['composite_tag'])
        elemen.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['composite_tag']) != COMPOSITE_RESOURCE['composite_tag'] or self.get_attribute_value(SummaryRMCPage.summary_dictionary['composite_tag']) != value):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value(SummaryRMCPage.summary_dictionary['composite_tag']) + " --Not equals-- " + COMPOSITE_RESOURCE['composite_tag'])
        time.sleep(2)


    def is_contained(self,value):
        time.sleep(2)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['contained_resource_types']) != COMPOSITE_RESOURCE['contained_resource_types'] or self.get_attribute_value(SummaryRMCPage.summary_dictionary['contained_resource_types']) != value):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value(SummaryRMCPage.summary_dictionary['contained_resource_types']) + " --Not equals-- " + COMPOSITE_RESOURCE['contained_resource_types'])
        time.sleep(2)

    def is_contained2(self,value):
        time.sleep(2)
        if (self.get_attribute_value(SummaryRMCPage.summary_dictionary['contained_resource_types']) != COMPOSITE_RESOURCE['contained_resource_types2'] or self.get_attribute_value(SummaryRMCPage.summary_dictionary['contained_resource_types']) != value):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value(SummaryRMCPage.summary_dictionary['contained_resource_types']) + " --Not equals-- " + COMPOSITE_RESOURCE['contained_resource_types2'])
        time.sleep(2)
