import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants


class PricingPlanRMCPage(FormPage,ActionPage):
    pricingPlan_dictionary = {
        'part tab': 'div.bx--tabs__nav-link',
        'add part button': '.bx--btn--primary:nth-child(1)',
        'search_input': '#search__input-10',
        'first_part': '.detail_value',
        'first_region': 'td:nth-child(3)',
        'first_type': 'td:nth-child(4)',
        'second_part': 'tr:nth-child(2) .detail_value',
        'second_region': 'tr:nth-child(2) > td:nth-child(3)',
        'second_type': 'tr:nth-child(2) > td:nth-child(4)',
        'view_json_button': 'div:nth-child(2) > .bx--btn--secondary',
        'edit_part_1': 'tr:nth-child(1) .bx--btn:nth-child(1)',
        'edit_part_2': 'tr:nth-child(2) .bx--btn:nth-child(1)',
#        'edit_part_3': 'tr:nth-child(3) .bx--btn:nth-child(1)',
        'edit_part3_3': '//div[@id="content"]/div/div/div[2]/div/div/div[2]/table/tbody/tr[3]/td[5]/div/button',
        'first_row_part': 'tr:nth-child(1) .detail_value',
        'first_row_region': 'tr:nth-child(1) > td:nth-child(3)',
        'first_row_type': 'tr:nth-child(1) > td:nth-child(4)',
        'second_row_part': 'tr:nth-child(2) .detail_value',
        'second_row_region': 'tr:nth-child(2) > td:nth-child(3)',
        'second_row_type': 'tr:nth-child(2) > td:nth-child(4)',
        'edit_first_row': 'tr:nth-child(1) .bx--btn:nth-child(1)',
        'duplicate_button': '.bx--btn--secondary:nth-child(3)'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "search_part": lambda value: self.search_part(value)
        }
        actions = {
            "select tab": lambda value: self.select_tab(value),
            "press_add_part": lambda value: self.press_add_part(value),
            "verify_part": lambda value1,value2: self.verify_part(value1,value2),
            "verify_region": lambda value1,value2: self.verify_region(value1,value2),
            "verify_type": lambda value1,value2: self.verify_type(value1,value2),
            "verify_part_status": lambda value1,value2,value3: self.verify_part_status(value1,value2,value3),
            "press_view_json_button": lambda: self.press_view_json_button(),
            "press_edit": lambda value: self.press_edit(value),
            "get_values_row": lambda value: self.get_values_row(value),
            "verify_values": lambda value: self.verify_values(value),
            "edit_action": lambda value1,value2: self.edit_action(value1,value2),
            "press_duplicate": lambda: self.press_duplicate()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def select_tab(self,value):
        time.sleep(2)
        if (value.upper() == "PART / PRICING DEFINITION"):
            self.click(PricingPlanRMCPage.pricingPlan_dictionary['part tab'])
            time.sleep(2)

    def press_add_part(self,value):
        if (value.upper() == "ADD PART"):
            self.click(PricingPlanRMCPage.pricingPlan_dictionary['add part button'])
            time.sleep(2)

    def search_part(self,value):
        self.click(PricingPlanRMCPage.pricingPlan_dictionary['search_input'])
        self.clear_value(PricingPlanRMCPage.pricingPlan_dictionary['search_input'])
        self.set_value(PricingPlanRMCPage.pricingPlan_dictionary['search_input'], value)
        time.sleep(2)

    def verify_part(self,value1,value2):
        if (value2.upper() == "FIRST"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part']) , value1)
            if (value1 not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part'])):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part']) + " --Not equals-- " + value1)
        elif (value2.upper() == "SECOND"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part']) , value1)
            if (value1 not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part'])):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part']) + " --Not equals-- " + value1)

    def verify_region(self,value1,value2):
        if (value2.upper() == "FIRST"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_region']) , value1)
            if (value1.upper() not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_region']).upper()):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_region']) + " --Not equals-- " + value1)
        if (value2.upper() == "SECOND"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_region']) , value1)
            if (value1.upper() not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_region']).upper()):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_region']).upper() + " --Not equals-- " + value1.upper())

    def verify_type(self,value1,value2):
        if (value2.upper() == "FIRST"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_type']) , value1)
            if (value1.upper() not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_type']).upper()):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_type']).upper() + " --Not equals-- " + value1.upper())
        if (value2.upper() == "SECOND"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_type']) , value1)
            if (value1.upper() not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_type']).upper()):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_type']).upper() + " --Not equals-- " + value1.upper())

    def verify_part_status(self,value1,value2,value3):
        if (value3.upper() == "FIRST"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part']) , value1)
            if (value1 not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part'])):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part']) + " --Not equals-- " + value1)
            if (value2.upper() not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part']).upper()):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_part']) + " --Not equals-- " + value2)
        if (value3.upper() == "SECOND"):
            print(self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part']) , value1)
            if (value1 not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part'])):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part']) + " --Not equals-- " + value1)
            if (value2.upper() not in self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part']).upper()):
                raise AssertionError("---> ERROR: " + self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_part']) + " --Not equals-- " + value2)

    def press_view_json_button(self):
        self.click(PricingPlanRMCPage.pricingPlan_dictionary['view_json_button'])
        time.sleep(2)

    def press_edit(self,value):
        time.sleep(10)
        if (value.upper() == "FIRST"):
            self.click(PricingPlanRMCPage.pricingPlan_dictionary['edit_part_1'])
            time.sleep(5)
        elif (value.upper() == "SECOND"):
            print("alejo0012: ",PricingPlanRMCPage.pricingPlan_dictionary['edit_part_2'])

            self.click(PricingPlanRMCPage.pricingPlan_dictionary['edit_part_2'])
            time.sleep(5)
        elif (value.upper() == "THIRD"):
            print("alejo112: ",PricingPlanRMCPage.pricingPlan_dictionary['edit_part3_3'])
            self.click(PricingPlanRMCPage.pricingPlan_dictionary['edit_part3_3'])
            time.sleep(10)

    def get_values_row(self,value):
        if (value.upper() == "FIRST"):
            constants.VALUES_FROM_PART = [{}, {}]
            constants.VALUES_FROM_PART[0]['partNumber'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_row_part'])
            constants.VALUES_FROM_PART[0]['region'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_row_region'])
            constants.VALUES_FROM_PART[0]['type'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['first_row_type'])
            constants.VALUES_FROM_PART[0]['effectiveFrom'] = ''
            constants.VALUES_FROM_PART[0]['partDescription'] = ''
            constants.VALUES_FROM_PART[0]['productName'] = ''
            constants.VALUES_FROM_PART[0]['productTradename'] = ''
            constants.VALUES_FROM_PART[0]['model'] = ''
            time.sleep(2)
        elif (value.upper() == "SECOND"):
            constants.VALUES_FROM_PART[1]['partNumber'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_row_part'])
            constants.VALUES_FROM_PART[1]['region'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_row_region'])
            constants.VALUES_FROM_PART[1]['type'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['second_row_type'])
            constants.VALUES_FROM_PART[1]['effectiveFrom'] = ''
            constants.VALUES_FROM_PART[1]['partDescription'] = ''
            constants.VALUES_FROM_PART[1]['productName'] = ''
            constants.VALUES_FROM_PART[1]['productTradename'] = ''
            constants.VALUES_FROM_PART[1]['model'] = ''
            constants.VALUES_FROM_PART[1]['unitQuantity'] = ''
            constants.VALUES_FROM_PART[1]['price'] = ''
            constants.VALUES_FROM_PART[1]['unitPrice'] = ''
            time.sleep(2)
        elif (value.upper() == "THIRD"):
            constants.VALUES_FROM_PART[2]['partNumber'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['third_row_part'])
            constants.VALUES_FROM_PART[2]['region'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['third_row_region'])
            constants.VALUES_FROM_PART[2]['type'] = self.get_value(PricingPlanRMCPage.pricingPlan_dictionary['third_row_type'])
            constants.VALUES_FROM_PART[2]['effectiveFrom'] = ''
            constants.VALUES_FROM_PART[2]['partDescription'] = ''
            constants.VALUES_FROM_PART[2]['productName'] = ''
            constants.VALUES_FROM_PART[2]['productTradename'] = ''
            constants.VALUES_FROM_PART[2]['model'] = ''
            constants.VALUES_FROM_PART[2]['unitQuantity'] = ''
            constants.VALUES_FROM_PART[2]['price'] = ''
            constants.VALUES_FROM_PART[2]['unitPrice'] = ''
            time.sleep(2)

    def verify_values(self,value):
        if (value.upper() == "FIRST"):
            print(constants.VALUES_FROM_PART[0]['partNumber'], constants.JSON_SCRIPT[0]['partNumber'])
            if (constants.JSON_SCRIPT[0]['partNumber'] not in constants.VALUES_FROM_PART[0]['partNumber']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['partNumber'] + " -not equal- " + constants.JSON_SCRIPT[0]['partNumber'])
            print(constants.VALUES_FROM_PART[0]['region'], constants.JSON_SCRIPT[0]['region'])
            if (constants.JSON_SCRIPT[0]['region'] not in constants.VALUES_FROM_PART[0]['region']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['region'] + " -not equal- " + constants.JSON_SCRIPT[0]['region'])
            print(constants.VALUES_FROM_PART[0]['type'], constants.JSON_SCRIPT[0]['type'])
            if (constants.JSON_SCRIPT[0]['type'] not in constants.VALUES_FROM_PART[0]['type']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['type'] + " -not equal- " + constants.JSON_SCRIPT[0]['type'])
            print(constants.VALUES_FROM_PART[0]['partDescription'], constants.JSON_SCRIPT[0]['partDescription'])
            if (constants.JSON_SCRIPT[0]['partDescription'] not in constants.VALUES_FROM_PART[0]['partDescription']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['partDescription'] + " -not equal- " + constants.JSON_SCRIPT[0]['partDescription'])
            print(constants.VALUES_FROM_PART[0]['productName'], constants.JSON_SCRIPT[0]['productName'])
            if (constants.JSON_SCRIPT[0]['productName'] not in constants.VALUES_FROM_PART[0]['productName']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['productName'] + " -not equal- " + constants.JSON_SCRIPT[0]['productName'])
            print(constants.VALUES_FROM_PART[0]['productTradename'], constants.JSON_SCRIPT[0]['productTradename'])
            if (constants.JSON_SCRIPT[0]['productTradename'] not in constants.VALUES_FROM_PART[0]['productTradename']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['productTradename'] + " -not equal- " + constants.JSON_SCRIPT[0]['productTradename'])
            strDate = constants.VALUES_FROM_PART[0]['effectiveFrom']
            print(constants.VALUES_FROM_PART[0]['effectiveFrom'], constants.JSON_SCRIPT[0]['effectiveFrom'])
            if ((strDate[0:1] not in constants.JSON_SCRIPT[0]['effectiveFrom']) and (strDate[3:4] not in constants.JSON_SCRIPT[0]['effectiveFrom']) and (strDate[5:8] not in constants.JSON_SCRIPT[0]['effectiveFrom'])):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['effectiveFrom'] + " -not equal- " + constants.JSON_SCRIPT[0]['effectiveFrom'])
            print(constants.VALUES_FROM_PART[0]['model'], constants.JSON_SCRIPT[0]['model'])
            if (constants.JSON_SCRIPT[0]['model'] != constants.VALUES_FROM_PART[0]['model']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['model'] + " -not equal- " + constants.JSON_SCRIPT[0]['model'])
            print(constants.VALUES_FROM_PART['partNumber'][1][1][1])

        elif (value.upper() == "SECOND"):
            print(constants.VALUES_FROM_PART[1]['partNumber'], constants.JSON_SCRIPT[1]['partNumber'])
            if (constants.JSON_SCRIPT[1]['partNumber'] not in constants.VALUES_FROM_PART[1]['partNumber']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[0]['partNumber'] + " -not equal- " + constants.JSON_SCRIPT[0]['partNumber'])
            print(constants.VALUES_FROM_PART[1]['region'], constants.JSON_SCRIPT[1]['region'])
            if (constants.JSON_SCRIPT[1]['region'] not in constants.VALUES_FROM_PART[1]['region']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[1]['region'] + " -not equal- " + constants.JSON_SCRIPT[1]['region'])
            print(constants.VALUES_FROM_PART[1]['type'], constants.JSON_SCRIPT[1]['type'])
            if (constants.JSON_SCRIPT[1]['type'] not in constants.VALUES_FROM_PART[1]['type']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[1]['type'] + " -not equal- " + constants.JSON_SCRIPT[1]['type'])
            print(constants.VALUES_FROM_PART[1]['partDescription'], constants.JSON_SCRIPT[1]['partDescription'])
            if (constants.JSON_SCRIPT[1]['partDescription'] not in constants.VALUES_FROM_PART[1]['partDescription']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[1]['partDescription'] + " -not equal- " + constants.JSON_SCRIPT[1]['partDescription'])
            strDate = constants.VALUES_FROM_PART[1]['effectiveFrom']
            print(constants.VALUES_FROM_PART[1]['effectiveFrom'], constants.JSON_SCRIPT[1]['effectiveFrom'])
            if ((strDate[0:1] not in constants.JSON_SCRIPT[1]['effectiveFrom']) and (strDate[3:4] not in constants.JSON_SCRIPT[1]['effectiveFrom']) and (strDate[5:8] not in constants.JSON_SCRIPT[1]['effectiveFrom'])):
                raise AssertionError("---> ERROR: ",constants.VALUES_FROM_PART[1]['effectiveFrom'] + " -not equal- " + constants.JSON_SCRIPT[1]['effectiveFrom'])
            print(constants.VALUES_FROM_PART[1]['model'], constants.JSON_SCRIPT[1]['model'])
            if (constants.JSON_SCRIPT[1]['model'] != constants.VALUES_FROM_PART[1]['model']):
                raise AssertionError("---> ERROR: ", constants.VALUES_FROM_PART[1]['model'] + " -not equal- " + constants.JSON_SCRIPT[1]['model'])
            time.sleep(2)
            print(constants.VALUES_FROM_PART['partNumber'][1][1][1])

    def edit_action(self,value1,value2):
        if (value1.upper() == "EDIT"):
            if (value2.upper() == "FIRST"):
                self.click(PricingPlanRMCPage.pricingPlan_dictionary['edit_first_row'])
                time.sleep(2)

    def press_duplicate(self):
        self.click(PricingPlanRMCPage.pricingPlan_dictionary['duplicate_button'])
        time.sleep(2)
