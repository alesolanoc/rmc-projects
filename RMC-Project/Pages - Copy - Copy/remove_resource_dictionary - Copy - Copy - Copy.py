from selenium.webdriver.common.by import By

class removeresourcePage():
    locator_dictionary = {
        "remove_input"   : (By.ID, 'deleteOfferingModal_offeringName'),
        "remove_confirm_button"  : (By.ID, 'deleteOfferingModal_deleteButton')

    }



