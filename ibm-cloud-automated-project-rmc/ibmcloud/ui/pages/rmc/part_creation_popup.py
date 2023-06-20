import datetime
import time

from selenium.webdriver.common.keys import Keys

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants
from core.ui.variables.constants import VALIDATE_REQUIRED_FIELDS_SERVICE, CURRENT_DATE, FUTURE_DATE


class PartPopupRMCPage(FormPage,ActionPage):
    PartPopup_dictionary = {
        'yes_choose_experience': '.bx--radio-button__label:nth-child(1) > .bx--radio-button__appearance',
        'no_choose_experience': '.bx--radio-button__label:nth-child(2) > .bx--radio-button__appearance',
        'yes_choose_part_type': '.bx--radio-button__label:nth-child(1) > .bx--radio-button__appearance',
        'no_choose_part_type': '.bx--radio-button__label:nth-child(2) > .bx--radio-button__appearance',
        'yes_choose_pricing_setting': '.bx--radio-button__label:nth-child(1) > .bx--radio-button__appearance',
        'no_choose_pricing_setting': '.bx--radio-button__label:nth-child(2) > .bx--radio-button__appearance',
        'yes_have_existing_part': '.bx--radio-button__label:nth-child(1) > .bx--radio-button__appearance',
        'no_have_existing_part': '.bx--radio-button__label:nth-child(2) > .bx--radio-button__appearance',
        'press_next_button': '.relativePosition > .bx--btn--primary',
        'part_number': '#addPartNumber',
        'dropdown_menu_region': '#pricing\/parts\/0\/region',
        'dropdown_menu_region_child': '#pricing\/parts\/1\/region',
        'dropdown_menu_region_child_2': '#pricing\/parts\/2\/region',
        'select_defualt_region': '#pricing\/parts\/0\/region > .bx--select-option',
        'select_global_region_2': '#pricing\/parts\/1\/region > .bx--select-option:nth-child(1)',
        'select_global_region_3': '#pricing\/parts\/2\/region > .bx--select-option:nth-child(2)',
        'release_date': 'svg[name="calendar"]',
        "current_date": '[aria-label="' + CURRENT_DATE + '"]',
        "future_date": '[aria-label="' + FUTURE_DATE + '"]',
        'part_description': '#pricing\/parts\/0\/partDescription',
        'part_description_1': '#pricing\/parts\/1\/partDescription',
        'product_name': '#pricing\/parts\/0\/productName',
        'product_tradename': '#pricing\/parts\/0\/productTradename',
        'edit_metric_button': 'div.bx--modal-content > div > button.bx--btn.bx--btn--primary',
        'no_custom_metric': '.bx--radio-button__label:nth-child(2) > .bx--radio-button__appearance',
        'invoice_dropdown': '#pricing\/parts\/1\/invoicePartNumber',
        'invoice_first_option': '#pricing\/parts\/1\/invoicePartNumber > .bx--select-option:nth-child(2)',
        'invoice_dropdown_1': '#pricing\/parts\/2\/invoicePartNumber',

        'invoice_first_option_1': '#pricing\/parts\/2\/invoicePartNumber > .bx--select-option:nth-child(2)',
        'metric_grouping_dropdown': '#metricsGrouppingDropdown',
        'access_metric': '#metricsGrouppingDropdown > .bx--select-option:nth-child(2)',
        'api_metric': '#metricsGrouppingDropdown > .bx--select-option:nth-child(3)',
        'select_metric_dropdown': '#metricsDropdown',
        'access_metric_option': '#metricsDropdown > .bx--select-option',
        'api_call_metric_option': '#metricsDropdown > .bx--select-option:nth-child(1)',
        'confirm_button': '.relativePosition > .bx--btn--primary',
        'publish_button': '.bx--modal__buttons > .bx--btn:nth-child(4)',
        'save_button': 'div.bx--modal__buttons > button.bx--btn.bx--btn--primary',
        'close_button': '.bx--btn--secondary:nth-child(2)',
        'pricing_model_1': '#pricing\/parts\/1\/model',
        'pricing_model_linner_tier_1': '#pricing\/parts\/1\/model > .bx--select-option:nth-child(2)',
        'pricing_model_simple_tier_1': '#pricing\/parts\/1\/model > .bx--select-option:nth-child(3)',
        'pricing_model_graduated_tier_1': '#pricing\/parts\/1\/model > .bx--select-option:nth-child(4)',
        'pricing_model_block_tier_1': '#pricing\/parts\/1\/model > .bx--select-option:nth-child(5)',
        'charge_unit_quantity_1': '#pricing\/parts\/1\/chargeUnitQuantity',
        'usa_price_1': '#pricing\/parts\/1\/countries\/0\/prices\/0\/price',
        'upper_limit_1': '#pricing\/parts\/1\/countries\/0\/prices\/0\/range\/1',
        'effective_from_date': '.bx--date-picker-container > #pricing\/parts\/0\/effectiveFrom',
        'effective_from_date_1': '.bx--date-picker-container > #pricing\/parts\/1\/effectiveFrom'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "fill_description": lambda value: self.set_descriptionValue(value),
            "fill_description_1": lambda value: self.set_descriptionValue_1(value),
            "fill_product_name": lambda value: self.set_product_nameValue(value),
            "fill_product_tradename": lambda value: self.set_product_tradenameValue(value),
            "charge_unit_quantity": lambda value: self.set_charge_unit_quantity(value),
            "usa_price": lambda value: self.set_usa_price(value),
            "upper_limit": lambda value: self.set_upper_limit(value)
        }
        actions = {
            "choose_new_experience": lambda value: self.choose_new_experience(value),
            "press_next_button": lambda value: self.press_next_button(value),
            "choose_part_type": lambda value: self.choose_part_type(value),
            "choose_price_setting": lambda value: self.choose_price_setting(value),
            "choose_new_part": lambda value: self.choose_new_part(value),
            "part_number": lambda value: self.part_number(value),
            "dropdown_menu": lambda value: self.dropdown_menu(value),
            "select_default_option": lambda value: self.select_default_option(value),
            "select_date": lambda value: self.select_date(value),
            "edit_metric_button": lambda: self.edit_metric_button(),
            "select_custom_metric": lambda value: self.select_custom_metric(value),
            "metric_grouping": lambda: self.metric_grouping(),
            "select_metric_option": lambda value: self.select_metric_option(value),
            "metric_option": lambda: self.metric_option(),
            "select_option": lambda value: self.select_option(value),
            "press_button_from_edit_metric": lambda value: self.press_button_from_edit_metric(value),
            "press_publish_pricing_button": lambda value: self.press_publish_pricing_button(value),
            "invoice_menu": lambda value: self.invoice_menu(value),
            "select_invoice_option": lambda value: self.select_invoice_option(value),
            "select_pricing_model": lambda value: self.select_pricing_model(value),
            "get_values_from_popup": lambda value: self.get_values_from_popup(value)
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def choose_new_experience(self,value):
        if (value.upper() == "YES"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['yes_choose_experience'])

    def press_next_button(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['press_next_button'])
        time.sleep(2)

    def choose_part_type(self,value):
        if (value.upper() == "YES"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['yes_choose_part_type'])
            time.sleep(2)
        elif (value.upper() == "NO"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['no_choose_part_type'])
            time.sleep(2)

    def choose_price_setting(self,value):
        if (value.upper() == "NO"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['no_choose_part_type'])
            time.sleep(2)

    def choose_new_part(self,value):
        if (value.upper() == "NO"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['no_have_existing_part'])
            time.sleep(2)

    def part_number(self,value):
        print("alejo ", self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['part_number']))
        if (value not in self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['part_number'])):
            raise AssertionError ("---> ERROR: " + self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['part_number']) + " --Not equals-- " + value)

    def dropdown_menu(self,value):
        if (value.upper() == "DEFAULT"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['dropdown_menu_region'])
            time.sleep(2)
        elif (value.upper() == "GLOBAL"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['dropdown_menu_region_child'])
            time.sleep(2)
        elif (value.upper() == "ALL REGIONS"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['dropdown_menu_region_child_2'])
            time.sleep(2)


    def select_default_option(self,value):
        if (value.upper() == "DEFAULT"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['select_defualt_region'])
            time.sleep(2)
        elif (value.upper() == "GLOBAL"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['select_global_region_2'])
            time.sleep(2)
        elif (value.upper() == "ALL REGIONS"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['select_global_region_3'])
            time.sleep(2)


    def select_date(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['release_date'])
        time.sleep(2)
        if (value.upper() == 'CURRENT'):
            self.click(PartPopupRMCPage.PartPopup_dictionary['current_date'])
            time.sleep(3)
        else:
            self.click(PartPopupRMCPage.PartPopup_dictionary['future_date'])

    def invoice_menu(self,value):
        if (value.upper() == "FIRST INVOICE"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['invoice_dropdown'])
            time.sleep(2)
        if (value.upper() == "SECOND INVOICE"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['invoice_dropdown_1'])
            time.sleep(2)

    def select_invoice_option(self,value):
        if (value.upper() == "FIRST INVOICE"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['invoice_first_option'])
            time.sleep(2)
        elif (value.upper() == "SECOND INVOICE"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['invoice_first_option_1'])
            time.sleep(2)


    def set_descriptionValue(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['part_description'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['part_description'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['part_description'], value)
        time.sleep(2)

    def set_descriptionValue_1(self, value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['part_description_1'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['part_description_1'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['part_description_1'], value)
        time.sleep(2)

    def set_product_nameValue(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['product_name'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['product_name'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['product_name'], value)
        time.sleep(2)

    def set_product_tradenameValue(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['product_tradename'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['product_tradename'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['product_tradename'], value)
        time.sleep(2)

    def edit_metric_button(self):
        self.click(PartPopupRMCPage.PartPopup_dictionary['edit_metric_button'])
        time.sleep(2)

    def select_custom_metric(self,value):
        if (value.upper() == "NO"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['no_custom_metric'])
            time.sleep(2)

    def metric_grouping(self):
        self.click(PartPopupRMCPage.PartPopup_dictionary['metric_grouping_dropdown'])
        time.sleep(2)

    def select_metric_option(self,value):
        if (value.upper() == "ACCESS"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['access_metric'])
            time.sleep(2)
        elif (value.upper() == "API"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['api_metric'])
            time.sleep(2)

    def metric_option(self):
        self.click(PartPopupRMCPage.PartPopup_dictionary['select_metric_dropdown'])
        time.sleep(2)

    def select_option(self,value):
        if (value.upper() == "ACCESS"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['access_metric_option'])
            time.sleep(2)
        elif (value.upper() == "API CALL"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['api_call_metric_option'])
            time.sleep(2)

    def press_button_from_edit_metric(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['confirm_button'])
        time.sleep(2)

    def press_publish_pricing_button(self,value):
        if (value.upper() == "PUBLISH PRICING"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['publish_button'])
            time.sleep(20)
        elif (value.upper() == "SAVE"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['save_button'])
            time.sleep(15)
        elif (value.upper() == "CLOSE"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['close_button'])
            time.sleep(3)

    def select_pricing_model(self,value):
        elemen = self.find_element(PartPopupRMCPage.PartPopup_dictionary['pricing_model_1'])
        elemen.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        self.click(PartPopupRMCPage.PartPopup_dictionary['pricing_model_1'])
        time.sleep(2)
        if (value.upper() == "LINEAR TIER"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['pricing_model_linner_tier_1'])
            time.sleep(2)
        elif (value.upper() == "SIMPLE TIER"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['pricing_model_simple_tier_1'])
            time.sleep(2)
        elif (value.upper() == "GRADUATED TIER"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['pricing_model_graduated_tier_1'])
            time.sleep(2)
        elif (value.upper() == "BLOCK TIER"):
            self.click(PartPopupRMCPage.PartPopup_dictionary['pricing_model_block_tier_1'])
            time.sleep(2)


    def set_charge_unit_quantity(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['charge_unit_quantity_1'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['charge_unit_quantity_1'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['charge_unit_quantity_1'], value)
        time.sleep(2)

    def set_usa_price(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['usa_price_1'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['usa_price_1'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['usa_price_1'], value)
        time.sleep(2)

    def set_upper_limit(self,value):
        self.click(PartPopupRMCPage.PartPopup_dictionary['upper_limit_1'])
        self.clear_value(PartPopupRMCPage.PartPopup_dictionary['upper_limit_1'])
        self.set_value(PartPopupRMCPage.PartPopup_dictionary['upper_limit_1'], value)
        time.sleep(2)

    def get_values_from_popup(self,value):
        if (value.upper() == "FIRST"):
            constants.VALUES_FROM_PART[0]['effectiveFrom'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['effective_from_date'])
            constants.VALUES_FROM_PART[0]['partDescription'] = self.get_value(PartPopupRMCPage.PartPopup_dictionary['part_description'])
            constants.VALUES_FROM_PART[0]['productName'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['product_name'])
            constants.VALUES_FROM_PART[0]['productTradename'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['product_tradename'])
            constants.VALUES_FROM_PART[0]['model'] = ''
        elif (value.upper() == "SECOND"):
            constants.VALUES_FROM_PART[1]['effectiveFrom'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['effective_from_date_1'])
            constants.VALUES_FROM_PART[1]['partDescription'] = self.get_value(PartPopupRMCPage.PartPopup_dictionary['part_description_1'])
            constants.VALUES_FROM_PART[1]['model'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['pricing_model_1'])
            constants.VALUES_FROM_PART[1]['unitQuantity'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['charge_unit_quantity_1'])
            constants.VALUES_FROM_PART[1]['price'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['usa_price_1'])
            constants.VALUES_FROM_PART[1]['unitPrice'] = self.get_attribute_value(PartPopupRMCPage.PartPopup_dictionary['usa_price_1'])
