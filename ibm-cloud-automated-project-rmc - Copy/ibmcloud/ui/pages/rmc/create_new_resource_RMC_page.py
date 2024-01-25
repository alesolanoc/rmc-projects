import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.variables import constants

class CreateNewResourceRMCPage(FormPage,ActionPage):
    create_resource_dictionary = {
        'create_resource_header_label': '//div/div[2]/div/div/div/div/div/div',
        'No_Would_you_like_to_import': '//label[2]/span',
        'No_Is_your_resource': '//span/form/div/div/label[2]/span',
        'Yes_Is_your_resource': '//span/form/div/div/label/span',
        'new_resource_input': '#newServiceName',
        'service_type_drop_down': '#newServiceType',
        'service_option': '#newServiceType > option.bx--select-option',
        'operations_option': '//option[@value="operations_only"]',
        'composite_option': '//option[@value="composite"]',
        'platform_service_option': '//option[@value="platform_service"]',
        'submit_button': 'div.relativePosition > button.bx--btn.bx--btn--primary',
        'composite_tag': '#newCompositeTag',
        'composite_childs': '#newContainedResourceTypes',
        'parent_Name': '#compositeParentName',
        'child_nane': '#compositeChildName'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "create_new_resource_input": lambda value: self.set_newResourceValue(value),
            "input_composite_tag":  lambda value: self.set_composite_tag(value),
            "input_composite_child": lambda value: self.set_composite_child(value),
            "input_resource_parent": lambda value: self.set_parent_resource(value),
            "input_resource_child": lambda value: self.set_child_resource(value)
        }
        actions = {
            "create resource title header": lambda value: self.is_there_create_label(value),
            "select No for would you like": lambda value: self.is_there_would_you(value),
            "select No for is your resource": lambda value: self.is_there_is_your_resource(value),
            "select service from service type": lambda value: self.is_there_service(value),
            "press submit button": lambda value: self.press_submit_button(value)
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def is_there_create_label(self,value):
        if (self.get_value(CreateNewResourceRMCPage.create_resource_dictionary['create_resource_header_label']).upper() != value):
            raise AssertionError ("---> ERROR: " + self.get_value((CreateNewResourceRMCPage.create_resource_dictionary['create_resource_header_label']).upper()) + " --Not equals-- " + value)

    def is_there_would_you(self,value):
        if (value.upper() == 'NO'):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['No_Would_you_like_to_import'])
        time.sleep(2)

    def is_there_is_your_resource(self,value):
        if (value.upper() == 'NO'):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['No_Is_your_resource'])
            time.sleep(2)
        elif (value.upper() == 'YES'):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['Yes_Is_your_resource'])
            time.sleep(2)

    def set_newResourceValue(self,value):
        self.click(CreateNewResourceRMCPage.create_resource_dictionary['new_resource_input'])
        self.clear_value(CreateNewResourceRMCPage.create_resource_dictionary['new_resource_input'])
        self.set_value(CreateNewResourceRMCPage.create_resource_dictionary['new_resource_input'], value)
        time.sleep(2)

    def is_there_service(self,value):
        self.click(CreateNewResourceRMCPage.create_resource_dictionary['service_type_drop_down'])
        time.sleep(1)
        if (value.upper() == constants.SERVICE_TYE['service']):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['service_option'])
            time.sleep(1)
        elif (value.upper() == constants.SERVICE_TYE['operations only']):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['operations_option'])
            time.sleep(1)
        elif (value.upper() == constants.SERVICE_TYE['composite']):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['composite_option'])
            time.sleep(1)
        elif (value.upper() == constants.SERVICE_TYE['platform service']):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['platform_service_option'])
            time.sleep(1)

    def press_submit_button(self,value):
        if (value.upper() == 'SUBMIT'):
            self.click(CreateNewResourceRMCPage.create_resource_dictionary['submit_button'])
            time.sleep(15)

    def set_composite_tag(self,value):
        self.click(CreateNewResourceRMCPage.create_resource_dictionary['composite_tag'])
        self.clear_value(CreateNewResourceRMCPage.create_resource_dictionary['composite_tag'])
        self.set_value(CreateNewResourceRMCPage.create_resource_dictionary['composite_tag'], value)
        time.sleep(2)

    def set_composite_child(self,value):
        self.click(CreateNewResourceRMCPage.create_resource_dictionary['composite_childs'])
        self.clear_value(CreateNewResourceRMCPage.create_resource_dictionary['composite_childs'])
        self.set_value(CreateNewResourceRMCPage.create_resource_dictionary['composite_childs'], value)
        time.sleep(2)

    def set_parent_resource(self,value):
        self.click(CreateNewResourceRMCPage.create_resource_dictionary['parent_Name'])
        self.clear_value(CreateNewResourceRMCPage.create_resource_dictionary['parent_Name'])
        self.set_value(CreateNewResourceRMCPage.create_resource_dictionary['parent_Name'], value)
        time.sleep(2)

    def set_child_resource(self,value):
        self.click(CreateNewResourceRMCPage.create_resource_dictionary['child_nane'])
        self.clear_value(CreateNewResourceRMCPage.create_resource_dictionary['child_nane'])
        self.set_value(CreateNewResourceRMCPage.create_resource_dictionary['child_nane'], value)
        time.sleep(2)