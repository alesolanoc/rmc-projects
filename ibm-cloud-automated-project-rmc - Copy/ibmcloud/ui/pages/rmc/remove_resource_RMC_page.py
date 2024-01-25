import time

from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage

class RemoveResourceRMCPage(ActionPage,FormPage):
    removeResource_dictionary = {
        'removeResource_RMC_page_header_label': '//h3',
        'removeResource_RMC_input': '#deleteOfferingModal_offeringName',
        'removeResource_RMC_button': '#deleteOfferingModal_deleteButton',
        'removeResource_RMC_resourceName': 'div.bx--modal-header__heading.bx--type-beta > p'
    }

    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "confirm_resource_name": lambda value: self.set_resourceNameToBeRemoved(value)
        }
        actions = {
            "remove confirmation title header": lambda value: self.is_there_remove_resource_label(value),
            "remove resource delete button": lambda: self.delete_button(),
            "remove resource should be displayed": lambda value: self.is_there_resource_name(value)
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def is_there_remove_resource_label(self, value):
        if (self.get_value(RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_page_header_label']).upper() != value):
            raise AssertionError ("---> ERROR: " + self.get_value((RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_page_header_label']).upper()) + " --Not equals-- " + value)

    def set_resourceNameToBeRemoved(self,value):
        self.click(RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_input'])
        self.clear_value(RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_input'])
        self.set_value(RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_input'], value)
        time.sleep(3)

    def delete_button(self):
        self.click(RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_button'])
        time.sleep(20)

    def is_there_resource_name(self,value):
        if (self.get_value(RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_resourceName']) != value):
            raise AssertionError ("---> ERROR: " + self.get_value((RemoveResourceRMCPage.removeResource_dictionary['removeResource_RMC_resourceName'])) + " --Not equals-- " + value)

